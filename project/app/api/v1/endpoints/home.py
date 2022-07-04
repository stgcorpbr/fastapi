
from datetime import datetime
import json
import random
import sqlalchemy as sa

from typing import List
from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession

from core import deps
from models import home_model, user_model, relatorio_model
from core.auth import autenticar, criar_token_acesso
from core.celery_worker import ajuste_apuracao_icms_task
from websocket import create_connection

from schemas import cliente_schema, base_schema, usuario_schema, relatorio_schema
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse
from fastapi import Request, APIRouter, WebSocket, status, Depends, HTTPException
from fastapi_redis_cache import cache
from fastapi_redis_cache import cache_one_minute
from fastapi.responses import FileResponse
import requests

import socketio

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

# POST Relatorio excel_ajuste_apuracao_icms
@router.post('/excel_ajuste_apuracao_icms/')
# @cache(expire=60)
async def ajuste_apuracao_icms(info : Request, current_user:  usuario_schema.AuthUserSchema = Depends(deps.get_current_user)):    
    dados = await info.json()
    dados = json.loads(dados['post_data'])
    base = dados.get('base')
    ws = create_connection(f"wss://stgapi.cf:7000/ws/{random.randint(10000, 99999)}")
    try:
        task = ajuste_apuracao_icms_task.delay(dados)        
        ws.send(str(task.get()).replace("'",'"'))
    except Exception as e:        
        print('erro aqui')
        x = {
        "data": f"Ocorreu um erro: { e._sql_message.__self__.statement }",
        "userId": f"{dados.get('userId')}",
        "page": f"{dados.get('page')}",
        "erro" : 1
        }
        ws.send(str(x).replace("'",'"'))


# POST All Relatorios
@router.post('/ajuste_apuracao_icms/')
@cache(expire=60)
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
        elif tipo == 'conciliar_sped_efd':            
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

