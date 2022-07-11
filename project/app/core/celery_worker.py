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

    data1 = convertData(rs.get('data_ini'))
    data2 = convertData(rs.get('data_fim'))

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


        notify('Arquivo criado com Sucesso', ws, rs)

        rs['nome_arquivo'] = arq_excel
        rs['total_registros'] = rst.qtd           
        notify('Retornando a MSG', ws, rs)
                
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
        ws = create_connection(f"wss://stgapi.cf:7000/ws/{random.randint(10000, 99999)}")
    except Exception as e:
        raise e 
    
    dataagora = datetime.now().strftime("%d%m%Y%H%M%S")
    value = {'sql_data': ''}
    base = rs.get('base')

    if len(rs.get('data_ini')) > 0 and len(rs.get('data_fim')) > 0:
         value['sql_data'] = f"""
            AND sped_pis_cofins_ctrl.DATA_INI BETWEEN '{ convertData(rs.get('data_ini'))}' AND '{ convertData(rs.get('data_fim'))}'
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

        notify('Ok abaixo de 1 milhão OK', ws, rs)

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
        rs['total_registros'] = max(list(rst.qtd))
        
        notify('Retornando a MSG', ws, rs)
      
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
        ws = create_connection(f"wss://stgapi.cf:7000/ws/{random.randint(10000, 99999)}")
    except Exception as e:
        raise e 
    
    dataagora = datetime.now().strftime("%d%m%Y%H%M%S")
    value = {'sql_data': ''}
    base = rs.get('base')

    if len(rs.get('data_ini')) > 0 and len(rs.get('data_fim')) > 0:
         value['sql_data'] = f"""
            AND sped_pis_cofins_ctrl.DATA_INI BETWEEN '{ convertData(rs.get('data_ini'))}' AND '{ convertData(rs.get('data_fim'))}'
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

        notify('Ok abaixo de 1 milhão OK', ws, rs)

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
        rs['total_registros'] = max(list(rst.qtd))
        
        notify('Retornando a MSG', ws, rs)
      
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
        ws = create_connection(f"wss://stgapi.cf:7000/ws/{random.randint(10000, 99999)}")
    except Exception as e:
        raise e 
    
    dataagora = datetime.now().strftime("%d%m%Y%H%M%S")
    value = {'sql_data': ''}
    base = rs.get('base')

    if len(rs.get('data_ini')) > 0 and len(rs.get('data_fim')) > 0:
         value['sql_data'] = f"""
            AND sped_icms_ipi_ctrl.DATA_INI BETWEEN '{ convertData(rs.get('data_ini'))}' AND '{ convertData(rs.get('data_fim'))}'
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

        df1['DATA_INI'] = converte_data(df1, 'DATA_INI').dt.strftime('%d/%m/%Y')
        df1['VL_AJ_APUR'] = df1['VL_AJ_APUR'].str.replace(',', '.').astype("float64")

        data_ = 'Perfeito para o excel'

        arq_excel = f'{rs.get("page")}_{rs.get("base")}_{rs.get("userId")}_{rs.get("username")}_{dataagora}.xlsx'

        if len(rs.get('data_ini')) > 0:
            arq_excel = f'{rs.get("page")}_{rs.get("base")}_{convertNumber(rs.get("data_ini"))}_{convertNumber(rs.get("data_fim"))}_{dataagora}.xlsx'

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
    
