import os
import random

from pathlib import Path
from datetime import datetime

from celery import Celery, shared_task
from celery.utils.log import get_task_logger
# from celery.schedules  import crontab

import pandas as pd
from pyexcelerate import Workbook

from websocket import create_connection
from sqlalchemy import create_engine, text
import xlsxwriter
from core.configs import settings
from core import utils
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
    except:
        pass


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
        ws = create_connection(f"wss://stgapi.cf:7000/ws/{random.randint(10000, 99999)}")
    except Exception as e:
        raise e 

    dataagora = datetime.now().strftime("%d%m%Y%H%M%S")
    value = {'sql_data': ''}
    base = rs.get('base')

    data1 = utils.convertData(rs.get('data_ini'))
    data2 = utils.convertData(rs.get('data_fim'))

    if len(rs.get('data_ini')) > 0 and len(rs.get('data_fim')) > 0:
         value['sql_data'] = f"""
            AND sped_icms_ipi_ctrl.DATA_INI BETWEEN '{data1}' AND '{data2}'
      """    

    notify(f'Conectando com a Base: DB_{base}', ws, rs)

    try:
        engine = create_engine(f"{URL_CONNECT}/DB_{base}")
    except Exception as e:
        raise e

    notify('Base conectada', ws, rs)

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
        notify('Ok abaixo de 1 milhão OK', ws, rs)
        
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
                        if utils.dif_month(data1, data2) != rst_[0]:
                            print(utils.dif_month(data1, data2),rst_[0], row[0])
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
                rst = connection.execute(sql).fetchmany()

                if len(list(connection.execute(sql).scalars().unique().all())) <= 0:
                    for t in x1_col:                
                        g.insert(0, 'N')
                    g.insert(0, row['cnpj'])                    
                    x1_df_new.loc[index] = g
                    g = []
                else:
                    for _,r in enumerate(rst):
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

        utils.write_title("A,B",3,'FILIAL,DATA',bold,worksheet2)

        cell_format = workbook.add_format()
        cell_format.set_num_format('dd/mm/yy')

        for index, row in fx.iterrows():
            utils.writeLine('A',3+index,row['FILIAL'],worksheet2)
            utils.writeLine('B',3+index,row['DATA'],worksheet2)

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

        notify('Arquivo criado com Sucesso', ws, rs)

        rs['nome_arquivo'] = arq_excel
        rs['total_registros'] = rst.qtd           
        notify('Retornando a MSG', ws, rs)
                
        utils.ren(rs,'id_user', 'userId') 
        utils.ren(rs,'cnpj_conta', 'base') 
        utils.ren(rs,'cliente', 'nomeEmpresa') 
        utils.ren(rs,'tipo_relatorio', 'page')         
        utils.ren(rs,'user_name', 'username')       
        
        rs.pop('idEmpresa') 

        try:
            utils.gravabanco_ctrl_arq_excel(rs)
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
        ws = create_connection(f"wss://stgapi.cf:7000/ws/{random.randint(10000, 99999)}")
    except Exception as e:
        raise e 

    
    dataagora = datetime.now().strftime("%d%m%Y%H%M%S")
    value = {'sql_data': ''}
    base = rs.get('base')

    if len(rs.get('data_ini')) > 0 and len(rs.get('data_fim')) > 0:
         value['sql_data'] = f"""
            AND sped_icms_ipi_ctrl.DATA_INI BETWEEN '{ utils.convertData(rs.get('data_ini'))}' AND '{ utils.convertData(rs.get('data_fim'))}'
      """

    notify(f'Conectando com a Base: DB_{base}', ws, rs)

    try:
        engine = create_engine(f"{URL_CONNECT}/DB_{base}")
    except Exception as e:
        raise e    

    notify('Base conectada', ws, rs)
    
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
        notify('Ok abaixo de 1 milhão OK', ws, rs)

        try:
            with engine.connect() as conn:
              df1 = pd.read_sql_query(sql, conn)
        except Exception as e:
            raise e
        
        df1.fillna(0, inplace=True)

        df1['DATA_INI'] = utils.converte_data(df1, 'DATA_INI').dt.strftime('%d/%m/%Y')
        df1['VL_AJ_APUR'] = df1['VL_AJ_APUR'].str.replace(',', '.').astype("float64")

        data_ = 'Perfeito para o excel'

        arq_excel = f'{rs.get("page")}_{rs.get("base")}_{rs.get("userId")}_{rs.get("username")}_{dataagora}.xlsx'

        if len(rs.get('data_ini')) > 0:
            arq_excel = f'{rs.get("page")}_{rs.get("base")}_{utils.convertNumber(rs.get("data_ini"))}_{utils.convertNumber(rs.get("data_fim"))}_{dataagora}.xlsx'

        urlxls = os.path.join(BASE_DIR, f"media/{arq_excel}") 

        notify(f'Criando o arquivo: {arq_excel}', ws, rs)  

        try:
            wb = Workbook()
            values = [df1.columns] + list(df1.values)
            wb.new_sheet('sheet name', data=values)
            wb.save(urlxls)
        except Exception as e:
            raise e 

        notify('Arquivo criado com Sucesso', ws, rs)

        rs['nome_arquivo'] = arq_excel   
        rs['total_registros'] = rst.qtd
        notify('Retornando a MSG', ws, rs)
      
        utils.ren(rs,'id_user', 'userId') 
        utils.ren(rs,'cnpj_conta', 'base') 
        utils.ren(rs,'cliente', 'nomeEmpresa') 
        utils.ren(rs,'tipo_relatorio', 'page')         
        utils.ren(rs,'user_name', 'username')       
        
        rs.pop('idEmpresa') 

        try:
            utils.gravabanco_ctrl_arq_excel(rs)
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
    
