from ast import Global
import json
import os
import random

from pathlib import Path
from datetime import datetime
from celery.signals import celeryd_init
from celery_singleton import Singleton, DuplicateTaskError
from celery_singleton.singleton import clear_locks
from celery import Celery, shared_task
from celery.utils.log import get_task_logger
# from celery.schedules  import crontab

import pandas as pd
from pyexcelerate import Workbook

from websocket import create_connection
from sqlalchemy import create_engine, text
import xlsxwriter
from core.configs import settings
from core.utils import *
from . import mail


# Initialize celery
celery_ = Celery(
    'tasks',
    broker=f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}/{settings.REDIS_DB}",
    backend=f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}/{settings.REDIS_DB}"
)

# Create logger - enable to display messages on task logger
celery_log = get_task_logger(__name__)

celery_.conf.imports = [
    'core.tasks'
]

celery_.conf.update(
    {
        "task_routes": {
            "worker.alert_celery": {"queue": "piport-celery"},
            "worker.schedule_task": {"queue": "beat-queue"},
        }
    }
)

# URL_CONNECT = "mysql+aiomysql://userdb:SysDb123#ee@stgbd.cf"
URL_CONNECT = "mysql+pymysql://userdb:SysDb123#ee@stgbd.cf"
BASE_DIR = Path(__file__).resolve().parent.parent

def notify(msg, ws, rs):
    if msg == 'fim': ws.send(msg)
    x = {
        "data": f"{msg}",
        "userId": f"{rs['userId']}",
        "page": f"{rs['page']}"
        }
    try: 
        ws.send(str(x).replace("'",'"'))
        return True
    except:
        return False


@celery_.on_after_configure.connect
def schedule_periodic_tasks(sender, **kwargs):
    pass

    # sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')

    # sender.add_periodic_task(5.0, test.s('world'), expires=10)

    # Executes every Monday morning at 7:30 am
    # sender.add_periodic_task(crontab(minute='*/1'), test.s('email') )

@celery_.task
def test(arg):
    print(arg)
    # Display log    
    celery_log.info(f"Order Complete!")

@shared_task
def send_email(email):
    print('dentro da função')
    return mail.core_notification(email)

@shared_task
def excel_checklist_icms_ipi_faltantes_task(rs):

    try:
        WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
    except Exception as e:
        raise e 

    dataagora = datetime.now().strftime("%d%m%Y%H%M%S")
    value = {'sql_data': ''}
    base = rs.get('base')

    data1 = convertData(rs.get('data_ini'))
    data2 = convertData(rs.get('data_fim'))

    if len(rs.get('data_ini')) > 0 and len(rs.get('data_fim')) > 0:
         value['sql_data'] = f"""
            AND sped_icms_ipi_ctrl.DATA_INI BETWEEN '{data1}' AND '{data2}'
      """    

    msg = f'Conectando com a Base: DB_{base}'
    if notify(f'{msg}', WS, rs) == False: 
        WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
        notify(f'{msg}', WS, rs)

    try:
        engine = create_engine(f"{URL_CONNECT}/DB_{base}")
    except Exception as e:
        raise e

    msg = f'Base conectada'
    if notify(f'{msg}', WS, rs) == False: 
        WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
        notify(f'{msg}', WS, rs)

    sql = f"""
        SELECT
                COUNT(*) as qtd
            from
                sped_icms_ipi_ctrl    
            WHERE
                sped_icms_ipi_ctrl.ENVIO = 1 AND
                sped_icms_ipi_ctrl.CANCELADO IS NULL
            {value['sql_data']}
            """

    try:
        with engine.connect() as conn:
            rst = pd.read_sql_query(sql, conn)
    except Exception as e:
        raise e

    if len(rst) < 1000000:
        df = pd.DataFrame(columns=['cnpj', 'data1', 'data2'])
        msg = f'Ok abaixo de 1 milhão OK'
    if notify(f'{msg}', WS, rs) == False: 
        WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
        notify(f'{msg}', WS, rs)
        
        sql = text(f"""
            SELECT DISTINCT CNPJ FROM `DB_{base}`.`sped_icms_ipi_ctrl`
        """)

        try:
            with engine.connect() as conn:
                for row in conn.execute(sql):
                    qry = text(f"""
                        SELECT
                            COUNT(sped_icms_ipi_ctrl.CNPJ) AS CONTADOR
                        FROM
                            `DB_{base}`.sped_icms_ipi_ctrl
                        WHERE
                            sped_icms_ipi_ctrl.DATA_INI BETWEEN '{data1}' AND '{data2}'
                            AND sped_icms_ipi_ctrl.CNPJ = '{row[0]}'
                        """)
                    for rst_ in conn.execute(qry):                        
                        if dif_month(data1, data2) != rst_[0]:
                            print(dif_month(data1, data2),rst_[0], row[0])
                            df.loc[len(df)] = [row[0], data1, data2]
        except Exception as e:
            raise e

        
        # montando o primeiro sheet sem conflitar com o segundo sheet por isso o x1
        df_x1 = pd.date_range(start=data1,end=data2, freq=pd.offsets.MonthBegin(1))
        x1_list_y1= list(df_x1.strftime('%d/%m/%Y'))
        x1_col= list(df_x1.strftime('%d/%m/%Y'))
        x1_list_y1.insert(0,'FILIAL')
        x1_df_new = pd.DataFrame(columns=x1_list_y1)

        with engine.connect() as connection:        
            for index, row in df.iterrows():     
                g = []
                sql = text(f"""
                SELECT                    
                    DATA_INI
                FROM
                    sped_icms_ipi_ctrl
                WHERE
                    sped_icms_ipi_ctrl.DATA_INI BETWEEN '{row['data1']}' AND '{row['data2']}' AND
                    sped_icms_ipi_ctrl.CNPJ = '{row['cnpj']}'
                """)
                rst_ = connection.execute(sql)

                if len(list(connection.execute(sql).scalars().unique().all())) <= 0:
                    for t in x1_col:                
                        g.insert(0, 'N')
                    g.insert(0, row['cnpj'])                    
                    x1_df_new.loc[index] = g
                    g = []
                else:
                    for _,r in enumerate(rst_):
                        for t in x1_col:
                            if str(type(r[0])) != "<class 'datetime.date'>":
                                g.insert(0, 'N')                
                            elif str(t) == str(r[0].strftime('%d/%m/%Y')):
                                g.insert(0, 'S')                
                            else:
                                g.insert(0, 'N')
                        g.insert(0, row['cnpj'])                        
                        x1_df_new.loc[index] = g
                        g = []

        df_new = pd.DataFrame(columns=['FILIAL', 'DATA'])

        with engine.connect() as connection:
            for _, row in df.iterrows():
                
                sql = text(f"""
                    SELECT
                        DATA_INI
                    FROM
                        sped_icms_ipi_ctrl
                    WHERE
                        sped_icms_ipi_ctrl.DATA_INI BETWEEN '{row['data1']}' AND '{row['data2']}' AND
                        sped_icms_ipi_ctrl.CNPJ = '{row['cnpj']}'
                """)

                try:                
                    df2 = pd.read_sql(sql,connection,index_col=None)
                    df2['DATA_INI'] = pd.to_datetime(df2['DATA_INI'])
                except Exception as e:
                    raise e 
                
                df3 = pd.DataFrame({'DATA_INI': pd.date_range(start=data1,end=data2, freq=pd.offsets.MonthBegin(1))})
                df3['DATA_INI'] = pd.to_datetime(df3['DATA_INI'])
                
                for x in list(set(df3.DATA_INI) - set(df2.DATA_INI)):
                    df_new.loc[len(df_new)] = [row['cnpj'], x.date()]

        df_new['DATA'] = pd.to_datetime(df_new['DATA'])
        df_new.sort_values(by=['FILIAL','DATA'], inplace=True)
        df_new['DATA'] = df_new['DATA'].dt.strftime('%d/%m/%Y')

        arq_excel = f'{rs.get("page")}_{rs.get("base")}_{rs.get("userId")}_{rs.get("username")}_{dataagora}.xlsx'

        if len(rs.get('data_ini')) > 0:
            arq_excel = f'{rs.get("page")}_{rs.get("base")}_{rs.get("userId")}_{rs.get("username")}_{data1}_{data2}_{dataagora}.xlsx'

        urlxls = os.path.join(BASE_DIR, f"media/{arq_excel}") 

        notify(f'Criando o arquivo: {arq_excel}', ws, rs)

        # Create a workbook and add a worksheet.
        workbook = xlsxwriter.Workbook(urlxls)
        
        worksheet1 = workbook.add_worksheet('REL.1')
        worksheet2 = workbook.add_worksheet('REL.2')

        bold = workbook.add_format({'bold': True})

        center_format = workbook.add_format({    
        'align': 'center',
        'valign': 'vcenter'})
        bg_verde = workbook.add_format({    
        'align': 'center',
        'valign': 'vcenter',
        'border': 0,
        'pattern': 1,
        'bottom' : 7,
        'bold': 1,
        'bg_color': 'green'})
        bg_red = workbook.add_format({    
        'align': 'center',
        'border': 0,
        'valign': 'vcenter',
        'pattern': 0,
        'bottom' : 7,
        'font_color': 'red'})
        bg_white = workbook.add_format({    
        'align': 'center',
        'border': 0,
        'valign': 'vcenter',
        'pattern': 0 })
        bg_white_border = workbook.add_format({    
        'align': 'center',
        'border': 1,
        'valign': 'vcenter',    
        'bold': 0 })
        merge_format = workbook.add_format({
        'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter'})

# SHEET 1 --------------------------------------------------------
        for z in range(0,len(x1_df_new.columns)):
            worksheet1.write(3, z, list(x1_df_new.columns)[z],merge_format)

        for index, row in x1_df_new.iterrows():    
            for k, v in enumerate(list(row)):
                cor = bg_white_border
                if v == 'S':
                    cor = bg_verde
                elif v == 'N':
                    cor = bg_red
                
                worksheet1.write(4+index, k, v, cor)

        for column in x1_df_new:
            value = x1_df_new[column].astype(str).map(len).max()    

            if value > 50:   
                column_width = len(column)
            else:
                column_width = max(value+5, len(column))
                
            col_idx = x1_df_new.columns.get_loc(column)
            worksheet1.set_column(col_idx, col_idx, column_width)

# FIM DO SHEET 1 ---------------------------------------------------------------


#  SHEET 2 --------------------------------------------------------        
        fx = df_new.reset_index()
        fx.index += 1 

        worksheet2.merge_range('A1:C1', 'SPED FALTANTES', merge_format)
        worksheet2.merge_range('D1:G1', f'Período: {data1} - {data2}', merge_format)

        write_title("A,B",3,'FILIAL,DATA',bold,worksheet2)

        cell_format = workbook.add_format()
        cell_format.set_num_format('dd/mm/yy')

        for index, row in fx.iterrows():
            writeLine('A',3+index,row['FILIAL'],worksheet2)
            writeLine('B',3+index,row['DATA'],worksheet2)

        for column in df_new:
            value = df_new[column].astype(str).map(len).max()    

            if value > 50:   
                column_width = len(column)
            else:
                column_width = max(value+5, len(column))
                
            col_idx = df_new.columns.get_loc(column)
            worksheet2.set_column(col_idx, col_idx, column_width)
        
# FIM DO SHEET 1 ---------------------------------------------------------------

        workbook.close()

        msg = f'Arquivo criado com Sucesso, gerando Link, pode demorar'
        if notify(f'{msg}', WS, rs) == False: 
            WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
            notify(f'{msg}', WS, rs)

        rs['nome_arquivo'] = arq_excel
        rs['total_registros'] = rst.qtd           
        msg = f'Retornando a MSG'
        if notify(f'{msg}', WS, rs) == False: 
            WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
            notify(f'{msg}', WS, rs)
                
        ren(rs,'id_user', 'userId') 
        ren(rs,'cnpj_conta', 'base') 
        ren(rs,'cliente', 'nomeEmpresa') 
        ren(rs,'tipo_relatorio', 'page')         
        ren(rs,'user_name', 'username')       
        
        rs.pop('idEmpresa') 

        try:
            gravabanco_ctrl_arq_excel(rs)
        except Exception as e:
            raise e
        
        msg_ = {
            "data": "Criado com Sucesso",
            "userId" : f"{rs['id_user']}",
            "page": f"{rs['tipo_relatorio']}",
            "erro" : 0,
            "link" : 1,
            "msg": f"https://stgapi.cf:9993/{arq_excel}",        
        }

        return msg_

@shared_task
def apuracao_cred_pis_cofins_task(rs):
    # raise Exception('Erro No Sistemas')

    try:
        WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
    except Exception as e:
        raise e 
    
    dataagora = datetime.now().strftime("%d%m%Y%H%M%S")
    value = {'sql_data': ''}
    base = rs.get('base')

    if len(rs.get('data_ini')) > 0 and len(rs.get('data_fim')) > 0:
         value['sql_data'] = f"""
            AND sped_pis_cofins_ctrl.DATA_INI BETWEEN '{ convertData(rs.get('data_ini'))}' AND '{ convertData(rs.get('data_fim'))}'
      """

    msg = f'Conectando com a Base: DB_{base}'
    if notify(f'{msg}', WS, rs) == False: 
        WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
        notify(f'{msg}', WS, rs)

    try:
        engine = create_engine(f"{URL_CONNECT}/DB_{base}")
    except Exception as e:
        raise e    

    msg = f'Base conectada'
    if notify(f'{msg}', WS, rs) == False: 
        WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
        notify(f'{msg}', WS, rs)

    sql = f"""
             SELECT
                    COUNT(*) as qtd
                FROM
                    sped_pis_cofins_M100
                INNER JOIN
                sped_pis_cofins_ctrl
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
                    sped_pis_cofins_M500
                INNER JOIN
                sped_pis_cofins_ctrl
                ON
                    sped_pis_cofins_M500.ID_EFD_CTRL_REG_0000 = sped_pis_cofins_ctrl.ID_SPEDFIS_CTRL_REG_0000
                WHERE
                    sped_pis_cofins_ctrl.CANCELADO IS NULL
                    AND
                sped_pis_cofins_ctrl.ENVIO = 1	
               {value['sql_data']}                    
               """             

    try:
        with engine.connect() as conn:
            rst = pd.read_sql_query(sql, conn)
    except Exception as e:
        raise e

    if int(max(list(rst.qtd))) < 1000000:
        sql = f"""
                SELECT
                sped_pis_cofins_ctrl.DATA_INI, 
                sped_pis_cofins_ctrl.CNPJ,	
                'M100' AS M100_M500, 
                sped_pis_cofins_M100.COD_CRED, 
                (SELECT descricao FROM gerencial.tb_tipo_cred WHERE codigo = sped_pis_cofins_M100.COD_CRED) AS DESC_COD_CRED,
                sped_pis_cofins_M100.IND_CRED_ORI, 
                sped_pis_cofins_M100.VL_BC_CRED, 
                sped_pis_cofins_M100.ALIQ_PIS, 
                sped_pis_cofins_M100.QUANT_BC_PIS, 
                sped_pis_cofins_M100.ALIQ_PIS_QUANT, 
                sped_pis_cofins_M100.VL_CRED, 
                sped_pis_cofins_M100.VL_AJUS_ACRES, 
                sped_pis_cofins_M100.VL_AJUS_REDUC, 
                sped_pis_cofins_M100.VL_CRED_DIF, 
                sped_pis_cofins_M100.VL_CRED_DISP, 
                sped_pis_cofins_M100.IND_DESC_CRED, 
                sped_pis_cofins_M100.VL_CRED_DESC, 
                sped_pis_cofins_M100.SLD_CRED 
                
                FROM
                sped_pis_cofins_M100
                INNER JOIN
                sped_pis_cofins_ctrl
                ON 
                    sped_pis_cofins_M100.ID_EFD_CTRL_REG_0000 = sped_pis_cofins_ctrl.ID_SPEDFIS_CTRL_REG_0000
                WHERE
                sped_pis_cofins_ctrl.CANCELADO IS NULL AND
                sped_pis_cofins_ctrl.ENVIO = 1
                {value['sql_data']}   
                
                UNION
                
                SELECT
                sped_pis_cofins_ctrl.DATA_INI, 
                sped_pis_cofins_ctrl.CNPJ,	
                'M500' AS M500_M500, 
                sped_pis_cofins_M500.COD_CRED, 
                (SELECT descricao FROM gerencial.tb_tipo_cred WHERE codigo = sped_pis_cofins_M500.COD_CRED) AS DESC_COD_CRED,
                sped_pis_cofins_M500.IND_CRED_ORI, 
                sped_pis_cofins_M500.VL_BC_CRED, 
                sped_pis_cofins_M500.ALIQ_COFINS, 
                sped_pis_cofins_M500.QUANT_BC_COFINS, 
                sped_pis_cofins_M500.ALIQ_COFINS_QUANT, 
                sped_pis_cofins_M500.VL_CRED, 
                sped_pis_cofins_M500.VL_AJUS_ACRES, 
                sped_pis_cofins_M500.VL_AJUS_REDUC, 
                sped_pis_cofins_M500.VL_CRED_DIF, 
                sped_pis_cofins_M500.VL_CRED_DISP, 
                sped_pis_cofins_M500.IND_DESC_CRED, 
                sped_pis_cofins_M500.VL_CRED_DESC, 
                sped_pis_cofins_M500.SLD_CRED 
                
                FROM
                sped_pis_cofins_M500
                INNER JOIN
                sped_pis_cofins_ctrl
                ON 
                    sped_pis_cofins_M500.ID_EFD_CTRL_REG_0000 = sped_pis_cofins_ctrl.ID_SPEDFIS_CTRL_REG_0000
                WHERE
                sped_pis_cofins_ctrl.CANCELADO IS NULL AND
                sped_pis_cofins_ctrl.ENVIO = 1	
                {value['sql_data']}                    
               """        

        msg = f'Ok abaixo de 1 milhão OK'
        if notify(f'{msg}', WS, rs) == False: 
            WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
            notify(f'{msg}', WS, rs)

        try:
            with engine.connect() as conn:
              df1 = pd.read_sql_query(sql, conn)
        except Exception as e:
            raise e
        
        df1.fillna(0, inplace=True)
        df1['DATA_INI'] = converte_data(df1,'DATA_INI').dt.strftime('%d/%m/%Y')
        df1['VL_BC_CRED'] = df1['VL_BC_CRED'].str.replace(',','.').astype("float64")
        df1['VL_CRED'] = df1['VL_CRED'].str.replace(',','.').astype("float64")
        df1['VL_AJUS_ACRES'] = df1['VL_AJUS_ACRES'].str.replace(',','.').astype("float64")
        df1['VL_AJUS_REDUC'] = df1['VL_AJUS_REDUC'].str.replace(',','.').astype("float64")
        df1['VL_CRED_DIF'] = df1['VL_CRED_DIF'].str.replace(',','.').astype("float64")
        df1['VL_CRED_DISP'] = df1['VL_CRED_DISP'].str.replace(',','.').astype("float64")
        df1['VL_CRED_DESC'] = df1['VL_CRED_DESC'].str.replace(',','.').astype("float64")
        df1['SLD_CRED'] = df1['SLD_CRED'].str.replace(',','.').astype("float64")

        arq_excel = f'{rs.get("page")}_{rs.get("base")}_{rs.get("userId")}_{rs.get("username")}_{dataagora}.xlsx'

        if len(rs.get('data_ini')) > 0:
            arq_excel = f'{rs.get("page")}_{rs.get("base")}_{convertNumber(rs.get("data_ini"))}_{convertNumber(rs.get("data_fim"))}_{dataagora}.xlsx'
        
        urlxls = os.path.join(BASE_DIR, f"media/{arq_excel}") 
        msg = f'criando o arquivo'
        if notify(f'{msg}', WS, rs) == False: 
            WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
            notify(f'{msg}', WS, rs)

        try:
            wb = Workbook()
            values = [df1.columns] + list(df1.values)
            wb.new_sheet('sheet name', data=values)
            wb.save(urlxls)
        except Exception as e:
            raise e 

        msg = f'Arquivo criado com Sucesso, gerando Link, pode demorar'
        if notify(f'{msg}', WS, rs) == False: 
            WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
            notify(f'{msg}', WS, rs)

        rs['nome_arquivo'] = arq_excel   
        rs['total_registros'] = max(list(rst.qtd))
        
        msg = f'Retornando a MSG'
        if notify(f'{msg}', WS, rs) == False: 
            WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
            notify(f'{msg}', WS, rs)
      
        ren(rs,'id_user', 'userId') 
        ren(rs,'cnpj_conta', 'base') 
        ren(rs,'cliente', 'nomeEmpresa') 
        ren(rs,'tipo_relatorio', 'page')         
        ren(rs,'user_name', 'username')       
        
        rs.pop('idEmpresa') 

        try:
            gravabanco_ctrl_arq_excel(rs)
        except Exception as e:
            raise e 
                        
        msg_ = {
            "data": "Criado com Sucesso",
            "userId" : f"{rs['id_user']}",
            "page": f"{rs['tipo_relatorio']}",
            "erro" : 0,
            "link" : 1,
            "msg": f"https://stgapi.cf:9993/{arq_excel}",        
        }

        return msg_ 

@shared_task
def apuracao_deb_pis_cofins_task(rs):
    # raise Exception('Erro No Sistemas')

    try:
        WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
    except Exception as e:
        raise e 
    
    dataagora = datetime.now().strftime("%d%m%Y%H%M%S")
    value = {'sql_data': ''}
    base = rs.get('base')

    if len(rs.get('data_ini')) > 0 and len(rs.get('data_fim')) > 0:
         value['sql_data'] = f"""
            AND sped_pis_cofins_ctrl.DATA_INI BETWEEN '{ convertData(rs.get('data_ini'))}' AND '{ convertData(rs.get('data_fim'))}'
      """

    msg = f'Conectando com a Base: DB_{base}'
    if notify(f'{msg}', WS, rs) == False: 
        WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
        notify(f'{msg}', WS, rs)

    try:
        engine = create_engine(f"{URL_CONNECT}/DB_{base}")
    except Exception as e:
        raise e    

    msg = f'Base conectada'
    if notify(f'{msg}', WS, rs) == False: 
        WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
        notify(f'{msg}', WS, rs)

    sql = f"""
             SELECT
                    COUNT(*) as qtd
                FROM
                    sped_pis_cofins_M100
                INNER JOIN
                sped_pis_cofins_ctrl
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
                    sped_pis_cofins_M500
                INNER JOIN
                sped_pis_cofins_ctrl
                ON
                    sped_pis_cofins_M500.ID_EFD_CTRL_REG_0000 = sped_pis_cofins_ctrl.ID_SPEDFIS_CTRL_REG_0000
                WHERE
                    sped_pis_cofins_ctrl.CANCELADO IS NULL
                    AND
                sped_pis_cofins_ctrl.ENVIO = 1	
               {value['sql_data']}                    
               """             

    try:
        with engine.connect() as conn:
            rst = pd.read_sql_query(sql, conn)
    except Exception as e:
        raise e

    if int(max(list(rst.qtd))) < 1000000:
        sql = f"""
                SELECT
                        sped_pis_cofins_ctrl.CNPJ, 
                        sped_pis_cofins_ctrl.DATA_INI, 	
                        'M200' AS M200_M600,
                        sped_pis_cofins_M200.VL_TOT_CONT_NC_PER, 
                        (SELECT
                              SUM(IF(M200.IND_AJ = 1, (REPLACE(M200.VL_AJ,",",".")*-1),REPLACE(M200.VL_AJ,",","."))) AS TOTAL
                           FROM
                              sped_pis_cofins_M220 AS M200
                           WHERE
                              M200.ID_EFD_CTRL_REG_0000 = sped_pis_cofins_M200.ID_EFD_CTRL_REG_0000) AS TOTAL_AJUSTE_M200_M600,
                        sped_pis_cofins_M200.VL_TOT_CRED_DESC, 
                        sped_pis_cofins_M200.VL_TOT_CRED_DESC_ANT, 
                        sped_pis_cofins_M200.VL_TOT_CONT_NC_DEV, 
                        sped_pis_cofins_M200.VL_RET_NC, 
                        sped_pis_cofins_M200.VL_OUT_DED_NC, 
                        sped_pis_cofins_M200.VL_CONT_NC_REC, 
                        sped_pis_cofins_M200.VL_TOT_CONT_CUM_PER, 
                        sped_pis_cofins_M200.VL_RET_CUM, 
                        sped_pis_cofins_M200.VL_OUT_DED_CUM, 
                        sped_pis_cofins_M200.VL_CONT_CUM_REC, 
                        sped_pis_cofins_M200.VL_TOT_CONT_REC
                     FROM
                        sped_pis_cofins_ctrl
                        INNER JOIN
                        sped_pis_cofins_M200
                        ON 
                           sped_pis_cofins_ctrl.ID_SPEDFIS_CTRL_REG_0000 = sped_pis_cofins_M200.ID_EFD_CTRL_REG_0000
                        
                     WHERE
                        sped_pis_cofins_ctrl.CANCELADO IS NULL AND
                        sped_pis_cofins_ctrl.ENVIO = 1
                        {value['sql_data']}
                        
                        UNION
                        
                        SELECT
                        sped_pis_cofins_ctrl.CNPJ, 
                        sped_pis_cofins_ctrl.DATA_INI, 
                        'M600' AS M200_M600,
                        sped_pis_cofins_M600.VL_TOT_CONT_NC_PER,
                        (SELECT
                              SUM(IF(M600.IND_AJ = 1, (REPLACE(M600.VL_AJ,",",".")*-1),REPLACE(M600.VL_AJ,",","."))) AS TOTAL
                           FROM
                              sped_pis_cofins_M620 AS M600
                           WHERE
                              M600.ID_EFD_CTRL_REG_0000 = sped_pis_cofins_M600.ID_EFD_CTRL_REG_0000) AS TOTAL_AJUSTE_M200_M600, 
                        sped_pis_cofins_M600.VL_TOT_CRED_DESC, 
                        sped_pis_cofins_M600.VL_TOT_CRED_DESC_ANT, 
                        sped_pis_cofins_M600.VL_TOT_CONT_NC_DEV, 
                        sped_pis_cofins_M600.VL_RET_NC, 
                        sped_pis_cofins_M600.VL_OUT_DED_NC, 
                        sped_pis_cofins_M600.VL_CONT_NC_REC, 
                        sped_pis_cofins_M600.VL_TOT_CONT_CUM_PER, 
                        sped_pis_cofins_M600.VL_RET_CUM, 
                        sped_pis_cofins_M600.VL_OUT_DED_CUM, 
                        sped_pis_cofins_M600.VL_CONT_CUM_REC, 
                        sped_pis_cofins_M600.VL_TOT_CONT_REC
                     FROM
                        sped_pis_cofins_ctrl
                        INNER JOIN
                        sped_pis_cofins_M600
                        ON 
                           sped_pis_cofins_ctrl.ID_SPEDFIS_CTRL_REG_0000 = sped_pis_cofins_M600.ID_EFD_CTRL_REG_0000
                     WHERE
                        sped_pis_cofins_ctrl.CANCELADO IS NULL AND
                        sped_pis_cofins_ctrl.ENVIO = 1 
                        {value['sql_data']}
                     ORDER BY
                        M200_M600, DATA_INI ASC
               """        

        msg = f'Ok abaixo de 1 milhão OK'
        if notify(f'{msg}', WS, rs) == False: 
            WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
            notify(f'{msg}', WS, rs)

        try:
            with engine.connect() as conn:
              df1 = pd.read_sql_query(sql, conn)
        except Exception as e:
            raise e
        
        df1.fillna(0, inplace=True)
        df1['DATA_INI'] = converte_data(df1,'DATA_INI').dt.strftime('%d/%m/%Y')
        df1['VL_TOT_CONT_NC_PER'] = df1['VL_TOT_CONT_NC_PER'].str.replace(',','.').astype("float64")
        df1['VL_TOT_CRED_DESC'] = df1['VL_TOT_CRED_DESC'].str.replace(',','.').astype("float64")
        df1['VL_TOT_CRED_DESC_ANT'] = df1['VL_TOT_CRED_DESC_ANT'].str.replace(',','.').astype("float64")
        df1['VL_TOT_CONT_NC_DEV'] = df1['VL_TOT_CONT_NC_DEV'].str.replace(',','.').astype("float64")
        df1['VL_RET_NC'] = df1['VL_RET_NC'].str.replace(',','.').astype("float64")
        df1['VL_OUT_DED_NC'] = df1['VL_OUT_DED_NC'].str.replace(',','.').astype("float64")
        df1['VL_CONT_NC_REC'] = df1['VL_CONT_NC_REC'].str.replace(',','.').astype("float64")
        df1['VL_TOT_CONT_CUM_PER'] = df1['VL_TOT_CONT_CUM_PER'].str.replace(',','.').astype("float64")
        df1['VL_RET_CUM'] = df1['VL_RET_CUM'].str.replace(',','.').astype("float64")
        df1['VL_OUT_DED_CUM'] = df1['VL_OUT_DED_CUM'].str.replace(',','.').astype("float64")
        df1['VL_CONT_CUM_REC'] = df1['VL_CONT_CUM_REC'].str.replace(',','.').astype("float64")
        df1['VL_TOT_CONT_REC'] = df1['VL_TOT_CONT_REC'].str.replace(',','.').astype("float64")

        arq_excel = f'{rs.get("page")}_{rs.get("base")}_{rs.get("userId")}_{rs.get("username")}_{dataagora}.xlsx'

        if len(rs.get('data_ini')) > 0:
            arq_excel = f'{rs.get("page")}_{rs.get("base")}_{convertNumber(rs.get("data_ini"))}_{convertNumber(rs.get("data_fim"))}_{dataagora}.xlsx'
        
        urlxls = os.path.join(BASE_DIR, f"media/{arq_excel}") 
        msg = f'criando o arquivo'
        if notify(f'{msg}', WS, rs) == False: 
            WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
            notify(f'{msg}', WS, rs)

        try:
            wb = Workbook()
            values = [df1.columns] + list(df1.values)
            wb.new_sheet('sheet name', data=values)
            wb.save(urlxls)
        except Exception as e:
            raise e 

        msg = f'Arquivo criado com Sucesso, gerando Link, pode demorar'
        if notify(f'{msg}', WS, rs) == False: 
            WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
            notify(f'{msg}', WS, rs)

        rs['nome_arquivo'] = arq_excel   
        rs['total_registros'] = max(list(rst.qtd))
        
        msg = f'Retornando a MSG'
        if notify(f'{msg}', WS, rs) == False: 
            WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
            notify(f'{msg}', WS, rs)
      
        ren(rs,'id_user', 'userId') 
        ren(rs,'cnpj_conta', 'base') 
        ren(rs,'cliente', 'nomeEmpresa') 
        ren(rs,'tipo_relatorio', 'page')         
        ren(rs,'user_name', 'username')       
        
        rs.pop('idEmpresa') 

        try:
            gravabanco_ctrl_arq_excel(rs)
        except Exception as e:
            raise e 
                        
        msg_ = {
            "data": "Criado com Sucesso",
            "userId" : f"{rs['id_user']}",
            "page": f"{rs['tipo_relatorio']}",
            "erro" : 0,
            "link" : 1,
            "msg": f"https://stgapi.cf:9993/{arq_excel}",        
        }

        return msg_ 


@shared_task
def ajuste_apuracao_icms_task(rs):
    # raise Exception('Erro No Sistemas')

    try:
        WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
    except Exception as e:
        raise e 
    
    dataagora = datetime.now().strftime("%d%m%Y%H%M%S")
    value = {'sql_data': ''}
    base = rs.get('base')

    if len(rs.get('data_ini')) > 0 and len(rs.get('data_fim')) > 0:
         value['sql_data'] = f"""
            AND sped_icms_ipi_ctrl.DATA_INI BETWEEN '{ convertData(rs.get('data_ini'))}' AND '{ convertData(rs.get('data_fim'))}'
      """

    msg = f'Conectando com a Base: DB_{base}'
    if notify(f'{msg}', WS, rs) == False: 
        WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
        notify(f'{msg}', WS, rs)

    try:
        engine = create_engine(f"{URL_CONNECT}/DB_{base}")
    except Exception as e:
        raise e    

    msg = f'Base conectada'
    if notify(f'{msg}', WS, rs) == False: 
        WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
        notify(f'{msg}', WS, rs)
    
    sql = f"""
        SELECT
                COUNT(*) as qtd
            from
                sped_icms_ipi_ctrl
                INNER JOIN
                sped_icms_ipi_E111
                ON
                    sped_icms_ipi_ctrl.ID_SPEDFIS_CTRL_REG_0000 = sped_icms_ipi_E111.ID_SPEDFIS_CTRL_REG_0000
            WHERE
                sped_icms_ipi_ctrl.ENVIO = 1 AND
                sped_icms_ipi_ctrl.CANCELADO IS NULL
            {value['sql_data']}
            """

    try:
        with engine.connect() as conn:
            rst = pd.read_sql_query(sql, conn)
    except Exception as e:
        raise e

    data_ = 'Acima do excel'

    if int(rst.qtd) < 1000000:
        sql = f"""
                SELECT
                sped_icms_ipi_ctrl.DATA_INI,
                sped_icms_ipi_ctrl.CNPJ,
                sped_icms_ipi_E111.COD_AJ_APUR,
                (SELECT `DESC` FROM gerencial.tb_cod_ajuste_apur_icms AS COD WHERE COD.COD_AJ_APUR = sped_icms_ipi_E111.COD_AJ_APUR LIMIT 1) AS DESCR_AJ_APUR,
                sped_icms_ipi_E111.DESCR_COMPL_AJ,
                sped_icms_ipi_E111.VL_AJ_APUR
            FROM
                sped_icms_ipi_ctrl
                INNER JOIN
                sped_icms_ipi_E111
                ON
                sped_icms_ipi_ctrl.ID_SPEDFIS_CTRL_REG_0000 = sped_icms_ipi_E111.ID_SPEDFIS_CTRL_REG_0000
            WHERE
            sped_icms_ipi_ctrl.ENVIO = 1 AND
            sped_icms_ipi_ctrl.CANCELADO IS NULL
                {value['sql_data']}
        """
        msg = f'Ok abaixo de 1 milhão OK'
        if notify(f'{msg}', WS, rs) == False: 
            WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
            notify(f'{msg}', WS, rs)

        try:
            with engine.connect() as conn:
              df1 = pd.read_sql_query(sql, conn)
        except Exception as e:
            raise e
        
        df1.fillna(0, inplace=True)

        df1['DATA_INI'] = converte_data(df1, 'DATA_INI').dt.strftime('%d/%m/%Y')
        df1['VL_AJ_APUR'] = df1['VL_AJ_APUR'].str.replace(',', '.').astype("float64")

        data_ = 'Perfeito para o excel'

        arq_excel = f'{rs.get("page")}_{rs.get("base")}_{rs.get("userId")}_{rs.get("username")}_{dataagora}.xlsx'

        if len(rs.get('data_ini')) > 0:
            arq_excel = f'{rs.get("page")}_{rs.get("base")}_{convertNumber(rs.get("data_ini"))}_{convertNumber(rs.get("data_fim"))}_{dataagora}.xlsx'

        urlxls = os.path.join(BASE_DIR, f"media/{arq_excel}") 

        msg = f'criando o arquivo'
        if notify(f'{msg}', WS, rs) == False: 
            WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
            notify(f'{msg}', WS, rs) 

        try:
            wb = Workbook()
            values = [df1.columns] + list(df1.values)
            wb.new_sheet('sheet name', data=values)
            wb.save(urlxls)
        except Exception as e:
            raise e 

        msg = f'Arquivo criado com Sucesso, gerando Link, pode demorar'
        if notify(f'{msg}', WS, rs) == False: 
            WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
            notify(f'{msg}', WS, rs)

        rs['nome_arquivo'] = arq_excel   
        rs['total_registros'] = rst.qtd
        msg = f'Retornando a MSG'
        if notify(f'{msg}', WS, rs) == False: 
            WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
            notify(f'{msg}', WS, rs)
      
        ren(rs,'id_user', 'userId') 
        ren(rs,'cnpj_conta', 'base') 
        ren(rs,'cliente', 'nomeEmpresa') 
        ren(rs,'tipo_relatorio', 'page')         
        ren(rs,'user_name', 'username')       
        
        rs.pop('idEmpresa') 

        try:
            gravabanco_ctrl_arq_excel(rs)
        except Exception as e:
            raise e 
                        
        msg_ = {
            "data": "Criado com Sucesso",
            "userId" : f"{rs['id_user']}",
            "page": f"{rs['tipo_relatorio']}",
            "erro" : 0,
            "link" : 1,
            "msg": f"https://stgapi.cf:9993/{arq_excel}",        
        }

        return msg_
    
@shared_task
def apuracao_icms_ipi_task(rs):
    # raise Exception('Erro No Sistemas')
    filtro = rs.get('tipoFiltro')

    try:
        WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
    except Exception as e:
        raise e 
    
    dataagora = datetime.now().strftime("%d%m%Y%H%M%S")
    value = {'sql_data': ''}
    base = rs.get('base')

    if len(rs.get('data_ini')) > 0 and len(rs.get('data_fim')) > 0:
         value['sql_data'] = f"""
            AND sped_icms_ipi_ctrl.DATA_INI BETWEEN '{ convertData(rs.get('data_ini'))}' AND '{ convertData(rs.get('data_fim'))}'
      """

    msg = f'Conectando com a Base: DB_{base}'
    if notify(f'{msg}', WS, rs) == False: 
        WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
        notify(f'{msg}', WS, rs)

    try:
        engine = create_engine(f"{URL_CONNECT}/DB_{base}")
    except Exception as e:
        raise e    

    msg = f'Base conectada'
    if notify(f'{msg}', WS, rs) == False: 
        WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
        notify(f'{msg}', WS, rs)
    
    sql = f"""
        SELECT
                COUNT(*) as qtd
            from
                sped_icms_ipi_ctrl
                INNER JOIN
                sped_icms_ipi_E111
                ON
                    sped_icms_ipi_ctrl.ID_SPEDFIS_CTRL_REG_0000 = sped_icms_ipi_E111.ID_SPEDFIS_CTRL_REG_0000
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
                sped_icms_ipi_ctrl
                INNER JOIN
                sped_icms_ipi_E520
                ON 
                    sped_icms_ipi_ctrl.ID_SPEDFIS_CTRL_REG_0000 = sped_icms_ipi_E520.ID_SPEDFIS_CTRL_REG_0000
            WHERE 
                sped_icms_ipi_ctrl.ENVIO = 1 AND
                sped_icms_ipi_ctrl.CANCELADO IS NULL
                {value['sql_data']}                    
        """

    try:
        with engine.connect() as conn:
            rst = pd.read_sql_query(sql, conn)
    except Exception as e:
        raise e

    data_ = 'Acima do excel'

    if int(rst.qtd) < 1000000:
        sql = f"""
            SELECT
                    sped_icms_ipi_ctrl.DATA_INI, 
                    sped_icms_ipi_ctrl.CNPJ, 	
                    sped_icms_ipi_E110.REG, 
                    REPLACE ( sped_icms_ipi_E110.VL_TOT_DEBITOS, ',', '.' ) AS VL_TOT_DEBITOS,
                    sped_icms_ipi_E110.VL_AJ_DEBITOS, 
                    sped_icms_ipi_E110.VL_TOT_AJ_DEBITOS, 
                    sped_icms_ipi_E110.VL_ESTORNOS_CRED, 
                    sped_icms_ipi_E110.VL_TOT_CREDITOS, 
                    sped_icms_ipi_E110.VL_AJ_CREDITOS, 
                    sped_icms_ipi_E110.VL_TOT_AJ_CREDITOS, 
                    sped_icms_ipi_E110.VL_ESTORNOS_DEB, 
                    sped_icms_ipi_E110.VL_SLD_CREDOR_ANT, 
                    sped_icms_ipi_E110.VL_SLD_APURADO, 
                    sped_icms_ipi_E110.VL_TOT_DED, 
                    sped_icms_ipi_E110.VL_ICMS_RECOLHER, 
                    sped_icms_ipi_E110.VL_SLD_CREDOR_TRANSPORTAR, 
                    sped_icms_ipi_E110.DEB_ESP, 
                    sped_icms_ipi_E110.ID_SPEDFIS_CTRL_REG_0000
                FROM
                    sped_icms_ipi_E110
                    INNER JOIN
                    sped_icms_ipi_ctrl
                    ON 
                    sped_icms_ipi_E110.ID_SPEDFIS_CTRL_REG_0000 = sped_icms_ipi_ctrl.ID_SPEDFIS_CTRL_REG_0000
                WHERE
                    sped_icms_ipi_ctrl.ENVIO = 1 AND
                    sped_icms_ipi_ctrl.CANCELADO IS NULL 
                    {value['sql_data']}
                ORDER BY
                        sped_icms_ipi_ctrl.DATA_INI ASC  
        """

        if filtro == 'ipi':

            sql = f"""
               SELECT
                  sped_icms_ipi_ctrl.DATA_INI, 
                  sped_icms_ipi_ctrl.CNPJ, 	
                  sped_icms_ipi_E520.VL_SD_ANT_IPI, 
                  sped_icms_ipi_E520.VL_DEB_IPI, 
                  sped_icms_ipi_E520.VL_CRED_IPI, 
                  sped_icms_ipi_E520.VL_OD_IPI, 
                  sped_icms_ipi_E520.VL_OC_IPI, 
                  sped_icms_ipi_E520.VL_SC_IPI, 
                  sped_icms_ipi_E520.VL_SD_IPI, 
                  sped_icms_ipi_E520.ID_SPEDFIS_CTRL_REG_0000
               FROM
                  sped_icms_ipi_ctrl
                  INNER JOIN
                  sped_icms_ipi_E520
                  ON 
                     sped_icms_ipi_ctrl.ID_SPEDFIS_CTRL_REG_0000 = sped_icms_ipi_E520.ID_SPEDFIS_CTRL_REG_0000
               WHERE 
                     sped_icms_ipi_ctrl.ENVIO = 1 AND
                  sped_icms_ipi_ctrl.CANCELADO IS NULL
                  {value['sql_data']} 
               ORDER BY
	               sped_icms_ipi_ctrl.DATA_INI ASC                   
            """

        msg = f'Ok abaixo de 1 milhão OK'
        if notify(f'{msg}', WS, rs) == False: 
            WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
            notify(f'{msg}', WS, rs)

        try:
            with engine.connect() as conn:
              df1 = pd.read_sql_query(sql, conn)
        except Exception as e:
            raise e
        
        df1.fillna(0, inplace=True)
        df1['DATA_INI'] = converte_data(df1, 'DATA_INI').dt.strftime('%d/%m/%Y')

        if filtro != 'ipi': df1['VL_TOT_DEBITOS'] = df1['VL_TOT_DEBITOS'].astype("float64")
        if filtro != 'ipi': df1['VL_AJ_DEBITOS'] = df1['VL_AJ_DEBITOS'].str.replace(',','.').astype("float64") 
        if filtro != 'ipi': df1['VL_TOT_AJ_DEBITOS'] = df1['VL_TOT_AJ_DEBITOS'].str.replace(',','.').astype("float64")

        if filtro != 'ipi': df1['VL_ESTORNOS_CRED'] = df1['VL_ESTORNOS_CRED'].str.replace(',','.').astype("float64")
        if filtro != 'ipi': df1['VL_TOT_CREDITOS'] = df1['VL_TOT_CREDITOS'].str.replace(',','.').astype("float64")
        if filtro != 'ipi': df1['VL_AJ_CREDITOS'] = df1['VL_AJ_CREDITOS'].str.replace(',','.').astype("float64")
        if filtro != 'ipi': df1['VL_TOT_AJ_CREDITOS'] = df1['VL_TOT_AJ_CREDITOS'].str.replace(',','.').astype("float64")
        if filtro != 'ipi': df1['VL_ESTORNOS_DEB'] = df1['VL_ESTORNOS_DEB'].str.replace(',','.').astype("float64")
        if filtro != 'ipi': df1['VL_SLD_CREDOR_ANT'] = df1['VL_SLD_CREDOR_ANT'].str.replace(',','.').astype("float64")
        if filtro != 'ipi': df1['VL_SLD_APURADO'] = df1['VL_SLD_APURADO'].str.replace(',','.').astype("float64")
        if filtro != 'ipi': df1['VL_TOT_DED'] = df1['VL_TOT_DED'].str.replace(',','.').astype("float64")
        if filtro != 'ipi': df1['VL_ICMS_RECOLHER'] = df1['VL_ICMS_RECOLHER'].str.replace(',','.').astype("float64")
        if filtro != 'ipi': df1['VL_SLD_CREDOR_TRANSPORTAR'] = df1['VL_SLD_CREDOR_TRANSPORTAR'].str.replace(',','.').astype("float64")
        if filtro != 'ipi': df1['DEB_ESP'] = df1['DEB_ESP'].str.replace(',','.').astype("float64")

        data_ = 'Perfeito para o excel'

        arq_excel = f'{rs.get("page")}_{rs.get("base")}_{rs.get("userId")}_{rs.get("username")}_{filtro}_{dataagora}.xlsx'

        if len(rs.get('data_ini')) > 0:
            arq_excel = f'{rs.get("page")}_{rs.get("base")}_{convertNumber(rs.get("data_ini"))}_{convertNumber(rs.get("data_fim"))}_{filtro}_{dataagora}.xlsx'

        urlxls = os.path.join(BASE_DIR, f"media/{arq_excel}") 

        msg = f'criando o arquivo'
        if notify(f'{msg}', WS, rs) == False: 
            WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
            notify(f'{msg}', WS, rs) 

        try:
            wb = Workbook()
            values = [df1.columns] + list(df1.values)
            wb.new_sheet('sheet name', data=values)
            wb.save(urlxls)
        except Exception as e:
            raise e 

        msg = f'Arquivo criado com Sucesso, gerando Link, pode demorar'
        if notify(f'{msg}', WS, rs) == False: 
            WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
            notify(f'{msg}', WS, rs)

        rs['nome_arquivo'] = arq_excel   
        rs['total_registros'] = rst.qtd
        msg = f'Retornando a MSG'
        if notify(f'{msg}', WS, rs) == False: 
            WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
            notify(f'{msg}', WS, rs)
      
        ren(rs,'id_user', 'userId') 
        ren(rs,'cnpj_conta', 'base') 
        ren(rs,'cliente', 'nomeEmpresa') 
        ren(rs,'tipo_relatorio', 'page')         
        ren(rs,'user_name', 'username')        
        ren(rs,'filtro', 'tipoFiltro')       
        
        rs.pop('idEmpresa') 

        try:
            gravabanco_ctrl_arq_excel(rs)
        except Exception as e:
            raise e 
                        
        msg_ = {
            "data": "Criado com Sucesso",
            "userId" : f"{rs['id_user']}",
            "page": f"{rs['tipo_relatorio']}",
            "erro" : 0,
            "link" : 1,
            "msg": f"https://stgapi.cf:9993/{arq_excel}",        
        }

        return msg_


@shared_task
def balancete_contabil_task(rs):
    # raise Exception('Erro No Sistemas')
    
    try:
        WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
    except Exception as e:
        raise e 
    
    dataagora = datetime.now().strftime("%d%m%Y%H%M%S")
    value = {
            'sql_data' : '',        
            'sql_codnatureza' : '',        
            'sql_codcta' : '',        
        }
    base = rs.get('base')

    if len(rs.get('data_ini')) > 0 and len(rs.get('data_fim')) > 0:
        value['sql_data'] = f""" 
            AND dw_balancete_contabil_geral.DT_FIN 
            BETWEEN '{ convertData(rs.get('data_ini'))}' AND '{ convertData(rs.get('data_fim'))}' 
        """
    
    if len(rs.get('codNatureza')) > 0:
        value['sql_codnatureza'] = f" AND `COD_NAT` = '{str(rs.get('codNatureza'))}' "

        
    if len(rs.get('codConta')) > 0:
        quebra_contas = rs.get('codConta').split(',')

        if len(quebra_contas) > 1:
            value['sql_codcta'] = f" AND `COD_CTA` IN {str(tuple([ str(x).strip() for x in quebra_contas]))}"
        else:
            value['sql_codcta'] = f" AND `COD_CTA` = '{str(rs.get('codConta'))}'"

    
    msg = f'Conectando com a Base: DB_{base}'
    if notify(f'{msg}', WS, rs) == False: 
        WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
        notify(f'{msg}', WS, rs)

    try:
        engine = create_engine(f"{URL_CONNECT}/DB_{base}")
    except Exception as e:
        raise e    

    msg = f'Base conectada'
    if notify(f'{msg}', WS, rs) == False: 
        WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
        notify(f'{msg}', WS, rs)
    
    sql = f"""
            SELECT count(*) as qtd FROM `DB_{base}`.`dw_balancete_contabil_geral` 
                WHERE `DT_ESCRIT` IS NOT NULL 
                    {value['sql_data']} 
                    {value['sql_codnatureza']} 
                    {value['sql_codcta']}            
        """

    try:
        with engine.connect() as conn:
            rst = pd.read_sql_query(sql, conn)
    except Exception as e:
        raise e

    data_ = 'Acima do excel'

    if int(rst.qtd) < 1000000:
        sql = f"""
        SELECT * FROM `DB_{base}`.`dw_balancete_contabil_geral` 
            WHERE `DT_ESCRIT` IS NOT NULL 
                {value['sql_data']} 
                {value['sql_codnatureza']} 
                {value['sql_codcta']}     

        """

        msg = f'Ok abaixo de 1 milhão OK'
        if notify(f'{msg}', WS, rs) == False: 
            WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
            notify(f'{msg}', WS, rs)

        try:
            with engine.connect() as conn:
              df1 = pd.read_sql_query(sql, conn)
        except Exception as e:
            raise e
        
        data_ = 'Perfeito para o excel'

        x = df1['COD_CTA'].unique()

        arq_excel = f'{rs.get("page")}_{rs.get("base")}_{rs.get("userId")}_{rs.get("username")}_{dataagora}.xlsx'

        if len(rs.get('data_ini')) > 0:
            arq_excel = f'{rs.get("page")}_{rs.get("base")}_{convertNumber(rs.get("data_ini"))}_{convertNumber(rs.get("data_fim"))}_{dataagora}.xlsx'

        urlxls = os.path.join(BASE_DIR, f"media/{arq_excel}") 

        df1['DT_FIN'] = pd.to_datetime(df1['DT_FIN']).dt.strftime('%d/%m/%Y')
        df1['DT_ESCRIT'] = pd.to_datetime(df1['DT_ESCRIT']).dt.strftime('%d/%m/%Y')

        df1['VL_SLD_INI'] = df1['VL_SLD_INI'].str.replace(',','.').astype("float64").fillna(0)
        df1['VL_DEB'] = df1['VL_DEB'].str.replace(',','.').astype("float64").fillna(0)
        df1['VL_CRED'] = df1['VL_CRED'].str.replace(',','.').astype("float64").fillna(0)
        df1['VL_SLD_FIN'] = df1['VL_SLD_FIN'].str.replace(',','.').astype("float64").fillna(0)
        df1['VL_SLD_FIN_I355'] = df1['VL_SLD_FIN_I355'].str.replace(',','.').astype("float64").fillna(0)

        msg = f'criando o arquivo'
        if notify(f'{msg}', WS, rs) == False: 
            WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
            notify(f'{msg}', WS, rs) 

        try:
            wb = Workbook()
            if json.loads(str(rs['sheet']).lower()):           
                for i in x:
                    sh = df1[df1['COD_CTA'] == i]
                    values = [sh.columns] + list(sh.values)
                    wb.new_sheet(i, data=[sh.columns] + list(sh.values))              
            else:     
                values = [df1.columns] + list(df1.values)
                wb.new_sheet('sheet name', data=values)
            wb.save(urlxls)
        except Exception as e:
            raise e 

        msg = f'Arquivo criado com Sucesso, gerando Link, pode demorar'
        if notify(f'{msg}', WS, rs) == False: 
            WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
            notify(f'{msg}', WS, rs)

        rs['nome_arquivo'] = arq_excel   
        # rs['total_registros'] = rst.qtd
        msg = f'Retornando a MSG'
        if notify(f'{msg}', WS, rs) == False: 
            WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
            notify(f'{msg}', WS, rs)
      
        ren(rs,'id_user', 'userId') 
        ren(rs,'cnpj_conta', 'base') 
        ren(rs,'cliente', 'nomeEmpresa') 
        ren(rs,'tipo_relatorio', 'page')         
        ren(rs,'user_name', 'username')
        ren(rs,'cod_natureza', 'codNatureza')       
        ren(rs,'cod_conta', 'codConta')       
        
        rs.pop('idEmpresa') 

        try:
            gravabanco_ctrl_arq_excel(rs)
        except Exception as e:
            raise e 
                        
        msg_ = {
            "data": "Criado com Sucesso",
            "userId" : f"{rs['id_user']}",
            "page": f"{rs['tipo_relatorio']}",
            "erro" : 0,
            "link" : 1,
            "msg": f"https://stgapi.cf:9993/{arq_excel}",        
        }

        return msg_

WS = ""
url_ws = "wss://stgapi.cf:7000/ws/"

@celeryd_init.connect()
def clear_all_locks(**kwargs):
    clear_locks(celery_)

@celery_.task(base=Singleton)
def b_total_icms_ipi_task(rs):
    global WS, url_ws
    # raise Exception('Erro No Sistemas')
    
    try:
        WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
    except Exception as e:
        raise e 
    
    dataagora = datetime.now().strftime("%d%m%Y%H%M%S")
    value = {        
        'sql_cfop' : '',
        'cfop_null' : '',
        'DATA_INI' : '',
        'geraCred' : ''
    }

    base = rs.get('base')
    page = rs.get('page')
    filtro = rs.get('filtro')

    if len(rs.get('cfop')) > 0:

         if '9999' in rs.get('cfop'):
            value['cfop_null'] = f" OR `CFOP` IS NULL"

         quebra_cfop = rs.get('cfop').split(',')

         if str(rs.get('geraCred')) == True:
            value['geraCred'] = f" AND (dw_icms_ipi_entradas.CFOP IN (SELECT cfop_credito.cfop FROM gerencial.cfop_credito) OR CFOP IS NULL)"

         if len(quebra_cfop) > 1:
               value['sql_cfop'] = f" AND `CFOP` IN {str(tuple([ str(x).strip() for x in quebra_cfop]))}"
         else:
               value['sql_cfop'] = f" AND `CFOP` = '{str(rs.get('cfop'))}'"

         if len(rs.get('data_ini')) > 0 and len(rs.get('data_fim')) > 0:
            value['DATA_INI'] = f""" 
                AND	(DATA_INI BETWEEN '{ convertData(rs.get('data_ini'))}' AND '{ convertData(rs.get('data_fim'))}')
            """      
    
    msg = f'Conectando com a Base: DB_{base}'
    if notify(f'{msg}', WS, rs) == False: 
        WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
        notify(f'{msg}', WS, rs)

    try:
        engine = create_engine(f"{URL_CONNECT}/DB_{base}")
    except Exception as e:
        raise e    

    msg = f'Base conectada'
    if notify(f'{msg}', WS, rs) == False: 
        WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
        notify(f'{msg}', WS, rs)
    
    sql = f"""        
        SELECT
            dw_icms_ipi_entradas.ID_ITEM,
            dw_icms_ipi_entradas.CHV_PK,
            dw_icms_ipi_entradas.DATA_INI,              
            dw_icms_ipi_entradas.CNPJ_FILIAL,
            dw_icms_ipi_entradas.RAZAO_FILIAL,
            dw_icms_ipi_entradas.UF_FILIAL,
            dw_icms_ipi_entradas.REGISTRO,
            (
                CASE
                    WHEN dw_icms_ipi_entradas.REGISTRO = 'D190' THEN CONCAT('CTe',dw_icms_ipi_entradas.CHV_NFE_CTE)
                    WHEN dw_icms_ipi_entradas.REGISTRO = 'C170' THEN CONCAT('NFe',dw_icms_ipi_entradas.CHV_NFE_CTE)
                    WHEN dw_icms_ipi_entradas.REGISTRO = 'C190' THEN CONCAT('NFe',dw_icms_ipi_entradas.CHV_NFE_CTE)
                ELSE dw_icms_ipi_entradas.CHV_NFE_CTE
                END
                ) as CHV_NFE_CTE, 
            0 as IND_OPER,                    
            cast(replace(dw_icms_ipi_entradas.VL_BC_ICMS,",",".") as decimal(15,2)) as VL_BC_ICMS,                   
            cast(replace(dw_icms_ipi_entradas.VL_ICMS,",",".") as decimal(15,2)) as VL_ICMS,               
            dw_icms_ipi_entradas.VL_DOC,
            dw_icms_ipi_entradas.COD_PART,
            SUBSTRING_INDEX( SUBSTRING_INDEX( D_PART_REG_0150, 'STG&', 2 ), 'STG&',- 1 ) AS RAZAO_PART,
            SUBSTRING_INDEX( D_PART_REG_0150, 'STG&', 1 ) AS CNPJ_PART,
            #SUBSTR(SUBSTRING_INDEX(D_PART_REG_0150,'STG&',-1),1,2)  AS UF_PART,
        (
            SELECT
                UF.descricao
            FROM
                gerencial.uf_codigo_sigla AS UF
            WHERE
                UF.codigo = SUBSTR( SUBSTRING_INDEX( D_PART_REG_0150, 'STG&',- 1 ), 1, 2 )
        ) AS UF_PART,
            dw_icms_ipi_entradas.NUM_DOC,
            dw_icms_ipi_entradas.DT_DOC,
            dw_icms_ipi_entradas.DT_E_S,
            dw_icms_ipi_entradas.IND_EMIT,
            dw_icms_ipi_entradas.COD_MOD,
            dw_icms_ipi_entradas.COD_SIT,
            dw_icms_ipi_entradas.SER,
            dw_icms_ipi_entradas.COD_ITEM,
            dw_icms_ipi_entradas.NUM_ITEM,
            dw_icms_ipi_entradas.DESCR_COMPL,
            SUBSTRING_INDEX( D_ITEM_REG_0200, 'STG&', 1 ) AS DESCR_0200,
            IF
        ( dw_icms_ipi_entradas.REGISTRO = 'C170',
            SUBSTRING_INDEX( D_ITEM_REG_0200, 'STG&',- 1 ),
            NULL ) AS COD_NCM_REG_0200,
            IF
        ( dw_icms_ipi_entradas.REGISTRO = 'C170',
            SUBSTRING_INDEX( SUBSTRING_INDEX( D_ITEM_REG_0200, 'STG&', 2 ), 'STG&',- 1 ),
            NULL ) AS TIPO_ITEM_REG_0200,
            dw_icms_ipi_entradas.VL_ITEM,
            dw_icms_ipi_entradas.CFOP,
            (
            SELECT
                DESCRICAO
            FROM
                gerencial.tb_cfop
            WHERE
                tb_cfop.CFOP = dw_icms_ipi_entradas.CFOP
            LIMIT 1 ) AS INF_CFOP,
            dw_icms_ipi_entradas.VL_BC_ICMS_ITEM,
            dw_icms_ipi_entradas.ALIQ_ICMS_ITEM,
            dw_icms_ipi_entradas.VL_ICMS_ITEM,
            dw_icms_ipi_entradas.CST_ICMS,
            dw_icms_ipi_entradas.VL_BC_ICMS_ST,
            dw_icms_ipi_entradas.ALIQ_ST,
            dw_icms_ipi_entradas.VL_ICMS_ST,
            dw_icms_ipi_entradas.VL_BC_IPI,
            dw_icms_ipi_entradas.ALIQ_IPI,
            dw_icms_ipi_entradas.VL_IPI,
            dw_icms_ipi_entradas.CST_IPI,
            dw_icms_ipi_entradas.CONCILIADO_PISCOFINS,
            dw_icms_ipi_entradas.CONCILIADO_XML,
            dw_icms_ipi_entradas.ID_SPEDFIS_CTRL_REG_0000
        FROM
            `DB_{base}`.dw_icms_ipi_entradas
        WHERE
            ID_ITEM IS NOT NULL 
            {value['DATA_INI']}
            {value['sql_cfop']}
            {value['cfop_null']}
            {value['geraCred']}
         """

    if filtro == 'saida':
         sql = f"""
        SELECT
               dw_icms_ipi_saidas.ID_ITEM,
               dw_icms_ipi_saidas.CHV_PK,
               dw_icms_ipi_saidas.DATA_INI,              
               dw_icms_ipi_saidas.CNPJ_FILIAL,
               dw_icms_ipi_saidas.RAZAO_FILIAL,
               dw_icms_ipi_saidas.UF_FILIAL,
               dw_icms_ipi_saidas.REGISTRO,
               (
               CASE
               WHEN dw_icms_ipi_saidas.REGISTRO = 'D190' THEN CONCAT('CTe',dw_icms_ipi_saidas.CHV_NFE_CTE)
               WHEN dw_icms_ipi_saidas.REGISTRO = 'C170' THEN CONCAT('NFe',dw_icms_ipi_saidas.CHV_NFE_CTE)
               WHEN dw_icms_ipi_saidas.REGISTRO = 'C190' THEN CONCAT('NFe',dw_icms_ipi_saidas.CHV_NFE_CTE)
               ELSE dw_icms_ipi_saidas.CHV_NFE_CTE
               END
               ) as CHV_NFE_CTE,
               1 as IND_OPER,              
               cast(replace(dw_icms_ipi_saidas.VL_BC_ICMS,",",".") as decimal(15,2)) as VL_BC_ICMS,                   
               cast(replace(dw_icms_ipi_saidas.VL_ICMS,",",".") as decimal(15,2)) as VL_ICMS,               
               dw_icms_ipi_saidas.VL_DOC,
               dw_icms_ipi_saidas.COD_PART,
               SUBSTRING_INDEX( SUBSTRING_INDEX( D_PART_REG_0150, 'STG&', 2 ), 'STG&',- 1 ) AS RAZAO_PART,
               SUBSTRING_INDEX( D_PART_REG_0150, 'STG&', 1 ) AS CNPJ_PART,
               #SUBSTR(SUBSTRING_INDEX(D_PART_REG_0150,'STG&',-1),1,2)  AS UF_PART,
            (
               SELECT
                  UF.descricao
               FROM
                  gerencial.uf_codigo_sigla AS UF
               WHERE
                  UF.codigo = SUBSTR( SUBSTRING_INDEX( D_PART_REG_0150, 'STG&',- 1 ), 1, 2 )
            ) AS UF_PART,
               dw_icms_ipi_saidas.NUM_DOC,
               dw_icms_ipi_saidas.DT_DOC,
               dw_icms_ipi_saidas.DT_E_S,
               dw_icms_ipi_saidas.IND_EMIT,
               dw_icms_ipi_saidas.COD_MOD,
               dw_icms_ipi_saidas.COD_SIT,
               dw_icms_ipi_saidas.SER,
               dw_icms_ipi_saidas.COD_ITEM,
               dw_icms_ipi_saidas.NUM_ITEM,
               dw_icms_ipi_saidas.DESCR_COMPL,
               SUBSTRING_INDEX( D_ITEM_REG_0200, 'STG&', 1 ) AS DESCR_0200,
               IF
            ( dw_icms_ipi_saidas.REGISTRO = 'C170',
               SUBSTRING_INDEX( D_ITEM_REG_0200, 'STG&',- 1 ),
               NULL ) AS COD_NCM_REG_0200,
               IF
            ( dw_icms_ipi_saidas.REGISTRO = 'C170',
               SUBSTRING_INDEX( SUBSTRING_INDEX( D_ITEM_REG_0200, 'STG&', 2 ), 'STG&',- 1 ),
               NULL ) AS TIPO_ITEM_REG_0200,
               dw_icms_ipi_saidas.VL_ITEM,
               dw_icms_ipi_saidas.CFOP,
               (
               SELECT
                  DESCRICAO
               FROM
                  gerencial.tb_cfop
               WHERE
                  tb_cfop.CFOP = dw_icms_ipi_saidas.CFOP
               LIMIT 1 ) AS INF_CFOP,
               dw_icms_ipi_saidas.VL_BC_ICMS_ITEM,
               dw_icms_ipi_saidas.ALIQ_ICMS_ITEM,
               dw_icms_ipi_saidas.VL_ICMS_ITEM,
               dw_icms_ipi_saidas.CST_ICMS,
               dw_icms_ipi_saidas.VL_BC_ICMS_ST,
               dw_icms_ipi_saidas.ALIQ_ST,
               dw_icms_ipi_saidas.VL_ICMS_ST,
               dw_icms_ipi_saidas.VL_BC_IPI,
               dw_icms_ipi_saidas.ALIQ_IPI,
               dw_icms_ipi_saidas.VL_IPI,
               dw_icms_ipi_saidas.CST_IPI,
               dw_icms_ipi_saidas.CONCILIADO_PISCOFINS,
               dw_icms_ipi_saidas.CONCILIADO_XML,
               dw_icms_ipi_saidas.ID_SPEDFIS_CTRL_REG_0000
            FROM
               `DB_{base}`.dw_icms_ipi_saidas
            WHERE
               ID_ITEM IS NOT NULL 
               {value['DATA_INI']}
               {value['sql_cfop']}
               {value['cfop_null']}
               {value['geraCred']}
            """
    elif filtro == 'ambos':
        sql = f"""
             SELECT                
                   dw_icms_ipi_saidas.ID_ITEM,
                   dw_icms_ipi_saidas.CHV_PK,
                   dw_icms_ipi_saidas.DATA_INI,                
                   dw_icms_ipi_saidas.CNPJ_FILIAL,
                   dw_icms_ipi_saidas.RAZAO_FILIAL,
                   dw_icms_ipi_saidas.UF_FILIAL,
                   dw_icms_ipi_saidas.REGISTRO,                    
              (
               CASE
               WHEN dw_icms_ipi_saidas.REGISTRO = 'D190' THEN CONCAT('CTe',dw_icms_ipi_saidas.CHV_NFE_CTE)
               WHEN dw_icms_ipi_saidas.REGISTRO = 'C170' THEN CONCAT('NFe',dw_icms_ipi_saidas.CHV_NFE_CTE)
               WHEN dw_icms_ipi_saidas.REGISTRO = 'C190' THEN CONCAT('NFe',dw_icms_ipi_saidas.CHV_NFE_CTE)
               ELSE dw_icms_ipi_saidas.CHV_NFE_CTE
               END
               ) as CHV_NFE_CTE,
               1 as IND_OPER,                      
                   cast(replace(dw_icms_ipi_saidas.VL_BC_ICMS,",",".") as decimal(15,2)) as VL_BC_ICMS,                   
                   cast(replace(dw_icms_ipi_saidas.VL_ICMS,",",".") as decimal(15,2)) as VL_ICMS,
                   dw_icms_ipi_saidas.VL_DOC,
                   dw_icms_ipi_saidas.COD_PART,
                   SUBSTRING_INDEX( SUBSTRING_INDEX( D_PART_REG_0150, 'STG&', 2 ), 'STG&',- 1 ) AS RAZAO_PART,
                   SUBSTRING_INDEX( D_PART_REG_0150, 'STG&', 1 ) AS CNPJ_PART,
                   #SUBSTR(SUBSTRING_INDEX(D_PART_REG_0150,'STG&',-1),1,2)  AS UF_PART,
                (
                   SELECT
                      UF.descricao
                   FROM
                      gerencial.uf_codigo_sigla AS UF
                   WHERE
                      UF.codigo = SUBSTR( SUBSTRING_INDEX( D_PART_REG_0150, 'STG&',- 1 ), 1, 2 )
                ) AS UF_PART,
                   dw_icms_ipi_saidas.NUM_DOC,
                   dw_icms_ipi_saidas.DT_DOC,
                   dw_icms_ipi_saidas.DT_E_S,
                   dw_icms_ipi_saidas.IND_EMIT,
                   dw_icms_ipi_saidas.COD_MOD,
                   dw_icms_ipi_saidas.COD_SIT,
                   dw_icms_ipi_saidas.SER,
                   dw_icms_ipi_saidas.COD_ITEM,
                   dw_icms_ipi_saidas.NUM_ITEM,
                   dw_icms_ipi_saidas.DESCR_COMPL,
                   SUBSTRING_INDEX( D_ITEM_REG_0200, 'STG&', 1 ) AS DESCR_0200,
                   IF
                ( dw_icms_ipi_saidas.REGISTRO = 'C170',
                   SUBSTRING_INDEX( D_ITEM_REG_0200, 'STG&',- 1 ),
                   NULL ) AS COD_NCM_REG_0200,
                   IF
                ( dw_icms_ipi_saidas.REGISTRO = 'C170',
                   SUBSTRING_INDEX( SUBSTRING_INDEX( D_ITEM_REG_0200, 'STG&', 2 ), 'STG&',- 1 ),
                   NULL ) AS TIPO_ITEM_REG_0200,
                   dw_icms_ipi_saidas.VL_ITEM,
                   dw_icms_ipi_saidas.CFOP,
                   (
                   SELECT
                      DESCRICAO
                   FROM
                      gerencial.tb_cfop
                   WHERE
                      tb_cfop.CFOP = dw_icms_ipi_saidas.CFOP
                   LIMIT 1 ) AS INF_CFOP,
                   dw_icms_ipi_saidas.VL_BC_ICMS_ITEM,
                   dw_icms_ipi_saidas.ALIQ_ICMS_ITEM,
                   dw_icms_ipi_saidas.VL_ICMS_ITEM,
                   dw_icms_ipi_saidas.CST_ICMS,
                   dw_icms_ipi_saidas.VL_BC_ICMS_ST,
                   dw_icms_ipi_saidas.ALIQ_ST,
                   dw_icms_ipi_saidas.VL_ICMS_ST,
                   dw_icms_ipi_saidas.VL_BC_IPI,
                   dw_icms_ipi_saidas.ALIQ_IPI,
                   dw_icms_ipi_saidas.VL_IPI,
                   dw_icms_ipi_saidas.CST_IPI,
                   dw_icms_ipi_saidas.CONCILIADO_PISCOFINS,
                   dw_icms_ipi_saidas.CONCILIADO_XML,
                   dw_icms_ipi_saidas.ID_SPEDFIS_CTRL_REG_0000
                FROM
                   `DB_{base}`.dw_icms_ipi_saidas
                WHERE
                   ID_ITEM IS NOT NULL
                   {value['DATA_INI']} 
                   {value['sql_cfop']}
                   {value['cfop_null']}
                   {value['geraCred']}
                UNION
                SELECT
                   dw_icms_ipi_entradas.ID_ITEM,
                   dw_icms_ipi_entradas.CHV_PK,
                   dw_icms_ipi_entradas.DATA_INI,                
                   dw_icms_ipi_entradas.CNPJ_FILIAL,
                   dw_icms_ipi_entradas.RAZAO_FILIAL,
                   dw_icms_ipi_entradas.UF_FILIAL,
                   dw_icms_ipi_entradas.REGISTRO,
            (
                  CASE
                     WHEN dw_icms_ipi_entradas.REGISTRO = 'D190' THEN CONCAT('CTe',dw_icms_ipi_entradas.CHV_NFE_CTE)
                     WHEN dw_icms_ipi_entradas.REGISTRO = 'C170' THEN CONCAT('NFe',dw_icms_ipi_entradas.CHV_NFE_CTE)
                     WHEN dw_icms_ipi_entradas.REGISTRO = 'C190' THEN CONCAT('NFe',dw_icms_ipi_entradas.CHV_NFE_CTE)
                  ELSE dw_icms_ipi_entradas.CHV_NFE_CTE
                  END
                  ) as CHV_NFE_CTE,
                  0 as IND_OPER,
                   cast(replace(dw_icms_ipi_entradas.VL_BC_ICMS,",",".") as decimal(15,2)) as VL_BC_ICMS,                   
                   cast(replace(dw_icms_ipi_entradas.VL_ICMS,",",".") as decimal(15,2)) as VL_ICMS,
                   dw_icms_ipi_entradas.VL_DOC,
                   dw_icms_ipi_entradas.COD_PART,
                   SUBSTRING_INDEX( SUBSTRING_INDEX( D_PART_REG_0150, 'STG&', 2 ), 'STG&',- 1 ) AS RAZAO_PART,
                   SUBSTRING_INDEX( D_PART_REG_0150, 'STG&', 1 ) AS CNPJ_PART,
                   #SUBSTR(SUBSTRING_INDEX(D_PART_REG_0150,'STG&',-1),1,2)  AS UF_PART,
                (
                   SELECT
                      UF.descricao
                   FROM
                      gerencial.uf_codigo_sigla AS UF
                   WHERE
                      UF.codigo = SUBSTR( SUBSTRING_INDEX( D_PART_REG_0150, 'STG&',- 1 ), 1, 2 )
                ) AS UF_PART,
                   dw_icms_ipi_entradas.NUM_DOC,
                   dw_icms_ipi_entradas.DT_DOC,
                   dw_icms_ipi_entradas.DT_E_S,
                   dw_icms_ipi_entradas.IND_EMIT,
                   dw_icms_ipi_entradas.COD_MOD,
                   dw_icms_ipi_entradas.COD_SIT,
                   dw_icms_ipi_entradas.SER,
                   dw_icms_ipi_entradas.COD_ITEM,
                   dw_icms_ipi_entradas.NUM_ITEM,
                   dw_icms_ipi_entradas.DESCR_COMPL,
                   SUBSTRING_INDEX( D_ITEM_REG_0200, 'STG&', 1 ) AS DESCR_0200,
                   IF
                ( dw_icms_ipi_entradas.REGISTRO = 'C170',
                   SUBSTRING_INDEX( D_ITEM_REG_0200, 'STG&',- 1 ),
                   NULL ) AS COD_NCM_REG_0200,
                   IF
                ( dw_icms_ipi_entradas.REGISTRO = 'C170',
                   SUBSTRING_INDEX( SUBSTRING_INDEX( D_ITEM_REG_0200, 'STG&', 2 ), 'STG&',- 1 ),
                   NULL ) AS TIPO_ITEM_REG_0200,
                   dw_icms_ipi_entradas.VL_ITEM,
                   dw_icms_ipi_entradas.CFOP,
                   (
                   SELECT
                      DESCRICAO
                   FROM
                      gerencial.tb_cfop
                   WHERE
                      tb_cfop.CFOP = dw_icms_ipi_entradas.CFOP
                   LIMIT 1 ) AS INF_CFOP,
                   dw_icms_ipi_entradas.VL_BC_ICMS_ITEM,
                   dw_icms_ipi_entradas.ALIQ_ICMS_ITEM,
                   dw_icms_ipi_entradas.VL_ICMS_ITEM,
                   dw_icms_ipi_entradas.CST_ICMS,
                   dw_icms_ipi_entradas.VL_BC_ICMS_ST,
                   dw_icms_ipi_entradas.ALIQ_ST,
                   dw_icms_ipi_entradas.VL_ICMS_ST,
                   dw_icms_ipi_entradas.VL_BC_IPI,
                   dw_icms_ipi_entradas.ALIQ_IPI,
                   dw_icms_ipi_entradas.VL_IPI,
                   dw_icms_ipi_entradas.CST_IPI,
                   dw_icms_ipi_entradas.CONCILIADO_PISCOFINS,
                   dw_icms_ipi_entradas.CONCILIADO_XML,
                   dw_icms_ipi_entradas.ID_SPEDFIS_CTRL_REG_0000                   
                FROM
                   `DB_{base}`.dw_icms_ipi_entradas
                WHERE
                   ID_ITEM IS NOT NULL
                   {value['DATA_INI']} 
                   {value['sql_cfop']}
                   {value['cfop_null']}
                   {value['geraCred']}
                """

    try:
        msg = f'Conectando Select'
        if notify(f'{msg}', WS, rs) == False: 
            WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
            notify(f'{msg}', WS, rs)   
        
        with engine.connect() as conn:
            
            msg = f'Preparando Select, pode demorar'
            if notify(f'{msg}', WS, rs) == False: 
                WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
                notify(f'{msg}', WS, rs)   
            
            df1 = pd.read_sql_query(sql, conn)
            
            msg = f'Select Transformada'
            if notify(f'{msg}', WS, rs) == False: 
                WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
                notify(f'{msg}', WS, rs) 
    except Exception as e:
        raise e
        
    df1.fillna(0, inplace=True)

    arq_excel = f'{rs.get("page")}_{rs.get("base")}_{rs.get("userId")}_{rs.get("username")}_{dataagora}.xlsx'

    if len(rs.get('data_ini')) > 0:
        arq_excel = f'{rs.get("page")}_{rs.get("base")}_{convertNumber(rs.get("data_ini"))}_{convertNumber(rs.get("data_fim"))}_{dataagora}.xlsx'

    urlxls = os.path.join(BASE_DIR, f"media/{arq_excel}") 

    msg = f'criando o arquivo'
    if notify(f'{msg}', WS, rs) == False: 
        WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
        notify(f'{msg}', WS, rs)

    if len(df1) > 1000000:
        msg_ = {
            'message': 'Hello world',
            'id_user' : rs.get('userId'),
            'msg': f'[{rs.get("page")}] - Total de Registros: {len(df1)}, precisa diminuir mais para gerar o excel'
        }
        raise msg_ 
    elif len(df1) > 795000:
        file_cache = os.path.join(BASE_DIR, f"media/cache_{dataagora}.pickle")      
        df1.to_pickle(f"{file_cache}")
        del df1

        df2 = pd.read_pickle(f"{file_cache}")

        if os.path.exists(file_cache):
            os.remove(file_cache)

        df2['DATA_INI'] = converte_data(df2,'DATA_INI').dt.strftime('%d/%m/%Y')
        df2['CHV_NFE_CTE'] =  df2['CHV_NFE_CTE'].astype("string")
        df2['DT_DOC'] = df2['DT_DOC'].astype("string")

        x = df2['CNPJ_FILIAL'].unique()

        writer = pd.ExcelWriter(urlxls, engine='xlsxwriter')
        
        if eval(rs.get('sheet')):
            for i in x:
                sh = df2[df2['CNPJ_FILIAL'] == i]
                sh.to_excel(writer, sheet_name=i, index=False)
        else:
            df2.to_excel(writer, sheet_name='sheet', index=False)
        
        del df2,x
        writer.save()
    else:
        df1['DATA_INI'] = converte_data(df1,'DATA_INI').dt.strftime('%d/%m/%Y')
        erro = False

        x = df1['CNPJ_FILIAL'].unique()
    
        urlxls = os.path.join(BASE_DIR, f"media/{arq_excel}")

        msg = f'criando o arquivo...'
        if notify(f'{msg}', WS, rs) == False: 
            WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
            notify(f'{msg}', WS, rs)

        try:
            wb = Workbook()
            if json.loads(str(rs.get('sheet')).lower()):           
                for i in x:
                    sh = df1[df1['COD_CTA'] == i]
                    values = [sh.columns] + list(sh.values)
                    wb.new_sheet(i, data=[sh.columns] + list(sh.values))              
            else:     
                values = [df1.columns] + list(df1.values)
                wb.new_sheet('sheet name', data=values)
            wb.save(urlxls)
        except Exception as e:
            raise e 

    msg = f'preparando o Link, pode demorar'
    if notify(f'{msg}', WS, rs) == False: 
        WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
        notify(f'{msg}', WS, rs)

    rs['nome_arquivo'] = arq_excel   
    rs['total_registros'] = len(df1)

    msg = f'Retornando a MSG'
    if notify(f'{msg}', WS, rs) == False: 
        WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
        notify(f'{msg}', WS, rs)

    msg_ = {
        "data": "Criado com Sucesso",
        "userId" : f"{rs['userId']}",
        "page": f"{rs['page']}",
        "erro" : 0,
        "link" : 1,
        "msg": f"https://stgapi.cf:9993/{arq_excel}",        
    }

    msg = f'Criado com Sucesso::https://stgapi.cf:9993/{arq_excel}'
    if notify(f'{msg}', WS, rs) == False: 
        WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
        notify(f'{msg}', WS, rs)

    ren(rs,'id_user', 'userId') 
    ren(rs,'cnpj_conta', 'base') 
    ren(rs,'cliente', 'nomeEmpresa') 
    ren(rs,'tipo_relatorio', 'page')         
    ren(rs,'user_name', 'username')
    ren(rs,'dados_cfop', 'cfop')

    rs.pop('idEmpresa') 
    rs.pop('tamanho') 

    try:
        gravabanco_ctrl_arq_excel(rs)
    except Exception as e:
        raise e 
    
    return msg_

@celery_.task(base=Singleton)
def b_total_pis_cofins_task(rs):
    global WS, url_ws   
    
    try:
        WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
    except Exception as e:
        raise e 
    
    dataagora = datetime.now().strftime("%d%m%Y%H%M%S")
    value = {        
        'sql_cfop' : '',
        'cfop_null' : '',
        'DATA_INI' : '',
        'geraCred' : ''
    }

    base = rs.get('base')
    page = rs.get('page')
    filtro = rs.get('filtro')

    if len(rs.get('cfop')) > 0:

         if '9999' in rs.get('cfop'):
            value['cfop_null'] = f" OR `CFOP` IS NULL"

         quebra_cfop = rs.get('cfop').split(',')

         if str(rs.get('geraCred')) == True:
            value['geraCred'] = f" AND (dw_pis_cofins_entradas.CFOP IN (SELECT cfop_credito.cfop FROM gerencial.cfop_credito) OR CFOP IS NULL)"

         if len(quebra_cfop) > 1:
               value['sql_cfop'] = f" AND `CFOP` IN {str(tuple([ str(x).strip() for x in quebra_cfop]))}"
         else:
               value['sql_cfop'] = f" AND `CFOP` = '{str(rs.get('cfop'))}'"

         if len(rs.get('data_ini')) > 0 and len(rs.get('data_fim')) > 0:
            value['DATA_INI'] = f""" 
                AND	(DATA_INI BETWEEN '{ convertData(rs.get('data_ini'))}' AND '{ convertData(rs.get('data_fim'))}')
            """      
    
    msg = f'Conectando com a Base: DB_{base}'
    if notify(f'{msg}', WS, rs) == False: 
        WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
        notify(f'{msg}', WS, rs)

    try:
        engine = create_engine(f"{URL_CONNECT}/DB_{base}", pool_pre_ping = True)
    except Exception as e:
        raise e    

    msg = f'Base conectada'
    if notify(f'{msg}', WS, rs) == False: 
        WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
        notify(f'{msg}', WS, rs)
    
    sql = f"""        
         SELECT
               dw_pis_cofins_entradas.ID_ITEM,
               dw_pis_cofins_entradas.PK,
               dw_pis_cofins_entradas.DATA_INI,               
               dw_pis_cofins_entradas.CNPJ_FILIAL,
               dw_pis_cofins_entradas.REGISTRO,
               dw_pis_cofins_entradas.IND_ESCRI,
               dw_pis_cofins_entradas.IND_OPER,
               dw_pis_cofins_entradas.IND_EMIT,
               dw_pis_cofins_entradas.COD_PART,
               SUBSTRING_INDEX( SUBSTRING_INDEX( D_PART_REG_0150, 'STG&', 2 ), 'STG&',- 1 ) AS RAZAO_PART,
               SUBSTRING_INDEX( D_PART_REG_0150, 'STG&', 1 ) AS CNPJ_PART,
               (
               SELECT UF.descricao FROM	gerencial.uf_codigo_sigla AS UF WHERE	UF.codigo = SUBSTR( SUBSTRING_INDEX( D_PART_REG_0150, 'STG&',- 1 ), 1, 2 ) 
               ) AS UF_PART,
               dw_pis_cofins_entradas.D_PART_REG_0150,
               dw_pis_cofins_entradas.COD_MOD,
               dw_pis_cofins_entradas.COD_SIT,
               dw_pis_cofins_entradas.SER,
               dw_pis_cofins_entradas.NUM_DOC,
               (
             CASE
               WHEN dw_pis_cofins_entradas.REGISTRO = 'D100' THEN CONCAT('CTe',dw_pis_cofins_entradas.CHV_NFE)
               WHEN dw_pis_cofins_entradas.REGISTRO = 'C100' THEN CONCAT('NFe',dw_pis_cofins_entradas.CHV_NFE)
               WHEN dw_pis_cofins_entradas.REGISTRO = 'C190' THEN CONCAT('NFe',dw_pis_cofins_entradas.CHV_NFE)
               ELSE dw_pis_cofins_entradas.CHV_NFE
               END
               ) as CHV_NFE,
               dw_pis_cofins_entradas.DT_DOC,
               dw_pis_cofins_entradas.DT_E_S,
               dw_pis_cofins_entradas.VL_DOC,
               dw_pis_cofins_entradas.IND_PGTO,
               dw_pis_cofins_entradas.VL_DESC,
               dw_pis_cofins_entradas.VL_ABAT_NT,
               dw_pis_cofins_entradas.VL_MERC,
               dw_pis_cofins_entradas.IND_FRT,
               dw_pis_cofins_entradas.VL_FRT,
               dw_pis_cofins_entradas.VL_SEG,
               dw_pis_cofins_entradas.VL_OUT_DA,
               cast(
               REPLACE ( dw_pis_cofins_entradas.VL_BC_ICMS, ",", "." ) AS DECIMAL ( 15, 2 )) AS VL_BC_ICMS,
               cast(
               REPLACE ( dw_pis_cofins_entradas.VL_ICMS, ",", "." ) AS DECIMAL ( 15, 2 )) AS VL_ICMS,
               dw_pis_cofins_entradas.VL_BC_ICMS_ST,
               dw_pis_cofins_entradas.VL_ICMS_ST,
               dw_pis_cofins_entradas.VL_IPI,
               dw_pis_cofins_entradas.VL_PIS,
               dw_pis_cofins_entradas.VL_COFINS,
               dw_pis_cofins_entradas.VL_PIS_ST,
               dw_pis_cofins_entradas.VL_COFINS_ST,
               dw_pis_cofins_entradas.NUM_ITEM,
               dw_pis_cofins_entradas.COD_ITEM,
               dw_pis_cofins_entradas.DESCR_COMPL,
               SUBSTRING_INDEX( D_ITEM_REG_0200, 'STG&', 1 ) AS DESCR_0200,
            IF
               ( dw_pis_cofins_entradas.REGISTRO = 'C170', SUBSTRING_INDEX( D_ITEM_REG_0200, 'STG&',- 1 ), NULL ) AS COD_NCM_REG_0200,
            IF
               ( dw_pis_cofins_entradas.REGISTRO = 'C170', SUBSTRING_INDEX( SUBSTRING_INDEX( D_ITEM_REG_0200, 'STG&', 2 ), 'STG&',- 1 ), NULL ) AS TIPO_ITEM_REG_0200,
               dw_pis_cofins_entradas.D_ITEM_REG_0200,              
               dw_pis_cofins_entradas.QTD,
               dw_pis_cofins_entradas.UNID,
               dw_pis_cofins_entradas.VL_ITEM,
               dw_pis_cofins_entradas.VL_DESC_ITEM,
               dw_pis_cofins_entradas.IND_MOV,
               dw_pis_cofins_entradas.CST_ICMS,
               dw_pis_cofins_entradas.CFOP,                
                (
               SELECT
                  DESCRICAO
               FROM
                  gerencial.tb_cfop
               WHERE
                  tb_cfop.CFOP = dw_pis_cofins_entradas.CFOP
               LIMIT 1 ) AS INF_CFOP,
               dw_pis_cofins_entradas.COD_NAT,
               dw_pis_cofins_entradas.VL_BC_ICMS_ITEM,
               dw_pis_cofins_entradas.ALIQ_ICMS,
               dw_pis_cofins_entradas.VL_ICMS_ITEM,
               dw_pis_cofins_entradas.VL_BC_ICMS_ST_ITEM,
               dw_pis_cofins_entradas.ALIQ_ST,
               dw_pis_cofins_entradas.VL_ICMS_ST_ITEM,
               dw_pis_cofins_entradas.IND_APUR,
               dw_pis_cofins_entradas.CST_IPI,
               dw_pis_cofins_entradas.COD_ENQ,
               dw_pis_cofins_entradas.VL_BC_IPI,
               dw_pis_cofins_entradas.ALIQ_IPI,
               dw_pis_cofins_entradas.VL_IPI_ITEM,
               dw_pis_cofins_entradas.CST_PIS,
               dw_pis_cofins_entradas.VL_BC_PIS,
               dw_pis_cofins_entradas.ALIQ_PIS,
               dw_pis_cofins_entradas.QUANT_BC_PIS,
               dw_pis_cofins_entradas.ALIQ_PIS_QUANT,
               dw_pis_cofins_entradas.VL_PIS_ITEM,
               dw_pis_cofins_entradas.CST_COFINS,
               dw_pis_cofins_entradas.VL_BC_COFINS,
               dw_pis_cofins_entradas.ALIQ_COFINS,
               dw_pis_cofins_entradas.QUANT_BC_COFINS,
               dw_pis_cofins_entradas.ALIQ_COFINS_QUANT,
               dw_pis_cofins_entradas.VL_COFINS_ITEM,
               dw_pis_cofins_entradas.COD_CTA,
               dw_pis_cofins_entradas.CONCILIADO_PISCOFINS,
               dw_pis_cofins_entradas.ID_EFD_CTRL_REG_0000 
            FROM
               `DB_{base}`.dw_pis_cofins_entradas
            WHERE
               ID_ITEM IS NOT NULL 
               {value['DATA_INI']}
               {value['sql_cfop']}
               {value['cfop_null']}
               {value['geraCred']}
         """

    if filtro == 'saida':
         sql = f"""
        SELECT
               dw_pis_cofins_saidas.ID_ITEM,
               dw_pis_cofins_saidas.PK,
               dw_pis_cofins_saidas.DATA_INI,               
               dw_pis_cofins_saidas.CNPJ_FILIAL,
               dw_pis_cofins_saidas.REGISTRO,
               dw_pis_cofins_saidas.IND_ESCRI,
               dw_pis_cofins_saidas.IND_OPER,
               dw_pis_cofins_saidas.IND_EMIT,
               dw_pis_cofins_saidas.COD_PART,
               SUBSTRING_INDEX( SUBSTRING_INDEX( D_PART_REG_0150, 'STG&', 2 ), 'STG&',- 1 ) AS RAZAO_PART,
               SUBSTRING_INDEX( D_PART_REG_0150, 'STG&', 1 ) AS CNPJ_PART,
               (
               SELECT UF.descricao FROM	gerencial.uf_codigo_sigla AS UF WHERE	UF.codigo = SUBSTR( SUBSTRING_INDEX( D_PART_REG_0150, 'STG&',- 1 ), 1, 2 ) 
               ) AS UF_PART,
               dw_pis_cofins_saidas.D_PART_REG_0150,
               dw_pis_cofins_saidas.COD_MOD,
               dw_pis_cofins_saidas.COD_SIT,
               dw_pis_cofins_saidas.SER,
               dw_pis_cofins_saidas.NUM_DOC,
               dw_pis_cofins_saidas.CHV_NFE,
               dw_pis_cofins_saidas.DT_DOC,
               dw_pis_cofins_saidas.DT_E_S,
               dw_pis_cofins_saidas.VL_DOC,
               dw_pis_cofins_saidas.IND_PGTO,
               dw_pis_cofins_saidas.VL_DESC,
               dw_pis_cofins_saidas.VL_ABAT_NT,
               dw_pis_cofins_saidas.VL_MERC,
               dw_pis_cofins_saidas.IND_FRT,
               dw_pis_cofins_saidas.VL_FRT,
               dw_pis_cofins_saidas.VL_SEG,
               dw_pis_cofins_saidas.VL_OUT_DA,
               cast(
               REPLACE ( dw_pis_cofins_saidas.VL_BC_ICMS, ",", "." ) AS DECIMAL ( 15, 2 )) AS VL_BC_ICMS,
               cast(
               REPLACE ( dw_pis_cofins_saidas.VL_ICMS, ",", "." ) AS DECIMAL ( 15, 2 )) AS VL_ICMS,
               dw_pis_cofins_saidas.VL_BC_ICMS_ST,
               dw_pis_cofins_saidas.VL_ICMS_ST,
               dw_pis_cofins_saidas.VL_IPI,
               dw_pis_cofins_saidas.VL_PIS,
               dw_pis_cofins_saidas.VL_COFINS,
               dw_pis_cofins_saidas.VL_PIS_ST,
               dw_pis_cofins_saidas.VL_COFINS_ST,
               dw_pis_cofins_saidas.NUM_ITEM,
               dw_pis_cofins_saidas.COD_ITEM,
               dw_pis_cofins_saidas.DESCR_COMPL,
               SUBSTRING_INDEX( D_ITEM_REG_0200, 'STG&', 1 ) AS DESCR_0200,
            IF
               ( dw_pis_cofins_saidas.REGISTRO = 'C170', SUBSTRING_INDEX( D_ITEM_REG_0200, 'STG&',- 1 ), NULL ) AS COD_NCM_REG_0200,
            IF
               ( dw_pis_cofins_saidas.REGISTRO = 'C170', SUBSTRING_INDEX( SUBSTRING_INDEX( D_ITEM_REG_0200, 'STG&', 2 ), 'STG&',- 1 ), NULL ) AS TIPO_ITEM_REG_0200,
               dw_pis_cofins_saidas.D_ITEM_REG_0200,
               dw_pis_cofins_saidas.QTD,
               dw_pis_cofins_saidas.UNID,
               dw_pis_cofins_saidas.VL_ITEM,
               dw_pis_cofins_saidas.VL_DESC_ITEM,
               dw_pis_cofins_saidas.IND_MOV,
               dw_pis_cofins_saidas.CST_ICMS,
               dw_pis_cofins_saidas.CFOP,
                  (
               SELECT
                  DESCRICAO
               FROM
                  gerencial.tb_cfop
               WHERE
                  tb_cfop.CFOP = dw_pis_cofins_saidas.CFOP
               LIMIT 1 ) AS INF_CFOP,
               dw_pis_cofins_saidas.COD_NAT,
               dw_pis_cofins_saidas.VL_BC_ICMS_ITEM,
               dw_pis_cofins_saidas.ALIQ_ICMS,
               dw_pis_cofins_saidas.VL_ICMS_ITEM,
               dw_pis_cofins_saidas.VL_BC_ICMS_ST_ITEM,
               dw_pis_cofins_saidas.ALIQ_ST,
               dw_pis_cofins_saidas.VL_ICMS_ST_ITEM,
               dw_pis_cofins_saidas.IND_APUR,
               dw_pis_cofins_saidas.CST_IPI,
               dw_pis_cofins_saidas.COD_ENQ,
               dw_pis_cofins_saidas.VL_BC_IPI,
               dw_pis_cofins_saidas.ALIQ_IPI,
               dw_pis_cofins_saidas.VL_IPI_ITEM,
               dw_pis_cofins_saidas.CST_PIS,
               dw_pis_cofins_saidas.VL_BC_PIS,
               dw_pis_cofins_saidas.ALIQ_PIS,
               dw_pis_cofins_saidas.QUANT_BC_PIS,
               dw_pis_cofins_saidas.ALIQ_PIS_QUANT,
               dw_pis_cofins_saidas.VL_PIS_ITEM,
               dw_pis_cofins_saidas.CST_COFINS,
               dw_pis_cofins_saidas.VL_BC_COFINS,
               dw_pis_cofins_saidas.ALIQ_COFINS,
               dw_pis_cofins_saidas.QUANT_BC_COFINS,
               dw_pis_cofins_saidas.ALIQ_COFINS_QUANT,
               dw_pis_cofins_saidas.VL_COFINS_ITEM,
               dw_pis_cofins_saidas.COD_CTA,
               dw_pis_cofins_saidas.CONCILIADO_PISCOFINS,
               dw_pis_cofins_saidas.ID_EFD_CTRL_REG_0000 
            FROM
               `DB_{base}`.dw_pis_cofins_saidas
            WHERE
               ID_ITEM IS NOT NULL 
               {value['DATA_INI']}
               {value['sql_cfop']}
               {value['cfop_null']}
               {value['geraCred']}
            """
    elif filtro == 'ambos':
        sql = f"""
              SELECT
               dw_pis_cofins_entradas.ID_ITEM,
               dw_pis_cofins_entradas.PK,
               dw_pis_cofins_entradas.DATA_INI,               
               dw_pis_cofins_entradas.CNPJ_FILIAL,
               dw_pis_cofins_entradas.REGISTRO,
               dw_pis_cofins_entradas.IND_ESCRI,
               dw_pis_cofins_entradas.IND_OPER,
               dw_pis_cofins_entradas.IND_EMIT,
               dw_pis_cofins_entradas.COD_PART,
               SUBSTRING_INDEX( SUBSTRING_INDEX( D_PART_REG_0150, 'STG&', 2 ), 'STG&',- 1 ) AS RAZAO_PART,
               SUBSTRING_INDEX( D_PART_REG_0150, 'STG&', 1 ) AS CNPJ_PART,
               (
               SELECT UF.descricao FROM	gerencial.uf_codigo_sigla AS UF WHERE	UF.codigo = SUBSTR( SUBSTRING_INDEX( D_PART_REG_0150, 'STG&',- 1 ), 1, 2 ) 
               ) AS UF_PART,
               dw_pis_cofins_entradas.D_PART_REG_0150,
               dw_pis_cofins_entradas.COD_MOD,
               dw_pis_cofins_entradas.COD_SIT,
               dw_pis_cofins_entradas.SER,
               dw_pis_cofins_entradas.NUM_DOC,
               (
             CASE
               WHEN dw_pis_cofins_entradas.REGISTRO = 'D100' THEN CONCAT('CTe',dw_pis_cofins_entradas.CHV_NFE)
               WHEN dw_pis_cofins_entradas.REGISTRO = 'C100' THEN CONCAT('NFe',dw_pis_cofins_entradas.CHV_NFE)
               WHEN dw_pis_cofins_entradas.REGISTRO = 'C190' THEN CONCAT('NFe',dw_pis_cofins_entradas.CHV_NFE)
               ELSE dw_pis_cofins_entradas.CHV_NFE
               END
               ) as CHV_NFE,
               dw_pis_cofins_entradas.DT_DOC,
               dw_pis_cofins_entradas.DT_E_S,
               dw_pis_cofins_entradas.VL_DOC,
               dw_pis_cofins_entradas.IND_PGTO,
               dw_pis_cofins_entradas.VL_DESC,
               dw_pis_cofins_entradas.VL_ABAT_NT,
               dw_pis_cofins_entradas.VL_MERC,
               dw_pis_cofins_entradas.IND_FRT,
               dw_pis_cofins_entradas.VL_FRT,
               dw_pis_cofins_entradas.VL_SEG,
               dw_pis_cofins_entradas.VL_OUT_DA,
               cast(
               REPLACE ( dw_pis_cofins_entradas.VL_BC_ICMS, ",", "." ) AS DECIMAL ( 15, 2 )) AS VL_BC_ICMS,
               cast(
               REPLACE ( dw_pis_cofins_entradas.VL_ICMS, ",", "." ) AS DECIMAL ( 15, 2 )) AS VL_ICMS,
               dw_pis_cofins_entradas.VL_BC_ICMS_ST,
               dw_pis_cofins_entradas.VL_ICMS_ST,
               dw_pis_cofins_entradas.VL_IPI,
               dw_pis_cofins_entradas.VL_PIS,
               dw_pis_cofins_entradas.VL_COFINS,
               dw_pis_cofins_entradas.VL_PIS_ST,
               dw_pis_cofins_entradas.VL_COFINS_ST,
               dw_pis_cofins_entradas.NUM_ITEM,
               dw_pis_cofins_entradas.COD_ITEM,
               dw_pis_cofins_entradas.DESCR_COMPL,
               SUBSTRING_INDEX( D_ITEM_REG_0200, 'STG&', 1 ) AS DESCR_0200,
            IF
               ( dw_pis_cofins_entradas.REGISTRO = 'C170', SUBSTRING_INDEX( D_ITEM_REG_0200, 'STG&',- 1 ), NULL ) AS COD_NCM_REG_0200,
            IF
               ( dw_pis_cofins_entradas.REGISTRO = 'C170', SUBSTRING_INDEX( SUBSTRING_INDEX( D_ITEM_REG_0200, 'STG&', 2 ), 'STG&',- 1 ), NULL ) AS TIPO_ITEM_REG_0200,
               dw_pis_cofins_entradas.D_ITEM_REG_0200,
               dw_pis_cofins_entradas.QTD,
               dw_pis_cofins_entradas.UNID,
               dw_pis_cofins_entradas.VL_ITEM,
               dw_pis_cofins_entradas.VL_DESC_ITEM,
               dw_pis_cofins_entradas.IND_MOV,
               dw_pis_cofins_entradas.CST_ICMS,
               dw_pis_cofins_entradas.CFOP,                
                (
               SELECT
                  DESCRICAO
               FROM
                  gerencial.tb_cfop
               WHERE
                  tb_cfop.CFOP = dw_pis_cofins_entradas.CFOP
               LIMIT 1 ) AS INF_CFOP,
               dw_pis_cofins_entradas.COD_NAT,
               dw_pis_cofins_entradas.VL_BC_ICMS_ITEM,
               dw_pis_cofins_entradas.ALIQ_ICMS,
               dw_pis_cofins_entradas.VL_ICMS_ITEM,
               dw_pis_cofins_entradas.VL_BC_ICMS_ST_ITEM,
               dw_pis_cofins_entradas.ALIQ_ST,
               dw_pis_cofins_entradas.VL_ICMS_ST_ITEM,
               dw_pis_cofins_entradas.IND_APUR,
               dw_pis_cofins_entradas.CST_IPI,
               dw_pis_cofins_entradas.COD_ENQ,
               dw_pis_cofins_entradas.VL_BC_IPI,
               dw_pis_cofins_entradas.ALIQ_IPI,
               dw_pis_cofins_entradas.VL_IPI_ITEM,
               dw_pis_cofins_entradas.CST_PIS,
               dw_pis_cofins_entradas.VL_BC_PIS,
               dw_pis_cofins_entradas.ALIQ_PIS,
               dw_pis_cofins_entradas.QUANT_BC_PIS,
               dw_pis_cofins_entradas.ALIQ_PIS_QUANT,
               dw_pis_cofins_entradas.VL_PIS_ITEM,
               dw_pis_cofins_entradas.CST_COFINS,
               dw_pis_cofins_entradas.VL_BC_COFINS,
               dw_pis_cofins_entradas.ALIQ_COFINS,
               dw_pis_cofins_entradas.QUANT_BC_COFINS,
               dw_pis_cofins_entradas.ALIQ_COFINS_QUANT,
               dw_pis_cofins_entradas.VL_COFINS_ITEM,
               dw_pis_cofins_entradas.COD_CTA,
               dw_pis_cofins_entradas.CONCILIADO_PISCOFINS,
               dw_pis_cofins_entradas.ID_EFD_CTRL_REG_0000 
            FROM
               `DB_{base}`.dw_pis_cofins_entradas
            WHERE
               ID_ITEM IS NOT NULL 
               {value['DATA_INI']}
               {value['sql_cfop']}
               {value['cfop_null']}
               {value['geraCred']}
                UNION
             SELECT
               dw_pis_cofins_saidas.ID_ITEM,
               dw_pis_cofins_saidas.PK,
               dw_pis_cofins_saidas.DATA_INI,
               dw_pis_cofins_saidas.CNPJ_FILIAL,
               dw_pis_cofins_saidas.REGISTRO,
               dw_pis_cofins_saidas.IND_ESCRI,
               dw_pis_cofins_saidas.IND_OPER,
               dw_pis_cofins_saidas.IND_EMIT,
               dw_pis_cofins_saidas.COD_PART,
               SUBSTRING_INDEX( SUBSTRING_INDEX( D_PART_REG_0150, 'STG&', 2 ), 'STG&',- 1 ) AS RAZAO_PART,
               SUBSTRING_INDEX( D_PART_REG_0150, 'STG&', 1 ) AS CNPJ_PART,
               (
               SELECT UF.descricao FROM	gerencial.uf_codigo_sigla AS UF WHERE	UF.codigo = SUBSTR( SUBSTRING_INDEX( D_PART_REG_0150, 'STG&',- 1 ), 1, 2 ) 
               ) AS UF_PART,
               dw_pis_cofins_saidas.D_PART_REG_0150,
               dw_pis_cofins_saidas.COD_MOD,
               dw_pis_cofins_saidas.COD_SIT,
               dw_pis_cofins_saidas.SER,
               dw_pis_cofins_saidas.NUM_DOC,
               dw_pis_cofins_saidas.CHV_NFE,
               dw_pis_cofins_saidas.DT_DOC,
               dw_pis_cofins_saidas.DT_E_S,
               dw_pis_cofins_saidas.VL_DOC,
               dw_pis_cofins_saidas.IND_PGTO,
               dw_pis_cofins_saidas.VL_DESC,
               dw_pis_cofins_saidas.VL_ABAT_NT,
               dw_pis_cofins_saidas.VL_MERC,
               dw_pis_cofins_saidas.IND_FRT,
               dw_pis_cofins_saidas.VL_FRT,
               dw_pis_cofins_saidas.VL_SEG,
               dw_pis_cofins_saidas.VL_OUT_DA,
               cast(
               REPLACE ( dw_pis_cofins_saidas.VL_BC_ICMS, ",", "." ) AS DECIMAL ( 15, 2 )) AS VL_BC_ICMS,
               cast(
               REPLACE ( dw_pis_cofins_saidas.VL_ICMS, ",", "." ) AS DECIMAL ( 15, 2 )) AS VL_ICMS,
               dw_pis_cofins_saidas.VL_BC_ICMS_ST,
               dw_pis_cofins_saidas.VL_ICMS_ST,
               dw_pis_cofins_saidas.VL_IPI,
               dw_pis_cofins_saidas.VL_PIS,
               dw_pis_cofins_saidas.VL_COFINS,
               dw_pis_cofins_saidas.VL_PIS_ST,
               dw_pis_cofins_saidas.VL_COFINS_ST,
               dw_pis_cofins_saidas.NUM_ITEM,
               dw_pis_cofins_saidas.COD_ITEM,
               dw_pis_cofins_saidas.DESCR_COMPL,
               SUBSTRING_INDEX( D_ITEM_REG_0200, 'STG&', 1 ) AS DESCR_0200,
            IF
               ( dw_pis_cofins_saidas.REGISTRO = 'C170', SUBSTRING_INDEX( D_ITEM_REG_0200, 'STG&',- 1 ), NULL ) AS COD_NCM_REG_0200,
            IF
               ( dw_pis_cofins_saidas.REGISTRO = 'C170', SUBSTRING_INDEX( SUBSTRING_INDEX( D_ITEM_REG_0200, 'STG&', 2 ), 'STG&',- 1 ), NULL ) AS TIPO_ITEM_REG_0200,
               dw_pis_cofins_saidas.D_ITEM_REG_0200,
               dw_pis_cofins_saidas.QTD,
               dw_pis_cofins_saidas.UNID,
               dw_pis_cofins_saidas.VL_ITEM,
               dw_pis_cofins_saidas.VL_DESC_ITEM,
               dw_pis_cofins_saidas.IND_MOV,
               dw_pis_cofins_saidas.CST_ICMS,
               dw_pis_cofins_saidas.CFOP,
                  (
               SELECT
                  DESCRICAO
               FROM
                  gerencial.tb_cfop
               WHERE
                  tb_cfop.CFOP = dw_pis_cofins_saidas.CFOP
               LIMIT 1 ) AS INF_CFOP,
               dw_pis_cofins_saidas.COD_NAT,
               dw_pis_cofins_saidas.VL_BC_ICMS_ITEM,
               dw_pis_cofins_saidas.ALIQ_ICMS,
               dw_pis_cofins_saidas.VL_ICMS_ITEM,
               dw_pis_cofins_saidas.VL_BC_ICMS_ST_ITEM,
               dw_pis_cofins_saidas.ALIQ_ST,
               dw_pis_cofins_saidas.VL_ICMS_ST_ITEM,
               dw_pis_cofins_saidas.IND_APUR,
               dw_pis_cofins_saidas.CST_IPI,
               dw_pis_cofins_saidas.COD_ENQ,
               dw_pis_cofins_saidas.VL_BC_IPI,
               dw_pis_cofins_saidas.ALIQ_IPI,
               dw_pis_cofins_saidas.VL_IPI_ITEM,
               dw_pis_cofins_saidas.CST_PIS,
               dw_pis_cofins_saidas.VL_BC_PIS,
               dw_pis_cofins_saidas.ALIQ_PIS,
               dw_pis_cofins_saidas.QUANT_BC_PIS,
               dw_pis_cofins_saidas.ALIQ_PIS_QUANT,
               dw_pis_cofins_saidas.VL_PIS_ITEM,
               dw_pis_cofins_saidas.CST_COFINS,
               dw_pis_cofins_saidas.VL_BC_COFINS,
               dw_pis_cofins_saidas.ALIQ_COFINS,
               dw_pis_cofins_saidas.QUANT_BC_COFINS,
               dw_pis_cofins_saidas.ALIQ_COFINS_QUANT,
               dw_pis_cofins_saidas.VL_COFINS_ITEM,
               dw_pis_cofins_saidas.COD_CTA,
               dw_pis_cofins_saidas.CONCILIADO_PISCOFINS,
               dw_pis_cofins_saidas.ID_EFD_CTRL_REG_0000 
            FROM
               `DB_{base}`.dw_pis_cofins_saidas
            WHERE
               ID_ITEM IS NOT NULL 
               {value['DATA_INI']}
               {value['sql_cfop']}
               {value['cfop_null']}
               {value['geraCred']}
                """
    try:
        msg = f'Conectando Select'
        if notify(f'{msg}', WS, rs) == False: 
            WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
            notify(f'{msg}', WS, rs)   
        
        with engine.connect() as conn:
            
            msg = f'Preparando Select, pode demorar'
            if notify(f'{msg}', WS, rs) == False: 
                WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
                notify(f'{msg}', WS, rs)   
            
            df1 = pd.read_sql_query(sql, conn)
            
            msg = f'Select Transformada'
            if notify(f'{msg}', WS, rs) == False: 
                WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
                notify(f'{msg}', WS, rs) 
    except Exception as e:
        raise e
        
    df1.fillna(0, inplace=True)

    arq_excel = f'{rs.get("page")}_{rs.get("base")}_{rs.get("userId")}_{rs.get("username")}_{dataagora}.xlsx'

    if len(rs.get('data_ini')) > 0:
        arq_excel = f'{rs.get("page")}_{rs.get("base")}_{convertNumber(rs.get("data_ini"))}_{convertNumber(rs.get("data_fim"))}_{dataagora}.xlsx'

    urlxls = os.path.join(BASE_DIR, f"media/{arq_excel}") 

    msg = f'criando o arquivo'
    if notify(f'{msg}', WS, rs) == False: 
        WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
        notify(f'{msg}', WS, rs)

    if len(df1) > 1000000:
        msg_ = {
            'message': 'Hello world',
            'id_user' : rs.get('userId'),
            'msg': f'[{rs.get("page")}] - Total de Registros: {len(df1)}, precisa diminuir mais para gerar o excel'
        }
        raise msg_ 
    else:
        try:
            listSheet = []
            x = df1['CNPJ_FILIAL'].unique()            

            # Create a workbook and add a worksheet.
            workbook = xlsxwriter.Workbook(urlxls)
            merge_format = workbook.add_format({
                            'bold': 1,
                            'border': 1,
                            'align': 'center',
                            'valign': 'vcenter'})     
            
            fx = df1.reset_index()
            del df1
            fx.index += 1 
            fx.drop(columns='index', inplace=True)

            msg = f'criando o arquivo, pode demorar...'
            if notify(f'{msg}', WS, rs) == False: 
                WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
                notify(f'{msg}', WS, rs)
            
            if eval(str(rs.get('sheet'))):
                for i in x:
                    sh = fx[fx['CNPJ_FILIAL'] == i]
                    listSheet.append( { "wk" : workbook.add_worksheet(str(i)), "sh" : sh })
                for idx in listSheet:                    
                    for z in range(0,len(idx['sh'].columns)):
                        idx['wk'].write(0, z, list(idx['sh'].columns)[z],merge_format)
                    
                    for index, row in idx['sh'].iterrows():    
                        for k, v in enumerate(list(row)):
                            idx['wk'].write(0+index, k, v)
                        
                for column in idx['sh']:
                    value = idx['sh'][column].astype(str).map(len).max()    

                    if value > 50:   
                        column_width = len(column)
                    else:
                        column_width = max(value+5, len(column))
                        
                    col_idx = idx['sh'].columns.get_loc(column)
                    idx['wk'].set_column(col_idx, col_idx, column_width)
            else:
                worksheet = workbook.add_worksheet()
                merge_format = workbook.add_format({
                'bold': 1,
                'border': 1,
                'align': 'center',
                'valign': 'vcenter'})
                for z in range(0,len(fx.columns)):
                    worksheet.write(0, z, list(fx.columns)[z],merge_format)
                    
                for index, row in fx.iterrows():    
                    for k, v in enumerate(list(row)):
                        worksheet.write(0+index, k, v)
                        msg = f'escrevendo XlS, {k}'
                        if notify(f'{msg}', WS, rs) == False: 
                            WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
                            notify(f'{msg}', WS, rs)
                        
                for column in fx:
                    value = fx[column].astype(str).map(len).max()    

                    if value > 50:   
                        column_width = len(column)
                    else:
                        column_width = max(value+5, len(column))                    
                    col_idx = fx.columns.get_loc(column)

                    msg = f'organizando colunas XlS, {column}, {col_idx}'
                    if notify(f'{msg}', WS, rs) == False: 
                        WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
                        notify(f'{msg}', WS, rs)                        

                    worksheet.set_column(col_idx, col_idx, column_width)                
            workbook.close()
        except Exception as e:
            raise e 
       
        msg = f'preparando o Link, pode demorar'
        if notify(f'{msg}', WS, rs) == False: 
            WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
            notify(f'{msg}', WS, rs)

        rs['nome_arquivo'] = arq_excel   
        rs['total_registros'] = len(fx)

        msg = f'Retornando a MSG'
        if notify(f'{msg}', WS, rs) == False: 
            WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
            notify(f'{msg}', WS, rs)

        msg_ = {
            "data": "Criado com Sucesso",
            "userId" : f"{rs['userId']}",
            "page": f"{rs['page']}",
            "erro" : 0,
            "link" : 1,
            "msg": f"https://stgapi.cf:9993/{arq_excel}",        
        }

        msg = f'Criado com Sucesso::https://stgapi.cf:9993/{arq_excel}'
        if notify(f'{msg}', WS, rs) == False: 
            WS = create_connection(f"{url_ws}{random.randint(10000, 99999)}")
            notify(f'{msg}', WS, rs)

        ren(rs,'id_user', 'userId') 
        ren(rs,'cnpj_conta', 'base') 
        ren(rs,'cliente', 'nomeEmpresa') 
        ren(rs,'tipo_relatorio', 'page')         
        ren(rs,'user_name', 'username')
        ren(rs,'dados_cfop', 'cfop')

        rs.pop('idEmpresa') 
        rs.pop('tamanho') 

        try:
            gravabanco_ctrl_arq_excel(rs)
        except Exception as e:
            raise e 
        
        return msg_
