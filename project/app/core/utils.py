from datetime import datetime
import pandas as pd
from sqlalchemy import create_engine


def gravabanco_ctrl_arq_excel(dados):
    df = pd.DataFrame(dados)

    engine = create_engine(f"{URL_CONNECT}/gerencial")
    with engine.connect() as conn:
        df.to_sql('ctrl_arq_excel_contabil', con=conn, if_exists='append', index_label='id', index=True)


def convertData(data_string):
      data_string = data_string.replace('/', '-')
      data = datetime.strptime(data_string, '%d-%m-%Y').date()
      return str(data.strftime('%Y-%m-%d'))

def converte_data(df, column_name):
      return pd.to_datetime(df[column_name])

def convertNumber(dados):
      return int(''.join(filter(str.isdigit, dados)))