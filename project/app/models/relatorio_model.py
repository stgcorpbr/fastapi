from typing import Optional
from datetime import datetime
from sqlmodel import Field, SQLModel
from sqlalchemy.orm import relationship
from sqlalchemy import CHAR, DECIMAL, Date, Integer, String, Column, Boolean, DateTime, Text, TIMESTAMP, INT
from core.configs import settings
from sqlalchemy import text


class CtrlArqExcelContabil(settings.DBBaseModel):
    __tablename__ = 'ctrl_arq_excel_contabil'

    id = Column(Integer, primary_key=True, autoincrement=True)    
    id_user = Column(Text)
    user_name = Column(Text)
    email = Column(Text)
    cnpj_conta = Column(Text)
    data_ini = Column(Text)
    data_fim = Column(Text)
    cod_natureza = Column(Text)
    cod_conta = Column(Text)
    sheet = Column(Text)
    tipo_relatorio = Column(Text)
    nome_arquivo = Column(Text)
    total_registros = Column(Text)
    data_cadastrada = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))
    cliente = Column(String(200))
    filtro = Column(String(50))
    mes = Column(String(2))
    uf_filial = Column(String(2))
    dados_cfop = Column(Text)
    geraCred = Column(String(50))