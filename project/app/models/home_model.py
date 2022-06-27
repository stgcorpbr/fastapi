from typing import Optional
from datetime import datetime
from sqlmodel import Field, SQLModel
from sqlalchemy.orm import relationship
from sqlalchemy import CHAR, DECIMAL, Date, Integer, String, Column, Boolean, DateTime, Text, TIMESTAMP, INT
from core.configs import settings
from sqlalchemy import text

class TbClientes(settings.DBBaseModel):
    __tablename__ = 'tb_clientes'

    id_cliente = Column(Integer, primary_key=True, autoincrement=True)    
    razao_social = Column(String(256), nullable=True)
    cnpj_compl = Column(String(256), nullable=True)
    apelido = Column(String(256), nullable=True)
    cnpj = Column(String(256), nullable=True)
    dt_final = Column(String(256), nullable=True)
    dt_inicial = Column(String(256), nullable=True)
    qtd_analise = Column(String(256), nullable=True)
    ativo = Column(String(256), nullable=True)
    dt_criacao = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))
    grupo = Column(String(256), nullable=True)


class DwIcmsIpiEntradas(settings.DBBaseModel):
    __tablename__ = 'dw_icms_ipi_entradas'

    ID_ITEM = Column(Integer, primary_key=True, autoincrement=True)
    CHV_PK = Column(String(55), index=True)
    DATA_INI = Column(Date, index=True)
    # CNPJ_FILIAL = Column(CHAR(14), index=True)
    # RAZAO_FILIAL = Column(String(255))
    # UF_FILIAL = Column(CHAR(2))
    # REGISTRO = Column(String(4), index=True)
    # CHV_NFE_CTE = Column(String(44), index=True)
    # VL_BC_ICMS = Column(String(30))
    # VL_ICMS = Column(String(30))
    # VL_DOC = Column(DECIMAL(15, 2))
    # COD_PART = Column(String(65))
    # D_PART_REG_0150 = Column(String(255), index=True)
    # RAZAO_PART = Column(String(255))
    # CNPJ_PART = Column(String(14), index=True)
    # UF_PART = Column(String(2))
    # NUM_DOC = Column(Integer, index=True)
    # DT_DOC = Column(String(10))
    # DT_E_S = Column(String(10))
    # IND_EMIT = Column(String(1))
    # COD_MOD = Column(String(2))
    # COD_SIT = Column(String(2))
    # SER = Column(String(3))
    # COD_ITEM = Column(String(60), index=True)
    # NUM_ITEM = Column(Integer)
    # DESCR_COMPL = Column(String(255))
    # D_ITEM_REG_0200 = Column(String(255))
    # COD_NCM_REG_0200 = Column(String(10))
    # TIPO_ITEM_REG_0200 = Column(String(3))
    # VL_ITEM = Column(DECIMAL(15, 2))
    # CFOP = Column(String(4), index=True)
    # VL_BC_ICMS_ITEM = Column(DECIMAL(21, 2))
    # ALIQ_ICMS_ITEM = Column(DECIMAL(8, 2))
    # VL_ICMS_ITEM = Column(DECIMAL(21, 2), index=True)
    # CST_ICMS = Column(String(3))
    # VL_BC_ICMS_ST = Column(DECIMAL(21, 2))
    # ALIQ_ST = Column(DECIMAL(8, 2))
    # VL_ICMS_ST = Column(DECIMAL(21, 2))
    # VL_BC_IPI = Column(DECIMAL(21, 2))
    # ALIQ_IPI = Column(DECIMAL(8, 2))
    # VL_IPI = Column(DECIMAL(21, 2))
    # CST_IPI = Column(String(2))
    # CONCILIADO_PISCOFINS = Column(String(150), index=True)
    # CONCILIADO_XML = Column(String(150))
    # ID_SPEDFIS_CTRL_REG_0000 = Column(Integer, index=True)