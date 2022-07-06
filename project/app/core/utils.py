from datetime import datetime
import pandas as pd
from sqlalchemy import create_engine
from core.configs import settings

def gravabanco_ctrl_arq_excel(dados):
#     df = pd.DataFrame.from_dict(dados, orient='index')
    df = pd.DataFrame(dados, index=[0])

    engine = create_engine(f"{settings.URL_CONNECT}/gerencial")
    
    try:
      with engine.connect() as conn:
            df.to_sql('ctrl_arq_excel_contabil', con=conn, if_exists='append', index_label='id', index=True)
    except Exception as e:
      raise e


def dif_month(data1, data2):    
    ano, mes, dia = data1.split('-')
    d1 = datetime(int(ano),int(mes),int(dia))    
    ano, mes, dia = data2.split('-')
    d2 = datetime(int(ano),int(mes),int(dia))
    return (d2 - d1).days // 30

def ren(dict, novo, antigo):
      dict[novo] = dict.pop(antigo)

def convertData(data_string):
      data_string = data_string.replace('/', '-')
      data = datetime.strptime(data_string, '%d-%m-%Y').date()
      return str(data.strftime('%Y-%m-%d'))

def converte_data(df, column_name):
      return pd.to_datetime(df[column_name])

def convertNumber(dados):
      return int(''.join(filter(str.isdigit, dados)))