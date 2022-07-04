import random
import os

from datetime import datetime
from pathlib import Path
from core import utils


from celery import shared_task
from sqlalchemy import create_engine

from core.configs import settings
from . import mail

from websocket import create_connection

import pandas as pd
from pyexcelerate import Workbook


# URL_CONNECT = "mysql+aiomysql://userdb:SysDb123#ee@stgbd.cf"
URL_CONNECT = "mysql+pymysql://userdb:SysDb123#ee@stgbd.cf"
BASE_DIR = Path(__file__).resolve().parent.parent

def notify(msg, ws, rs):
    if msg == 'fim': ws.send(msg)
    x = {
        'data': msg,
        'userId': rs['userId'],
        'page': rs['page']
        }
    try: 
        ws.send(str(x))
    except:
        pass

@shared_task
def send_email(email):
    print('dentro da função')
    return mail.core_notification(email)

@shared_task
def ajuste_apuracao_icms_task(rs):
    ws = create_connection(f"wss://stgapi.cf:7000/ws/{random.randint(10000, 99999)}")
    dataagora = datetime.now().strftime("%d%m%Y%H%M%S")
    value = {'sql_data': ''}
    base = rs.get('base')

    if len(rs.get('data_ini')) > 0 and len(rs.get('data_fim')) > 0:
         value['sql_data'] = f"""
            AND sped_icms_ipi_ctrl.DATA_INI BETWEEN '{ utils.convertData(rst.get('data_ini'))}' AND '{ utils.convertData(rst.get('data_fim'))}'
      """

    notify(f'Conectando com a Base: DB_{base}', ws, rs)
    engine = create_engine(f"{URL_CONNECT}/DB_{base}")
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

    with engine.connect() as conn:
        rst = pd.read_sql_query(sql, conn)

    data_ = 'Acima do excel'

    if len(rst) < 1000000:
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
        with engine.connect() as conn:
            df1 = pd.read_sql_query(sql, conn)
        
        df1.fillna(0, inplace=True)

        df1['DATA_INI'] = utils.converte_data(df1, 'DATA_INI').dt.strftime('%d/%m/%Y')
        df1['VL_AJ_APUR'] = df1['VL_AJ_APUR'].str.replace(',', '.').astype("float64")

        data_ = 'Perfeito para o excel'

        arq_excel = f'{rs.get("page")}_{rs.get("cnpj_conta")}_{rs.get("userId")}_{rs.get("username")}_{dataagora}.xlsx'

        if len(rs.get('data_ini')) > 0:
            arq_excel = f'{rs.get("page")}_{rs.get("cnpj_conta")}_{utils.convertNumber(rs.get("data_ini"))}_{utils.convertNumber(rs.get("data_fim"))}.xlsx'

        urlxls = os.path.join(BASE_DIR, f"media/{arq_excel}") 

        notify(f'Criando o arquivo: {arq_excel}', ws, rs)             

        wb = Workbook()
        values = [df1.columns] + list(df1.values)
        wb.new_sheet('sheet name', data=values)
        wb.save(urlxls)

        notify('Arquivo criado com Sucesso', ws, rs)

        rs['nome_arquivo'] = arq_excel   
        notify('Retornando a MSG', ws, rs)
        msg_ = {
            'message': 'Hello world',
            'id_user': rs.get('userId'),
            'msg': f'{arq_excel}'
        } 
        
        # utils.gravabanco_ctrl_arq_excel(rs)
        # notify('fim', ws, rs)
        return str(urlxls)
        
        msg_ = {
        'message': 'Hello world',
        'id_user': rs.get('userId'),
        'msg': f'https://www.stganalytics.com.br/media/{arq_excel}'
        }
    