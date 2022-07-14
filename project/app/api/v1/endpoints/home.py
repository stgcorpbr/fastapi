
from datetime import datetime
import json
import os, re
import random
import pandas as pd
import sqlalchemy as sa
from typing import List
from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession
from core import deps
from models import home_model, user_model, relatorio_model
from core.auth import autenticar, criar_token_acesso
from core.celery_worker import ajuste_apuracao_icms_task, apuracao_cred_pis_cofins_task, apuracao_deb_pis_cofins_task, apuracao_icms_ipi_task, b_total_icms_ipi_task, balancete_contabil_task, clear_all_locks, excel_checklist_icms_ipi_faltantes_task, notify
from websocket import create_connection
from schemas import cliente_schema, base_schema, usuario_schema, relatorio_schema
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse
from fastapi import Request, APIRouter, status, Depends, HTTPException
from fastapi_redis_cache import cache
from fastapi_redis_cache import cache_one_minute
from core.send_email import return_email_async, send_email_background, send_email_async
from fastapi import BackgroundTasks
from logging import error
from redis import Redis
import socketio
from functools import wraps

WS = ""
url_ws = "wss://stgapi.cf:7000/ws/"

sio = socketio.Client()

@sio.event
def connect():
    print('connection established')

@sio.event
def my_message(data):
    print('message received with ', data)
    sio.emit('my response', {'response': 'my response'})

@sio.event
def disconnect():
    print('disconnected from server')


# Bypass warning SQLmodel select
from sqlmodel.sql.expression import Select, SelectOfScalar

SelectOfScalar.inherit_cache = True # type: ignore
Select.inherit_cache = True # type: ignore
# Fim Bypass

def convertData(data_string):
    data = datetime.strptime(data_string, '%d-%m-%Y').date()
    return str(data.strftime('%Y-%m-%d'))

router = APIRouter()

@router.get('/send-email/asynchronous')
async def send_email_asynchronous():
    await send_email_async("Erro no Sistema", "fersoftware@gmail.com", {
        "title": "Erro no SQL",
        "name": "Linha tal"
    })
    return 'Success'


@router.get('/send-email/backgroundtasks')
def send_email_backgroundtasks(background_tasks: BackgroundTasks):
    send_email_background(background_tasks, 'Hello World', 'someemail@gmail.com', {
        'title': 'Hello World',
        'name': 'John Doe'
    })
    return 'Success'

@router.get("/date")
async def get_data():  
    sio.connect('http://localhost:6000')
    # sio.emit('my response', {'response': 'my response'})

# POST Login
@router.post('/login')
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(deps.get_session_sistemas)):
    usuario = await autenticar(cliente_id=form_data.username, senha=form_data.password, db=db)

    if not usuario:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Dados de acesso incorretos.')

    return JSONResponse(content={"access_token": criar_token_acesso(sub=usuario.id), "token_type": "bearer"}, status_code=status.HTTP_200_OK)

#GET test User
@router.get('/user/{cliente_id}', response_model=usuario_schema.AuthUserSchema, status_code=status.HTTP_200_OK)
async def get_user(cliente_id: int, current_user:  usuario_schema.AuthUserSchema = Depends(deps.get_current_user), db: AsyncSession = Depends(deps.get_session_sistemas)):
    async with db as session:
        query = select(user_model.AuthUser).filter(user_model.AuthUser.is_active == 1, user_model.AuthUser.id == current_user.id)
        result = await session.execute(query)
        user: List[user_model.AuthUser] = result.scalar_one_or_none()
        print('acessoLiberado')        
        return user    

# GET Lista Arquivos Relatorios
@router.get('/lista_files_excel/{cliente_id}/{tipo}', response_model=List[relatorio_schema.CtrlArqExcelContabilSchema])
async def get_lista_files_excel(cliente_id: int, tipo: str, current_user:  usuario_schema.AuthUserSchema = Depends(deps.get_current_user), db: AsyncSession = Depends(deps.get_session_gerencial)):
    
    async with db as session:
        query = select(relatorio_model.CtrlArqExcelContabil).filter(relatorio_model.CtrlArqExcelContabil.id_user == int(cliente_id), relatorio_model.CtrlArqExcelContabil.tipo_relatorio == str(tipo))
        result = await session.execute(query)
        lista: List[relatorio_model.CtrlArqExcelContabil] = result.scalars().unique().all()

        return lista

#GET only CLients
@cache(expire=3600)
@router.get('/only_clients/{cliente_id}', response_model=List[cliente_schema.OnlyClienteSchema])
async def get_only_clients(current_user:  usuario_schema.AuthUserSchema = Depends(deps.get_current_user), db: AsyncSession = Depends(deps.get_session_gerencial)):
    async with db as session:
        query = select(home_model.TbClientes).filter(home_model.TbClientes.ativo == 1)        
        result = await session.execute(query)
        clientes: List[home_model.TbClientes] = result.scalars().unique().all()
        return clientes    

# GET Clientes
@router.get('/', response_model=List[cliente_schema.ClienteSchema])
async def get_clientes(db: AsyncSession = Depends(deps.get_session_gerencial)):
    
    async with db as session:
        query = select(home_model.TbClientes)
        result = await session.execute(query)
        clientes: List[home_model.TbClientes] = result.scalars().unique().all()

        return clientes

# GET DwIcmsIpiEntradas
@router.get('/dw/', response_model=List[base_schema.DwIcmsIpiEntradasSchema])
async def get_DwIcmsIpiEntradas(db: AsyncSession = Depends(deps.get_session_gerencial)):
    async with db as session:
        query = '''
        SELECT
            ID_ITEM, CHV_PK, DATA_INI
        FROM
            DB_00820120.dw_icms_ipi_entradas
        WHERE
            DB_00820120.dw_icms_ipi_entradas.ID_ITEM IS NOT NULL
        '''
        result = await session.execute(sa.text(query))
        clientes = result.fetchall()
        
        return clientes

# POST All Relatorios
@router.post('/get_uf_filial/')
@cache(expire=60)
async def get_uf_filial(info : Request, current_user:  usuario_schema.AuthUserSchema = Depends(deps.get_current_user), db: AsyncSession = Depends(deps.get_session_gerencial)):
    async with db as session:
        dados = await info.json()
        dados = dados['post_data']
        base = dados.get('base')
        page = dados.get('page')

        if page == 'b_total_icms_ipi':
            sql = f"""            
                SELECT DISTINCT UF FROM `DB_{base}`.`sped_icms_ipi_ctrl`
            """
        elif page == 'b_total_pis_cofins':
            sql = f"""            
                SELECT 'SP' as UF
            """

        uf_rst = await session.execute(sa.text(sql))

        if page == 'b_total_icms_ipi':
            sql = f"""            
                SELECT DISTINCT
                    DATE_FORMAT( DATA_INI, "%Y" ) DATA_INI 
                FROM
                    DB_{base}.`sped_icms_ipi_ctrl` 
                WHERE
                    `ENVIO` = '1' 
                    AND `CANCELADO` IS NULL 
                    AND `DW_ENTRADAS` = '1' 
                    OR `DW_SAIDAS` = '1'
            """

            data_ini_rst = await session.execute(sa.text(sql))

            sql = f"""
                SELECT DISTINCT CST_ICMS FROM DB_{base}.dw_icms_ipi_entradas 
                UNION
                SELECT DISTINCT CST_ICMS FROM DB_{base}.dw_icms_ipi_saidas 
            """

            cst_ini_rst = await session.execute(sa.text(sql))
            
        elif page == 'b_total_pis_cofins':
            sql = f""" 
                SELECT DISTINCT
                    DATE_FORMAT( DATA_INI, "%Y" ) DATA_INI 
                FROM
                    DB_{base}.`sped_pis_cofins_ctrl` 
                WHERE
                    `ENVIO` = '1' 
                    AND `CANCELADO` IS NULL 
                    AND `DW_ENTRADAS` = '1' 
                    OR `DW_SAIDAS` = '1'
            """
            data_ini_rst = await session.execute(sa.text(sql))

            sql = f"""
                SELECT DISTINCT CST_PIS FROM DB_{base}.dw_pis_cofins_entradas 
                UNION 
                SELECT DISTINCT CST_PIS FROM DB_{base}.dw_pis_cofins_saidas 
            """

            cst_ini_rst = await session.execute(sa.text(sql))
            
        return {               
            "uf": uf_rst.fetchall(),
            "data_ini": data_ini_rst.fetchall(),
            "cst": cst_ini_rst.fetchall(),
        }

# POST Relatorio excel_checklist_icms_ipi_faltantes
@router.post('/excel_checklist_icms_ipi_faltantes')
# @cache(expire=60)
async def excel_checklist_icms_ipi_faltantes(info : Request, background_tasks: BackgroundTasks, current_user:  usuario_schema.AuthUserSchema = Depends(deps.get_current_user)):    
    dados = await info.json()
    dados = json.loads(dados['post_data'])
    base = dados.get('base')
    WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
    try:
        task = excel_checklist_icms_ipi_faltantes_task.delay(dados)
        msg = f"""{str(task.get()).replace("'",'"')}"""
        try:
            WS.send(msg)
        except:
            WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
            WS.send(msg)
        
        await return_email_async("Arquivo Gerado pelo Sistema", dados.get('email'), {
            "title": f"O Sistema gerou um arquivo em formato Excel",
            "page": dados.get('page'),
            "userId" : dados.get('userId'),
            "username" : dados.get('username'),
            "base" : dados.get('base'),
            "nomeEmpresa" : dados.get('nomeEmpresa'),
            "arquivo" : task.get()['msg']
        })

        return {
            "erro": False, 
            "page": f"{dados.get('page')}",
            "rst": "2",
            "userId": f"{dados.get('userId')}",
            "msg":  str(task.get())
        }     
    except Exception as e:
        WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
        await send_email_async("Erro no Sistema", dados.get('email'), {
            "title": f"Ocorreu um erro: { e.args[0] }",
            "page": dados.get('page'),
            "userId" : dados.get('userId'),
            "username" : dados.get('username'),
            "base" : dados.get('base'),
            "nomeEmpresa" : dados.get('nomeEmpresa'),
        })        

        print('erro aqui')

        t =  re.sub('\W+', '', e.args[0])

        x = {
        "data": f"Ocorreu um erro: { t }",
        "userId": f"{dados.get('userId')}",
        "page": f"{dados.get('page')}",
        "erro" : 1
        }
        msg = f"""{str(x).replace("'",'"')}"""
        try:
            WS.send(msg)
        except:
            WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
            WS.send(msg)
        return {
            "erro": "sim", 
            "data": "data",
            "rst": "2"
        }     

# POST Relatorio apuracao_deb_pis_cofins
@router.post('/excel_apuracao_deb_pis_cofins/')
async def excel_apuracao_deb_pis_cofins(info : Request, background_tasks: BackgroundTasks, current_user:  usuario_schema.AuthUserSchema = Depends(deps.get_current_user)):    
    dados = await info.json()
    dados = json.loads(dados['post_data'])
    base = dados.get('base')
    WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
    try:
        task = apuracao_deb_pis_cofins_task.delay(dados)        
        # task = apuracao_deb_pis_cofins_task(dados)        
        msg = f"""{str(task.get()).replace("'",'"')}"""
        try:
            WS.send(msg)
        except:
            WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
            WS.send(msg)
        
        await return_email_async("Arquivo Gerado pelo Sistema", dados.get('email'), {
            "title": f"O Sistema gerou um arquivo em formato Excel",
            "page": dados.get('page'),
            "userId" : dados.get('userId'),
            "username" : dados.get('username'),
            "base" : dados.get('base'),
            "nomeEmpresa" : dados.get('nomeEmpresa'),
            "arquivo" : task.get()['msg']
        })

        return {
            "erro": False, 
            "page": f"{dados.get('page')}",
            "rst": "2",
            "userId": f"{dados.get('userId')}",
            "msg":  str(task.get())
        }     
    except Exception as e:
        WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
        await send_email_async("Erro no Sistema", dados.get('email'), {
            "title": f"Ocorreu um erro: { e.args[0] }",
            "page": dados.get('page'),
            "userId" : dados.get('userId'),
            "username" : dados.get('username'),
            "base" : dados.get('base'),
            "nomeEmpresa" : dados.get('nomeEmpresa'),
        })        

        print('erro aqui')

        t =  re.sub('\W+', '', e.args[0])

        x = {
        "data": f"Ocorreu um erro: { t }",
        "userId": f"{dados.get('userId')}",
        "page": f"{dados.get('page')}",
        "erro" : 1
        }

        msg = f"""{str(x).replace("'",'"')}"""
        try:
            WS.send(msg)
        except:
            WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
            WS.send(msg)
        return {
            "erro": "sim", 
            "data": "data",
            "rst": "2"
        }     


# POST Relatorio apuracao_icms_ipi
@router.post('/excel_apuracao_icms_ipi')
async def excel_apuracao_icms_ipi(info : Request, background_tasks: BackgroundTasks, current_user:  usuario_schema.AuthUserSchema = Depends(deps.get_current_user)):    
    dados = await info.json()
    dados = json.loads(dados['post_data'])
    base = dados.get('base')
    WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
    try:
        task = apuracao_icms_ipi_task.delay(dados)        
        # task = apuracao_icms_ipi_task(dados)        
        msg = f"""{str(task.get()).replace("'",'"')}"""
        try:
            WS.send(msg)
        except:
            WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
            WS.send(msg)
        
        await return_email_async("Arquivo Gerado pelo Sistema", dados.get('email'), {
            "title": f"O Sistema gerou um arquivo em formato Excel",
            "page": dados.get('page'),
            "userId" : dados.get('userId'),
            "username" : dados.get('username'),
            "base" : dados.get('base'),
            "nomeEmpresa" : dados.get('nomeEmpresa'),
            "arquivo" : task.get()['msg']
        })

        return {
            "erro": False, 
            "page": f"{dados.get('page')}",
            "rst": "2",
            "userId": f"{dados.get('userId')}",
            "msg":  str(task.get())
        }     
    except Exception as e:
        WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
        await send_email_async("Erro no Sistema", dados.get('email'), {
            "title": f"Ocorreu um erro: { e.args[0] }",
            "page": dados.get('page'),
            "userId" : dados.get('userId'),
            "username" : dados.get('username'),
            "base" : dados.get('base'),
            "nomeEmpresa" : dados.get('nomeEmpresa'),
        })        

        print('erro aqui')

        t =  re.sub('\W+', '', e.args[0])

        x = {
        "data": f"Ocorreu um erro: { t }",
        "userId": f"{dados.get('userId')}",
        "page": f"{dados.get('page')}",
        "erro" : 1
        }

        msg = f"""{str(x).replace("'",'"')}"""
        try:
            WS.send(msg)
        except:
            WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
            WS.send(msg)
        return {
            "erro": "sim", 
            "data": "data",
            "rst": "2"
        }     

# POST Relatorio balancete_contabil
@router.post('/excel_balancete_contabil')
async def excel_balancete_contabil(info : Request, background_tasks: BackgroundTasks, current_user:  usuario_schema.AuthUserSchema = Depends(deps.get_current_user)):    
    dados = await info.json()
    dados = json.loads(dados['post_data'])
    base = dados.get('base')
    WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
    try:
        # task = balancete_contabil_task.delay(dados)        
        task = balancete_contabil_task(dados)        
        msg = f"""{str(task.get()).replace("'",'"')}"""
        try:
            WS.send(msg)
        except:
            WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
            WS.send(msg)
        
        await return_email_async("Arquivo Gerado pelo Sistema", dados.get('email'), {
            "title": f"O Sistema gerou um arquivo em formato Excel",
            "page": dados.get('page'),
            "userId" : dados.get('userId'),
            "username" : dados.get('username'),
            "base" : dados.get('base'),
            "nomeEmpresa" : dados.get('nomeEmpresa'),
            "arquivo" : task.get()['msg']
        })

        return {
            "erro": False, 
            "page": f"{dados.get('page')}",
            "rst": "2",
            "userId": f"{dados.get('userId')}",
            "msg":  str(task.get())
        }     
    except Exception as e:
        WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
        await send_email_async("Erro no Sistema", dados.get('email'), {
            "title": f"Ocorreu um erro: { e.args[0] }",
            "page": dados.get('page'),
            "userId" : dados.get('userId'),
            "username" : dados.get('username'),
            "base" : dados.get('base'),
            "nomeEmpresa" : dados.get('nomeEmpresa'),
        })        

        print('erro aqui')

        t =  re.sub('\W+', '', e.args[0])

        x = {
        "data": f"Ocorreu um erro: { t }",
        "userId": f"{dados.get('userId')}",
        "page": f"{dados.get('page')}",
        "erro" : 1
        }

        msg = f"""{str(x).replace("'",'"')}"""
        try:
            WS.send(msg)
        except:
            WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
            WS.send(msg)
        return {
            "erro": "sim", 
            "data": "data",
            "rst": "2"
        }     


# POST Relatorio apuracao_cred_pis_cofins
@router.post('/excel_apuracao_cred_pis_cofins/')
async def excel_apuracao_cred_pis_cofins(info : Request, background_tasks: BackgroundTasks, current_user:  usuario_schema.AuthUserSchema = Depends(deps.get_current_user)):    
    dados = await info.json()
    dados = json.loads(dados['post_data'])
    base = dados.get('base')
    WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
    try:
        task = apuracao_cred_pis_cofins_task.delay(dados)        
        # task = apuracao_cred_pis_cofins_task(dados)        
        msg = f"""{str(task.get()).replace("'",'"')}"""
        try:
            WS.send(msg)
        except:
            WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
            WS.send(msg)
        
        await return_email_async("Arquivo Gerado pelo Sistema", dados.get('email'), {
            "title": f"O Sistema gerou um arquivo em formato Excel",
            "page": dados.get('page'),
            "userId" : dados.get('userId'),
            "username" : dados.get('username'),
            "base" : dados.get('base'),
            "nomeEmpresa" : dados.get('nomeEmpresa'),
            "arquivo" : task.get()['msg']
        })

        return {
            "erro": False, 
            "page": f"{dados.get('page')}",
            "rst": "2",
            "userId": f"{dados.get('userId')}",
            "msg":  str(task.get())
        }     
    except Exception as e:
        WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
        await send_email_async("Erro no Sistema", dados.get('email'), {
            "title": f"Ocorreu um erro: { e.args[0] }",
            "page": dados.get('page'),
            "userId" : dados.get('userId'),
            "username" : dados.get('username'),
            "base" : dados.get('base'),
            "nomeEmpresa" : dados.get('nomeEmpresa'),
        })        

        print('erro aqui')

        t =  re.sub('\W+', '', e.args[0])

        x = {
        "data": f"Ocorreu um erro: { t }",
        "userId": f"{dados.get('userId')}",
        "page": f"{dados.get('page')}",
        "erro" : 1
        }

        msg = f"""{str(x).replace("'",'"')}"""
        try:
            WS.send(msg)
        except:
            WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
            WS.send(msg)
        return {
            "erro": "sim", 
            "data": "data",
            "rst": "2"
        }     


# POST Relatorio excel_ajuste_apuracao_icms
@router.post('/excel_ajuste_apuracao_icms/')
# @cache(expire=60)
async def ajuste_apuracao_icms(info : Request, background_tasks: BackgroundTasks, current_user:  usuario_schema.AuthUserSchema = Depends(deps.get_current_user)):    
    dados = await info.json()
    dados = json.loads(dados['post_data'])
    base = dados.get('base')
    WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
    try:
        task = ajuste_apuracao_icms_task.delay(dados)        
        msg = f"""{str(task.get()).replace("'",'"')}"""
        try:
            WS.send(msg)
        except:
            WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
            WS.send(msg)
        
        await return_email_async("Arquivo Gerado pelo Sistema", dados.get('email'), {
            "title": f"O Sistema gerou um arquivo em formato Excel",
            "page": dados.get('page'),
            "userId" : dados.get('userId'),
            "username" : dados.get('username'),
            "base" : dados.get('base'),
            "nomeEmpresa" : dados.get('nomeEmpresa'),
            "arquivo" : task.get()['msg']
        })

        return {
            "erro": False, 
            "page": f"{dados.get('page')}",
            "rst": "2",
            "userId": f"{dados.get('userId')}",
            "msg":  str(task.get())
        }     
    except Exception as e:
        WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
        await send_email_async("Erro no Sistema", dados.get('email'), {
            "title": f"Ocorreu um erro: { e.args[0] }",
            "page": dados.get('page'),
            "userId" : dados.get('userId'),
            "username" : dados.get('username'),
            "base" : dados.get('base'),
            "nomeEmpresa" : dados.get('nomeEmpresa'),
        })        

        print('erro aqui')

        t =  re.sub('\W+', '', e.args[0])

        x = {
        "data": f"Ocorreu um erro: { t }",
        "userId": f"{dados.get('userId')}",
        "page": f"{dados.get('page')}",
        "erro" : 1
        }

        msg = f"""{str(x).replace("'",'"')}"""
        try:
            WS.send(msg)
        except:
            WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
            WS.send(msg)
        return {
            "erro": "sim", 
            "data": "data",
            "rst": "2"
        }     

# POST Relatorio excel_b_total_icms_ipi
@router.post('/excel_b_total_icms_ipi/')
async def xlsx_b_total_icms_ipi(info : Request, background_tasks: BackgroundTasks, current_user:  usuario_schema.AuthUserSchema = Depends(deps.get_current_user)):
    global url_ws, WS    
    dados = await info.json()
    dados = json.loads(dados['post_data'])
    dados = dict(dados)
    base = dados.get('base')
    WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
    try:        
        task = b_total_icms_ipi_task.delay(dados)        

        # msg = f"""{str(task.get()).replace("'",'"')}"""
        # try:
        #     WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
        #     WS.send(msg)
        # except:
        #     WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
        #     WS.send(msg)
        
        await return_email_async("Arquivo Gerado pelo Sistema", dados.get('email'), {
            "title": f"O Sistema gerou um arquivo em formato Excel",
            "page": dados.get('page'),
            "userId" : dados.get('userId'),
            "username" : dados.get('username'),
            "base" : dados.get('base'),
            "nomeEmpresa" : dados.get('nomeEmpresa'),
            "arquivo" : task.get()['msg']
        })

        clear_all_locks()

        return {
            "erro": False, 
            "page": f"{dados.get('page')}",
            "rst": "2",
            "userId": f"{dados.get('userId')}",
            "msg":  str(task.get())
        }     
    except Exception as e:
        WSs = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
        await send_email_async("Erro no Sistema", dados.get('email'), {
            "title": f"Ocorreu um erro: { e.args[0] }",
            "page": dados.get('page'),
            "userId" : dados.get('userId'),
            "username" : dados.get('username'),
            "base" : dados.get('base'),
            "nomeEmpresa" : dados.get('nomeEmpresa'),
        })        

        print('erro aqui')

        t =  re.sub('\W+', '', e.args[0])

        x = {
        "data": f"Ocorreu um erro: { t }",
        "userId": f"{dados.get('userId')}",
        "page": f"{dados.get('page')}",
        "erro" : 1
        }

        msg = f"""{str(x).replace("'",'"')}"""
        try:
            WSs.send(msg)
        except:
            WSs = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
            WSs.send(msg)

        return {
            "erro": "sim", 
            "data": "data",
            "rst": "2"
        }     


# POST All Relatorios
@router.post('/checklist_icms_ipi_faltantes/')
@cache(expire=60)
async def checklist_icms_ipi_faltantes(info : Request, current_user:  usuario_schema.AuthUserSchema = Depends(deps.get_current_user), db: AsyncSession = Depends(deps.get_session_gerencial)):
    async with db as session:
        dados = await info.json()
        dados = json.loads(dados['post_data'])
        base = dados.get('base')

        value = {
            'sql_data' : '',        
        }

        if len(dados.get('data_ini')) > 0 and len(dados.get('data_fim')) > 0:
            value['sql_data'] = f""" 
                AND sped_icms_ipi_ctrl.DATA_INI 
                BETWEEN '{ convertData(dados.get('data_ini'))}' AND '{ convertData(dados.get('data_fim'))}' 
            """
        sql = f"""
            SELECT
                COUNT(*) as qtd
            from
                `DB_{base}`.sped_icms_ipi_ctrl                
            WHERE 
                sped_icms_ipi_ctrl.ENVIO = 1 AND
                sped_icms_ipi_ctrl.CANCELADO IS NULL 
                {value['sql_data']}                    
        """ 

        result = await session.execute(sa.text(sql))
        qtd = result.scalar_one_or_none()
        data_ =  'Perfeito para o excel'
        erro = False

        if int(qtd) > 1000000:
            data_ = 'Acima do excel'
            erro = True
        
        return {
            "erro": erro, 
            "data": data_,
            "rst": str(qtd)
        }     


# POST All Relatorios
@router.post('/apuracao_icms_ipi/')
# @cache(expire=60)
async def apuracao_icms_ipi(info : Request, current_user:  usuario_schema.AuthUserSchema = Depends(deps.get_current_user), db: AsyncSession = Depends(deps.get_session_gerencial)):
    async with db as session:
        dados = await info.json()
        dados = json.loads(dados['post_data'])
        base = dados.get('base')
        filtro = dados.get('tipoFiltro')

        value = {
            'sql_data' : '',        
        }

        if len(dados.get('data_ini')) > 0 and len(dados.get('data_fim')) > 0:
            value['sql_data'] = f""" 
                AND sped_icms_ipi_ctrl.DATA_INI 
                BETWEEN '{ convertData(dados.get('data_ini'))}' AND '{ convertData(dados.get('data_fim'))}' 
            """

        sql = f"""
            SELECT
                    COUNT(*) as qtd
                from
                    `DB_{base}`.sped_icms_ipi_E110
                INNER JOIN 
                    `DB_{base}`.sped_icms_ipi_ctrl ON
                    sped_icms_ipi_E110.ID_SPEDFIS_CTRL_REG_0000 = sped_icms_ipi_ctrl.ID_SPEDFIS_CTRL_REG_0000
                WHERE 
                    sped_icms_ipi_ctrl.ENVIO = 1 AND
	                sped_icms_ipi_ctrl.CANCELADO IS NULL 
                    {value['sql_data']}                     
        """ 

        if filtro == 'ipi':

            sql = f"""
                SELECT
                    COUNT(*) as qtd
                from
                    `DB_{base}`.sped_icms_ipi_ctrl
                    INNER JOIN
                    `DB_{base}`.sped_icms_ipi_E520
                    ON 
                        sped_icms_ipi_ctrl.ID_SPEDFIS_CTRL_REG_0000 = sped_icms_ipi_E520.ID_SPEDFIS_CTRL_REG_0000
                WHERE 
                    sped_icms_ipi_ctrl.ENVIO = 1 AND
                    sped_icms_ipi_ctrl.CANCELADO IS NULL
                    {value['sql_data']}
            """
            

        result = await session.execute(sa.text(sql))
        qtd = max(result.fetchall())[0]
        data_ =  'Perfeito para o excel'
        erro = False

        if int(qtd) > 1000000:
            data_ = 'Acima do excel'
            erro = True
        
        return {
            "erro": erro, 
            "data": data_,
            "rst": str(qtd)
        }


# POST All Relatorios
@router.post('/b_total_icms_ipi/')
# @cache(expire=60)
async def b_total_icms_ipi(info : Request, current_user:  usuario_schema.AuthUserSchema = Depends(deps.get_current_user), db: AsyncSession = Depends(deps.get_session_gerencial)):
    async with db as session:
        dados = await info.json()
        dados = json.loads(dados['post_data'])
        base = dados.get('base')
        
        value = {
            'DATA_INI' : '',
            'UF_FILIAL' : '',
            'CNPJ_FILIAL' : '',
            'CST' : ''
        }

        if len(dados.get('data_ini')) > 0 and len(dados.get('data_fim')) > 0:
            value['sql_data'] = f""" 
                AND DATA_INI 
                BETWEEN '{ convertData(dados.get('data_ini'))}' AND '{ convertData(dados.get('data_fim'))}' 
            """

        if len(dados.get('cst')) > 0:
            value['CST'] = f" AND CST_ICMS = {dados.get('cst')[0]}" if len(dados.get('cst')) == 1 else f" AND CST_ICMS in {str(tuple(dados.get('cst')))}"

        if len(dados.get('uf')) > 0:
            value['UF_FILIAL'] = f"  AND UF_FILIAL = '{str(dados.get('uf'))}' "

        if len(dados.get('cnpj_filial')) > 0:

            quebra_cnpj = dados.get('cnpj_filial').split(',')
            value['CNPJ_FILIAL'] = f" AND `CNPJ_FILIAL` = '{str(dados.get('cnpj_filial'))}'"

            if len(quebra_cnpj) > 1:
                value['CNPJ_FILIAL'] = f" AND `CNPJ_FILIAL` IN {str(tuple([ str(x) for x in quebra_cnpj]))}"        

        sql = f"""
        SELECT
                dw_icms_ipi_entradas.ID_ITEM,
                dw_icms_ipi_entradas.VL_ITEM,
                dw_icms_ipi_entradas.CFOP,
                CNPJ_FILIAL
            FROM
                `DB_{base}`.dw_icms_ipi_entradas
            WHERE
                ID_ITEM IS NOT NULL 
                {value['DATA_INI']} 
                {value['UF_FILIAL']} 
                {value['CNPJ_FILIAL']}
                {value['CST']}             
        """ 

        if dados.get('filtrEntradaSaida') == 'ambos':
            sql = f"""        
            SELECT
                dw_icms_ipi_saidas.ID_ITEM,
                dw_icms_ipi_saidas.VL_ITEM,
                dw_icms_ipi_saidas.CFOP,
                CNPJ_FILIAL
            FROM
                `DB_{base}`.dw_icms_ipi_saidas
            WHERE
                ID_ITEM IS NOT NULL
                {value['DATA_INI']} 
                {value['UF_FILIAL']} 
                {value['CNPJ_FILIAL']}
                {value['CST']}
            UNION
            SELECT
                dw_icms_ipi_entradas.ID_ITEM,
                dw_icms_ipi_entradas.VL_ITEM,
                dw_icms_ipi_entradas.CFOP,
                CNPJ_FILIAL
            FROM
                `DB_{base}`.dw_icms_ipi_entradas
            WHERE
                ID_ITEM IS NOT NULL 
                {value['DATA_INI']} 
                {value['UF_FILIAL']} 
                {value['CNPJ_FILIAL']}
                {value['CST']}                
            """
        elif dados.get('filtrEntradaSaida') == 'saida':
            sql = f"""        
            SELECT
                dw_icms_ipi_saidas.ID_ITEM,
                dw_icms_ipi_saidas.VL_ITEM,
                dw_icms_ipi_saidas.CFOP,
                CNPJ_FILIAL
            FROM
                `DB_{base}`.dw_icms_ipi_saidas
            WHERE
                ID_ITEM IS NOT NULL
                {value['DATA_INI']} 
                {value['UF_FILIAL']} 
                {value['CNPJ_FILIAL']}
                {value['CST']}
            """

        result = await session.execute(sa.text(sql))
        rst2 = pd.DataFrame(data=result.fetchall())
        rst2['CFOP'].fillna('9999', inplace=True)

        df_linhas = pd.DataFrame()
        vl_item =  rst2.groupby(rst2['CFOP'])['VL_ITEM'].sum()
        qtd_linhas  = rst2.groupby(rst2['CFOP'])['VL_ITEM'].count()

        df_linhas['NULL'] = 'null'
        df_linhas['CFOP'] = qtd_linhas.index
        df_linhas['VL_ITEM'] = vl_item.values
        df_linhas['QTD_LINHAS'] = qtd_linhas.values
        df_linhas['PROPOR_VALOR'] = list(map('{:.2f}%'.format,( qtd_linhas.values / qtd_linhas.sum())))
        df_linhas['PROPOR_LINHAS'] = list(map('{:.2f}%'.format,( vl_item.values / vl_item.sum())))

        sql = f"""             
            SELECT tb_cfop.ICMS, 
            tb_cfop.IPI,
            tb_cfop.CFOP as ID
        FROM
            gerencial.tb_cfop     
            """
        result = await session.execute(sa.text(sql))
        df1 = pd.DataFrame(data=result.fetchall())

        df2 = pd.merge(df_linhas,df1, how='left', left_on='CFOP', right_on='ID')
        df2.fillna(0, inplace=True)
        df2.drop(columns='ID', inplace=True)

        sql = f"""             
            SELECT cfop FROM `gerencial`.`cfop_credito`;
        """
        result = await session.execute(sa.text(sql))
        df_ = pd.DataFrame(data=result.fetchall())

        df2['GERADOR_CRED_PVA'] = df2['CFOP'].apply(lambda x: x in list(df_['cfop']))
        df2['GERADOR_CRED_PVA'] = df2['GERADOR_CRED_PVA'].replace(True,'SIM')
        df2['GERADOR_CRED_PVA'] = df2['GERADOR_CRED_PVA'].replace(False,'NÃO')

        result = df2.to_json(orient="split")
        parsed = json.loads(result)
               
        return { 
            "erro": False,
            "data": parsed,
            "rst": str(len(rst2))            
        }


# POST All Relatorios
@router.post('/balancete_contabil/')
# @cache(expire=60)
async def balancete_contabil(info : Request, current_user:  usuario_schema.AuthUserSchema = Depends(deps.get_current_user), db: AsyncSession = Depends(deps.get_session_gerencial)):
    async with db as session:
        dados = await info.json()
        dados = json.loads(dados['post_data'])
        base = dados.get('base')
        
        value = {
            'sql_data' : '',        
            'sql_codnatureza' : '',        
            'sql_codcta' : '',        
        }

        if len(dados.get('data_ini')) > 0 and len(dados.get('data_fim')) > 0:
            value['sql_data'] = f""" 
                AND dw_balancete_contabil_geral.DT_FIN 
                BETWEEN '{ convertData(dados.get('data_ini'))}' AND '{ convertData(dados.get('data_fim'))}' 
            """
        
        if len(dados.get('codNatureza')) > 0:
            value['sql_codnatureza'] = f" AND `COD_NAT` = '{str(dados.get('codNatureza'))}' "

        
        if len(dados.get('codConta')) > 0:
            quebra_contas = dados.get('codConta').split(',')

            if len(quebra_contas) > 1:
                value['sql_codcta'] = f" AND `COD_CTA` IN {str(tuple([ str(x).strip() for x in quebra_contas]))}"
            else:
                value['sql_codcta'] = f" AND `COD_CTA` = '{str(dados.get('codConta'))}'"

                   
        sql = f"""
            SELECT count(*) as qtd FROM `DB_{base}`.`dw_balancete_contabil_geral` 
                WHERE `DT_ESCRIT` IS NOT NULL 
                    {value['sql_data']} 
                    {value['sql_codnatureza']} 
                    {value['sql_codcta']}            
        """ 

        result = await session.execute(sa.text(sql))
        qtd = max(result.fetchall())[0]
        data_ =  'Perfeito para o excel'
        erro = False

        if int(qtd) > 1000000:
            data_ = 'Acima do excel'
            erro = True
        
        return {
            "erro": erro, 
            "data": data_,
            "rst": str(qtd)
        }


# POST All Relatorios
@router.post('/apuracao_cred_pis_cofins/')
# @cache(expire=60)
async def apuracao_cred_pis_cofins(info : Request, current_user:  usuario_schema.AuthUserSchema = Depends(deps.get_current_user), db: AsyncSession = Depends(deps.get_session_gerencial)):
    async with db as session:
        dados = await info.json()
        dados = json.loads(dados['post_data'])
        base = dados.get('base')

        value = {
            'sql_data' : '',        
        }

        if len(dados.get('data_ini')) > 0 and len(dados.get('data_fim')) > 0:
            value['sql_data'] = f""" 
                AND sped_pis_cofins_ctrl.DATA_INI 
                BETWEEN '{ convertData(dados.get('data_ini'))}' AND '{ convertData(dados.get('data_fim'))}' 
            """

        sql = f"""
         SELECT
                COUNT(*) as qtd
            FROM
                `DB_{base}`.sped_pis_cofins_M100
            INNER JOIN
            `DB_{base}`.sped_pis_cofins_ctrl
            ON
                sped_pis_cofins_M100.ID_EFD_CTRL_REG_0000 = sped_pis_cofins_ctrl.ID_SPEDFIS_CTRL_REG_0000
            WHERE
                sped_pis_cofins_ctrl.CANCELADO IS NULL
                AND
            sped_pis_cofins_ctrl.ENVIO = 1
                
            UNION

            SELECT
                COUNT(*) as qtd
            FROM
                `DB_{base}`.sped_pis_cofins_M500
            INNER JOIN
            `DB_{base}`.sped_pis_cofins_ctrl
            ON
                sped_pis_cofins_M500.ID_EFD_CTRL_REG_0000 = sped_pis_cofins_ctrl.ID_SPEDFIS_CTRL_REG_0000
            WHERE
                sped_pis_cofins_ctrl.CANCELADO IS NULL
                AND
            sped_pis_cofins_ctrl.ENVIO = 1	
                {value['sql_data']}                 
        """ 

        result = await session.execute(sa.text(sql))
        qtd = max(result.fetchall())[0]
        data_ =  'Perfeito para o excel'
        erro = False

        if int(qtd) > 1000000:
            data_ = 'Acima do excel'
            erro = True
        
        return {
            "erro": erro, 
            "data": data_,
            "rst": str(qtd)
        }

# POST All Relatorios
@router.post('/apuracao_deb_pis_cofins/')
# @cache(expire=60)
async def apuracao_deb_pis_cofins(info : Request, current_user:  usuario_schema.AuthUserSchema = Depends(deps.get_current_user), db: AsyncSession = Depends(deps.get_session_gerencial)):
    async with db as session:
        dados = await info.json()
        dados = json.loads(dados['post_data'])
        base = dados.get('base')

        value = {
            'sql_data' : '',        
        }

        if len(dados.get('data_ini')) > 0 and len(dados.get('data_fim')) > 0:
            value['sql_data'] = f""" 
                AND sped_pis_cofins_ctrl.DATA_INI 
                BETWEEN '{ convertData(dados.get('data_ini'))}' AND '{ convertData(dados.get('data_fim'))}' 
            """

        sql = f"""
            SELECT
                    COUNT(*) as qtd
                FROM
                    `DB_{base}`.sped_pis_cofins_ctrl
                INNER JOIN
                    `DB_{base}`.sped_pis_cofins_M200
                ON
                    sped_pis_cofins_ctrl.ID_SPEDFIS_CTRL_REG_0000 = sped_pis_cofins_M200.ID_EFD_CTRL_REG_0000
                WHERE
                    sped_pis_cofins_ctrl.CANCELADO IS NULL
                    AND
                    sped_pis_cofins_ctrl.ENVIO = 1
                    {value['sql_data']}

                UNION

                SELECT
                    COUNT(*) as qtd
                FROM
                    `DB_{base}`.sped_pis_cofins_ctrl
                INNER JOIN
                    `DB_{base}`.sped_pis_cofins_M600
                ON
                    sped_pis_cofins_ctrl.ID_SPEDFIS_CTRL_REG_0000 = sped_pis_cofins_M600.ID_EFD_CTRL_REG_0000
                WHERE
                    sped_pis_cofins_ctrl.CANCELADO IS NULL
                    AND
                    sped_pis_cofins_ctrl.ENVIO = 1                    
                    {value['sql_data']}
        """ 

        result = await session.execute(sa.text(sql))
        qtd = max(result.fetchall())[0]
        data_ =  'Perfeito para o excel'
        erro = False

        if int(qtd) > 1000000:
            data_ = 'Acima do excel'
            erro = True
        
        return {
            "erro": erro, 
            "data": data_,
            "rst": str(qtd)
        }


# POST All Relatorios
@router.post('/ajuste_apuracao_icms/')
# @cache(expire=60)
async def ajuste_apuracao_icms(info : Request, current_user:  usuario_schema.AuthUserSchema = Depends(deps.get_current_user), db: AsyncSession = Depends(deps.get_session_gerencial)):
    async with db as session:
        dados = await info.json()
        dados = json.loads(dados['post_data'])
        base = dados.get('base')

        value = {
            'sql_data' : '',        
        }

        if len(dados.get('data_ini')) > 0 and len(dados.get('data_fim')) > 0:
            value['sql_data'] = f""" 
                AND sped_icms_ipi_ctrl.DATA_INI 
                BETWEEN '{ convertData(dados.get('data_ini'))}' AND '{ convertData(dados.get('data_fim'))}' 
            """
        sql = f"""
            SELECT
                COUNT(*) as qtd
            from
                `DB_{base}`.sped_icms_ipi_ctrl
                INNER JOIN
                `DB_{base}`.sped_icms_ipi_E111
                ON 
                    sped_icms_ipi_ctrl.ID_SPEDFIS_CTRL_REG_0000 = sped_icms_ipi_E111.ID_SPEDFIS_CTRL_REG_0000
            WHERE 
                sped_icms_ipi_ctrl.ENVIO = 1 AND
                sped_icms_ipi_ctrl.CANCELADO IS NULL 
                {value['sql_data']}                    
        """ 

        result = await session.execute(sa.text(sql))
        qtd = result.scalar_one_or_none()
        data_ =  'Perfeito para o excel'
        erro = False

        if int(qtd) > 1000000:
            data_ = 'Acima do excel'
            erro = True
        
        return {
            "erro": erro, 
            "data": data_,
            "rst": str(qtd)
        }     


# GET data inicial empresa
@router.get('/get_data_empresa/{base}/{tipo}')
@cache_one_minute()
async def get_empresa_dataIni(base: str, tipo: str, current_user:  usuario_schema.AuthUserSchema = Depends(deps.get_current_user), db: AsyncSession = Depends(deps.get_session_gerencial)):
    async with db as session:
        if tipo == 'ajuste_apuracao_icms' or tipo == 'apuracao_icms_ipi'or tipo == 'gerar_sped_fiscal':
            sql = f"""            
                SELECT DISTINCT
                    DATE_FORMAT( DATA_INI, "%Y" ) DATA_INI 
                FROM
                    `DB_{base}`.`sped_icms_ipi_ctrl` 
                WHERE
                    `ENVIO` = '1' 
                    AND `CANCELADO` IS NULL 
                    AND `DW_ENTRADAS` = '1' 
                    OR `DW_SAIDAS` = '1'
            """
        elif tipo == 'apuracao_cred_pis_cofins' or tipo == 'apuracao_deb_pis_cofins' or tipo == 'gerar_registros_efd':        
            sql = f"""            
                SELECT DISTINCT
                    DATE_FORMAT( DATA_INI, "%Y" ) DATA_INI 
                FROM
                    `DB_{base}`.`sped_pis_cofins_ctrl` 
                WHERE
                    `ENVIO` = '1' 
                    AND `CANCELADO` IS NULL 
                    AND `DW_ENTRADAS` = '1' 
                    OR `DW_SAIDAS` = '1'               
            """
        elif tipo == 'balancete_contabil' or tipo == 'razao_contabil' or tipo == 'b_contabil_saldo_final_conta_i355':        
            sql = f"""            
                SELECT DISTINCT
                    DATE_FORMAT( DATA_INI, "%Y" ) DATA_INI 
                FROM
                    `DB_{base}`.`sped_contabil_ctrl` 
                WHERE
                    `ENVIO` = '1' 
                    AND `CANCELADO` IS NULL 
            """
        elif tipo in ('conciliar_sped_efd','checklist_icms_ipi_faltantes'):
            sql = f"""            
                SELECT DISTINCT
                    DATE_FORMAT( DATA_INI, "%Y" ) DATA_INI 
                FROM
                    `DB_{base}`.`sped_pis_cofins_ctrl` 
                WHERE
                    `ENVIO` = '1' 
                    AND `CANCELADO` IS NULL 
                    AND `DW_ENTRADAS` = '1' 
                    OR `DW_SAIDAS` = '1' UNION
                SELECT DISTINCT
                    DATE_FORMAT( DATA_INI, "%Y" ) DATA_INI 
                FROM
                    `DB_{base}`.`sped_icms_ipi_ctrl` 
                WHERE
                    `ENVIO` = '1' 
                    AND `CANCELADO` IS NULL 
                    AND `DW_ENTRADAS` = '1' 
                    OR `DW_SAIDAS` = '1'
            """

        result = await session.execute(sa.text(sql))
        
        return {               
            'data_ini': result.fetchall()
        }

#GET get_combo_charts
@router.get('/get_combo_charts/{base}')
async def get_filial_uf_dataIni(base: str, current_user:  usuario_schema.AuthUserSchema = Depends(deps.get_current_user), db: AsyncSession = Depends(deps.get_session_gerencial)):
    async with db as session:
        sql = f"""            
                SELECT DISTINCT `CNPJ_FILIAL` FROM `DB_{base}`.`dw_pis_cofins_entradas`;
            """        
        
        result = await session.execute(sa.text(sql))
        d_cnpj_filial = result.fetchall()

        sql = f"""            
            SELECT DISTINCT DATE_FORMAT( DATA_INI, "%Y" ) DATA_INI FROM `DB_{base}`.`sped_icms_ipi_ctrl` WHERE `ENVIO` = '1' AND `CANCELADO` IS NULL AND `DW_ENTRADAS` = '1' OR `DW_SAIDAS` = '1'
            UNION
            SELECT DISTINCT DATE_FORMAT( DATA_INI, "%Y" ) DATA_INI FROM `DB_{base}`.`sped_pis_cofins_ctrl` WHERE `ENVIO` = '1' AND `CANCELADO` IS NULL AND `DW_ENTRADAS` = '1' OR `DW_SAIDAS` = '1';
            """
        
        result = await session.execute(sa.text(sql))
        d_data_ini = result.fetchall()

        sql = f"""            
                SELECT DISTINCT `UF` FROM `DB_{base}`.`sped_icms_ipi_ctrl` WHERE `ENVIO` = '1' AND `CANCELADO` IS NULL AND `DW_ENTRADAS` = '1' OR `DW_SAIDAS` = '1';
                
            """
        
        result = await session.execute(sa.text(sql))
        d_uf = result.fetchall()

        dados = {
                'cnpj_filial':d_cnpj_filial,
                'uf': d_uf,
                'data_ini': d_data_ini
            }
        
        return dados   

# DELETE tables
@router.delete('/del_table')
async def del_table(info : Request, current_user:  usuario_schema.AuthUserSchema = Depends(deps.get_current_user), db: AsyncSession = Depends(deps.get_session_gerencial)):
    dados = await info.json()
    WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
    x = {
        "data": f"Aguarde procurando o arquivo!",
        "userId": f"{dados['post_data']['userId']}",
        "page": f"{dados['post_data']['page']}",
        "erro" : 0
    }
    msg = f"""{str(x).replace("'",'"')}"""
    try:
        WS.send(msg)
    except:
        WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
        WS.send(msg)

    async with db as session:        
        id = dados['post_data']['data'].split('|')[0]
        
        sql = f"""
           SELECT nome_arquivo FROM gerencial.ctrl_arq_excel_contabil WHERE id = {id}               
        """

        result = await session.execute(sa.text(sql))
        nome_file = result.scalar_one_or_none()

        urlxls = __file__.replace('/api/v1/endpoints/home.py', '/media/')+nome_file

        if os.path.exists(urlxls):
            os.remove(urlxls)
            x = {
                "data": f"Arquivo encontrado e removido",
                "userId": f"{dados['post_data']['userId']}",
                "page": f"{dados['post_data']['page']}",
                "erro" : 0
            }
            msg = f"""{str(x).replace("'",'"')}"""
        try:
            WS.send(msg)
        except:
            WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
            WS.send(msg)
        else:
            erro = True
            msg_ = f'O Arquivo não existe: {urlxls}'
            x = {
                "data": f"Arquivo não encontrado",
                "userId": f"{dados['post_data']['userId']}",
                "page": f"{dados['post_data']['page']}",
                "erro" : 1
            }
            msg = f"""{str(x).replace("'",'"')}"""
        try:
            WS.send(msg)
        except:
            WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
            WS.send(msg)

        sql = f"""
           DELETE FROM `gerencial`.`ctrl_arq_excel_contabil` WHERE `id` = {id}         
        """

        result = await session.execute(sa.text(sql))
        teste = await session.commit()
        if result.rowcount > 0:
            erro = False
            msg_ = f'Arquivo Deletado com Sucesso: {urlxls}'
        else:
            erro = True
            msg_ = f'Erro ao limpar do banco de dados: {urlxls}'

        return {"erro": erro, 'data': msg_}

# DELETE table ajuste_apuracao_icms
@router.delete('/del_table_ajuste_apuracao_icms')
async def del_ajuste_apuracao_icms(info : Request, current_user:  usuario_schema.AuthUserSchema = Depends(deps.get_current_user), db: AsyncSession = Depends(deps.get_session_gerencial)):
    dados = await info.json()
    WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
    x = {
        "data": f"Aguarde procurando o arquivo!",
        "userId": f"{dados['post_data']['userId']}",
        "page": f"{dados['post_data']['page']}",
        "erro" : 0
    }
    msg = f"""{str(x).replace("'",'"')}"""
    try:
        WS.send(msg)
    except:
        WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
        WS.send(msg)

    async with db as session:        
        id = dados['post_data']['data'].split('|')[0]
        
        sql = f"""
           SELECT nome_arquivo FROM gerencial.ctrl_arq_excel_contabil WHERE id = {id}               
        """

        result = await session.execute(sa.text(sql))
        nome_file = result.scalar_one_or_none()

        urlxls = __file__.replace('/api/v1/endpoints/home.py', '/media/')+nome_file

        if os.path.exists(urlxls):
            os.remove(urlxls)
            x = {
                "data": f"Arquivo encontrado e removido",
                "userId": f"{dados['post_data']['userId']}",
                "page": f"{dados['post_data']['page']}",
                "erro" : 0
            }
            msg = f"""{str(x).replace("'",'"')}"""
        try:
            WS.send(msg)
        except:
            WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
            WS.send(msg)
        else:
            erro = True
            msg_ = f'O Arquivo não existe: {urlxls}'
            x = {
                "data": f"Arquivo não encontrado",
                "userId": f"{dados['post_data']['userId']}",
                "page": f"{dados['post_data']['page']}",
                "erro" : 1
            }
            msg = f"""{str(x).replace("'",'"')}"""
        try:
            WS.send(msg)
        except:
            WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
            WS.send(msg)

        sql = f"""
           DELETE FROM `gerencial`.`ctrl_arq_excel_contabil` WHERE `id` = {id}         
        """

        result = await session.execute(sa.text(sql))
        teste = await session.commit()
        if result.rowcount > 0:
            erro = False
            msg_ = f'Arquivo Deletado com Sucesso: {urlxls}'
        else:
            erro = True
            msg_ = f'Erro ao limpar do banco de dados: {urlxls}'

        return {"erro": erro, 'data': msg_}




# def write_notification(email: str, message=""):
#     with open("log.txt", mode="w") as email_file:
#         content = f"notification for {email}: {message}"
#         email_file.write(content)


# @app.post("/send-notification/{email}")
# async def send_notification(email: str, background_tasks: BackgroundTasks):
#     background_tasks.add_task(write_notification, email, message="some notification")
#     return {"message": "Notification sent in the background"}


# GET Cliente
# @router.get('/{cliente_id}', response_model=TbClientes, status_code=status.HTTP_200_OK)
# async def get_cliente(cliente_id: int, db: AsyncSession = Depends(get_session)):
#     async with db as session:
#         query = select(TbClientes).filter(TbClientes.id_cliente == cliente_id)
#         result = await session.execute(query)
#         cliente = TbClientes = result.scalar_one_or_none()

#         if cliente:
#             return cliente
#         else:
#             raise HTTPException(detail='Cliente não encontrado', status_code=status.HTTP_404_NOT_FOUND)

