# coding: utf-8
from sqlalchemy import CHAR, Column, DECIMAL, Date, DateTime, Float, Index, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import BIGINT, INTEGER, LONGTEXT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


t_dl_nt_icms_entradas_cfop_n = Table(
    'dl_nt_icms_entradas_cfop_n', metadata,
    Column('ID_ITEM', BIGINT(25), nullable=False),
    Column('CHV_PK', String(55)),
    Column('DATA_INI', Date),
    Column('CNPJ_FILIAL', CHAR(14)),
    Column('RAZAO_FILIAL', String(255)),
    Column('UF_FILIAL', CHAR(2)),
    Column('REGISTRO', String(4)),
    Column('CHV_NFE_CTE', String(44)),
    Column('VL_BC_ICMS', String(30)),
    Column('VL_ICMS', String(30)),
    Column('VL_DOC', DECIMAL(15, 2)),
    Column('COD_PART', String(65)),
    Column('RAZAO_PART', String(255)),
    Column('CNPJ_PART', String(255)),
    Column('UF_PART', String(2)),
    Column('NUM_DOC', String(9)),
    Column('DT_DOC', String(10)),
    Column('DT_E_S', String(10)),
    Column('IND_EMIT', String(1)),
    Column('COD_MOD', String(2)),
    Column('COD_SIT', String(2)),
    Column('SER', String(3)),
    Column('COD_ITEM', String(60)),
    Column('NUM_ITEM', INTEGER(3)),
    Column('DESCR_COMPL', String(255)),
    Column('DESCR_0200', String(255)),
    Column('COD_NCM_REG_0200', String(255)),
    Column('TIPO_ITEM_REG_0200', String(255)),
    Column('VL_ITEM', DECIMAL(15, 2)),
    Column('CFOP', String(4)),
    Column('ID_SPEDFIS_CTRL_REG_0000', INTEGER(11))
)


t_dl_nt_icms_entradas_cfop_s_t = Table(
    'dl_nt_icms_entradas_cfop_s_t', metadata,
    Column('ID_ITEM', BIGINT(25), nullable=False),
    Column('CHV_PK', String(55)),
    Column('DATA_INI', Date),
    Column('CNPJ_FILIAL', CHAR(14)),
    Column('RAZAO_FILIAL', String(255)),
    Column('UF_FILIAL', CHAR(2)),
    Column('REGISTRO', String(4)),
    Column('CHV_NFE_CTE', String(44)),
    Column('VL_BC_ICMS', String(30)),
    Column('VL_ICMS', String(30)),
    Column('VL_DOC', DECIMAL(15, 2)),
    Column('COD_PART', String(65)),
    Column('RAZAO_PART', String(255)),
    Column('CNPJ_PART', String(255)),
    Column('UF_PART', String(2)),
    Column('NUM_DOC', String(9)),
    Column('DT_DOC', String(10)),
    Column('DT_E_S', String(10)),
    Column('IND_EMIT', String(1)),
    Column('COD_MOD', String(2)),
    Column('COD_SIT', String(2)),
    Column('SER', String(3)),
    Column('COD_ITEM', String(60)),
    Column('NUM_ITEM', INTEGER(3)),
    Column('DESCR_COMPL', String(255)),
    Column('DESCR_0200', String(255)),
    Column('COD_NCM_REG_0200', String(255)),
    Column('TIPO_ITEM_REG_0200', String(255)),
    Column('VL_ITEM', DECIMAL(15, 2)),
    Column('CFOP', String(4)),
    Column('ID_SPEDFIS_CTRL_REG_0000', INTEGER(11))
)


class DwBalanceteContabilGeral(Base):
    __tablename__ = 'dw_balancete_contabil_geral'

    ID_BALANCETE_GERAL = Column(INTEGER(11), primary_key=True)
    DT_FIN = Column(Date)
    DT_ESCRIT = Column(VARCHAR(10))
    COD_NAT = Column(VARCHAR(2))
    COD_CTA = Column(VARCHAR(255))
    CTA = Column(VARCHAR(255))
    COD_CCUS = Column(VARCHAR(255))
    VL_SLD_INI = Column(VARCHAR(30))
    IND_DC_INI = Column(VARCHAR(1))
    VL_DEB = Column(VARCHAR(30))
    VL_CRED = Column(VARCHAR(30))
    VL_SLD_FIN = Column(VARCHAR(30))
    VL_SLD_FIN_I355 = Column(VARCHAR(30))
    IND_DC_FIN = Column(VARCHAR(1))
    ID_SPEDCONT_CTRL_REG_0000 = Column(INTEGER(11))


class DwIcmsIpiEntradas(Base):
    __tablename__ = 'dw_icms_ipi_entradas'

    ID_ITEM = Column(BIGINT(25), primary_key=True)
    CHV_PK = Column(String(55), index=True)
    DATA_INI = Column(Date, index=True)
    CNPJ_FILIAL = Column(CHAR(14), index=True)
    RAZAO_FILIAL = Column(String(255))
    UF_FILIAL = Column(CHAR(2))
    REGISTRO = Column(String(4), index=True)
    CHV_NFE_CTE = Column(String(44), index=True)
    VL_BC_ICMS = Column(String(30))
    VL_ICMS = Column(String(30))
    VL_DOC = Column(DECIMAL(15, 2))
    COD_PART = Column(String(65))
    D_PART_REG_0150 = Column(String(255), index=True)
    RAZAO_PART = Column(String(255))
    CNPJ_PART = Column(String(14), index=True)
    UF_PART = Column(String(2))
    NUM_DOC = Column(INTEGER(9), index=True)
    DT_DOC = Column(String(10))
    DT_E_S = Column(String(10))
    IND_EMIT = Column(String(1))
    COD_MOD = Column(String(2))
    COD_SIT = Column(String(2))
    SER = Column(String(3))
    COD_ITEM = Column(String(60), index=True)
    NUM_ITEM = Column(INTEGER(3))
    DESCR_COMPL = Column(String(255))
    D_ITEM_REG_0200 = Column(String(255))
    COD_NCM_REG_0200 = Column(String(10))
    TIPO_ITEM_REG_0200 = Column(String(3))
    VL_ITEM = Column(DECIMAL(15, 2))
    CFOP = Column(String(4), index=True)
    VL_BC_ICMS_ITEM = Column(DECIMAL(21, 2))
    ALIQ_ICMS_ITEM = Column(DECIMAL(8, 2))
    VL_ICMS_ITEM = Column(DECIMAL(21, 2), index=True)
    CST_ICMS = Column(String(3))
    VL_BC_ICMS_ST = Column(DECIMAL(21, 2))
    ALIQ_ST = Column(DECIMAL(8, 2))
    VL_ICMS_ST = Column(DECIMAL(21, 2))
    VL_BC_IPI = Column(DECIMAL(21, 2))
    ALIQ_IPI = Column(DECIMAL(8, 2))
    VL_IPI = Column(DECIMAL(21, 2))
    CST_IPI = Column(String(2))
    CONCILIADO_PISCOFINS = Column(String(150), index=True)
    CONCILIADO_XML = Column(String(150))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11), index=True)


class DwIcmsIpiSaidas(Base):
    __tablename__ = 'dw_icms_ipi_saidas'

    ID_ITEM = Column(BIGINT(25), primary_key=True)
    CHV_PK = Column(String(55), index=True)
    DATA_INI = Column(Date, index=True)
    CNPJ_FILIAL = Column(CHAR(14), index=True)
    RAZAO_FILIAL = Column(String(255))
    UF_FILIAL = Column(CHAR(2))
    REGISTRO = Column(String(4), index=True)
    CHV_NFE_CTE = Column(String(44), index=True)
    VL_BC_ICMS = Column(String(30))
    VL_ICMS = Column(String(30))
    VL_DOC = Column(DECIMAL(15, 2))
    COD_PART = Column(String(65))
    D_PART_REG_0150 = Column(String(255))
    RAZAO_PART = Column(String(255))
    CNPJ_PART = Column(String(14), index=True)
    UF_PART = Column(String(2))
    NUM_DOC = Column(INTEGER(9), index=True)
    DT_DOC = Column(String(10))
    DT_E_S = Column(String(10))
    IND_EMIT = Column(String(1))
    COD_MOD = Column(String(2))
    COD_SIT = Column(String(2))
    SER = Column(String(3))
    COD_ITEM = Column(String(60), index=True)
    NUM_ITEM = Column(INTEGER(3))
    DESCR_COMPL = Column(String(255))
    D_ITEM_REG_0200 = Column(String(255))
    COD_NCM_REG_0200 = Column(String(10))
    TIPO_ITEM_REG_0200 = Column(String(3))
    VL_ITEM = Column(DECIMAL(15, 2))
    CFOP = Column(String(4), index=True)
    VL_BC_ICMS_ITEM = Column(DECIMAL(21, 2))
    ALIQ_ICMS_ITEM = Column(DECIMAL(8, 2))
    VL_ICMS_ITEM = Column(DECIMAL(21, 2), index=True)
    CST_ICMS = Column(String(3))
    VL_BC_ICMS_ST = Column(DECIMAL(21, 2))
    ALIQ_ST = Column(DECIMAL(8, 2))
    VL_ICMS_ST = Column(DECIMAL(21, 2))
    VL_BC_IPI = Column(DECIMAL(21, 2))
    ALIQ_IPI = Column(DECIMAL(8, 2))
    VL_IPI = Column(DECIMAL(21, 2))
    CST_IPI = Column(String(2))
    CONCILIADO_PISCOFINS = Column(String(150), index=True)
    CONCILIADO_XML = Column(String(150))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11), index=True)


class DwPisCofinsEntradas(Base):
    __tablename__ = 'dw_pis_cofins_entradas'

    ID_ITEM = Column(BIGINT(25), primary_key=True)
    PK = Column(VARCHAR(65))
    DATA_INI = Column(Date)
    CNPJ_FILIAL = Column(VARCHAR(14))
    REGISTRO = Column(VARCHAR(4), server_default=text("''"))
    IND_ESCRI = Column(VARCHAR(1))
    IND_OPER = Column(VARCHAR(1))
    IND_EMIT = Column(VARCHAR(1))
    COD_PART = Column(VARCHAR(60))
    D_PART_REG_0150 = Column(VARCHAR(140))
    RAZAO_PART = Column(String(140))
    CNPJ_PART = Column(String(14))
    UF_PART = Column(String(2))
    COD_MOD = Column(VARCHAR(2))
    COD_SIT = Column(VARCHAR(2))
    SER = Column(VARCHAR(3))
    NUM_DOC = Column(INTEGER(9), index=True)
    CHV_NFE = Column(VARCHAR(44), index=True)
    DT_DOC = Column(VARCHAR(100))
    DT_E_S = Column(VARCHAR(100))
    VL_DOC = Column(DECIMAL(15, 2))
    IND_PGTO = Column(VARCHAR(1))
    VL_DESC = Column(DECIMAL(15, 2))
    VL_ABAT_NT = Column(DECIMAL(15, 2))
    VL_MERC = Column(DECIMAL(15, 2))
    IND_FRT = Column(VARCHAR(1))
    VL_FRT = Column(DECIMAL(15, 2))
    VL_SEG = Column(DECIMAL(15, 2))
    VL_OUT_DA = Column(DECIMAL(15, 2))
    VL_BC_ICMS = Column(DECIMAL(15, 2))
    VL_ICMS = Column(DECIMAL(15, 2))
    VL_BC_ICMS_ST = Column(DECIMAL(15, 2))
    VL_ICMS_ST = Column(DECIMAL(15, 2))
    VL_IPI = Column(DECIMAL(15, 2))
    VL_PIS = Column(DECIMAL(15, 2))
    VL_COFINS = Column(DECIMAL(15, 2))
    VL_PIS_ST = Column(DECIMAL(15, 2))
    VL_COFINS_ST = Column(DECIMAL(15, 2))
    NUM_ITEM = Column(INTEGER(3))
    COD_ITEM = Column(VARCHAR(60))
    DESCR_COMPL = Column(VARCHAR(255))
    D_ITEM_REG_0200 = Column(VARCHAR(273))
    COD_NCM_REG_0200 = Column(String(10))
    TIPO_ITEM_REG_0200 = Column(String(3))
    QTD = Column(VARCHAR(12))
    UNID = Column(VARCHAR(6))
    VL_ITEM = Column(DECIMAL(15, 2))
    VL_DESC_ITEM = Column(DECIMAL(15, 2))
    IND_MOV = Column(VARCHAR(1))
    CST_ICMS = Column(VARCHAR(3))
    CFOP = Column(VARCHAR(4))
    COD_NAT = Column(VARCHAR(10))
    VL_BC_ICMS_ITEM = Column(DECIMAL(15, 2))
    ALIQ_ICMS = Column(DECIMAL(8, 2))
    VL_ICMS_ITEM = Column(DECIMAL(15, 2))
    VL_BC_ICMS_ST_ITEM = Column(DECIMAL(15, 2))
    ALIQ_ST = Column(DECIMAL(8, 2))
    VL_ICMS_ST_ITEM = Column(DECIMAL(15, 2))
    IND_APUR = Column(VARCHAR(1))
    CST_IPI = Column(VARCHAR(2))
    COD_ENQ = Column(VARCHAR(3))
    VL_BC_IPI = Column(DECIMAL(15, 2))
    ALIQ_IPI = Column(DECIMAL(15, 2))
    VL_IPI_ITEM = Column(DECIMAL(15, 2))
    CST_PIS = Column(VARCHAR(2))
    VL_BC_PIS = Column(DECIMAL(15, 2))
    ALIQ_PIS = Column(DECIMAL(8, 2))
    QUANT_BC_PIS = Column(DECIMAL(15, 2))
    ALIQ_PIS_QUANT = Column(DECIMAL(8, 2))
    VL_PIS_ITEM = Column(DECIMAL(15, 2))
    CST_COFINS = Column(VARCHAR(2))
    VL_BC_COFINS = Column(DECIMAL(15, 2))
    ALIQ_COFINS = Column(DECIMAL(8, 2))
    QUANT_BC_COFINS = Column(DECIMAL(15, 2))
    ALIQ_COFINS_QUANT = Column(DECIMAL(8, 2))
    VL_COFINS_ITEM = Column(DECIMAL(15, 2))
    COD_CTA = Column(VARCHAR(60))
    CONCILIADO_PISCOFINS = Column(String(150))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class DwPisCofinsSaidas(Base):
    __tablename__ = 'dw_pis_cofins_saidas'

    ID_ITEM = Column(BIGINT(25), primary_key=True)
    PK = Column(VARCHAR(65))
    DATA_INI = Column(Date)
    CNPJ_FILIAL = Column(VARCHAR(14))
    REGISTRO = Column(VARCHAR(4), server_default=text("''"))
    IND_ESCRI = Column(VARCHAR(1))
    IND_OPER = Column(VARCHAR(1))
    IND_EMIT = Column(VARCHAR(1))
    COD_PART = Column(VARCHAR(60))
    D_PART_REG_0150 = Column(VARCHAR(140))
    RAZAO_PART = Column(String(140))
    CNPJ_PART = Column(String(14))
    UF_PART = Column(String(2))
    COD_MOD = Column(VARCHAR(2))
    COD_SIT = Column(VARCHAR(2))
    SER = Column(VARCHAR(3))
    NUM_DOC = Column(INTEGER(9))
    CHV_NFE = Column(VARCHAR(44))
    DT_DOC = Column(VARCHAR(100))
    DT_E_S = Column(VARCHAR(100))
    VL_DOC = Column(DECIMAL(15, 2))
    IND_PGTO = Column(VARCHAR(1))
    VL_DESC = Column(DECIMAL(15, 2))
    VL_ABAT_NT = Column(DECIMAL(15, 2))
    VL_MERC = Column(DECIMAL(15, 2))
    IND_FRT = Column(VARCHAR(1))
    VL_FRT = Column(DECIMAL(15, 2))
    VL_SEG = Column(DECIMAL(15, 2))
    VL_OUT_DA = Column(DECIMAL(15, 2))
    VL_BC_ICMS = Column(DECIMAL(15, 2))
    VL_ICMS = Column(DECIMAL(15, 2))
    VL_BC_ICMS_ST = Column(DECIMAL(15, 2))
    VL_ICMS_ST = Column(DECIMAL(15, 2))
    VL_IPI = Column(DECIMAL(15, 2))
    VL_PIS = Column(DECIMAL(15, 2))
    VL_COFINS = Column(DECIMAL(15, 2))
    VL_PIS_ST = Column(DECIMAL(15, 2))
    VL_COFINS_ST = Column(DECIMAL(15, 2))
    NUM_ITEM = Column(INTEGER(3))
    COD_ITEM = Column(VARCHAR(60))
    DESCR_COMPL = Column(VARCHAR(255))
    D_ITEM_REG_0200 = Column(VARCHAR(273))
    COD_NCM_REG_0200 = Column(String(10))
    TIPO_ITEM_REG_0200 = Column(String(3))
    QTD = Column(VARCHAR(12))
    UNID = Column(VARCHAR(6))
    VL_ITEM = Column(DECIMAL(15, 2))
    VL_DESC_ITEM = Column(DECIMAL(15, 2))
    IND_MOV = Column(VARCHAR(1))
    CST_ICMS = Column(VARCHAR(3))
    CFOP = Column(VARCHAR(4))
    COD_NAT = Column(VARCHAR(10))
    VL_BC_ICMS_ITEM = Column(DECIMAL(15, 2))
    ALIQ_ICMS = Column(DECIMAL(8, 2))
    VL_ICMS_ITEM = Column(DECIMAL(15, 2))
    VL_BC_ICMS_ST_ITEM = Column(DECIMAL(15, 2))
    ALIQ_ST = Column(DECIMAL(8, 2))
    VL_ICMS_ST_ITEM = Column(DECIMAL(15, 2))
    IND_APUR = Column(VARCHAR(1))
    CST_IPI = Column(VARCHAR(2))
    COD_ENQ = Column(VARCHAR(3))
    VL_BC_IPI = Column(DECIMAL(15, 2))
    ALIQ_IPI = Column(DECIMAL(15, 2))
    VL_IPI_ITEM = Column(DECIMAL(15, 2))
    CST_PIS = Column(VARCHAR(2))
    VL_BC_PIS = Column(DECIMAL(15, 2))
    ALIQ_PIS = Column(DECIMAL(8, 2))
    QUANT_BC_PIS = Column(DECIMAL(15, 2))
    ALIQ_PIS_QUANT = Column(DECIMAL(8, 2))
    VL_PIS_ITEM = Column(DECIMAL(15, 2))
    CST_COFINS = Column(VARCHAR(2))
    VL_BC_COFINS = Column(DECIMAL(15, 2))
    ALIQ_COFINS = Column(DECIMAL(8, 2))
    QUANT_BC_COFINS = Column(DECIMAL(15, 2))
    ALIQ_COFINS_QUANT = Column(DECIMAL(8, 2))
    VL_COFINS_ITEM = Column(DECIMAL(15, 2))
    COD_CTA = Column(VARCHAR(60))
    CONCILIADO_PISCOFINS = Column(String(150))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class DwRazaoContabil04(Base):
    __tablename__ = 'dw_razao_contabil_04'

    ID_RAZAO_04 = Column(INTEGER(15), primary_key=True)
    DATA_LCTO_CONT = Column(Date)
    IND_LCTO = Column(VARCHAR(12), nullable=False, server_default=text("''"))
    COD_CONTA_CONT = Column(VARCHAR(255))
    DESCRICAO_CTA_CONT = Column(VARCHAR(255))
    COD_CENTRO_CUSTO = Column(VARCHAR(255))
    DESCRICAO_CENTRO_CUSTO = Column(VARCHAR(255))
    VALOR_PARTIDA = Column(DECIMAL(15, 2), index=True)
    NATUREZA_PARTIDA = Column(VARCHAR(1), index=True)
    NUMERO_LOC_LANCAMENTOS = Column(VARCHAR(255))
    COD_HIST_PADRAO = Column(VARCHAR(255))
    DESCR_HISTORICO_PADRAO = Column(VARCHAR(255))
    HISTORIO_PARTIDA = Column(LONGTEXT)
    COD_PARTICIPANTE = Column(VARCHAR(255))
    COD_CTA = Column(VARCHAR(255), index=True)
    COD_NAT = Column(VARCHAR(2))
    ACHEI_NO_DEB = Column(INTEGER(1))
    ACHEI_NO_CRED = Column(INTEGER(1))
    ID_SPEDCONT_CTRL_REG_0000 = Column(INTEGER(11), index=True)


class EfdCtrlEnvio(Base):
    __tablename__ = 'efd_ctrl_envio'

    ID = Column(INTEGER(11), primary_key=True)
    DATA_INI = Column(Date)
    DATA_FIM = Column(Date)
    CNPJ = Column(CHAR(14))
    DATA_HORA = Column(DateTime)
    ID_REG_0000 = Column(INTEGER(11), index=True)
    TIPO_SPED = Column(String(20))
    RETIFICADOR = Column(INTEGER(1))
    RAZAO_SOCIAL = Column(String(255))
    CANCELADO = Column(String(10))
    UF = Column(CHAR(2))
    CONCILIADO_PISCOFINS = Column(String(10))
    VALIDACAO_ENVIO = Column(String(20))
    ANALISE = Column(String(20))
    ANALISE_EFD_TOMADOS = Column(String(20))


class EfdTotalBaseEntradaSaida(Base):
    __tablename__ = 'efd_total_base_entrada_saida'

    ID = Column(INTEGER(11), primary_key=True)
    CHV_PRIMARIA = Column(VARCHAR(60), index=True)
    DATA_INI = Column(Date, index=True)
    REGISTRO = Column(VARCHAR(4), nullable=False, index=True, server_default=text("''"))
    DADOS_FILIAL = Column(String(14), index=True)
    COD_PART_CNPJ_PART = Column(String(60), index=True)
    DADOS_PART = Column(String(125))
    IND_OPER = Column(String(1), index=True)
    CHV_NFE = Column(String(44), index=True)
    VL_DOC = Column(DECIMAL(30, 2))
    VL_ITEM = Column(DECIMAL(30, 2), index=True)
    DESCR_COMPL = Column(String(255))
    DADOS_PRODUTO = Column(String(265))
    COD_ITEM = Column(String(60), index=True)
    CFOP = Column(String(4), index=True)
    INF_CFOP = Column(String(267))
    VL_BC_PIS = Column(String(255))
    ALIQ_PIS = Column(String(255))
    VL_PIS = Column(String(255))
    COD_CTA = Column(String(60))
    CST_PIS = Column(String(50))
    ID_EFD_CTRL_REG_0000 = Column(String(255), index=True)
    CONSTA_NO_SPED = Column(String(100))
    DT_DOC = Column(String(80))
    NUM_DOC = Column(String(200), index=True)
    DT_E_S = Column(String(80))
    CPF_CNPJ_PART = Column(String(80), index=True)
    VL_BC_COFINS = Column(String(80))
    ALIQ_COFINS = Column(String(80))
    VL_COFINS = Column(String(80))


class Registers(Base):
    __tablename__ = 'registers'

    id = Column(BIGINT(20), primary_key=True)
    products = Column(String(20), nullable=False)
    created_at = Column(Date, nullable=False, index=True)
    expire_at = Column(Date, nullable=False, index=True)


class SpedContabil0000(Base):
    __tablename__ = 'sped_contabil_0000'

    ID_REG_0000 = Column(INTEGER(30), primary_key=True)
    ID_LOTES_ARQUIVOS = Column(INTEGER(30), nullable=False, index=True)
    LINHA = Column(INTEGER(30), nullable=False)
    REG = Column(String(4))
    LECD = Column(String(4))
    DT_INI = Column(String(20))
    DT_FIN = Column(String(20))
    NOME = Column(String(255))
    CNPJ = Column(String(14))
    UF = Column(String(2))
    IE = Column(String(255))
    COD_MUN = Column(String(7))
    IM = Column(String(255))
    IND_SIT_ESP = Column(String(1))
    IND_SIT_INI_PER = Column(String(1))
    IND_NIRE = Column(String(1))
    IND_FIN_ESC = Column(String(1))
    COD_HASH_SUB = Column(String(40))
    NIRE_SUBST = Column(String(11))
    IND_GRANDE_PORTE = Column(String(1))
    TIP_ECD = Column(String(1))
    COD_SCP = Column(String(14))
    IDENT_MF = Column(String(1))
    IND_ESC_CONS = Column(String(10))


class SpedContabil0001(Base):
    __tablename__ = 'sped_contabil_0001'

    ID_REG_0001 = Column(BIGINT(25), primary_key=True)
    ID_REG_0000 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(30), nullable=False)
    REG = Column(String(4))
    IND_DAD = Column(String(1))
    ID_SPEDCONT_CTRL_REG_0000 = Column(INTEGER(11))


class SpedContabil0007(Base):
    __tablename__ = 'sped_contabil_0007'

    ID_REG_0007 = Column(BIGINT(25), primary_key=True)
    ID_REG_0001 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(30), nullable=False)
    REG = Column(String(4))
    COD_ENT_REF = Column(String(255))
    COD_INSCR = Column(String(255))
    ID_SPEDCONT_CTRL_REG_0000 = Column(INTEGER(11))


class SpedContabil0020(Base):
    __tablename__ = 'sped_contabil_0020'

    ID_REG_0020 = Column(BIGINT(25), primary_key=True)
    ID_REG_0001 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(30), nullable=False)
    REG = Column(String(4))
    IND_DEC = Column(String(1))
    CNPJ = Column(String(14))
    UF = Column(String(2))
    IE = Column(String(255))
    COD_MUN = Column(String(7))
    IM = Column(String(255))
    NIRE = Column(String(11))
    ID_SPEDCONT_CTRL_REG_0000 = Column(INTEGER(11))


class SpedContabil0035(Base):
    __tablename__ = 'sped_contabil_0035'

    ID_REG_0035 = Column(BIGINT(25), primary_key=True)
    ID_REG_0001 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(30), nullable=False)
    REG = Column(String(4))
    COD_SCP = Column(String(14))
    NOME_SCP = Column(String(255))
    ID_SPEDCONT_CTRL_REG_0000 = Column(INTEGER(11))


class SpedContabil0150(Base):
    __tablename__ = 'sped_contabil_0150'

    ID_REG_0150 = Column(BIGINT(25), primary_key=True)
    ID_REG_0001 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(30), nullable=False)
    REG = Column(String(4))
    COD_PART = Column(String(255))
    NOME = Column(String(255))
    COD_PAIS = Column(String(5))
    CNPJ = Column(String(14))
    CPF = Column(String(11))
    NIT = Column(String(11))
    UF = Column(String(2))
    IE = Column(String(255))
    IE_ST = Column(String(255))
    COD_MUN = Column(String(7))
    IM = Column(String(255))
    SUFRAMA = Column(String(9))
    ID_SPEDCONT_CTRL_REG_0000 = Column(INTEGER(11))


class SpedContabil0180(Base):
    __tablename__ = 'sped_contabil_0180'

    ID_REG_0180 = Column(BIGINT(25), primary_key=True)
    ID_REG_0001 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(30), nullable=False)
    REG = Column(String(4))
    COD_REL = Column(String(2))
    DT_INI_REL = Column(String(20))
    DT_FIN_REL = Column(String(20))
    ID_SPEDCONT_CTRL_REG_0000 = Column(INTEGER(11))


class SpedContabil0990(Base):
    __tablename__ = 'sped_contabil_0990'

    ID_REG_0990 = Column(BIGINT(25), primary_key=True)
    ID_REG_0000 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(30), nullable=False)
    REG = Column(String(4))
    QTD_LIN_0 = Column(String(255))
    ID_SPEDCONT_CTRL_REG_0000 = Column(INTEGER(11))


class SpedContabil9001(Base):
    __tablename__ = 'sped_contabil_9001'

    ID_REG_9001 = Column(BIGINT(25), primary_key=True)
    ID_REG_0000 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(30), nullable=False)
    REG = Column(String(4))
    IND_DAD = Column(String(1))
    ID_SPEDCONT_CTRL_REG_0000 = Column(INTEGER(11))


class SpedContabil9900(Base):
    __tablename__ = 'sped_contabil_9900'

    ID_REG_9900 = Column(BIGINT(25), primary_key=True)
    ID_REG_9001 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(30), nullable=False)
    REG = Column(String(4))
    REG_BLC = Column(String(4))
    QTD_REG_BLC = Column(String(255))
    ID_SPEDCONT_CTRL_REG_0000 = Column(INTEGER(11))


class SpedContabil9990(Base):
    __tablename__ = 'sped_contabil_9990'

    ID_REG_9990 = Column(BIGINT(25), primary_key=True)
    ID_REG_0000 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(30), nullable=False)
    REG = Column(String(4))
    QTD_LIN_9 = Column(String(255))
    ID_SPEDCONT_CTRL_REG_0000 = Column(INTEGER(11))


class SpedContabil9999(Base):
    __tablename__ = 'sped_contabil_9999'

    ID_REG_9999 = Column(BIGINT(25), primary_key=True)
    ID_LOTES_ARQUIVOS = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(30), nullable=False)
    REG = Column(String(4))
    QTD_LIN = Column(String(255))
    ID_SPEDCONT_CTRL_REG_0000 = Column(INTEGER(11))


class SpedContabilI001(Base):
    __tablename__ = 'sped_contabil_I001'

    ID_REG_I001 = Column(BIGINT(25), primary_key=True)
    ID_REG_0000 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(30), nullable=False)
    REG = Column(String(4))
    IND_DAD = Column(String(1))
    ID_SPEDCONT_CTRL_REG_0000 = Column(INTEGER(11))


class SpedContabilI010(Base):
    __tablename__ = 'sped_contabil_I010'

    ID_REG_I010 = Column(BIGINT(25), primary_key=True)
    ID_REG_I001 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(30), nullable=False)
    REG = Column(String(4))
    IND_ESC = Column(String(1))
    COD_VER_LC = Column(String(255))
    ID_SPEDCONT_CTRL_REG_0000 = Column(INTEGER(11))


class SpedContabilI012(Base):
    __tablename__ = 'sped_contabil_I012'

    ID_REG_I012 = Column(BIGINT(25), primary_key=True)
    ID_REG_I010 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(30), nullable=False)
    REG = Column(String(4))
    NUM_ORD = Column(String(255))
    NAT_LIVRO = Column(String(80))
    TIPO = Column(String(1))
    COD_HASH_AUX = Column(String(40))
    ID_SPEDCONT_CTRL_REG_0000 = Column(INTEGER(11))


class SpedContabilI015(Base):
    __tablename__ = 'sped_contabil_I015'

    ID_REG_I015 = Column(BIGINT(25), primary_key=True)
    ID_REG_I012 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(30), nullable=False)
    REG = Column(String(4))
    COD_CTA_RES = Column(String(255))
    ID_SPEDCONT_CTRL_REG_0000 = Column(INTEGER(11))


class SpedContabilI020(Base):
    __tablename__ = 'sped_contabil_I020'

    ID_REG_I020 = Column(BIGINT(25), primary_key=True)
    ID_REG_I010 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(30), nullable=False)
    REG = Column(String(4))
    REG_COD = Column(String(4))
    NUM_AD = Column(String(255))
    CAMPO = Column(String(255))
    DESCRICAO = Column(String(255))
    TIPO = Column(String(255))
    ID_SPEDCONT_CTRL_REG_0000 = Column(INTEGER(11))


class SpedContabilI030(Base):
    __tablename__ = 'sped_contabil_I030'

    ID_REG_I030 = Column(BIGINT(25), primary_key=True)
    ID_REG_I010 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(30), nullable=False)
    REG = Column(String(4))
    DNRC_ABERT = Column(String(17))
    NUM_ORD = Column(String(18))
    NAT_LIVR = Column(String(80))
    QTD_LIN = Column(String(255))
    NOME = Column(String(255))
    NIRE = Column(String(11))
    CNPJ = Column(String(14))
    DT_ARQ = Column(String(20))
    DT_ARQ_CONV = Column(String(20))
    DESC_MUN = Column(String(255))
    DT_EX_SOCIAL = Column(String(20))
    ID_SPEDCONT_CTRL_REG_0000 = Column(INTEGER(11))


class SpedContabilI050(Base):
    __tablename__ = 'sped_contabil_I050'

    ID_REG_I050 = Column(BIGINT(25), primary_key=True)
    ID_REG_I010 = Column(BIGINT(25), nullable=False)
    LINHA = Column(INTEGER(30), nullable=False)
    REG = Column(String(4))
    DT_ALT = Column(String(20))
    COD_NAT = Column(String(2))
    IND_CTA = Column(String(1))
    NIVEL = Column(String(255))
    COD_CTA = Column(String(255), index=True)
    COD_CTA_SUP = Column(String(255))
    CTA = Column(String(255))
    ID_SPEDCONT_CTRL_REG_0000 = Column(INTEGER(11), index=True)


class SpedContabilI051(Base):
    __tablename__ = 'sped_contabil_I051'

    ID_REG_I051 = Column(BIGINT(25), primary_key=True)
    ID_REG_I050 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(30), nullable=False)
    REG = Column(String(4))
    COD_CCUS = Column(String(255))
    COD_CTA_REF = Column(String(255))
    ID_SPEDCONT_CTRL_REG_0000 = Column(INTEGER(11))


class SpedContabilI052(Base):
    __tablename__ = 'sped_contabil_I052'

    ID_REG_I052 = Column(BIGINT(25), primary_key=True)
    ID_REG_I050 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(30), nullable=False)
    REG = Column(String(4))
    COD_CCUS = Column(String(255))
    COD_AGL = Column(String(255))
    ID_SPEDCONT_CTRL_REG_0000 = Column(INTEGER(11))


class SpedContabilI053(Base):
    __tablename__ = 'sped_contabil_I053'

    ID_REG_I053 = Column(BIGINT(25), primary_key=True)
    ID_REG_I050 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(30), nullable=False)
    REG = Column(String(4))
    COD_ID_SPEDCONT_REG_T = Column(String(6))
    COD_CNT_CORR = Column(String(255))
    NAT_SUB_CNT = Column(String(2))
    ID_SPEDCONT_CTRL_REG_0000 = Column(INTEGER(11))


class SpedContabilI075(Base):
    __tablename__ = 'sped_contabil_I075'

    ID_REG_I075 = Column(BIGINT(25), primary_key=True)
    ID_REG_I010 = Column(BIGINT(25), nullable=False)
    LINHA = Column(INTEGER(30), nullable=False)
    REG = Column(String(4))
    COD_HIST = Column(String(255), index=True)
    DESCR_HIST = Column(String(255))
    ID_SPEDCONT_CTRL_REG_0000 = Column(INTEGER(11))


class SpedContabilI100(Base):
    __tablename__ = 'sped_contabil_I100'

    ID_REG_I100 = Column(BIGINT(25), primary_key=True)
    ID_REG_I010 = Column(BIGINT(25), nullable=False)
    LINHA = Column(INTEGER(30), nullable=False)
    REG = Column(String(4))
    DT_ALT = Column(String(20))
    COD_CCUS = Column(String(255), index=True)
    CCUS = Column(String(255))
    ID_SPEDCONT_CTRL_REG_0000 = Column(INTEGER(11))


class SpedContabilI150(Base):
    __tablename__ = 'sped_contabil_I150'

    ID_REG_I150 = Column(BIGINT(25), primary_key=True)
    ID_REG_I010 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(30), nullable=False)
    REG = Column(String(4))
    DT_INI = Column(String(20))
    DT_FIN = Column(String(20))
    ID_SPEDCONT_CTRL_REG_0000 = Column(INTEGER(11))


class SpedContabilI151(Base):
    __tablename__ = 'sped_contabil_I151'

    ID_REG_I151 = Column(BIGINT(25), primary_key=True)
    ID_REG_I150 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(30), nullable=False)
    REG = Column(String(4))
    ASSIN_DIG = Column(String(255))
    ID_SPEDCONT_CTRL_REG_0000 = Column(INTEGER(11))


class SpedContabilI155(Base):
    __tablename__ = 'sped_contabil_I155'

    ID_REG_I155 = Column(BIGINT(25), primary_key=True)
    ID_REG_I150 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(30), nullable=False)
    REG = Column(String(4))
    COD_CTA = Column(String(255))
    COD_CCUS = Column(String(255))
    VL_SLD_INI = Column(String(30))
    IND_DC_INI = Column(String(1))
    VL_DEB = Column(String(30))
    VL_CRED = Column(String(30))
    VL_SLD_FIN = Column(String(30))
    IND_DC_FIN = Column(String(1))
    ID_SPEDCONT_CTRL_REG_0000 = Column(INTEGER(11))


class SpedContabilI157(Base):
    __tablename__ = 'sped_contabil_I157'

    ID_REG_I157 = Column(BIGINT(25), primary_key=True)
    ID_REG_I155 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(30), nullable=False)
    REG = Column(String(4))
    COD_CTA = Column(String(255))
    COD_CCUS = Column(String(255))
    VL_SLD_INI = Column(String(30))
    IND_DC_INI = Column(String(1))
    ID_SPEDCONT_CTRL_REG_0000 = Column(INTEGER(11))


class SpedContabilI200(Base):
    __tablename__ = 'sped_contabil_I200'

    ID_REG_I200 = Column(BIGINT(25), primary_key=True)
    ID_REG_I010 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(30), nullable=False)
    REG = Column(String(4))
    NUM_LCTO = Column(String(255))
    DT_LCTO = Column(String(20))
    VL_LCTO = Column(String(30))
    IND_LCTO = Column(String(1))
    VL_LCTO_MF = Column(String(30))
    ID_SPEDCONT_CTRL_REG_0000 = Column(INTEGER(11))


class SpedContabilI250(Base):
    __tablename__ = 'sped_contabil_I250'

    ID_REG_I250 = Column(BIGINT(25), primary_key=True)
    ID_REG_I200 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(30), nullable=False)
    REG = Column(String(4))
    COD_CTA = Column(String(255), index=True)
    COD_CCUS = Column(String(255))
    VL_DC = Column(String(30))
    IND_DC = Column(String(1))
    NUM_ARQ = Column(String(255))
    COD_HIST_PAD = Column(String(255))
    HIST = Column(LONGTEXT)
    COD_PART = Column(String(255))
    ID_SPEDCONT_CTRL_REG_0000 = Column(INTEGER(11), index=True)


class SpedContabilI300(Base):
    __tablename__ = 'sped_contabil_I300'

    ID_REG_I300 = Column(BIGINT(25), primary_key=True)
    ID_REG_I010 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(30), nullable=False)
    REG = Column(String(4))
    DT_BCTE = Column(String(20))
    ID_SPEDCONT_CTRL_REG_0000 = Column(INTEGER(11))


class SpedContabilI310(Base):
    __tablename__ = 'sped_contabil_I310'

    ID_REG_I310 = Column(BIGINT(25), primary_key=True)
    ID_REG_I300 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(30), nullable=False)
    REG = Column(String(4))
    COD_CTA = Column(String(255))
    COD_CCUS = Column(String(255))
    VAL_DEBD = Column(String(30))
    VAL_CREDD = Column(String(30))
    ID_SPEDCONT_CTRL_REG_0000 = Column(INTEGER(11))


class SpedContabilI350(Base):
    __tablename__ = 'sped_contabil_I350'

    ID_REG_I350 = Column(BIGINT(25), primary_key=True)
    ID_REG_I010 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(30), nullable=False)
    REG = Column(String(4))
    DT_RES = Column(String(20))
    ID_SPEDCONT_CTRL_REG_0000 = Column(INTEGER(11))


class SpedContabilI355(Base):
    __tablename__ = 'sped_contabil_I355'

    ID_REG_I355 = Column(BIGINT(25), primary_key=True)
    ID_REG_I350 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(30), nullable=False)
    REG = Column(String(4))
    COD_CTA = Column(String(255))
    COD_CCUS = Column(String(255))
    VL_CTA = Column(String(30))
    IND_DC = Column(String(1))
    ID_SPEDCONT_CTRL_REG_0000 = Column(INTEGER(11))


class SpedContabilI500(Base):
    __tablename__ = 'sped_contabil_I500'

    ID_REG_I500 = Column(BIGINT(25), primary_key=True)
    ID_REG_I010 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(30), nullable=False)
    REG = Column(String(4))
    TAM_FONTE = Column(String(2))
    ID_SPEDCONT_CTRL_REG_0000 = Column(INTEGER(11))


class SpedContabilI510(Base):
    __tablename__ = 'sped_contabil_I510'

    ID_REG_I510 = Column(BIGINT(25), primary_key=True)
    ID_REG_I010 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(30), nullable=False)
    REG = Column(String(4))
    NM_CAMPO = Column(String(16))
    DESC_CAMPO = Column(String(50))
    TIPO_CAMPO = Column(String(1))
    TAM_CAMPO = Column(String(3))
    DEC_CAMPO = Column(String(2))
    COL_CAMPO = Column(String(3))
    ID_SPEDCONT_CTRL_REG_0000 = Column(INTEGER(11))


class SpedContabilI550(Base):
    __tablename__ = 'sped_contabil_I550'

    ID_REG_I550 = Column(BIGINT(25), primary_key=True)
    ID_REG_I010 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(30), nullable=False)
    REG = Column(String(4))
    ID_SPEDCONT_CTRL_REG_0000 = Column(INTEGER(11))


class SpedContabilI555(Base):
    __tablename__ = 'sped_contabil_I555'

    ID_REG_I555 = Column(BIGINT(25), primary_key=True)
    ID_REG_I550 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(30), nullable=False)
    REG = Column(String(4))
    ID_SPEDCONT_CTRL_REG_0000 = Column(INTEGER(11))


class SpedContabilI990(Base):
    __tablename__ = 'sped_contabil_I990'

    ID_REG_I990 = Column(BIGINT(25), primary_key=True)
    ID_REG_0000 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(30), nullable=False)
    REG = Column(String(4))
    QTD_LIN_I = Column(String(255))
    ID_SPEDCONT_CTRL_REG_0000 = Column(INTEGER(11))


class SpedContabilJ001(Base):
    __tablename__ = 'sped_contabil_J001'

    ID_REG_J001 = Column(BIGINT(25), primary_key=True)
    ID_REG_0000 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(30), nullable=False)
    REG = Column(String(4))
    IND_DAD = Column(String(1))
    ID_SPEDCONT_CTRL_REG_0000 = Column(INTEGER(11))


class SpedContabilJ005(Base):
    __tablename__ = 'sped_contabil_J005'

    ID_REG_J005 = Column(BIGINT(25), primary_key=True)
    ID_REG_J001 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(30), nullable=False)
    REG = Column(String(4))
    DT_INI = Column(String(20))
    DT_FIN = Column(String(20))
    ID_REG__DEM = Column(String(1))
    CAB_DEM = Column(String(255))
    ID_SPEDCONT_CTRL_REG_0000 = Column(INTEGER(11))


class SpedContabilJ100(Base):
    __tablename__ = 'sped_contabil_J100'

    ID_REG_J100 = Column(BIGINT(25), primary_key=True)
    ID_REG_J005 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(30), nullable=False)
    REG = Column(String(4))
    COD_AGL = Column(String(255))
    NIVEL_AGL = Column(String(255))
    IND_GRP_BAL = Column(String(10))
    DESCR_COD_AGL = Column(String(255))
    VL_CTA = Column(String(30))
    IND_DC_BAL = Column(String(10))
    VL_CTA_INI = Column(String(30))
    IND_DC_BAL_INI = Column(String(10))
    ID_SPEDCONT_CTRL_REG_0000 = Column(INTEGER(11))


class SpedContabilJ150(Base):
    __tablename__ = 'sped_contabil_J150'

    ID_REG_J150 = Column(BIGINT(25), primary_key=True)
    ID_REG_J005 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(30), nullable=False)
    REG = Column(String(4))
    COD_AGL = Column(String(255))
    NIVEL_AGL = Column(String(255))
    DESCR_COD_AGL = Column(String(255))
    VL_CTA = Column(String(30))
    IND_VL = Column(String(10))
    VL_CTA_ULT_DRE = Column(String(30))
    IND_VL_ULT_DRE = Column(String(10))
    ID_SPEDCONT_CTRL_REG_0000 = Column(INTEGER(11))


class SpedContabilJ200(Base):
    __tablename__ = 'sped_contabil_J200'

    ID_REG_J200 = Column(BIGINT(25), primary_key=True)
    ID_REG_J005 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(30), nullable=False)
    REG = Column(String(4))
    COD_HIST_FAT = Column(String(255))
    DESC_FAT = Column(String(255))
    ID_SPEDCONT_CTRL_REG_0000 = Column(INTEGER(11))


class SpedContabilJ210(Base):
    __tablename__ = 'sped_contabil_J210'

    ID_REG_J210 = Column(BIGINT(25), primary_key=True)
    ID_REG_J005 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(30), nullable=False)
    REG = Column(String(4))
    IND_TIP = Column(String(1))
    COD_AGL = Column(String(255))
    DESCR_COD_AGL = Column(String(255))
    VL_CTA = Column(String(30))
    IND_DC_CTA = Column(String(1))
    VL_CTA_INI = Column(String(30))
    IND_DC_CTA_INI = Column(String(1))
    ID_SPEDCONT_CTRL_REG_0000 = Column(INTEGER(11))


class SpedContabilJ215(Base):
    __tablename__ = 'sped_contabil_J215'

    ID_REG_J215 = Column(BIGINT(25), primary_key=True)
    ID_REG_J210 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(30), nullable=False)
    REG = Column(String(4))
    COD_HIST_FAT = Column(String(255))
    VL_FAT_CONT = Column(String(30))
    IND_DC_FAT = Column(String(1))
    ID_SPEDCONT_CTRL_REG_0000 = Column(INTEGER(11))


class SpedContabilJ800(Base):
    __tablename__ = 'sped_contabil_J800'

    ID_REG_J800 = Column(BIGINT(25), primary_key=True)
    ID_REG_J005 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(30), nullable=False)
    REG = Column(String(4))
    ARQ_RTF = Column(String(255))
    IND_FIN_RTF = Column(String(255))
    ID_SPEDCONT_CTRL_REG_0000 = Column(INTEGER(11))


class SpedContabilJ900(Base):
    __tablename__ = 'sped_contabil_J900'

    ID_REG_J900 = Column(BIGINT(25), primary_key=True)
    ID_REG_J001 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(30), nullable=False)
    REG = Column(String(4))
    DNRC_ENCER = Column(String(21))
    NUM_ORD = Column(String(255))
    NAT_LIVRO = Column(String(80))
    NOME = Column(String(255))
    QTD_LIN = Column(String(255))
    DT_INI_ESCR = Column(String(20))
    DT_FIN_ESCR = Column(String(20))
    ID_SPEDCONT_CTRL_REG_0000 = Column(INTEGER(11))


class SpedContabilJ930(Base):
    __tablename__ = 'sped_contabil_J930'

    ID_REG_J930 = Column(BIGINT(25), primary_key=True)
    ID_REG_J900 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(30), nullable=False)
    REG = Column(String(4))
    IDENT_NOM = Column(String(255))
    IDENT_CPF = Column(String(15))
    IDENT_QUALIF = Column(String(255))
    COD_ASSIN = Column(String(3))
    IND_CRC = Column(String(255))
    EMAIL = Column(String(60))
    FONE = Column(String(14))
    UF_CRC = Column(String(2))
    NUM_SEQ_CRC = Column(String(255))
    DT_CRC = Column(String(20))
    IND_RESP_LEGAL = Column(String(10))
    ID_SPEDCONT_CTRL_REG_0000 = Column(INTEGER(11))


class SpedContabilJ935(Base):
    __tablename__ = 'sped_contabil_J935'

    ID_REG_J935 = Column(BIGINT(25), primary_key=True)
    ID_REG_J900 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(30), nullable=False)
    REG = Column(String(4))
    NOME_AUDITOR = Column(String(255))
    COD_CVM_AUDITOR = Column(String(255))
    ID_SPEDCONT_CTRL_REG_0000 = Column(INTEGER(11))


class SpedContabilJ990(Base):
    __tablename__ = 'sped_contabil_J990'

    ID_REG_J990 = Column(BIGINT(25), primary_key=True)
    ID_REG_0000 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(30), nullable=False)
    REG = Column(String(4))
    QTD_LIN_J = Column(String(255))
    ID_SPEDCONT_CTRL_REG_0000 = Column(INTEGER(11))


class SpedContabilCtrl(Base):
    __tablename__ = 'sped_contabil_ctrl'
    __table_args__ = (
        Index('IDX_CANCELAMENTO', 'DATA_INI', 'DATA_FIM', 'CNPJ'),
    )

    ID = Column(INTEGER(11), primary_key=True)
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11), index=True)
    DATA_INI = Column(Date)
    DATA_FIM = Column(Date)
    CNPJ = Column(CHAR(14))
    DATA_HORA = Column(DateTime)
    TIPO = Column(String(20))
    ENVIO = Column(INTEGER(1))
    CANCELADO = Column(INTEGER(1))
    RAZAO_SOCIAL = Column(String(255))
    RETIFICADOR = Column(INTEGER(1))
    NOME_ARQUIVO = Column(String(255))
    DW_BALANCETE_GERAL = Column(INTEGER(1))
    DW_RAZAO_04 = Column(INTEGER(1))
    SPR_ZERAMENTO_RAZAO_04 = Column(INTEGER(1))


class SpedIcmsIpi0000(Base):
    __tablename__ = 'sped_icms_ipi_0000'

    ID_REG_0000 = Column(INTEGER(11), primary_key=True)
    ID_LOTES_ARQUIVOS = Column(DECIMAL(15, 0), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    COD_VER = Column(String(10))
    COD_FIN = Column(String(1))
    DT_INI = Column(Date)
    DT_FIN = Column(Date)
    NOME = Column(String(100))
    CNPJ = Column(String(14))
    CPF = Column(String(11))
    UF = Column(String(2))
    IE = Column(String(14))
    COD_MUN = Column(String(7))
    IM = Column(String(255))
    SUFRAMA = Column(String(9))
    IND_PERFIL = Column(String(1))
    IND_ATIV = Column(String(1))


class SpedIcmsIpi0001(Base):
    __tablename__ = 'sped_icms_ipi_0001'

    ID_REG_0001 = Column(BIGINT(25), primary_key=True)
    ID_REG_0000 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    IND_MOV = Column(String(1))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpi0005(Base):
    __tablename__ = 'sped_icms_ipi_0005'

    ID_REG_0005 = Column(BIGINT(25), primary_key=True)
    ID_REG_0001 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    FANTASIA = Column(String(60))
    CEP = Column(String(8))
    ENDERECO = Column(String(60))
    NUM = Column(String(10))
    COMPL = Column(String(60))
    BAIRRO = Column(String(60))
    FONE = Column(String(11))
    FAX = Column(String(11))
    EMAIL = Column(String(60))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpi0015(Base):
    __tablename__ = 'sped_icms_ipi_0015'

    ID_REG_0015 = Column(BIGINT(25), primary_key=True)
    ID_REG_0001 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    UF_ST = Column(String(2))
    IE_ST = Column(String(14))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpi0100(Base):
    __tablename__ = 'sped_icms_ipi_0100'

    ID_REG_0100 = Column(BIGINT(25), primary_key=True)
    ID_REG_0001 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    NOME = Column(String(60))
    CPF = Column(String(11))
    CRC = Column(String(15))
    CNPJ = Column(String(14))
    CEP = Column(String(8))
    ENDERECO = Column(String(60))
    NUM = Column(String(10))
    COMPL = Column(String(60))
    BAIRRO = Column(String(60))
    FONE = Column(String(11))
    FAX = Column(String(11))
    EMAIL = Column(String(60))
    COD_MUN = Column(String(7))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpi0150(Base):
    __tablename__ = 'sped_icms_ipi_0150'
    __table_args__ = (
        Index('IDX_DUPLO', 'COD_PART', 'ID_SPEDFIS_CTRL_REG_0000'),
    )

    ID_REG_0150 = Column(BIGINT(25), primary_key=True)
    ID_REG_0001 = Column(BIGINT(25), nullable=False)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    COD_PART = Column(String(60))
    NOME = Column(String(255))
    COD_PAIS = Column(String(5))
    CNPJ = Column(String(14))
    CPF = Column(String(11))
    IE = Column(String(14))
    COD_MUN = Column(String(7))
    SUFRAMA = Column(String(9))
    ENDERECO = Column(String(255))
    NUM = Column(String(10))
    COMPL = Column(String(255))
    BAIRRO = Column(String(255))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpi0175(Base):
    __tablename__ = 'sped_icms_ipi_0175'

    ID_REG_0175 = Column(BIGINT(25), primary_key=True)
    ID_REG_0150 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    DT_ALT = Column(String(10))
    NR_CAMPO = Column(String(2))
    CONT_ANT = Column(String(100))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpi0190(Base):
    __tablename__ = 'sped_icms_ipi_0190'

    ID_REG_0190 = Column(BIGINT(25), primary_key=True)
    ID_REG_0001 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    UNID_ = Column(String(6))
    DESCR = Column(String(255))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpi0200(Base):
    __tablename__ = 'sped_icms_ipi_0200'
    __table_args__ = (
        Index('IDX_DUPLO', 'COD_ITEM', 'ID_SPEDFIS_CTRL_REG_0000'),
    )

    ID_REG_0200 = Column(BIGINT(25), primary_key=True)
    ID_REG_0001 = Column(BIGINT(25), nullable=False)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(255))
    COD_ITEM = Column(String(255))
    DESCR_ITEM = Column(String(255))
    COD_BARRA = Column(String(255))
    COD_ANT_ITEM = Column(String(255))
    UNID_INV = Column(String(255))
    TIPO_ITEM = Column(String(255))
    COD_NCM = Column(String(255))
    EX_IPI = Column(String(255))
    COD_GEN = Column(String(255))
    COD_LST = Column(String(255))
    ALIQ_ICMS = Column(String(255))
    CEST = Column(String(255))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpi0205(Base):
    __tablename__ = 'sped_icms_ipi_0205'

    ID_REG_0205 = Column(BIGINT(25), primary_key=True)
    ID_REG_0200 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    DESCR_ANT_ITEM = Column(String(255))
    DT_INI = Column(String(10))
    DT_FIM = Column(String(10))
    COD_ANT_ITEM = Column(String(60))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpi0206(Base):
    __tablename__ = 'sped_icms_ipi_0206'

    ID_REG_0206 = Column(BIGINT(25), primary_key=True)
    ID_REG_0200 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    COD_COMB = Column(String(255))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpi0210(Base):
    __tablename__ = 'sped_icms_ipi_0210'

    ID_REG_0210 = Column(BIGINT(25), primary_key=True)
    ID_REG_0200 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    COD_ITEM_COMP = Column(String(60))
    QTD_COMP = Column(String(30))
    PERDA = Column(String(10))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpi0220(Base):
    __tablename__ = 'sped_icms_ipi_0220'

    ID_REG_0220 = Column(BIGINT(25), primary_key=True)
    ID_REG_0200 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    UNID_CONV = Column(String(6))
    FAT_CONV = Column(String(30))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpi0300(Base):
    __tablename__ = 'sped_icms_ipi_0300'

    ID_REG_0300 = Column(BIGINT(25), primary_key=True)
    ID_REG_0001 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    COD_IND_BEM = Column(String(60))
    IDENT_MERC = Column(String(1))
    DESCR_ITEM = Column(String(255))
    COD_PRNC = Column(String(60))
    COD_CTA = Column(String(60))
    NR_PARC = Column(String(3))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpi0305(Base):
    __tablename__ = 'sped_icms_ipi_0305'

    ID_REG_0305 = Column(BIGINT(25), primary_key=True)
    ID_REG_0300 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    COD_CCUS = Column(String(60))
    FUNC = Column(String(255))
    VIDA_UTIL = Column(String(3))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpi0400(Base):
    __tablename__ = 'sped_icms_ipi_0400'

    ID_REG_0400 = Column(BIGINT(25), primary_key=True)
    ID_REG_0001 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    COD_NAT = Column(String(10))
    DESCR_NAT = Column(String(255))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpi0450(Base):
    __tablename__ = 'sped_icms_ipi_0450'

    ID_REG_0450 = Column(BIGINT(25), primary_key=True)
    ID_REG_0001 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    COD_INF = Column(String(6))
    TXT = Column(LONGTEXT)
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpi0460(Base):
    __tablename__ = 'sped_icms_ipi_0460'

    ID_REG_0460 = Column(BIGINT(25), primary_key=True)
    ID_REG_0001 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    COD_OBS = Column(String(6))
    TXT = Column(LONGTEXT)
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpi0500(Base):
    __tablename__ = 'sped_icms_ipi_0500'

    ID_REG_0500 = Column(BIGINT(25), primary_key=True)
    ID_REG_0001 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    DT_ALT = Column(String(10))
    COD_NAT_CC = Column(String(2))
    IND_CTA = Column(String(1))
    NIVEL = Column(String(5))
    COD_CTA = Column(String(60))
    NOME_CTA = Column(String(60))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpi0600(Base):
    __tablename__ = 'sped_icms_ipi_0600'

    ID_REG_0600 = Column(BIGINT(25), primary_key=True)
    ID_REG_0001 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    DT_ALT = Column(String(10))
    COD_CCUS = Column(String(60))
    CCUS = Column(String(60))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpi0990(Base):
    __tablename__ = 'sped_icms_ipi_0990'

    ID_REG_0990 = Column(BIGINT(25), primary_key=True)
    ID_REG_0000 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    QTD_LIN_0 = Column(String(255))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpi1001(Base):
    __tablename__ = 'sped_icms_ipi_1001'

    ID_REG_1001 = Column(BIGINT(25), primary_key=True)
    ID_REG_0000 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    IND_MOV = Column(String(1))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpi1010(Base):
    __tablename__ = 'sped_icms_ipi_1010'

    ID_REG_1010 = Column(BIGINT(25), primary_key=True)
    ID_REG_1001 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    IND_EXP = Column(String(1))
    IND_CCRF = Column(String(1))
    IND_COMB = Column(String(1))
    IND_USINA = Column(String(1))
    IND_VA = Column(String(1))
    IND_EE = Column(String(1))
    IND_CART = Column(String(1))
    IND_FORM = Column(String(1))
    IND_AER = Column(String(1))
    ND_GIAF1 = Column(String(1))
    ND_GIAF3 = Column(String(1))
    ND_GIAF4 = Column(String(1))
    IND_REST_RESSARC_COMPL_ICMS = Column(String(1))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpi1100(Base):
    __tablename__ = 'sped_icms_ipi_1100'

    ID_REG_1100 = Column(BIGINT(25), primary_key=True)
    ID_REG_1001 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    IND_DOC = Column(String(1))
    NRO_DE = Column(String(11))
    DT_DE = Column(String(10))
    NAT_EXP = Column(String(1))
    NRO_RE = Column(String(12))
    DT_RE = Column(String(10))
    CHC_EMB = Column(String(18))
    DT_CHC = Column(String(10))
    DT_AVB = Column(String(10))
    TP_CHC = Column(String(2))
    PAIS = Column(String(3))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpi1105(Base):
    __tablename__ = 'sped_icms_ipi_1105'

    ID_REG_1105 = Column(BIGINT(25), primary_key=True)
    ID_REG_1100 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    COD_MOD = Column(String(2))
    SER = Column(String(3))
    NUM_DOC = Column(String(9))
    CHV_NFE = Column(String(44))
    DT_DOC = Column(String(10))
    COD_ITEM = Column(String(60))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpi1110(Base):
    __tablename__ = 'sped_icms_ipi_1110'

    ID_REG_1110 = Column(BIGINT(25), primary_key=True)
    ID_REG_1105 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    COD_PART = Column(String(60))
    COD_MOD = Column(String(2))
    SER = Column(String(4))
    NUM_DOC = Column(String(9))
    DT_DOC = Column(String(10))
    CHV_NFE = Column(String(44))
    NR_MEMO = Column(String(255))
    QTD = Column(String(30))
    UNID_ = Column(String(6))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpi1200(Base):
    __tablename__ = 'sped_icms_ipi_1200'

    ID_REG_1200 = Column(BIGINT(25), primary_key=True)
    ID_REG_1001 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    COD_AJ_APUR = Column(String(8))
    SLD_CRED = Column(String(30))
    CRED_APR = Column(String(30))
    CRED_RECEB = Column(String(30))
    CRED_UTIL = Column(String(30))
    SLD_CRED_FIM = Column(String(30))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpi1210(Base):
    __tablename__ = 'sped_icms_ipi_1210'

    ID_REG_1210 = Column(BIGINT(25), primary_key=True)
    ID_REG_1200 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    TIPO_UTIL = Column(String(4))
    NR_DOC = Column(String(255))
    VL_CRED_UTIL = Column(String(30))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpi1300(Base):
    __tablename__ = 'sped_icms_ipi_1300'

    ID_REG_1300 = Column(BIGINT(25), primary_key=True)
    ID_REG_1001 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    COD_ITEM = Column(String(60))
    DT_FECH = Column(String(10))
    ESTQ_ABERT = Column(String(30))
    VOL_ENTR = Column(String(30))
    VOL_DISP = Column(String(30))
    VOL_SAIDAS = Column(String(30))
    ESTQ_ESCR = Column(String(30))
    VAL_AJ_PERDA = Column(String(30))
    VAL_AJ_GANHO = Column(String(30))
    FECH_FISICO = Column(String(30))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpi1310(Base):
    __tablename__ = 'sped_icms_ipi_1310'

    ID_REG_1310 = Column(BIGINT(25), primary_key=True)
    ID_REG_1300 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    NUM_TANQUE = Column(String(3))
    ESTQ_ABERT = Column(String(30))
    VOL_ENTR = Column(String(30))
    VOL_DISP = Column(String(30))
    VOL_SAIDAS = Column(String(30))
    ESTQ_ESCR = Column(String(30))
    VAL_AJ_PERDA = Column(String(30))
    VAL_AJ_GANHO = Column(String(30))
    FECH_FISICO = Column(String(30))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpi1320(Base):
    __tablename__ = 'sped_icms_ipi_1320'

    ID_REG_1320 = Column(BIGINT(25), primary_key=True)
    ID_REG_1310 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    NUM_BICO = Column(String(255))
    NR_INTERV = Column(String(255))
    MOT_INTERV = Column(String(50))
    NOM_INTERV = Column(String(30))
    CNPJ_INTERV = Column(String(14))
    CPF_INTERV = Column(String(11))
    VAL_FECHA = Column(String(30))
    VAL_ABERT = Column(String(30))
    VOL_AFERI = Column(String(30))
    VOL_VENDAS = Column(String(30))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpi1350(Base):
    __tablename__ = 'sped_icms_ipi_1350'

    ID_REG_1350 = Column(BIGINT(25), primary_key=True)
    ID_REG_1001 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    SERIE = Column(String(255))
    FABRICANTE = Column(String(60))
    MODELO = Column(String(255))
    TIPO_MEDICAO = Column(String(1))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpi1360(Base):
    __tablename__ = 'sped_icms_ipi_1360'

    ID_REG_1360 = Column(BIGINT(25), primary_key=True)
    ID_REG_1350 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    NUM_LACRE = Column(String(20))
    DAT_APLICACAO = Column(String(10))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpi1370(Base):
    __tablename__ = 'sped_icms_ipi_1370'

    ID_REG_1370 = Column(BIGINT(25), primary_key=True)
    ID_REG_1350 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    NUM_BICO = Column(String(3))
    COD_ITEM = Column(String(60))
    NUM_TANQUE = Column(String(3))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpi1390(Base):
    __tablename__ = 'sped_icms_ipi_1390'

    ID_REG_1390 = Column(BIGINT(25), primary_key=True)
    ID_REG_1001 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    COD_PROD = Column(String(2))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpi1391(Base):
    __tablename__ = 'sped_icms_ipi_1391'

    ID_REG_1391 = Column(BIGINT(25), primary_key=True)
    ID_REG_1390 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    DT_REGISTRO = Column(String(10))
    QTD_MOID_ = Column(String(30))
    ESTQ_INI = Column(String(30))
    QTD_PRODUZ = Column(String(30))
    ENT_ANID_HID_ = Column(String(30))
    OUTR_ENTR = Column(String(30))
    PERDA = Column(String(30))
    CONS = Column(String(30))
    SAI_ANI_HID_ = Column(String(30))
    SAIDAS = Column(String(30))
    ESTQ_FIN = Column(String(30))
    ESTQ_INI_MEL = Column(String(30))
    PROD_DIA_MEL = Column(String(30))
    UTIL_MEL = Column(String(30))
    PROD_ALC_MEL = Column(String(30))
    OBS = Column(String(255))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpi1400(Base):
    __tablename__ = 'sped_icms_ipi_1400'

    ID_REG_1400 = Column(BIGINT(25), primary_key=True)
    ID_REG_1001 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    COD_ITEM_IPM = Column(String(60))
    MUN = Column(String(7))
    VALOR = Column(String(30))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpi1500(Base):
    __tablename__ = 'sped_icms_ipi_1500'

    ID_REG_1500 = Column(BIGINT(25), primary_key=True)
    ID_REG_1001 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    IND_OPER = Column(String(1))
    IND_EMIT = Column(String(1))
    COD_PART = Column(String(60))
    COD_MOD = Column(String(2))
    COD_SIT = Column(String(2))
    SER = Column(String(4))
    SUB = Column(String(3))
    COD_CONS = Column(String(2))
    NUM_DOC = Column(String(9))
    DT_DOC = Column(String(10))
    DT_E_S = Column(String(10))
    VL_DOC = Column(String(30))
    VL_DESC = Column(String(30))
    VL_FORN = Column(String(30))
    VL_SERV_NT = Column(String(30))
    VL_TERC = Column(String(30))
    VL_DA = Column(String(30))
    VL_BC_ICMS = Column(String(30))
    VL_ICMS = Column(String(30))
    VL_BC_ICMS_ST = Column(String(30))
    VL_ICMS_ST = Column(String(30))
    COD_INF = Column(String(6))
    VL_PIS = Column(String(30))
    VL_COFIS = Column(String(30))
    TP_LIGACAO = Column(String(1))
    COD_GRUPO_TENSAO = Column(String(2))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpi1510(Base):
    __tablename__ = 'sped_icms_ipi_1510'

    ID_REG_1510 = Column(BIGINT(25), primary_key=True)
    ID_REG_1500 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    NUM_ITEM = Column(String(3))
    COD_ITEM = Column(String(60))
    COD_CLASS = Column(String(4))
    QTD = Column(String(30))
    UNID_ = Column(String(6))
    VL_ITEM = Column(String(30))
    VL_DESC = Column(String(30))
    CST_ICMS = Column(String(3))
    CFOP = Column(String(4))
    VL_BC_ICMS = Column(String(30))
    ALIQ_ICMS = Column(String(30))
    VL_ICMS = Column(String(30))
    VL_BC_ICMS_ST = Column(String(30))
    ALIQ_ST = Column(String(30))
    VL_ICMS_ST = Column(String(30))
    IND_REC = Column(String(1))
    COD_PART = Column(String(60))
    VL_PIS = Column(String(30))
    VL_COFIS = Column(String(30))
    COD_CTA = Column(String(255))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpi1600(Base):
    __tablename__ = 'sped_icms_ipi_1600'

    ID_REG_1600 = Column(BIGINT(25), primary_key=True)
    ID_REG_1001 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    COD_PART = Column(String(60))
    TOT_CREDITO = Column(String(30))
    TOT_DEBITO = Column(String(30))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpi1700(Base):
    __tablename__ = 'sped_icms_ipi_1700'

    ID_REG_1700 = Column(BIGINT(25), primary_key=True)
    ID_REG_1001 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    COD_DISP = Column(String(2))
    COD_MOD = Column(String(2))
    SER = Column(String(4))
    SUB = Column(String(3))
    NUM_DOC_INI = Column(String(12))
    NUM_DOC_FIN = Column(String(12))
    NUM_AUT = Column(String(60))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpi1710(Base):
    __tablename__ = 'sped_icms_ipi_1710'

    ID_REG_1710 = Column(BIGINT(25), primary_key=True)
    ID_REG_1700 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    NUM_DOC_INI = Column(String(12))
    NUM_DOC_FIN = Column(String(12))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpi1800(Base):
    __tablename__ = 'sped_icms_ipi_1800'

    ID_REG_1800 = Column(BIGINT(25), primary_key=True)
    ID_REG_1001 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    VL_CARGA = Column(String(30))
    VL_PASS = Column(String(30))
    VL_FAT = Column(String(30))
    IND_RAT = Column(String(30))
    VL_ICMS_ANT = Column(String(30))
    VL_BC_ICMS = Column(String(30))
    VL_ICMS_APUR = Column(String(30))
    VL_BC_ICMS_APUR = Column(String(30))
    VL_DIF = Column(String(30))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpi1900(Base):
    __tablename__ = 'sped_icms_ipi_1900'

    ID_REG_1900 = Column(BIGINT(25), primary_key=True)
    ID_REG_1001 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    IND_APUR_ICMS = Column(String(1))
    DESCR_COMPL_OUT_APUR = Column(String(255))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpi1910(Base):
    __tablename__ = 'sped_icms_ipi_1910'

    ID_REG_1910 = Column(BIGINT(25), primary_key=True)
    ID_REG_1900 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    DT_INI = Column(String(10))
    DT_FIN = Column(String(10))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpi1920(Base):
    __tablename__ = 'sped_icms_ipi_1920'

    ID_REG_1920 = Column(BIGINT(25), primary_key=True)
    ID_REG_1910 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    VL_TOT_TRANSF_DEBITOS_OA = Column(String(30))
    VL_TOT_AJ_DEBITOS_OA = Column(String(30))
    VL_ESTORNOS_CRED_OA = Column(String(30))
    VL_TOT_TRANSF_CREDITOS_OA = Column(String(30))
    VL_TOT_AJ_CREDITOS_OA = Column(String(30))
    VL_ESTORNOS_DEB_OA = Column(String(30))
    VL_SLD_CREDOR_ANT_OA = Column(String(30))
    VL_SLD_APURADO_OA = Column(String(30))
    VL_TOT_DED = Column(String(30))
    VL_ICMS_RECOLHER_OA = Column(String(30))
    VL_SLD_CREDOR_TRANSP_OA = Column(String(30))
    DEB_ESP_OA = Column(String(30))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpi1921(Base):
    __tablename__ = 'sped_icms_ipi_1921'

    ID_REG_1921 = Column(BIGINT(25), primary_key=True)
    ID_REG_1920 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    COD_AJ_APUR = Column(String(8))
    DESCR_COMPL_AJ = Column(String(255))
    VL_AJ_APUR = Column(String(30))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpi1922(Base):
    __tablename__ = 'sped_icms_ipi_1922'

    ID_REG_1922 = Column(BIGINT(25), primary_key=True)
    ID_REG_1921 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    NUM_DA = Column(String(255))
    NUM_PROC = Column(String(15))
    IND_PROC = Column(String(1))
    PROCESS = Column(String(255))
    TXT_COMPL = Column(String(255))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpi1923(Base):
    __tablename__ = 'sped_icms_ipi_1923'

    ID_REG_1923 = Column(BIGINT(25), primary_key=True)
    ID_REG_1921 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    COD_PART = Column(String(60))
    COD_MOD = Column(String(2))
    SER = Column(String(4))
    SUB = Column(String(3))
    NUM_DOC = Column(String(9))
    DT_DOC = Column(String(10))
    COD_ITEM = Column(String(60))
    VL_AJ_ITEM = Column(String(30))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpi1925(Base):
    __tablename__ = 'sped_icms_ipi_1925'

    ID_REG_1925 = Column(BIGINT(25), primary_key=True)
    ID_REG_1920 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    COD_INF_ADIC = Column(String(8))
    VL_INF_ADIC = Column(String(30))
    DESC_COMPL_AJ = Column(String(255))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpi1926(Base):
    __tablename__ = 'sped_icms_ipi_1926'

    ID_REG_1926 = Column(BIGINT(25), primary_key=True)
    ID_REG_1920 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    COD_OR = Column(String(3))
    VL_OR = Column(String(30))
    DT_VCTO = Column(String(10))
    COD_REC = Column(String(255))
    NUM_PROC = Column(String(15))
    IND_PROC = Column(String(1))
    PROCESS = Column(String(255))
    TXT_COMPL = Column(String(255))
    MES_REF = Column(String(6))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpi1990(Base):
    __tablename__ = 'sped_icms_ipi_1990'

    ID_REG_1990 = Column(BIGINT(25), primary_key=True)
    ID_REG_0000 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    QTD_LIN_1 = Column(String(255))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpi9001(Base):
    __tablename__ = 'sped_icms_ipi_9001'

    ID_REG_9001 = Column(BIGINT(25), primary_key=True)
    ID_REG_0000 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    IND_MOV = Column(String(1))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpi9900(Base):
    __tablename__ = 'sped_icms_ipi_9900'

    ID_REG_9900 = Column(BIGINT(25), primary_key=True)
    ID_REG_9001 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    SPEDFIS_REG_BLC = Column(String(4))
    QTD_SPEDFIS_REG_BLC = Column(String(255))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpi9990(Base):
    __tablename__ = 'sped_icms_ipi_9990'

    ID_REG_9990 = Column(BIGINT(25), primary_key=True)
    ID_REG_0000 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    QTD_LIN_9 = Column(String(255))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpi9999(Base):
    __tablename__ = 'sped_icms_ipi_9999'

    ID_REG_9999 = Column(BIGINT(25), primary_key=True)
    ID_LOTES_ARQUIVOS = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    QTD_LIN = Column(String(255))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiC001(Base):
    __tablename__ = 'sped_icms_ipi_C001'

    ID_REG_C001 = Column(BIGINT(25), primary_key=True)
    ID_REG_0000 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    IND_MOV = Column(String(1))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiC100(Base):
    __tablename__ = 'sped_icms_ipi_C100'

    ID_REG_C100 = Column(BIGINT(25), primary_key=True)
    ID_REG_C001 = Column(BIGINT(25), nullable=False)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(255))
    IND_OPER = Column(String(255))
    IND_EMIT = Column(String(255))
    COD_PART = Column(String(255))
    COD_MOD = Column(String(2))
    COD_SIT = Column(String(2))
    SER = Column(String(3))
    NUM_DOC = Column(String(9))
    CHV_NFE = Column(String(44))
    DT_DOC = Column(String(10))
    DT_E_S = Column(String(10))
    VL_DOC = Column(String(30))
    IND_PGTO = Column(String(1))
    VL_DESC = Column(String(30))
    VL_ABAT_NT = Column(String(30))
    VL_MERC = Column(String(30))
    IND_FRT = Column(String(1))
    VL_FRT = Column(String(30))
    VL_SEG = Column(String(30))
    VL_OUT_DA = Column(String(30))
    VL_BC_ICMS = Column(String(30))
    VL_ICMS = Column(String(30))
    VL_BC_ICMS_ST = Column(String(30))
    VL_ICMS_ST = Column(String(30))
    VL_IPI = Column(String(30))
    VL_PIS = Column(String(30))
    VL_COFINS = Column(String(30))
    VL_PIS_ST = Column(String(30))
    VL_COFINS_ST = Column(String(30))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11), index=True)


class SpedIcmsIpiC101(Base):
    __tablename__ = 'sped_icms_ipi_C101'

    ID_REG_C101 = Column(BIGINT(25), primary_key=True)
    ID_REG_C100 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    VL_FCP_UF_DEST = Column(String(30))
    VL_ICMS_UF_DEST = Column(String(30))
    VL_ICMS_UF_REM = Column(String(30))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiC105(Base):
    __tablename__ = 'sped_icms_ipi_C105'

    ID_REG_C105 = Column(BIGINT(25), primary_key=True)
    ID_REG_C100 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    OPER = Column(String(1))
    COD_UF = Column(String(2))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiC110(Base):
    __tablename__ = 'sped_icms_ipi_C110'

    ID_REG_C110 = Column(BIGINT(25), primary_key=True)
    ID_REG_C100 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    COD_INF = Column(String(6))
    TXT_COMPL = Column(LONGTEXT)
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiC111(Base):
    __tablename__ = 'sped_icms_ipi_C111'

    ID_REG_C111 = Column(BIGINT(25), primary_key=True)
    ID_REG_C110 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    NUM_PROC = Column(String(15))
    IND_PROC = Column(String(1))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiC112(Base):
    __tablename__ = 'sped_icms_ipi_C112'

    ID_REG_C112 = Column(BIGINT(25), primary_key=True)
    ID_REG_C110 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    COD_DA = Column(String(1))
    UF = Column(String(2))
    NUM_DA = Column(String(255))
    COD_AUT = Column(String(255))
    VL_DA = Column(String(30))
    DT_VCTO = Column(String(10))
    DT_PGTO = Column(String(10))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiC113(Base):
    __tablename__ = 'sped_icms_ipi_C113'

    ID_REG_C113 = Column(BIGINT(25), primary_key=True)
    ID_REG_C110 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    IND_OPER = Column(String(1))
    IND_EMIT = Column(String(1))
    COD_PART = Column(String(60))
    COD_MOD = Column(String(2))
    SER = Column(String(4))
    SUB = Column(String(3))
    NUM_DOC = Column(String(9))
    DT_DOC = Column(String(10))
    CHV_DOCe = Column(String(255))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiC114(Base):
    __tablename__ = 'sped_icms_ipi_C114'

    ID_REG_C114 = Column(BIGINT(25), primary_key=True)
    ID_REG_C110 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    COD_MOD = Column(String(2))
    ECF_FAB = Column(String(21))
    ECF_CX = Column(String(3))
    NUM_DOC = Column(String(9))
    DT_DOC = Column(String(10))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiC115(Base):
    __tablename__ = 'sped_icms_ipi_C115'

    ID_REG_C115 = Column(BIGINT(25), primary_key=True)
    ID_REG_C110 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    IND_CARGA = Column(String(1))
    CNPJ_COL = Column(String(14))
    IE_COL = Column(String(14))
    CPF_COL = Column(String(11))
    COD_MUN_COL = Column(String(7))
    CNPJ_ENTG = Column(String(14))
    IE_ENTG = Column(String(14))
    CPF_ENTG = Column(String(11))
    COD_MUN_ENTG = Column(String(7))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiC116(Base):
    __tablename__ = 'sped_icms_ipi_C116'

    ID_REG_C116 = Column(BIGINT(25), primary_key=True)
    ID_REG_C110 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    COD_MOD = Column(String(2))
    NR_SAT = Column(String(9))
    CHV_CFE = Column(String(44))
    NUM_CFE = Column(String(6))
    DT_DOC = Column(String(8))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiC120(Base):
    __tablename__ = 'sped_icms_ipi_C120'

    ID_REG_C120 = Column(BIGINT(25), primary_key=True)
    ID_REG_C100 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    COD_DOC_IMP = Column(String(1))
    NUM_DOC_IMP = Column(String(12))
    PIS_IMP = Column(String(30))
    COFINS_IMP = Column(String(30))
    NUM_ACDRAW = Column(String(20))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiC130(Base):
    __tablename__ = 'sped_icms_ipi_C130'

    ID_REG_C130 = Column(BIGINT(25), primary_key=True)
    ID_REG_C100 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    VL_SERV_NT = Column(String(30))
    VL_BC_ISSQN = Column(String(30))
    VL_ISSQN = Column(String(30))
    VL_BC_IRRF = Column(String(30))
    VL_IRRF = Column(String(30))
    VL_BC_PREV = Column(String(30))
    VL_PREV = Column(String(30))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiC140(Base):
    __tablename__ = 'sped_icms_ipi_C140'

    ID_REG_C140 = Column(BIGINT(25), primary_key=True)
    ID_REG_C100 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    IND_EMIT = Column(String(1))
    IND_TIT = Column(String(2))
    DESC_TIT = Column(String(255))
    NUM_TIT = Column(String(255))
    QTD_PARC = Column(String(2))
    VL_TIT = Column(String(30))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiC141(Base):
    __tablename__ = 'sped_icms_ipi_C141'

    ID_REG_C141 = Column(BIGINT(25), primary_key=True)
    ID_REG_C140 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    NUM_PARC = Column(String(2))
    DT_VCTO = Column(String(10))
    VL_PARC = Column(String(30))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiC160(Base):
    __tablename__ = 'sped_icms_ipi_C160'

    ID_REG_C160 = Column(BIGINT(25), primary_key=True)
    ID_REG_C100 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    COD_PART = Column(String(60))
    VEIC_ID_ = Column(String(7))
    QTD_VOL = Column(String(255))
    PESO_BRT = Column(String(30))
    PESO_LIQ = Column(String(30))
    UF_ID_ = Column(String(2))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiC165(Base):
    __tablename__ = 'sped_icms_ipi_C165'

    ID_REG_C165 = Column(BIGINT(25), primary_key=True)
    ID_REG_C100 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    COD_PART = Column(String(60))
    VEIC_ID_ = Column(String(7))
    COD_AUT = Column(String(255))
    NR_PASSE = Column(String(255))
    HORA = Column(String(6))
    TEMPER = Column(String(30))
    QTD_VOL = Column(String(255))
    PESO_BRT = Column(String(30))
    PESO_LIQ = Column(String(30))
    NOM_MOT = Column(String(60))
    CPF = Column(String(11))
    UF_ID_ = Column(String(2))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiC170(Base):
    __tablename__ = 'sped_icms_ipi_C170'

    ID_REG_C170 = Column(BIGINT(25), primary_key=True)
    ID_REG_C100 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    NUM_ITEM = Column(String(3))
    COD_ITEM = Column(String(60))
    DESCR_COMPL = Column(String(255))
    QTD = Column(String(30))
    UNID_ = Column(String(6))
    VL_ITEM = Column(String(30))
    VL_DESC = Column(String(30))
    IND_MOV = Column(String(1))
    CST_ICMS = Column(String(3))
    CFOP = Column(String(4))
    COD_NAT = Column(String(10))
    VL_BC_ICMS = Column(String(30))
    ALIQ_ICMS = Column(String(30))
    VL_ICMS = Column(String(30))
    VL_BC_ICMS_ST = Column(String(30))
    ALIQ_ST = Column(String(30))
    VL_ICMS_ST = Column(String(30))
    IND_APUR = Column(String(1))
    CST_IPI = Column(String(2))
    COD_ENQ = Column(String(3))
    VL_BC_IPI = Column(String(30))
    ALIQ_IPI = Column(String(30))
    VL_IPI = Column(String(30))
    CST_PIS = Column(String(2))
    VL_BC_PIS = Column(String(30))
    ALIQ_PIS_PERC = Column(String(30))
    QUANT_BC_PIS = Column(String(30))
    ALIQ_PIS_REAIS = Column(String(30))
    VL_PIS = Column(String(30))
    CST_COFINS = Column(String(2))
    VL_BC_COFINS = Column(String(30))
    ALIQ_COFINS_PERC = Column(String(30))
    QUANT_BC_COFINS = Column(String(30))
    ALIQ_COFINS_REAIS = Column(String(30))
    VL_COFINS = Column(String(30))
    COD_CTA = Column(String(255))
    VL_ABAT_NT = Column(String(100))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11), index=True)


class SpedIcmsIpiC171(Base):
    __tablename__ = 'sped_icms_ipi_C171'

    ID_REG_C171 = Column(BIGINT(25), primary_key=True)
    ID_REG_C170 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    NUM_TANQUE = Column(String(3))
    QTDE = Column(String(30))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiC172(Base):
    __tablename__ = 'sped_icms_ipi_C172'

    ID_REG_C172 = Column(BIGINT(25), primary_key=True)
    ID_REG_C170 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    VL_BC_ISSQN = Column(String(30))
    ALIQ_ISSQN = Column(String(30))
    VL_ISSQN = Column(String(30))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiC173(Base):
    __tablename__ = 'sped_icms_ipi_C173'

    ID_REG_C173 = Column(BIGINT(25), primary_key=True)
    ID_REG_C170 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    LOTE_MED = Column(String(255))
    QTD_ITEM = Column(String(10))
    DT_FAB = Column(String(10))
    DT_VAL = Column(String(10))
    IND_MED = Column(String(1))
    TP_PROD = Column(String(1))
    VL_TAB_MAX = Column(String(30))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiC174(Base):
    __tablename__ = 'sped_icms_ipi_C174'

    ID_REG_C174 = Column(BIGINT(25), primary_key=True)
    ID_REG_C170 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    IND_ARM = Column(String(1))
    NUM_ARM = Column(String(255))
    DESCR_COMPL = Column(String(255))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiC175(Base):
    __tablename__ = 'sped_icms_ipi_C175'

    ID_REG_C175 = Column(BIGINT(25), primary_key=True)
    ID_REG_C170 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    IND_VEIC_OPER = Column(String(1))
    CNPJ = Column(String(14))
    UF = Column(String(2))
    CHASSI_VEIC = Column(String(17))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiC176(Base):
    __tablename__ = 'sped_icms_ipi_C176'

    ID_REG_C176 = Column(BIGINT(25), primary_key=True)
    ID_REG_C170 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    COD_MOD_ULT_E = Column(String(2))
    NUM_DOC_ULT_E = Column(String(9))
    SER_ULT_E = Column(String(3))
    DT_ULT_E = Column(String(10))
    COD_PART_ULT_E = Column(String(60))
    QUANT_ULT_E = Column(String(30))
    VL_UNIT_ULT_E = Column(String(30))
    VL_UNIT_BC_ST = Column(String(30))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiC177(Base):
    __tablename__ = 'sped_icms_ipi_C177'

    ID_REG_C177 = Column(BIGINT(25), primary_key=True)
    ID_REG_C170 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    COD_SELO_IPI = Column(String(6))
    QT_SELO_IPI = Column(String(12))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiC178(Base):
    __tablename__ = 'sped_icms_ipi_C178'

    ID_REG_C178 = Column(BIGINT(25), primary_key=True)
    ID_REG_C170 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    CL_ENQ = Column(String(5))
    VL_UNID_ = Column(String(30))
    QUANT_PAD = Column(String(30))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiC179(Base):
    __tablename__ = 'sped_icms_ipi_C179'

    ID_REG_C179 = Column(BIGINT(25), primary_key=True)
    ID_REG_C170 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    BC_ST_ORIG_DEST = Column(String(30))
    ICMS_ST_REP = Column(String(30))
    ICMS_ST_COMPL = Column(String(30))
    BC_RET = Column(String(30))
    ICMS_RET = Column(String(30))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiC190(Base):
    __tablename__ = 'sped_icms_ipi_C190'

    ID_REG_C190 = Column(BIGINT(25), primary_key=True)
    ID_REG_C100 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    CST_ICMS = Column(String(3))
    CFOP = Column(String(4))
    ALIQ_ICMS = Column(String(30))
    VL_OPR = Column(String(30))
    VL_BC_ICMS = Column(String(30))
    VL_ICMS = Column(String(30))
    VL_BC_ICMS_ST = Column(String(30))
    VL_ICMS_ST = Column(String(30))
    VL_RED_BC = Column(String(30))
    VL_IPI = Column(String(30))
    COD_OBS = Column(String(6))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11), index=True)


class SpedIcmsIpiC195(Base):
    __tablename__ = 'sped_icms_ipi_C195'

    ID_REG_C195 = Column(BIGINT(25), primary_key=True)
    ID_REG_C100 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    COD_OBS = Column(String(255))
    TXT_COMPL = Column(LONGTEXT)
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiC197(Base):
    __tablename__ = 'sped_icms_ipi_C197'

    ID_REG_C197 = Column(BIGINT(25), primary_key=True)
    ID_REG_C195 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    COD_AJ = Column(String(10))
    DESCR_COMPL_AJ = Column(String(255))
    COD_ITEM = Column(String(60))
    VL_BC_ICMS = Column(String(30))
    ALIQ_ICMS = Column(String(30))
    VL_ICMS = Column(String(30))
    VL_OUTROS = Column(String(30))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiC300(Base):
    __tablename__ = 'sped_icms_ipi_C300'

    ID_REG_C300 = Column(BIGINT(25), primary_key=True)
    ID_REG_C001 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    COD_MOD = Column(String(2))
    SER = Column(String(4))
    SUB = Column(String(3))
    NUM_DOC_INI = Column(String(6))
    NUM_DOC_FIN = Column(String(6))
    DT_DOC = Column(String(10))
    VL_DOC = Column(String(30))
    VL_PIS = Column(String(30))
    VL_COFINS = Column(String(30))
    COD_CTA = Column(String(255))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiC310(Base):
    __tablename__ = 'sped_icms_ipi_C310'

    ID_REG_C310 = Column(BIGINT(25), primary_key=True)
    ID_REG_C300 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    NUM_DOC_CANC = Column(String(6))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiC320(Base):
    __tablename__ = 'sped_icms_ipi_C320'

    ID_REG_C320 = Column(BIGINT(25), primary_key=True)
    ID_REG_C300 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    CST_ICMS = Column(String(3))
    CFOP = Column(String(4))
    ALIQ_ICMS = Column(String(30))
    VL_OPR = Column(String(30))
    VL_BC_ICMS = Column(String(30))
    VL_ICMS = Column(String(30))
    VL_RED_BC = Column(String(30))
    COD_OBS = Column(String(6))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiC321(Base):
    __tablename__ = 'sped_icms_ipi_C321'

    ID_REG_C321 = Column(BIGINT(25), primary_key=True)
    ID_REG_C320 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    COD_ITEM = Column(String(60))
    QTD = Column(String(30))
    UNID_ = Column(String(6))
    VL_ITEM = Column(String(30))
    VL_DESC = Column(String(30))
    VL_BC_ICMS = Column(String(30))
    VL_ICMS = Column(String(30))
    VL_PIS = Column(String(30))
    VL_COFINS = Column(String(30))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiC350(Base):
    __tablename__ = 'sped_icms_ipi_C350'

    ID_REG_C350 = Column(BIGINT(25), primary_key=True)
    ID_REG_C001 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    SER = Column(String(4))
    SUB_SER = Column(String(3))
    NUM_DOC = Column(String(6))
    DT_DOC = Column(String(10))
    CNPJ_CPF = Column(String(14))
    VL_MERC = Column(String(30))
    VL_DOC = Column(String(30))
    VL_DESC = Column(String(30))
    VL_PIS = Column(String(30))
    VL_COFIS = Column(String(30))
    COD_CTA = Column(String(255))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiC370(Base):
    __tablename__ = 'sped_icms_ipi_C370'

    ID_REG_C370 = Column(BIGINT(25), primary_key=True)
    ID_REG_C350 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    NUM_ITEM = Column(String(3))
    COD_ITEM = Column(String(60))
    QTD = Column(String(30))
    UNID_ = Column(String(6))
    VL_ITEM = Column(String(30))
    VL_DESC = Column(String(30))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiC390(Base):
    __tablename__ = 'sped_icms_ipi_C390'

    ID_REG_C390 = Column(BIGINT(25), primary_key=True)
    ID_REG_C350 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    CST_ICMS = Column(String(3))
    CFOP = Column(String(4))
    ALIQ_ICMS = Column(String(30))
    VL_OPR = Column(String(30))
    VL_BC_ICMS = Column(String(30))
    VL_ICMS = Column(String(30))
    VL_RED_BC = Column(String(30))
    COD_OBS = Column(String(6))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiC400(Base):
    __tablename__ = 'sped_icms_ipi_C400'

    ID_REG_C400 = Column(BIGINT(25), primary_key=True)
    ID_REG_C001 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    COD_MOD = Column(String(2))
    ECF_MOD = Column(String(20))
    ECF_FAB = Column(String(21))
    ECF_CX = Column(String(3))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiC405(Base):
    __tablename__ = 'sped_icms_ipi_C405'

    ID_REG_C405 = Column(BIGINT(25), primary_key=True)
    ID_REG_C400 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    DT_DOC = Column(String(10))
    CRO = Column(String(3))
    CRZ = Column(String(6))
    NUM_COO_FIN = Column(String(9))
    GT_FIN = Column(String(30))
    VL_BRT = Column(String(30))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiC410(Base):
    __tablename__ = 'sped_icms_ipi_C410'

    ID_REG_C410 = Column(BIGINT(25), primary_key=True)
    ID_REG_C405 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    VL_PIS = Column(String(30))
    VL_COFINS = Column(String(30))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiC420(Base):
    __tablename__ = 'sped_icms_ipi_C420'

    ID_REG_C420 = Column(BIGINT(25), primary_key=True)
    ID_REG_C405 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    COD_TOT_PAR = Column(String(7))
    VLR_ACUM_TOT = Column(String(30))
    NR_TOT = Column(String(2))
    DESCR_NR_TOT = Column(String(255))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiC425(Base):
    __tablename__ = 'sped_icms_ipi_C425'

    ID_REG_C425 = Column(BIGINT(25), primary_key=True)
    ID_REG_C420 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    COD_ITEM = Column(String(60))
    QTD = Column(String(30))
    UNID_ = Column(String(6))
    VL_ITEM = Column(String(30))
    VL_PIS = Column(String(30))
    VL_COFINS = Column(String(30))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiC460(Base):
    __tablename__ = 'sped_icms_ipi_C460'

    ID_REG_C460 = Column(BIGINT(25), primary_key=True)
    ID_REG_C405 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    COD_MOD = Column(String(2))
    COD_SIT = Column(String(2))
    NUM_DOC = Column(String(9))
    DT_DOC = Column(String(10))
    VL_DOC = Column(String(30))
    VL_PIS = Column(String(30))
    VL_COFINS = Column(String(30))
    CPF_CNPJ = Column(String(14))
    NOME_ADQ = Column(String(60))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiC465(Base):
    __tablename__ = 'sped_icms_ipi_C465'

    ID_REG_C465 = Column(BIGINT(25), primary_key=True)
    ID_REG_C460 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    CHV_CFE = Column(String(44))
    NUM_CCF = Column(String(9))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiC470(Base):
    __tablename__ = 'sped_icms_ipi_C470'

    ID_REG_C470 = Column(BIGINT(25), primary_key=True)
    ID_REG_C460 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    COD_ITEM = Column(String(60))
    QTD = Column(String(30))
    QTD_CANC = Column(String(30))
    UNID_ = Column(String(6))
    VL_ITEM = Column(String(30))
    CST_ICMS = Column(String(3))
    CFOP = Column(String(4))
    ALIQ_ICMS = Column(String(30))
    VL_PIS = Column(String(30))
    VL_COFINS = Column(String(30))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiC490(Base):
    __tablename__ = 'sped_icms_ipi_C490'

    ID_REG_C490 = Column(BIGINT(25), primary_key=True)
    ID_REG_C405 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    CST_ICMS = Column(String(3))
    CFOP = Column(String(4))
    ALIQ_ICMS = Column(String(30))
    VL_OPR = Column(String(30))
    VL_BC_ICMS = Column(String(30))
    VL_ICMS = Column(String(30))
    COD_OBS = Column(String(6))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiC495(Base):
    __tablename__ = 'sped_icms_ipi_C495'

    ID_REG_C495 = Column(BIGINT(25), primary_key=True)
    ID_REG_C001 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    ALIQ_ICMS = Column(String(30))
    COD_ITEM = Column(String(60))
    QTD = Column(String(30))
    QTD_CANC = Column(String(30))
    UNID = Column(String(6))
    VL_ITEM = Column(String(30))
    VL_DESC = Column(String(30))
    VL_CANC = Column(String(30))
    VL_ACMO = Column(String(30))
    VL_BC_ICMS = Column(String(30))
    VL_ICMS = Column(String(30))
    VL_ISEN = Column(String(30))
    VL_NT = Column(String(30))
    VL_ICMS_ST = Column(String(30))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiC500(Base):
    __tablename__ = 'sped_icms_ipi_C500'

    ID_REG_C500 = Column(BIGINT(25), primary_key=True)
    ID_REG_C001 = Column(BIGINT(25), nullable=False)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    IND_OPER = Column(String(1))
    IND_EMIT = Column(String(1))
    COD_PART = Column(String(60))
    COD_MOD = Column(String(2))
    COD_SIT = Column(String(2))
    SER = Column(String(4))
    SUB = Column(String(3))
    COD_CONS = Column(String(2))
    NUM_DOC = Column(String(9))
    DT_DOC = Column(String(10))
    DT_E_S = Column(String(10))
    VL_DOC = Column(String(30))
    VL_DESC = Column(String(30))
    VL_FORN = Column(String(30))
    VL_SERV_NT = Column(String(30))
    VL_TERC = Column(String(30))
    VL_DA = Column(String(30))
    VL_BC_ICMS = Column(String(30))
    VL_ICMS = Column(String(30))
    VL_BC_ICMS_ST = Column(String(30))
    VL_ICMS_ST = Column(String(30))
    COD_INF = Column(String(6))
    VL_PIS = Column(String(30))
    VL_COFINS = Column(String(30))
    TP_LIGACAO = Column(String(1))
    COD_GRUPO_TENSAO = Column(String(2))
    CHV_DOCe = Column(String(100))
    FIN_DOCe = Column(String(100))
    CHV_DOCe_REF = Column(String(100))
    IND_DEST = Column(String(100))
    COD_MUN_DEST = Column(String(100))
    COD_CTA = Column(String(100))
    HASH_DOC_REF = Column(String(10))
    SER_DOC_REF = Column(String(10))
    NUM_DOC_REF = Column(String(10))
    MES_DOC_REF = Column(String(10))
    ENER_INJET = Column(String(100))
    OUTRAS_DED = Column(String(100))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11), index=True)


class SpedIcmsIpiC510(Base):
    __tablename__ = 'sped_icms_ipi_C510'

    ID_REG_C510 = Column(BIGINT(25), primary_key=True)
    ID_REG_C500 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    NUM_ITEM = Column(String(3))
    COD_ITEM = Column(String(60))
    COD_CLASS = Column(String(4))
    QTD = Column(String(30))
    UNID_ = Column(String(6))
    VL_ITEM = Column(String(30))
    VL_DESC = Column(String(30))
    CST_ICMS = Column(String(3))
    CFOP = Column(String(4))
    VL_BC_ICMS = Column(String(30))
    ALIQ_ICMS = Column(String(30))
    VL_ICMS = Column(String(30))
    VL_BC_ICMS_ST = Column(String(30))
    ALIQ_ST = Column(String(30))
    VL_ICMS_ST = Column(String(30))
    IND_REC = Column(String(1))
    COD_PART = Column(String(60))
    VL_PIS = Column(String(30))
    VL_COFINS = Column(String(30))
    COD_CTA = Column(String(255))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiC590(Base):
    __tablename__ = 'sped_icms_ipi_C590'

    ID_REG_C590 = Column(BIGINT(25), primary_key=True)
    ID_REG_C500 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    CST_ICMS = Column(String(3))
    CFOP = Column(String(4))
    ALIQ_ICMS = Column(String(30))
    VL_OPR = Column(String(30))
    VL_BC_ICMS = Column(String(30))
    VL_ICMS = Column(String(30))
    VL_BC_ICMS_ST = Column(String(30))
    VL_ICMS_ST = Column(String(30))
    VL_RED_BC = Column(String(30))
    COD_OBS = Column(String(6))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11), index=True)


class SpedIcmsIpiC600(Base):
    __tablename__ = 'sped_icms_ipi_C600'

    ID_REG_C600 = Column(BIGINT(25), primary_key=True)
    ID_REG_C001 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    COD_MOD = Column(String(2))
    COD_MUN = Column(String(7))
    SER = Column(String(4))
    SUB = Column(String(3))
    COD_CONS = Column(String(2))
    QTD_CONS = Column(String(255))
    QTD_CANC = Column(String(255))
    DT_DOC = Column(String(10))
    VL_DOC = Column(String(30))
    VL_DESC = Column(String(30))
    CONS = Column(String(255))
    VL_FORN = Column(String(30))
    VL_SERV_NT = Column(String(30))
    VL_TERC = Column(String(30))
    VL_DA = Column(String(30))
    VL_BC_ICMS = Column(String(30))
    VL_ICMS = Column(String(30))
    VL_BC_ICMS_ST = Column(String(30))
    VL_ICMS_ST = Column(String(30))
    VL_PIS = Column(String(30))
    VL_COFINS = Column(String(30))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiC601(Base):
    __tablename__ = 'sped_icms_ipi_C601'

    ID_REG_C601 = Column(BIGINT(25), primary_key=True)
    ID_REG_C600 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    NUM_DOC_CANC = Column(String(9))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiC610(Base):
    __tablename__ = 'sped_icms_ipi_C610'

    ID_REG_C610 = Column(BIGINT(25), primary_key=True)
    ID_REG_C600 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    COD_CLASS = Column(String(4))
    COD_ITEM = Column(String(60))
    QTD = Column(String(30))
    UNID_ = Column(String(6))
    VL_ITEM = Column(String(30))
    VL_DESC = Column(String(30))
    CST_ICMS = Column(String(3))
    CFOP = Column(String(4))
    ALIQ_ICMS = Column(String(30))
    VL_BC_ICMS = Column(String(30))
    VL_ICMS = Column(String(30))
    VL_BC_ICMS_ST = Column(String(30))
    VL_ICMS_ST = Column(String(30))
    VL_PIS = Column(String(30))
    VL_COFINS = Column(String(30))
    COD_CTA = Column(String(255))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiC690(Base):
    __tablename__ = 'sped_icms_ipi_C690'

    ID_REG_C690 = Column(BIGINT(25), primary_key=True)
    ID_REG_C600 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    CST_ICMS = Column(String(3))
    CFOP = Column(String(4))
    ALIQ_ICMS = Column(String(30))
    VL_OPR = Column(String(30))
    VL_BC_ICMS = Column(String(30))
    VL_ICMS = Column(String(30))
    VL_RED_BC = Column(String(30))
    VL_BC_ICMS_ST = Column(String(30))
    VL_ICMS_ST = Column(String(30))
    COD_OBS = Column(String(6))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiC700(Base):
    __tablename__ = 'sped_icms_ipi_C700'

    ID_REG_C700 = Column(BIGINT(25), primary_key=True)
    ID_REG_C001 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    COD_MOD = Column(String(2))
    SER = Column(String(4))
    NRO_ORD_INI = Column(String(9))
    NRO_ORD_FIN = Column(String(9))
    DT_DOC_INI = Column(String(10))
    DT_DOC_FIN = Column(String(10))
    NOM_MEST = Column(String(15))
    CHV_COD_DIG = Column(String(32))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiC790(Base):
    __tablename__ = 'sped_icms_ipi_C790'

    ID_REG_C790 = Column(BIGINT(25), primary_key=True)
    ID_REG_C700 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    CST_ICMS = Column(String(3))
    CFOP = Column(String(4))
    ALIQ_ICMS = Column(String(30))
    VL_OPR = Column(String(30))
    VL_BC_ICMS = Column(String(30))
    VL_ICMS = Column(String(30))
    VL_BC_ICMS_ST = Column(String(30))
    VL_ICMS_ST = Column(String(30))
    VL_RED_BC = Column(String(30))
    COD_OBS = Column(String(6))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiC791(Base):
    __tablename__ = 'sped_icms_ipi_C791'

    ID_REG_C791 = Column(BIGINT(25), primary_key=True)
    ID_REG_C790 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    UF = Column(String(2))
    VL_BC_ICMS_ST = Column(String(30))
    VL_ICMS_ST = Column(String(30))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiC800(Base):
    __tablename__ = 'sped_icms_ipi_C800'

    ID_REG_C800 = Column(BIGINT(25), primary_key=True)
    ID_REG_C001 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    COD_MOD = Column(String(2))
    COD_SIT = Column(String(2))
    NUM_CFE = Column(String(6))
    DT_DOC = Column(String(10))
    VL_CFE = Column(String(30))
    VL_PIS = Column(String(30))
    VL_COFINS = Column(String(30))
    CNPJ_CPF = Column(String(14))
    NR_SAT = Column(String(9))
    CHV_CFE = Column(String(44))
    VL_DESC = Column(String(30))
    VL_MERC = Column(String(30))
    VL_OUT_DA = Column(String(30))
    VL_ICMS = Column(String(30))
    VL_PIS_ST = Column(String(30))
    VL_COFINS_ST = Column(String(30))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiC850(Base):
    __tablename__ = 'sped_icms_ipi_C850'

    ID_REG_C850 = Column(BIGINT(25), primary_key=True)
    ID_REG_C800 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    CST_ICMS = Column(String(3))
    CFOP = Column(String(4))
    ALIQ_ICMS = Column(String(30))
    VL_OPR = Column(String(30))
    VL_BC_ICMS = Column(String(30))
    VL_ICMS = Column(String(30))
    COD_OBS = Column(String(6))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiC860(Base):
    __tablename__ = 'sped_icms_ipi_C860'

    ID_REG_C860 = Column(BIGINT(25), primary_key=True)
    ID_REG_C001 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    COD_MOD = Column(String(2))
    NR_SAT = Column(String(9))
    DT_DOC = Column(String(10))
    DOC_INI = Column(String(6))
    DOC_FIM = Column(String(6))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiC890(Base):
    __tablename__ = 'sped_icms_ipi_C890'

    ID_REG_C890 = Column(BIGINT(25), primary_key=True)
    ID_REG_C860 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    CST_ICMS = Column(String(3))
    CFOP = Column(String(4))
    ALIQ_ICMS = Column(String(30))
    VL_OPR = Column(String(30))
    VL_BC_ICMS = Column(String(30))
    VL_ICMS = Column(String(30))
    COD_OBS = Column(String(6))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiC990(Base):
    __tablename__ = 'sped_icms_ipi_C990'

    ID_REG_C990 = Column(BIGINT(25), primary_key=True)
    ID_REG_0000 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    QTD_LIN_C = Column(String(255))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiD001(Base):
    __tablename__ = 'sped_icms_ipi_D001'

    ID_REG_D001 = Column(BIGINT(25), primary_key=True)
    ID_REG_0000 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    IND_MOV = Column(String(1))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiD100(Base):
    __tablename__ = 'sped_icms_ipi_D100'

    ID_REG_D100 = Column(BIGINT(25), primary_key=True)
    ID_REG_D001 = Column(BIGINT(25), nullable=False)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    IND_OPER = Column(String(1))
    IND_EMIT = Column(String(1))
    COD_PART = Column(String(60))
    COD_MOD = Column(String(2))
    COD_SIT = Column(String(2))
    SER = Column(String(4))
    SUB = Column(String(3))
    NUM_DOC = Column(String(9))
    CHV_CTE = Column(String(44))
    DT_DOC = Column(String(10))
    DT_A_P = Column(String(10))
    TP_CT_E = Column(String(1))
    CHV_CTE_REF = Column(String(44))
    VL_DOC = Column(String(30))
    VL_DESC = Column(String(30))
    IND_FRT = Column(String(1))
    VL_SERV = Column(String(30))
    VL_BC_ICMS = Column(String(30))
    VL_ICMS = Column(String(30))
    VL_NT = Column(String(30))
    COD_INF = Column(String(60))
    COD_CTA = Column(String(255))
    COD_MUN_ORIG = Column(String(255))
    COD_MUN_DEST = Column(String(255))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11), index=True)


class SpedIcmsIpiD101(Base):
    __tablename__ = 'sped_icms_ipi_D101'

    ID_REG_D101 = Column(BIGINT(25), primary_key=True)
    ID_REG_D100 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    VL_FCP_UF_DEST = Column(String(30))
    VL_ICMS_UF_DEST = Column(String(30))
    VL_ICMS_UF_REM = Column(String(30))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiD110(Base):
    __tablename__ = 'sped_icms_ipi_D110'

    ID_REG_D110 = Column(BIGINT(25), primary_key=True)
    ID_REG_D100 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    NUM_ITEM = Column(String(3))
    COD_ITEM = Column(String(60))
    VL_SERV = Column(String(30))
    VL_OUT = Column(String(30))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiD120(Base):
    __tablename__ = 'sped_icms_ipi_D120'

    ID_REG_D120 = Column(BIGINT(25), primary_key=True)
    ID_REG_D110 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    COD_MUN_ORIG = Column(String(7))
    COD_MUN_DEST = Column(String(7))
    VEIC_ID_ = Column(String(7))
    UF_ID_ = Column(String(2))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiD130(Base):
    __tablename__ = 'sped_icms_ipi_D130'

    ID_REG_D130 = Column(BIGINT(25), primary_key=True)
    ID_REG_D100 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    COD_PART_CONSG = Column(String(60))
    COD_PART_RED = Column(String(60))
    IND_FRT_RED = Column(String(1))
    COD_MUN_ORIG = Column(String(7))
    COD_MUN_DEST = Column(String(7))
    VEIC_ID_ = Column(String(7))
    VL_LIQ_FRT = Column(String(30))
    VL_SEC_CAT = Column(String(30))
    VL_DESP = Column(String(30))
    VL_PEDG = Column(String(30))
    VL_OUT = Column(String(30))
    VL_FRT = Column(String(30))
    UF_ID_ = Column(String(2))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiD140(Base):
    __tablename__ = 'sped_icms_ipi_D140'

    ID_REG_D140 = Column(BIGINT(25), primary_key=True)
    ID_REG_D100 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    COD_PART_CONSG = Column(String(60))
    COD_MUN_ORIG = Column(String(7))
    COD_MUN_DEST = Column(String(7))
    IND_VEIC = Column(String(1))
    VEIC_ID_ = Column(String(255))
    IND_NAV = Column(String(1))
    VIAGEM = Column(String(255))
    VL_FRT_LIQ = Column(String(30))
    VL_DESP_PORT = Column(String(30))
    VL_DESP_CAR_DESC = Column(String(30))
    VL_OUT = Column(String(30))
    VL_FRT_BRT = Column(String(30))
    VL_FRT_MM = Column(String(30))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiD150(Base):
    __tablename__ = 'sped_icms_ipi_D150'

    ID_REG_D150 = Column(BIGINT(25), primary_key=True)
    ID_REG_D100 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    COD_MUN_ORIG = Column(String(7))
    COD_MUN_DEST = Column(String(7))
    VEIC_ID_ = Column(String(255))
    VIAGEM = Column(String(255))
    IND_TFA = Column(String(1))
    VL_PESO_TX = Column(String(30))
    VL_TX_TERR = Column(String(30))
    VL_TX_RED = Column(String(30))
    VL_OUT = Column(String(30))
    VL_TX_ADV = Column(String(30))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiD160(Base):
    __tablename__ = 'sped_icms_ipi_D160'

    ID_REG_D160 = Column(BIGINT(25), primary_key=True)
    ID_REG_D100 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    DESPACHO = Column(String(255))
    CNPJ_CPF_REM = Column(String(14))
    IE_REM = Column(String(14))
    COD_MUN_ORI = Column(String(7))
    CNPJ_CPF_DEST = Column(String(14))
    IE_DEST = Column(String(14))
    COD_MUN_DEST = Column(String(7))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiD161(Base):
    __tablename__ = 'sped_icms_ipi_D161'

    ID_REG_D161 = Column(BIGINT(25), primary_key=True)
    ID_REG_D160 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    IND_CARGA = Column(String(1))
    CNPJ_CPF_COL = Column(String(14))
    IE_COL = Column(String(14))
    COD_MUN_COL = Column(String(7))
    CNPJ_CPF_ENTG = Column(String(14))
    IE_ENTG = Column(String(14))
    COD_MUN_ENTG = Column(String(7))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiD162(Base):
    __tablename__ = 'sped_icms_ipi_D162'

    ID_REG_D162 = Column(BIGINT(25), primary_key=True)
    ID_REG_D160 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    COD_MOD = Column(String(2))
    SER = Column(String(4))
    NUM_DOC = Column(String(9))
    DT_DOC = Column(String(10))
    VL_DOC = Column(String(30))
    VL_MERC = Column(String(30))
    QTD_VOL = Column(String(255))
    PESO_BRT = Column(String(30))
    PESO_LIQ = Column(String(30))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiD170(Base):
    __tablename__ = 'sped_icms_ipi_D170'

    ID_REG_D170 = Column(BIGINT(25), primary_key=True)
    ID_REG_D100 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    COD_PART_CONSG = Column(String(60))
    COD_PART_RED = Column(String(60))
    COD_MUN_ORIG = Column(String(7))
    COD_MUN_DEST = Column(String(7))
    OTM = Column(String(255))
    IND_NAT_FRT = Column(String(1))
    VL_LIQ_FRT = Column(String(30))
    VL_GRIS = Column(String(30))
    VL_PDG = Column(String(30))
    VL_OUT = Column(String(30))
    VL_FRT = Column(String(30))
    VEIC_ID_ = Column(String(7))
    UF_ID_ = Column(String(2))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiD180(Base):
    __tablename__ = 'sped_icms_ipi_D180'

    ID_REG_D180 = Column(BIGINT(25), primary_key=True)
    ID_REG_D100 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    NUM_SEQ = Column(String(255))
    IND_EMIT = Column(String(1))
    CNPJ_CPF_EMIT = Column(String(14))
    UF_EMIT = Column(String(2))
    IE_EMIT = Column(String(14))
    COD_MUN_ORIG = Column(String(7))
    CNPJ_CPF_TOM = Column(String(14))
    UF_TOM = Column(String(2))
    IE_TOM = Column(String(14))
    COD_MUN_DEST = Column(String(7))
    COD_MOD = Column(String(2))
    SER = Column(String(4))
    SUB = Column(String(3))
    NUM_DOC = Column(String(9))
    DT_DOC = Column(String(10))
    VL_DOC = Column(String(30))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiD190(Base):
    __tablename__ = 'sped_icms_ipi_D190'

    ID_REG_D190 = Column(BIGINT(25), primary_key=True)
    ID_REG_D100 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    CST_ICMS = Column(String(3))
    CFOP = Column(String(4))
    ALIQ_ICMS = Column(String(30))
    VL_OPR = Column(String(30))
    VL_BC_ICMS = Column(String(30))
    VL_ICMS = Column(String(30))
    VL_RED_BC = Column(String(30))
    COD_OBS = Column(String(6))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11), index=True)


class SpedIcmsIpiD195(Base):
    __tablename__ = 'sped_icms_ipi_D195'

    ID_REG_D195 = Column(BIGINT(25), primary_key=True)
    ID_REG_D100 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    COD_OBS = Column(String(6))
    TXT_COMPL = Column(String(255))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiD197(Base):
    __tablename__ = 'sped_icms_ipi_D197'

    ID_REG_D197 = Column(BIGINT(25), primary_key=True)
    ID_REG_D195 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    COD_AJ = Column(String(10))
    DESCR_COMPL_AJ = Column(String(255))
    COD_ITEM = Column(String(60))
    VL_BC_ICMS = Column(String(30))
    ALIQ_ICMS = Column(String(30))
    VL_ICMS = Column(String(30))
    VL_OUTROS = Column(String(30))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiD300(Base):
    __tablename__ = 'sped_icms_ipi_D300'

    ID_REG_D300 = Column(BIGINT(25), primary_key=True)
    ID_REG_D001 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    COD_MOD = Column(String(2))
    SER = Column(String(4))
    SUB = Column(String(4))
    NUM_DOC_INI = Column(String(6))
    NUM_DOC_FIN = Column(String(255))
    CST_ICMS = Column(String(3))
    CFOP = Column(String(4))
    ALIQ_ICMS = Column(String(30))
    DT_DOC = Column(String(10))
    VL_OPR = Column(String(30))
    VL_DESC = Column(String(30))
    VL_SERV = Column(String(30))
    VL_SEG = Column(String(30))
    VL_OUT_DESP = Column(String(30))
    VL_BC_ICMS = Column(String(30))
    VL_ICMS = Column(String(30))
    VL_RED_BC = Column(String(30))
    COD_OBS = Column(String(6))
    COD_CTA = Column(String(255))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiD301(Base):
    __tablename__ = 'sped_icms_ipi_D301'

    ID_REG_D301 = Column(BIGINT(25), primary_key=True)
    ID_REG_D300 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    NUM_DOC_CANC = Column(String(255))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiD310(Base):
    __tablename__ = 'sped_icms_ipi_D310'

    ID_REG_D310 = Column(BIGINT(25), primary_key=True)
    ID_REG_D300 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    COD_MUN_ORIG = Column(String(7))
    VL_SERV = Column(String(30))
    VL_BC_ICMS = Column(String(30))
    VL_ICMS = Column(String(30))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiD350(Base):
    __tablename__ = 'sped_icms_ipi_D350'

    ID_REG_D350 = Column(BIGINT(25), primary_key=True)
    ID_REG_D001 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    COD_MOD = Column(String(2))
    ECF_MOD = Column(String(20))
    ECF_FAB = Column(String(21))
    ECF_CX = Column(String(3))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiD355(Base):
    __tablename__ = 'sped_icms_ipi_D355'

    ID_REG_D355 = Column(BIGINT(25), primary_key=True)
    ID_REG_D350 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    DT_DOC = Column(String(10))
    CRO = Column(String(3))
    CRZ = Column(String(6))
    NUM_COO_FIN = Column(String(9))
    GT_FIN = Column(String(30))
    VL_BRT = Column(String(30))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiD360(Base):
    __tablename__ = 'sped_icms_ipi_D360'

    ID_REG_D360 = Column(BIGINT(25), primary_key=True)
    ID_REG_D355 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    VL_PIS = Column(String(30))
    VL_COFINS = Column(String(30))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiD365(Base):
    __tablename__ = 'sped_icms_ipi_D365'

    ID_REG_D365 = Column(BIGINT(25), primary_key=True)
    ID_REG_D355 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    COD_TOT_PAR = Column(String(7))
    VLR_ACUM_TOT = Column(String(30))
    NR_TOT = Column(String(2))
    DESCR_NR_TOT = Column(String(255))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiD370(Base):
    __tablename__ = 'sped_icms_ipi_D370'

    ID_REG_D370 = Column(BIGINT(25), primary_key=True)
    ID_REG_D365 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    COD_MUN_ORIG = Column(String(7))
    VL_SERV = Column(String(30))
    QTD_BILH = Column(String(255))
    VL_BC_ICMS = Column(String(30))
    VL_ICMS = Column(String(30))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiD390(Base):
    __tablename__ = 'sped_icms_ipi_D390'

    ID_REG_D390 = Column(BIGINT(25), primary_key=True)
    ID_REG_D355 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    CST_ICMS = Column(String(3))
    CFOP = Column(String(4))
    ALIQ_ICMS = Column(String(30))
    VL_OPR = Column(String(30))
    VL_BC_ISSQN = Column(String(30))
    ALIQ_ISSQN = Column(String(30))
    VL_ISSQN = Column(String(30))
    VL_BC_ICMS = Column(String(30))
    VL_ICMS = Column(String(30))
    COD_OBS = Column(String(6))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiD400(Base):
    __tablename__ = 'sped_icms_ipi_D400'

    ID_REG_D400 = Column(BIGINT(25), primary_key=True)
    ID_REG_D001 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    COD_PART = Column(String(60))
    COD_MOD = Column(String(2))
    COD_SIT = Column(String(2))
    SER = Column(String(4))
    SUB = Column(String(3))
    NUM_DOC = Column(String(6))
    DT_DOC = Column(String(10))
    VL_DOC = Column(String(30))
    VL_DESC = Column(String(30))
    VL_SERV = Column(String(30))
    VL_BC_ICMS = Column(String(30))
    VL_ICMS = Column(String(30))
    VL_PIS = Column(String(30))
    VL_COFINS = Column(String(30))
    COD_CTA = Column(String(255))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiD410(Base):
    __tablename__ = 'sped_icms_ipi_D410'

    ID_REG_D410 = Column(BIGINT(25), primary_key=True)
    ID_REG_D400 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    COD_MOD = Column(String(2))
    SER = Column(String(4))
    SUB = Column(String(3))
    NUM_DOC_INI = Column(String(6))
    NUM_DOC_FIN = Column(String(6))
    DT_DOC = Column(String(10))
    CST_ICMS = Column(String(3))
    CFOP = Column(String(4))
    ALIQ_ICMS = Column(String(30))
    VL_OPR = Column(String(30))
    VL_DESC = Column(String(30))
    VL_SERV = Column(String(30))
    VL_BC_ICMS = Column(String(30))
    VL_ICMS = Column(String(30))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiD411(Base):
    __tablename__ = 'sped_icms_ipi_D411'

    ID_REG_D411 = Column(BIGINT(25), primary_key=True)
    ID_REG_D410 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    NUM_DOC_CANC = Column(String(6))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiD420(Base):
    __tablename__ = 'sped_icms_ipi_D420'

    ID_REG_D420 = Column(BIGINT(25), primary_key=True)
    ID_REG_D400 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    COD_MUN_ORIG = Column(String(7))
    VL_SERV = Column(String(30))
    VL_BC_ICMS = Column(String(30))
    VL_ICMS = Column(String(30))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiD500(Base):
    __tablename__ = 'sped_icms_ipi_D500'

    ID_REG_D500 = Column(BIGINT(25), primary_key=True)
    ID_REG_D001 = Column(BIGINT(25), nullable=False)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    IND_OPER = Column(String(1))
    IND_EMIT = Column(String(1))
    COD_PART = Column(String(60))
    COD_MOD = Column(String(2))
    COD_SIT = Column(String(2))
    SER = Column(String(4))
    SUB = Column(String(3))
    NUM_DOC = Column(String(9))
    DT_DOC = Column(String(10))
    DT_A_P = Column(String(10))
    VL_DOC = Column(String(30))
    VL_DESC = Column(String(30))
    VL_SERV = Column(String(30))
    VL_SERV_NT = Column(String(30))
    VL_TERC = Column(String(30))
    VL_DA = Column(String(30))
    VL_BC_ICMS = Column(String(30))
    VL_ICMS = Column(String(30))
    COD_INF = Column(String(6))
    VL_PIS = Column(String(30))
    VL_COFINS = Column(String(30))
    COD_CTA = Column(String(255))
    TP_ASSINANTE = Column(String(1))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11), index=True)


class SpedIcmsIpiD510(Base):
    __tablename__ = 'sped_icms_ipi_D510'

    ID_REG_D510 = Column(BIGINT(25), primary_key=True)
    ID_REG_D500 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    NUM_ITEM = Column(String(3))
    COD_ITEM = Column(String(60))
    COD_CLASS = Column(String(4))
    QTD = Column(String(30))
    UNID_ = Column(String(6))
    VL_ITEM = Column(String(30))
    VL_DESC = Column(String(30))
    CST_ICMS = Column(String(3))
    CFOP = Column(String(4))
    VL_BC_ICMS = Column(String(30))
    ALIQ_ICMS = Column(String(30))
    VL_ICMS = Column(String(30))
    VL_BC_ICMS_ST = Column(String(30))
    VL_ICMS_ST = Column(String(30))
    IND_REC = Column(String(1))
    COD_PART = Column(String(60))
    VL_PIS = Column(String(30))
    VL_COFINS = Column(String(30))
    COD_CTA = Column(String(255))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiD530(Base):
    __tablename__ = 'sped_icms_ipi_D530'

    ID_REG_D530 = Column(BIGINT(25), primary_key=True)
    ID_REG_D500 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    IND_SERV = Column(String(1))
    DT_INI_SERV = Column(String(10))
    DT_FIN_SERV = Column(String(10))
    PER_FISCAL = Column(String(6))
    COD_AREA = Column(String(255))
    TERMINAL = Column(String(255))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiD590(Base):
    __tablename__ = 'sped_icms_ipi_D590'

    ID_REG_D590 = Column(BIGINT(25), primary_key=True)
    ID_REG_D500 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    CST_ICMS = Column(String(3))
    CFOP = Column(String(4))
    ALIQ_ICMS = Column(String(30))
    VL_OPR = Column(String(30))
    VL_BC_ICMS = Column(String(30))
    VL_ICMS = Column(String(30))
    VL_BC_ICMS_ST = Column(String(30))
    VL_ICMS_ST = Column(String(30))
    VL_RED_BC = Column(String(30))
    COD_OBS = Column(String(6))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11), index=True)


class SpedIcmsIpiD600(Base):
    __tablename__ = 'sped_icms_ipi_D600'

    ID_REG_D600 = Column(BIGINT(25), primary_key=True)
    ID_REG_D001 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    COD_MOD = Column(String(2))
    COD_MUN = Column(String(7))
    SER = Column(String(4))
    SUB = Column(String(3))
    COD_CONS = Column(String(2))
    QTD_CONS = Column(String(255))
    DT_DOC = Column(String(10))
    VL_DOC = Column(String(30))
    VL_DESC = Column(String(30))
    VL_SERV = Column(String(30))
    VL_SERV_NT = Column(String(30))
    VL_TERC = Column(String(30))
    VL_DA = Column(String(30))
    VL_BC_ICMS = Column(String(30))
    VL_ICMS = Column(String(30))
    VL_PIS = Column(String(30))
    VL_COFINS = Column(String(30))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiD610(Base):
    __tablename__ = 'sped_icms_ipi_D610'

    ID_REG_D610 = Column(BIGINT(25), primary_key=True)
    ID_REG_D600 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    COD_CLASS = Column(String(4))
    COD_ITEM = Column(String(60))
    QTD = Column(String(30))
    UNID_ = Column(String(6))
    VL_ITEM = Column(String(30))
    VL_DESC = Column(String(30))
    CST_ICMS = Column(String(3))
    CFOP = Column(String(4))
    ALIQ_ICMS = Column(String(30))
    VL_BC_ICMS = Column(String(30))
    VL_ICMS = Column(String(30))
    VL_BC_ICMS_ST = Column(String(30))
    VL_ICMS_ST = Column(String(30))
    VL_RED_BC = Column(String(30))
    VL_PIS = Column(String(30))
    VL_COFINS = Column(String(30))
    COD_CTA = Column(String(255))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiD690(Base):
    __tablename__ = 'sped_icms_ipi_D690'

    ID_REG_D690 = Column(BIGINT(25), primary_key=True)
    ID_REG_D600 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    CST_ICMS = Column(String(3))
    CFOP = Column(String(4))
    ALIQ_ICMS = Column(String(30))
    VL_OPR = Column(String(30))
    VL_BC_ICMS = Column(String(30))
    VL_ICMS = Column(String(30))
    VL_BC_ICMS_ST = Column(String(30))
    VL_ICMS_ST = Column(String(30))
    VL_RED_BC = Column(String(30))
    COD_OBS = Column(String(6))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiD695(Base):
    __tablename__ = 'sped_icms_ipi_D695'

    ID_REG_D695 = Column(BIGINT(25), primary_key=True)
    ID_REG_D001 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    COD_MOD = Column(String(2))
    SER = Column(String(4))
    NRO_ORD_INI = Column(String(255))
    NRO_ORD_FIN = Column(String(255))
    DT_DOC_INI = Column(String(10))
    DT_DOC_FIN = Column(String(10))
    NOM_MEST = Column(String(15))
    CHV_COD_DIG = Column(String(32))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiD696(Base):
    __tablename__ = 'sped_icms_ipi_D696'

    ID_REG_D696 = Column(BIGINT(25), primary_key=True)
    ID_REG_D695 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    CST_ICMS = Column(String(3))
    CFOP = Column(String(4))
    ALIQ_ICMS = Column(String(30))
    VL_OPR = Column(String(30))
    VL_BC_ICMS = Column(String(30))
    VL_ICMS = Column(String(30))
    VL_BC_ICMS_ST = Column(String(30))
    VL_ICMS_ST = Column(String(30))
    VL_RED_BC = Column(String(30))
    COD_OBS = Column(String(6))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiD697(Base):
    __tablename__ = 'sped_icms_ipi_D697'

    ID_REG_D697 = Column(BIGINT(25), primary_key=True)
    ID_REG_D696 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    UF = Column(String(2))
    VL_BC_ICMS_ST = Column(String(30))
    VL_ICMS_ST = Column(String(30))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiD990(Base):
    __tablename__ = 'sped_icms_ipi_D990'

    ID_REG_D990 = Column(BIGINT(25), primary_key=True)
    ID_REG_0000 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    QTD_LIN_D = Column(String(255))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiE001(Base):
    __tablename__ = 'sped_icms_ipi_E001'

    ID_REG_E001 = Column(BIGINT(25), primary_key=True)
    ID_REG_0000 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    IND_MOV = Column(String(1))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiE100(Base):
    __tablename__ = 'sped_icms_ipi_E100'

    ID_REG_E100 = Column(BIGINT(25), primary_key=True)
    ID_REG_E001 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    DT_INI = Column(String(10))
    DT_FIN = Column(String(10))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiE110(Base):
    __tablename__ = 'sped_icms_ipi_E110'

    ID_REG_E110 = Column(BIGINT(25), primary_key=True)
    ID_REG_E100 = Column(BIGINT(25), nullable=False)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    VL_TOT_DEBITOS = Column(String(30))
    VL_AJ_DEBITOS = Column(String(30))
    VL_TOT_AJ_DEBITOS = Column(String(30))
    VL_ESTORNOS_CRED = Column(String(30))
    VL_TOT_CREDITOS = Column(String(30))
    VL_AJ_CREDITOS = Column(String(30))
    VL_TOT_AJ_CREDITOS = Column(String(30))
    VL_ESTORNOS_DEB = Column(String(30))
    VL_SLD_CREDOR_ANT = Column(String(30))
    VL_SLD_APURADO = Column(String(30))
    VL_TOT_DED = Column(String(30))
    VL_ICMS_RECOLHER = Column(String(30))
    VL_SLD_CREDOR_TRANSPORTAR = Column(String(30))
    DEB_ESP = Column(String(30))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11), index=True)


class SpedIcmsIpiE111(Base):
    __tablename__ = 'sped_icms_ipi_E111'

    ID_REG_E111 = Column(BIGINT(25), primary_key=True)
    ID_REG_E110 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    COD_AJ_APUR = Column(String(8))
    DESCR_COMPL_AJ = Column(String(255))
    VL_AJ_APUR = Column(String(30))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiE112(Base):
    __tablename__ = 'sped_icms_ipi_E112'

    ID_REG_E112 = Column(BIGINT(25), primary_key=True)
    ID_REG_E111 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    NUM_DA = Column(String(255))
    NUM_PROC = Column(String(15))
    IND_PROC = Column(String(1))
    PROCESS = Column(String(255))
    TXT_COMPL = Column(String(255))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiE113(Base):
    __tablename__ = 'sped_icms_ipi_E113'

    ID_REG_E113 = Column(BIGINT(25), primary_key=True)
    ID_REG_E111 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(INTEGER(11), nullable=False)
    REG = Column(String(4))
    COD_PART = Column(String(60))
    COD_MOD = Column(String(2))
    SER = Column(String(4))
    SUB = Column(String(3))
    NUM_DOC = Column(String(9))
    DT_DOC = Column(String(10))
    COD_ITEM = Column(String(60))
    VL_AJ_ITEM = Column(String(30))
    CHV_DOCe = Column(String(255))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiE115(Base):
    __tablename__ = 'sped_icms_ipi_E115'

    ID_REG_E115 = Column(BIGINT(25), primary_key=True)
    ID_REG_E110 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    COD_INF_ADIC = Column(String(8))
    VL_INF_ADIC = Column(String(30))
    DESCR_COMPL_AJ = Column(String(255))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiE116(Base):
    __tablename__ = 'sped_icms_ipi_E116'

    ID_REG_E116 = Column(BIGINT(25), primary_key=True)
    ID_REG_E110 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    COD_OR = Column(String(3))
    VL_OR = Column(String(30))
    DT_VCTO = Column(String(10))
    COD_REC = Column(String(255))
    NUM_PROC = Column(String(15))
    IND_PROC = Column(String(1))
    PROCESS = Column(String(255))
    TXT_COMPL = Column(String(255))
    MES_REF = Column(String(6))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiE200(Base):
    __tablename__ = 'sped_icms_ipi_E200'

    ID_REG_E200 = Column(BIGINT(25), primary_key=True)
    ID_REG_E001 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    UF = Column(String(2))
    DT_INI = Column(String(10))
    DT_FIN = Column(String(10))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiE210(Base):
    __tablename__ = 'sped_icms_ipi_E210'

    ID_REG_E210 = Column(BIGINT(25), primary_key=True)
    ID_REG_E200 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    IND_MOV_ST = Column(String(1))
    VL_SLD_CRED_ANT_ST = Column(String(30))
    VL_DEVOL_ST = Column(String(30))
    VL_RESSARC_ST = Column(String(30))
    VL_OUT_CRED_ST = Column(String(30))
    VL_AJ_CREDITOS_ST = Column(String(30))
    VL_RETENCAO_ST = Column(String(30))
    VL_OUT_DEB_ST = Column(String(30))
    VL_AJ_DEBITOS_ST = Column(String(30))
    VL_SLD_DEV_ANT_ST = Column(String(30))
    VL_DEDUCOES_ST = Column(String(30))
    VL_ICMS_RECOL_ST = Column(String(30))
    VL_SLD_CRED_ST_TRANSPORTAR = Column(String(30))
    DEB_ESP_ST = Column(String(30))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiE220(Base):
    __tablename__ = 'sped_icms_ipi_E220'

    ID_REG_E220 = Column(BIGINT(25), primary_key=True)
    ID_REG_E210 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    COD_AJ_APUR = Column(String(8))
    DESCR_COMPL_AJ = Column(String(255))
    VL_AJ_APUR = Column(String(30))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiE230(Base):
    __tablename__ = 'sped_icms_ipi_E230'

    ID_REG_E230 = Column(BIGINT(25), primary_key=True)
    ID_REG_E220 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    NUM_DA = Column(String(255))
    NUM_PROC = Column(String(15))
    IND_PROC = Column(String(1))
    PROCESS = Column(String(255))
    TXT_COMPL = Column(String(255))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiE240(Base):
    __tablename__ = 'sped_icms_ipi_E240'

    ID_REG_E240 = Column(BIGINT(25), primary_key=True)
    ID_REG_E220 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    COD_PART = Column(String(60))
    COD_MOD = Column(String(2))
    SER = Column(String(4))
    SUB = Column(String(3))
    NUM_DOC = Column(String(9))
    DT_DOC = Column(String(10))
    COD_ITEM = Column(String(60))
    VL_AJ_ITEM = Column(String(30))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiE250(Base):
    __tablename__ = 'sped_icms_ipi_E250'

    ID_REG_E250 = Column(BIGINT(25), primary_key=True)
    ID_REG_E210 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    COD_OR = Column(String(3))
    VL_OR = Column(String(30))
    DT_VCTO = Column(String(10))
    COD_REC = Column(String(255))
    NUM_PROC = Column(String(15))
    IND_PROC = Column(String(1))
    PROCESS = Column(String(255))
    TXT_COMPL = Column(String(255))
    MES_REF = Column(String(6))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiE300(Base):
    __tablename__ = 'sped_icms_ipi_E300'

    ID_REG_E300 = Column(BIGINT(25), primary_key=True)
    ID_REG_E001 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    UF = Column(String(2))
    DT_INI = Column(String(10))
    DT_FIN = Column(String(10))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiE310012017(Base):
    __tablename__ = 'sped_icms_ipi_E310_01_2017'

    ID_REG_E310 = Column(BIGINT(25), primary_key=True, nullable=False)
    ID_REG_E300 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    IND_MOV_FCP_DIFAL = Column(String(1))
    VL_SLD_CRED_ANT_DIFAL = Column(String(30), primary_key=True, nullable=False)
    VL_TOT_DEBITOS_DIFAL = Column(String(255))
    VL_OUT_DEB_DIFAL = Column(String(255))
    VL_TOT_CREDITOS_DIFAL = Column(String(255))
    VL_OUT_CRED_DIFAL = Column(String(255))
    VL_SLD_DEV_ANT_DIFAL = Column(String(255))
    VL_DEDUÇÕES_DIFAL = Column(String(255))
    VL_RECOL_DIFAL = Column(String(255))
    VL_SLD_CRED_TRANSPORTAR_DIFAL = Column(String(255))
    DEB_ESP_DIFAL = Column(String(255))
    VL_SLD_CRED_ANT_FCP = Column(String(255))
    VL_TOT_DEB_FCP = Column(String(255))
    VL_OUT_DEB_FCP = Column(String(255))
    VL_TOT_CRED_FCP = Column(String(255))
    VL_OUT_CRED_FCP = Column(String(255))
    VL_SLD_DEV_ANT_FCP = Column(String(255))
    VL_DEDUÇÕES_FCP = Column(String(255))
    VL_RECOL_FCP = Column(String(255))
    VL_SLD_CRED_TRANSPORTAR_FCP = Column(String(255))
    DEB_ESP_FCP = Column(String(255))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiE310122016(Base):
    __tablename__ = 'sped_icms_ipi_E310_12_2016'

    ID_REG_E310 = Column(BIGINT(25), primary_key=True)
    ID_REG_E300 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    IND_MOV_DIFAL = Column(String(1))
    VL_SLD_CRED_ANT_DIFAL = Column(String(30))
    VL_TOT_DEBITOS_DIFAL = Column(String(30))
    VL_OUT_DEB_DIFAL = Column(String(30))
    VL_TOT_DEB_FCP = Column(String(30))
    VL_TOT_CREDITOS_DIFAL = Column(String(30))
    VL_TOT_CRED_FCP = Column(String(30))
    VL_OUT_CRED_DIFAL = Column(String(30))
    VL_SLD_DEV_ANT_DIFAL = Column(String(30))
    VL_DEDUCOES_DIFAL = Column(String(30))
    VL_RECOL = Column(String(30))
    VL_SLD_CRED_TRANSPORTAR = Column(String(30))
    DEB_ESP_DIFAL = Column(String(30))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiE311(Base):
    __tablename__ = 'sped_icms_ipi_E311'

    ID_REG_E311 = Column(BIGINT(25), primary_key=True)
    ID_REG_E310 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    COD_AJ_APUR = Column(String(8))
    DESCR_COMPL_AJ = Column(String(255))
    VL_AJ_APUR = Column(String(30))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiE312(Base):
    __tablename__ = 'sped_icms_ipi_E312'

    ID_REG_E312 = Column(BIGINT(25), primary_key=True)
    ID_REG_E311 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    NUM_DA = Column(String(255))
    NUM_PROC = Column(String(15))
    IND_PROC = Column(String(1))
    PROCESS = Column(String(255))
    TXT_COMPL = Column(String(255))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiE313(Base):
    __tablename__ = 'sped_icms_ipi_E313'

    ID_REG_E313 = Column(BIGINT(25), primary_key=True)
    ID_REG_E311 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    COD_PART = Column(String(60))
    COD_MOD = Column(String(2))
    SER = Column(String(4))
    SUB = Column(String(3))
    NUM_DOC = Column(String(9))
    CHV_DOCE = Column(String(44))
    DT_DOC = Column(String(10))
    COD_ITEM = Column(String(60))
    VL_AJ_ITEM = Column(String(30))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiE316(Base):
    __tablename__ = 'sped_icms_ipi_E316'

    ID_REG_E316 = Column(BIGINT(25), primary_key=True)
    ID_REG_E310 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    COD_OR = Column(String(3))
    VL_OR = Column(String(30))
    DT_VCTO = Column(String(10))
    COD_REC = Column(String(255))
    NUM_PROC = Column(String(15))
    IND_PROC = Column(String(1))
    PROCESS = Column(String(255))
    TXT_COMPL = Column(String(255))
    MES_REF = Column(String(6))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiE500(Base):
    __tablename__ = 'sped_icms_ipi_E500'

    ID_REG_E500 = Column(BIGINT(25), primary_key=True)
    ID_REG_E001 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    IND_APUR = Column(String(1))
    DT_INI = Column(String(10))
    DT_FIN = Column(String(10))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiE510(Base):
    __tablename__ = 'sped_icms_ipi_E510'

    ID_REG_E510 = Column(BIGINT(25), primary_key=True)
    ID_REG_E500 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    CFOP = Column(String(4))
    CST_IPI = Column(String(2))
    VL_CONT_IPI = Column(String(30))
    VL_BC_IPI = Column(String(30))
    VL_IPI = Column(String(30))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiE520(Base):
    __tablename__ = 'sped_icms_ipi_E520'

    ID_REG_E520 = Column(BIGINT(25), primary_key=True)
    ID_REG_E500 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    VL_SD_ANT_IPI = Column(String(30))
    VL_DEB_IPI = Column(String(30))
    VL_CRED_IPI = Column(String(30))
    VL_OD_IPI = Column(String(30))
    VL_OC_IPI = Column(String(30))
    VL_SC_IPI = Column(String(30))
    VL_SD_IPI = Column(String(30))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiE530(Base):
    __tablename__ = 'sped_icms_ipi_E530'

    ID_REG_E530 = Column(BIGINT(25), primary_key=True)
    ID_REG_E520 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    IND_AJ = Column(String(1))
    VL_AJ = Column(String(30))
    COD_AJ = Column(String(3))
    IND_DOC = Column(String(1))
    NUM_DOC = Column(String(255))
    DESCR_AJ = Column(String(255))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiE990(Base):
    __tablename__ = 'sped_icms_ipi_E990'

    ID_REG_E990 = Column(BIGINT(25), primary_key=True)
    ID_REG_0000 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    QTD_LIN_E = Column(String(255))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiG001(Base):
    __tablename__ = 'sped_icms_ipi_G001'

    ID_REG_G001 = Column(BIGINT(25), primary_key=True)
    ID_REG_0000 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    IND_MOV = Column(String(1))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiG110(Base):
    __tablename__ = 'sped_icms_ipi_G110'

    ID_REG_G110 = Column(BIGINT(25), primary_key=True)
    ID_REG_G001 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    DT_INI = Column(String(10))
    DT_FIN = Column(String(10))
    SALDO_IN_ICMS = Column(String(30))
    SOM_PARC = Column(String(30))
    VL_TRIB_EXP = Column(String(30))
    VL_TOTAL = Column(String(30))
    IND_PER_SAI = Column(String(30))
    ICMS_APROP = Column(String(30))
    SOM_ICMS_OC = Column(String(30))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiG125(Base):
    __tablename__ = 'sped_icms_ipi_G125'

    ID_REG_G125 = Column(BIGINT(25), primary_key=True)
    ID_REG_G110 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    COD_IND_BEM = Column(String(60))
    DT_MOV = Column(String(10))
    TIPO_MOV = Column(String(2))
    VL_IMOB_ICMS_OP = Column(String(30))
    VL_IMOB_ICMS_ST = Column(String(30))
    VL_IMOB_ICMS_FRT = Column(String(30))
    VL_IMOB_ICMS_DIF = Column(String(30))
    NUM_PARC = Column(String(3))
    VL_PARC_PASS = Column(String(30))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiG126(Base):
    __tablename__ = 'sped_icms_ipi_G126'

    ID_REG_G126 = Column(BIGINT(25), primary_key=True)
    ID_REG_G125 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    DT_INI = Column(String(10))
    DT_FIN = Column(String(10))
    NUM_PARC = Column(String(3))
    VL_PARC_PASS = Column(String(30))
    VL_TRIB_OC = Column(String(30))
    VL_TOTAL = Column(String(30))
    IND_PER_SAI = Column(String(30))
    VL_PARC_APROP = Column(String(30))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiG130(Base):
    __tablename__ = 'sped_icms_ipi_G130'

    ID_REG_G130 = Column(BIGINT(25), primary_key=True)
    ID_REG_G125 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    IND_EMIT = Column(String(1))
    COD_PART = Column(String(60))
    COD_MOD = Column(String(2))
    SERIE = Column(String(3))
    NUM_DOC = Column(String(9))
    CHV_NFE_CTE = Column(String(44))
    DT_DOC = Column(String(10))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiG140(Base):
    __tablename__ = 'sped_icms_ipi_G140'

    ID_REG_G140 = Column(BIGINT(25), primary_key=True)
    ID_REG_G130 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    NUM_ITEM = Column(String(3))
    COD_ITEM = Column(String(60))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiG990(Base):
    __tablename__ = 'sped_icms_ipi_G990'

    ID_REG_G990 = Column(BIGINT(25), primary_key=True)
    ID_REG_0000 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    QTD_LIN_G = Column(String(255))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiH001(Base):
    __tablename__ = 'sped_icms_ipi_H001'

    ID_REG_H001 = Column(BIGINT(25), primary_key=True)
    ID_REG_0000 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    IND_MOV = Column(String(1))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiH005(Base):
    __tablename__ = 'sped_icms_ipi_H005'

    ID_REG_H005 = Column(BIGINT(25), primary_key=True)
    ID_REG_H001 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    DT_INV = Column(String(10))
    VL_INV = Column(String(30))
    MOT_INV = Column(String(2))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiH010(Base):
    __tablename__ = 'sped_icms_ipi_H010'

    ID_REG_H010 = Column(BIGINT(25), primary_key=True)
    ID_REG_H005 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    COD_ITEM = Column(String(60))
    UNID_ = Column(String(6))
    QTD = Column(String(30))
    VL_UNIT = Column(String(30))
    VL_ITEM = Column(String(30))
    IND_PROP = Column(String(1))
    COD_PART = Column(String(60))
    TXT_COMPL = Column(String(255))
    COD_CTA = Column(String(255))
    VL_ITEM_IR = Column(String(30))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiH020(Base):
    __tablename__ = 'sped_icms_ipi_H020'

    ID_REG_H020 = Column(BIGINT(25), primary_key=True)
    ID_REG_H010 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    CST_ICMS = Column(String(3))
    BL_ICMS = Column(String(30))
    VL_ICMS = Column(String(30))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiH990(Base):
    __tablename__ = 'sped_icms_ipi_H990'

    ID_REG_H990 = Column(BIGINT(25), primary_key=True)
    ID_REG_0000 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    QTD_LIN_H = Column(String(255))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiK001(Base):
    __tablename__ = 'sped_icms_ipi_K001'

    ID_REG_K001 = Column(BIGINT(25), primary_key=True)
    ID_REG_0000 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    IND_MOV = Column(String(1))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiK100(Base):
    __tablename__ = 'sped_icms_ipi_K100'

    ID_REG_K100 = Column(BIGINT(25), primary_key=True)
    ID_REG_K001 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    DT_INI = Column(String(10))
    DT_FIN = Column(String(10))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiK200(Base):
    __tablename__ = 'sped_icms_ipi_K200'

    ID_REG_K200 = Column(BIGINT(25), primary_key=True)
    ID_REG_K100 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    DT_EST = Column(String(10))
    COD_ITEM = Column(String(60))
    QTD = Column(String(30))
    IND_EST = Column(String(1))
    COD_PART = Column(String(60))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiK220(Base):
    __tablename__ = 'sped_icms_ipi_K220'

    ID_REG_K220 = Column(BIGINT(25), primary_key=True)
    ID_REG_K100 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    DT_MOV = Column(String(10))
    COD_ITEM_ORI = Column(String(60))
    COD_ITEM_DEST = Column(String(60))
    QTD = Column(String(30))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiK230(Base):
    __tablename__ = 'sped_icms_ipi_K230'

    ID_REG_K230 = Column(BIGINT(25), primary_key=True)
    ID_REG_K100 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    DT_INI_OP = Column(String(10))
    DT_FIN_OP = Column(String(10))
    COD_DOC_OP = Column(String(30))
    COD_ITEM = Column(String(60))
    QTD_ENC = Column(String(30))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiK235(Base):
    __tablename__ = 'sped_icms_ipi_K235'

    ID_REG_K235 = Column(BIGINT(25), primary_key=True)
    ID_REG_K230 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    DT_SAIDA = Column(String(10))
    COD_ITEM = Column(String(60))
    QTD = Column(String(30))
    COD_INS_SUBST = Column(String(255))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiK250(Base):
    __tablename__ = 'sped_icms_ipi_K250'

    ID_REG_K250 = Column(BIGINT(25), primary_key=True)
    ID_REG_K100 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    DT_PROD = Column(String(10))
    COD_ITEM = Column(String(60))
    QTD = Column(String(30))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiK255(Base):
    __tablename__ = 'sped_icms_ipi_K255'

    ID_REG_K255 = Column(BIGINT(25), primary_key=True)
    ID_REG_K250 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    DT_CONS = Column(String(10))
    COD_ITEM = Column(String(60))
    QTD = Column(String(30))
    COD_INS_SUBST = Column(String(60))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiK990(Base):
    __tablename__ = 'sped_icms_ipi_K990'

    ID_REG_K990 = Column(BIGINT(25), primary_key=True)
    ID_REG_0000 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    QTD_LIN_K = Column(String(255))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedIcmsIpiCtrl(Base):
    __tablename__ = 'sped_icms_ipi_ctrl'
    __table_args__ = (
        Index('IDX_CANCELAMENTO', 'DATA_INI', 'DATA_FIM', 'CNPJ'),
    )

    ID = Column(INTEGER(11), primary_key=True)
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11), index=True)
    DATA_INI = Column(Date)
    DATA_FIM = Column(Date)
    CNPJ = Column(CHAR(14))
    DATA_HORA = Column(DateTime)
    TIPO = Column(String(20))
    ENVIO = Column(INTEGER(1))
    CANCELADO = Column(INTEGER(1))
    RAZAO_SOCIAL = Column(String(255))
    UF = Column(CHAR(2))
    RETIFICADOR = Column(INTEGER(1))
    NOME_ARQUIVO = Column(String(255))
    DW_ENTRADAS = Column(INTEGER(1))
    DW_SAIDAS = Column(INTEGER(1))
    DW_NTOMADOS = Column(INTEGER(1))
    DW_TOMADOS = Column(INTEGER(1))


class SpedPisCofins0000(Base):
    __tablename__ = 'sped_pis_cofins_0000'

    ID_REG_0000 = Column(BIGINT(25), primary_key=True)
    ID_LOTES_ARQUIVOS = Column(INTEGER(20))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(BIGINT(25))
    COD_VER = Column(String(3))
    TIPO_ESCRIT = Column(String(1))
    IND_SIT_ESP = Column(String(1))
    NUM_REC_ANTERIOR = Column(String(41))
    DT_INI = Column(String(100))
    DT_FIN = Column(String(100))
    NOME = Column(String(100))
    CNPJ = Column(String(14))
    UF = Column(String(2))
    COD_MUN = Column(String(7))
    SUFRAMA = Column(String(9))
    IND_NAT_PJ = Column(String(2))
    IND_ATIV = Column(String(1))


class SpedPisCofins0001(Base):
    __tablename__ = 'sped_pis_cofins_0001'

    ID_REG_0001 = Column(BIGINT(25), primary_key=True)
    ID_REG_0000 = Column(BIGINT(25), index=True)
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    IND_MOV = Column(String(1))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofins0035(Base):
    __tablename__ = 'sped_pis_cofins_0035'

    ID_REG_0035 = Column(BIGINT(25), primary_key=True)
    ID_REG_0001 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    COD_SCP = Column(String(14))
    NOME_SCP = Column(String(255))
    INF_COMP = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofins0100(Base):
    __tablename__ = 'sped_pis_cofins_0100'

    ID_REG_0100 = Column(BIGINT(25), primary_key=True)
    ID_REG_0001 = Column(BIGINT(25), nullable=False)
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    NOME = Column(String(100))
    CPF = Column(String(11))
    CRC = Column(String(15))
    CNPJ = Column(String(14))
    CEP = Column(String(8))
    ENDER = Column(String(60))
    NUM = Column(String(255))
    COMPL = Column(String(60))
    BAIRRO = Column(String(60))
    FONE = Column(String(11))
    FAX = Column(String(11))
    EMAIL = Column(String(255))
    COD_MUN = Column(String(7))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofins0110(Base):
    __tablename__ = 'sped_pis_cofins_0110'

    ID_REG_0110 = Column(BIGINT(25), primary_key=True)
    ID_REG_0001 = Column(BIGINT(25), nullable=False)
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    COD_INC_TRIB = Column(String(1))
    IND_APRO_CRED = Column(String(1))
    COD_TIPO_CONT = Column(String(1))
    IND_EFD_REG_CUM = Column(String(1))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofins0111(Base):
    __tablename__ = 'sped_pis_cofins_0111'

    ID_REG_0111 = Column(BIGINT(25), primary_key=True)
    ID_REG_0110 = Column(BIGINT(25), nullable=False)
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    REC_BRU_NCUM_TRIB_MI = Column(String(255))
    REC_BRU_NCUM_NT_MI = Column(String(255))
    REC_BRU_NCUM_EXP = Column(String(255))
    REC_BRU_CUM = Column(String(255))
    REC_BRU_TOTAL = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofins0120(Base):
    __tablename__ = 'sped_pis_cofins_0120'

    ID_REG_0120 = Column(BIGINT(25), primary_key=True)
    ID_REG_0001 = Column(BIGINT(25), nullable=False)
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    MES_DISPENSA = Column(String(6))
    INF_COMP = Column(String(90))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofins0140(Base):
    __tablename__ = 'sped_pis_cofins_0140'

    ID_REG_0140 = Column(BIGINT(25), primary_key=True)
    ID_REG_0001 = Column(BIGINT(25), nullable=False)
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    COD_EST = Column(String(60))
    NOME = Column(String(100))
    CNPJ = Column(String(14))
    UF = Column(String(2))
    IE = Column(String(14))
    COD_MUN = Column(String(7))
    IM = Column(String(255))
    SUFRAMA = Column(String(9))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofins0145(Base):
    __tablename__ = 'sped_pis_cofins_0145'

    ID_REG_0145 = Column(BIGINT(25), primary_key=True)
    ID_REG_0140 = Column(BIGINT(25), nullable=False)
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    COD_INC_TRIB = Column(String(1))
    VL_REC_TOT = Column(String(255))
    VL_REC_ATIV = Column(String(255))
    VL_REC_DEMAIS_ATIV = Column(String(255))
    INFO_COMPL = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofins0150(Base):
    __tablename__ = 'sped_pis_cofins_0150'
    __table_args__ = (
        Index('IDX_DUPLO', 'COD_PART', 'ID_EFD_CTRL_REG_0000'),
    )

    ID_REG_0150 = Column(BIGINT(25), primary_key=True)
    ID_REG_0140 = Column(BIGINT(25), nullable=False)
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    COD_PART = Column(String(60))
    NOME = Column(String(100))
    COD_PAIS = Column(String(5))
    CNPJ = Column(String(14))
    CPF = Column(String(11))
    IE = Column(String(14))
    COD_MUN = Column(String(7))
    SUFRAMA = Column(String(9))
    ENDER = Column(String(60))
    NUM = Column(String(255))
    COMPL = Column(String(60))
    BAIRRO = Column(String(60))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))
    CNPJ_FILIAL = Column(String(40))


t_sped_pis_cofins_0150_ID_1000 = Table(
    'sped_pis_cofins_0150_ID_1000', metadata,
    Column('COD_PART', String(60), index=True),
    Column('NOME', String(100)),
    Column('COD_PAIS', String(5)),
    Column('CNPJ', String(14), index=True),
    Column('CPF', String(11), index=True),
    Column('COD_MUN', String(7)),
    Column('ID_EFD_CTRL_REG_0000', INTEGER(11))
)


t_sped_pis_cofins_0150_ID_1001 = Table(
    'sped_pis_cofins_0150_ID_1001', metadata,
    Column('COD_PART', String(60), index=True),
    Column('NOME', String(100)),
    Column('COD_PAIS', String(5)),
    Column('CNPJ', String(14), index=True),
    Column('CPF', String(11), index=True),
    Column('COD_MUN', String(7)),
    Column('ID_EFD_CTRL_REG_0000', INTEGER(11))
)


t_sped_pis_cofins_0150_ID_1002 = Table(
    'sped_pis_cofins_0150_ID_1002', metadata,
    Column('COD_PART', String(60), index=True),
    Column('NOME', String(100)),
    Column('COD_PAIS', String(5)),
    Column('CNPJ', String(14), index=True),
    Column('CPF', String(11), index=True),
    Column('COD_MUN', String(7)),
    Column('ID_EFD_CTRL_REG_0000', INTEGER(11))
)


t_sped_pis_cofins_0150_ID_1003 = Table(
    'sped_pis_cofins_0150_ID_1003', metadata,
    Column('COD_PART', String(60), index=True),
    Column('NOME', String(100)),
    Column('COD_PAIS', String(5)),
    Column('CNPJ', String(14), index=True),
    Column('CPF', String(11), index=True),
    Column('COD_MUN', String(7)),
    Column('ID_EFD_CTRL_REG_0000', INTEGER(11))
)


t_sped_pis_cofins_0150_ID_1004 = Table(
    'sped_pis_cofins_0150_ID_1004', metadata,
    Column('COD_PART', String(60), index=True),
    Column('NOME', String(100)),
    Column('COD_PAIS', String(5)),
    Column('CNPJ', String(14), index=True),
    Column('CPF', String(11), index=True),
    Column('COD_MUN', String(7)),
    Column('ID_EFD_CTRL_REG_0000', INTEGER(11))
)


t_sped_pis_cofins_0150_ID_1005 = Table(
    'sped_pis_cofins_0150_ID_1005', metadata,
    Column('COD_PART', String(60), index=True),
    Column('NOME', String(100)),
    Column('COD_PAIS', String(5)),
    Column('CNPJ', String(14), index=True),
    Column('CPF', String(11), index=True),
    Column('COD_MUN', String(7)),
    Column('ID_EFD_CTRL_REG_0000', INTEGER(11))
)


t_sped_pis_cofins_0150_ID_1006 = Table(
    'sped_pis_cofins_0150_ID_1006', metadata,
    Column('COD_PART', String(60), index=True),
    Column('NOME', String(100)),
    Column('COD_PAIS', String(5)),
    Column('CNPJ', String(14), index=True),
    Column('CPF', String(11), index=True),
    Column('COD_MUN', String(7)),
    Column('ID_EFD_CTRL_REG_0000', INTEGER(11))
)


t_sped_pis_cofins_0150_ID_1007 = Table(
    'sped_pis_cofins_0150_ID_1007', metadata,
    Column('COD_PART', String(60), index=True),
    Column('NOME', String(100)),
    Column('COD_PAIS', String(5)),
    Column('CNPJ', String(14), index=True),
    Column('CPF', String(11), index=True),
    Column('COD_MUN', String(7)),
    Column('ID_EFD_CTRL_REG_0000', INTEGER(11))
)


t_sped_pis_cofins_0150_ID_1008 = Table(
    'sped_pis_cofins_0150_ID_1008', metadata,
    Column('COD_PART', String(60), index=True),
    Column('NOME', String(100)),
    Column('COD_PAIS', String(5)),
    Column('CNPJ', String(14), index=True),
    Column('CPF', String(11), index=True),
    Column('COD_MUN', String(7)),
    Column('ID_EFD_CTRL_REG_0000', INTEGER(11))
)


t_sped_pis_cofins_0150_ID_1009 = Table(
    'sped_pis_cofins_0150_ID_1009', metadata,
    Column('COD_PART', String(60), index=True),
    Column('NOME', String(100)),
    Column('COD_PAIS', String(5)),
    Column('CNPJ', String(14), index=True),
    Column('CPF', String(11), index=True),
    Column('COD_MUN', String(7)),
    Column('ID_EFD_CTRL_REG_0000', INTEGER(11))
)


t_sped_pis_cofins_0150_ID_1010 = Table(
    'sped_pis_cofins_0150_ID_1010', metadata,
    Column('COD_PART', String(60), index=True),
    Column('NOME', String(100)),
    Column('COD_PAIS', String(5)),
    Column('CNPJ', String(14), index=True),
    Column('CPF', String(11), index=True),
    Column('COD_MUN', String(7)),
    Column('ID_EFD_CTRL_REG_0000', INTEGER(11))
)


t_sped_pis_cofins_0150_ID_1011 = Table(
    'sped_pis_cofins_0150_ID_1011', metadata,
    Column('COD_PART', String(60), index=True),
    Column('NOME', String(100)),
    Column('COD_PAIS', String(5)),
    Column('CNPJ', String(14), index=True),
    Column('CPF', String(11), index=True),
    Column('COD_MUN', String(7)),
    Column('ID_EFD_CTRL_REG_0000', INTEGER(11))
)


t_sped_pis_cofins_0150_ID_1012 = Table(
    'sped_pis_cofins_0150_ID_1012', metadata,
    Column('COD_PART', String(60), index=True),
    Column('NOME', String(100)),
    Column('COD_PAIS', String(5)),
    Column('CNPJ', String(14), index=True),
    Column('CPF', String(11), index=True),
    Column('COD_MUN', String(7)),
    Column('ID_EFD_CTRL_REG_0000', INTEGER(11))
)


t_sped_pis_cofins_0150_ID_1013 = Table(
    'sped_pis_cofins_0150_ID_1013', metadata,
    Column('COD_PART', String(60), index=True),
    Column('NOME', String(100)),
    Column('COD_PAIS', String(5)),
    Column('CNPJ', String(14), index=True),
    Column('CPF', String(11), index=True),
    Column('COD_MUN', String(7)),
    Column('ID_EFD_CTRL_REG_0000', INTEGER(11))
)


t_sped_pis_cofins_0150_ID_1014 = Table(
    'sped_pis_cofins_0150_ID_1014', metadata,
    Column('COD_PART', String(60), index=True),
    Column('NOME', String(100)),
    Column('COD_PAIS', String(5)),
    Column('CNPJ', String(14), index=True),
    Column('CPF', String(11), index=True),
    Column('COD_MUN', String(7)),
    Column('ID_EFD_CTRL_REG_0000', INTEGER(11))
)


t_sped_pis_cofins_0150_ID_1015 = Table(
    'sped_pis_cofins_0150_ID_1015', metadata,
    Column('COD_PART', String(60), index=True),
    Column('NOME', String(100)),
    Column('COD_PAIS', String(5)),
    Column('CNPJ', String(14), index=True),
    Column('CPF', String(11), index=True),
    Column('COD_MUN', String(7)),
    Column('ID_EFD_CTRL_REG_0000', INTEGER(11))
)


t_sped_pis_cofins_0150_ID_1016 = Table(
    'sped_pis_cofins_0150_ID_1016', metadata,
    Column('COD_PART', String(60), index=True),
    Column('NOME', String(100)),
    Column('COD_PAIS', String(5)),
    Column('CNPJ', String(14), index=True),
    Column('CPF', String(11), index=True),
    Column('COD_MUN', String(7)),
    Column('ID_EFD_CTRL_REG_0000', INTEGER(11))
)


t_sped_pis_cofins_0150_ID_1017 = Table(
    'sped_pis_cofins_0150_ID_1017', metadata,
    Column('COD_PART', String(60), index=True),
    Column('NOME', String(100)),
    Column('COD_PAIS', String(5)),
    Column('CNPJ', String(14), index=True),
    Column('CPF', String(11), index=True),
    Column('COD_MUN', String(7)),
    Column('ID_EFD_CTRL_REG_0000', INTEGER(11))
)


t_sped_pis_cofins_0150_ID_1018 = Table(
    'sped_pis_cofins_0150_ID_1018', metadata,
    Column('COD_PART', String(60), index=True),
    Column('NOME', String(100)),
    Column('COD_PAIS', String(5)),
    Column('CNPJ', String(14), index=True),
    Column('CPF', String(11), index=True),
    Column('COD_MUN', String(7)),
    Column('ID_EFD_CTRL_REG_0000', INTEGER(11))
)


t_sped_pis_cofins_0150_ID_1019 = Table(
    'sped_pis_cofins_0150_ID_1019', metadata,
    Column('COD_PART', String(60), index=True),
    Column('NOME', String(100)),
    Column('COD_PAIS', String(5)),
    Column('CNPJ', String(14), index=True),
    Column('CPF', String(11), index=True),
    Column('COD_MUN', String(7)),
    Column('ID_EFD_CTRL_REG_0000', INTEGER(11))
)


t_sped_pis_cofins_0150_ID_1020 = Table(
    'sped_pis_cofins_0150_ID_1020', metadata,
    Column('COD_PART', String(60), index=True),
    Column('NOME', String(100)),
    Column('COD_PAIS', String(5)),
    Column('CNPJ', String(14), index=True),
    Column('CPF', String(11), index=True),
    Column('COD_MUN', String(7)),
    Column('ID_EFD_CTRL_REG_0000', INTEGER(11))
)


t_sped_pis_cofins_0150_ID_1021 = Table(
    'sped_pis_cofins_0150_ID_1021', metadata,
    Column('COD_PART', String(60), index=True),
    Column('NOME', String(100)),
    Column('COD_PAIS', String(5)),
    Column('CNPJ', String(14), index=True),
    Column('CPF', String(11), index=True),
    Column('COD_MUN', String(7)),
    Column('ID_EFD_CTRL_REG_0000', INTEGER(11))
)


t_sped_pis_cofins_0150_ID_1022 = Table(
    'sped_pis_cofins_0150_ID_1022', metadata,
    Column('COD_PART', String(60), index=True),
    Column('NOME', String(100)),
    Column('COD_PAIS', String(5)),
    Column('CNPJ', String(14), index=True),
    Column('CPF', String(11), index=True),
    Column('COD_MUN', String(7)),
    Column('ID_EFD_CTRL_REG_0000', INTEGER(11))
)


t_sped_pis_cofins_0150_ID_1023 = Table(
    'sped_pis_cofins_0150_ID_1023', metadata,
    Column('COD_PART', String(60), index=True),
    Column('NOME', String(100)),
    Column('COD_PAIS', String(5)),
    Column('CNPJ', String(14), index=True),
    Column('CPF', String(11), index=True),
    Column('COD_MUN', String(7)),
    Column('ID_EFD_CTRL_REG_0000', INTEGER(11))
)


t_sped_pis_cofins_0150_ID_1024 = Table(
    'sped_pis_cofins_0150_ID_1024', metadata,
    Column('COD_PART', String(60), index=True),
    Column('NOME', String(100)),
    Column('COD_PAIS', String(5)),
    Column('CNPJ', String(14), index=True),
    Column('CPF', String(11), index=True),
    Column('COD_MUN', String(7)),
    Column('ID_EFD_CTRL_REG_0000', INTEGER(11))
)


t_sped_pis_cofins_0150_ID_1025 = Table(
    'sped_pis_cofins_0150_ID_1025', metadata,
    Column('COD_PART', String(60), index=True),
    Column('NOME', String(100)),
    Column('COD_PAIS', String(5)),
    Column('CNPJ', String(14), index=True),
    Column('CPF', String(11), index=True),
    Column('COD_MUN', String(7)),
    Column('ID_EFD_CTRL_REG_0000', INTEGER(11))
)


t_sped_pis_cofins_0150_ID_1026 = Table(
    'sped_pis_cofins_0150_ID_1026', metadata,
    Column('COD_PART', String(60), index=True),
    Column('NOME', String(100)),
    Column('COD_PAIS', String(5)),
    Column('CNPJ', String(14), index=True),
    Column('CPF', String(11), index=True),
    Column('COD_MUN', String(7)),
    Column('ID_EFD_CTRL_REG_0000', INTEGER(11))
)


t_sped_pis_cofins_0150_ID_1027 = Table(
    'sped_pis_cofins_0150_ID_1027', metadata,
    Column('COD_PART', String(60), index=True),
    Column('NOME', String(100)),
    Column('COD_PAIS', String(5)),
    Column('CNPJ', String(14), index=True),
    Column('CPF', String(11), index=True),
    Column('COD_MUN', String(7)),
    Column('ID_EFD_CTRL_REG_0000', INTEGER(11))
)


t_sped_pis_cofins_0150_ID_1028 = Table(
    'sped_pis_cofins_0150_ID_1028', metadata,
    Column('COD_PART', String(60), index=True),
    Column('NOME', String(100)),
    Column('COD_PAIS', String(5)),
    Column('CNPJ', String(14), index=True),
    Column('CPF', String(11), index=True),
    Column('COD_MUN', String(7)),
    Column('ID_EFD_CTRL_REG_0000', INTEGER(11))
)


t_sped_pis_cofins_0150_ID_1029 = Table(
    'sped_pis_cofins_0150_ID_1029', metadata,
    Column('COD_PART', String(60), index=True),
    Column('NOME', String(100)),
    Column('COD_PAIS', String(5)),
    Column('CNPJ', String(14), index=True),
    Column('CPF', String(11), index=True),
    Column('COD_MUN', String(7)),
    Column('ID_EFD_CTRL_REG_0000', INTEGER(11))
)


t_sped_pis_cofins_0150_ID_1030 = Table(
    'sped_pis_cofins_0150_ID_1030', metadata,
    Column('COD_PART', String(60), index=True),
    Column('NOME', String(100)),
    Column('COD_PAIS', String(5)),
    Column('CNPJ', String(14), index=True),
    Column('CPF', String(11), index=True),
    Column('COD_MUN', String(7)),
    Column('ID_EFD_CTRL_REG_0000', INTEGER(11))
)


t_sped_pis_cofins_0150_ID_1031 = Table(
    'sped_pis_cofins_0150_ID_1031', metadata,
    Column('COD_PART', String(60), index=True),
    Column('NOME', String(100)),
    Column('COD_PAIS', String(5)),
    Column('CNPJ', String(14), index=True),
    Column('CPF', String(11), index=True),
    Column('COD_MUN', String(7)),
    Column('ID_EFD_CTRL_REG_0000', INTEGER(11))
)


t_sped_pis_cofins_0150_ID_1032 = Table(
    'sped_pis_cofins_0150_ID_1032', metadata,
    Column('COD_PART', String(60), index=True),
    Column('NOME', String(100)),
    Column('COD_PAIS', String(5)),
    Column('CNPJ', String(14), index=True),
    Column('CPF', String(11), index=True),
    Column('COD_MUN', String(7)),
    Column('ID_EFD_CTRL_REG_0000', INTEGER(11))
)


t_sped_pis_cofins_0150_ID_1033 = Table(
    'sped_pis_cofins_0150_ID_1033', metadata,
    Column('COD_PART', String(60), index=True),
    Column('NOME', String(100)),
    Column('COD_PAIS', String(5)),
    Column('CNPJ', String(14), index=True),
    Column('CPF', String(11), index=True),
    Column('COD_MUN', String(7)),
    Column('ID_EFD_CTRL_REG_0000', INTEGER(11))
)


t_sped_pis_cofins_0150_ID_1034 = Table(
    'sped_pis_cofins_0150_ID_1034', metadata,
    Column('COD_PART', String(60), index=True),
    Column('NOME', String(100)),
    Column('COD_PAIS', String(5)),
    Column('CNPJ', String(14), index=True),
    Column('CPF', String(11), index=True),
    Column('COD_MUN', String(7)),
    Column('ID_EFD_CTRL_REG_0000', INTEGER(11))
)


t_sped_pis_cofins_0150_ID_1035 = Table(
    'sped_pis_cofins_0150_ID_1035', metadata,
    Column('COD_PART', String(60), index=True),
    Column('NOME', String(100)),
    Column('COD_PAIS', String(5)),
    Column('CNPJ', String(14), index=True),
    Column('CPF', String(11), index=True),
    Column('COD_MUN', String(7)),
    Column('ID_EFD_CTRL_REG_0000', INTEGER(11))
)


t_sped_pis_cofins_0150_ID_1036 = Table(
    'sped_pis_cofins_0150_ID_1036', metadata,
    Column('COD_PART', String(60), index=True),
    Column('NOME', String(100)),
    Column('COD_PAIS', String(5)),
    Column('CNPJ', String(14), index=True),
    Column('CPF', String(11), index=True),
    Column('COD_MUN', String(7)),
    Column('ID_EFD_CTRL_REG_0000', INTEGER(11))
)


t_sped_pis_cofins_0150_ID_1037 = Table(
    'sped_pis_cofins_0150_ID_1037', metadata,
    Column('COD_PART', String(60), index=True),
    Column('NOME', String(100)),
    Column('COD_PAIS', String(5)),
    Column('CNPJ', String(14), index=True),
    Column('CPF', String(11), index=True),
    Column('COD_MUN', String(7)),
    Column('ID_EFD_CTRL_REG_0000', INTEGER(11))
)


t_sped_pis_cofins_0150_ID_1038 = Table(
    'sped_pis_cofins_0150_ID_1038', metadata,
    Column('COD_PART', String(60), index=True),
    Column('NOME', String(100)),
    Column('COD_PAIS', String(5)),
    Column('CNPJ', String(14), index=True),
    Column('CPF', String(11), index=True),
    Column('COD_MUN', String(7)),
    Column('ID_EFD_CTRL_REG_0000', INTEGER(11))
)


t_sped_pis_cofins_0150_ID_1039 = Table(
    'sped_pis_cofins_0150_ID_1039', metadata,
    Column('COD_PART', String(60), index=True),
    Column('NOME', String(100)),
    Column('COD_PAIS', String(5)),
    Column('CNPJ', String(14), index=True),
    Column('CPF', String(11), index=True),
    Column('COD_MUN', String(7)),
    Column('ID_EFD_CTRL_REG_0000', INTEGER(11))
)


t_sped_pis_cofins_0150_ID_1040 = Table(
    'sped_pis_cofins_0150_ID_1040', metadata,
    Column('COD_PART', String(60), index=True),
    Column('NOME', String(100)),
    Column('COD_PAIS', String(5)),
    Column('CNPJ', String(14), index=True),
    Column('CPF', String(11), index=True),
    Column('COD_MUN', String(7)),
    Column('ID_EFD_CTRL_REG_0000', INTEGER(11))
)


t_sped_pis_cofins_0150_ID_1041 = Table(
    'sped_pis_cofins_0150_ID_1041', metadata,
    Column('COD_PART', String(60), index=True),
    Column('NOME', String(100)),
    Column('COD_PAIS', String(5)),
    Column('CNPJ', String(14), index=True),
    Column('CPF', String(11), index=True),
    Column('COD_MUN', String(7)),
    Column('ID_EFD_CTRL_REG_0000', INTEGER(11))
)


t_sped_pis_cofins_0150_ID_1042 = Table(
    'sped_pis_cofins_0150_ID_1042', metadata,
    Column('COD_PART', String(60), index=True),
    Column('NOME', String(100)),
    Column('COD_PAIS', String(5)),
    Column('CNPJ', String(14), index=True),
    Column('CPF', String(11), index=True),
    Column('COD_MUN', String(7)),
    Column('ID_EFD_CTRL_REG_0000', INTEGER(11))
)


t_sped_pis_cofins_0150_ID_1043 = Table(
    'sped_pis_cofins_0150_ID_1043', metadata,
    Column('COD_PART', String(60), index=True),
    Column('NOME', String(100)),
    Column('COD_PAIS', String(5)),
    Column('CNPJ', String(14), index=True),
    Column('CPF', String(11), index=True),
    Column('COD_MUN', String(7)),
    Column('ID_EFD_CTRL_REG_0000', INTEGER(11))
)


t_sped_pis_cofins_0150_ID_1044 = Table(
    'sped_pis_cofins_0150_ID_1044', metadata,
    Column('COD_PART', String(60), index=True),
    Column('NOME', String(100)),
    Column('COD_PAIS', String(5)),
    Column('CNPJ', String(14), index=True),
    Column('CPF', String(11), index=True),
    Column('COD_MUN', String(7)),
    Column('ID_EFD_CTRL_REG_0000', INTEGER(11))
)


t_sped_pis_cofins_0150_ID_1045 = Table(
    'sped_pis_cofins_0150_ID_1045', metadata,
    Column('COD_PART', String(60), index=True),
    Column('NOME', String(100)),
    Column('COD_PAIS', String(5)),
    Column('CNPJ', String(14), index=True),
    Column('CPF', String(11), index=True),
    Column('COD_MUN', String(7)),
    Column('ID_EFD_CTRL_REG_0000', INTEGER(11))
)


t_sped_pis_cofins_0150_ID_1046 = Table(
    'sped_pis_cofins_0150_ID_1046', metadata,
    Column('COD_PART', String(60), index=True),
    Column('NOME', String(100)),
    Column('COD_PAIS', String(5)),
    Column('CNPJ', String(14), index=True),
    Column('CPF', String(11), index=True),
    Column('COD_MUN', String(7)),
    Column('ID_EFD_CTRL_REG_0000', INTEGER(11))
)


t_sped_pis_cofins_0150_ID_1047 = Table(
    'sped_pis_cofins_0150_ID_1047', metadata,
    Column('COD_PART', String(60), index=True),
    Column('NOME', String(100)),
    Column('COD_PAIS', String(5)),
    Column('CNPJ', String(14), index=True),
    Column('CPF', String(11), index=True),
    Column('COD_MUN', String(7)),
    Column('ID_EFD_CTRL_REG_0000', INTEGER(11))
)


t_sped_pis_cofins_0150_ID_1048 = Table(
    'sped_pis_cofins_0150_ID_1048', metadata,
    Column('COD_PART', String(60), index=True),
    Column('NOME', String(100)),
    Column('COD_PAIS', String(5)),
    Column('CNPJ', String(14), index=True),
    Column('CPF', String(11), index=True),
    Column('COD_MUN', String(7)),
    Column('ID_EFD_CTRL_REG_0000', INTEGER(11))
)


t_sped_pis_cofins_0150_ID_1049 = Table(
    'sped_pis_cofins_0150_ID_1049', metadata,
    Column('COD_PART', String(60), index=True),
    Column('NOME', String(100)),
    Column('COD_PAIS', String(5)),
    Column('CNPJ', String(14), index=True),
    Column('CPF', String(11), index=True),
    Column('COD_MUN', String(7)),
    Column('ID_EFD_CTRL_REG_0000', INTEGER(11))
)


t_sped_pis_cofins_0150_ID_1050 = Table(
    'sped_pis_cofins_0150_ID_1050', metadata,
    Column('COD_PART', String(60), index=True),
    Column('NOME', String(100)),
    Column('COD_PAIS', String(5)),
    Column('CNPJ', String(14), index=True),
    Column('CPF', String(11), index=True),
    Column('COD_MUN', String(7)),
    Column('ID_EFD_CTRL_REG_0000', INTEGER(11))
)


t_sped_pis_cofins_0150_ID_1051 = Table(
    'sped_pis_cofins_0150_ID_1051', metadata,
    Column('COD_PART', String(60), index=True),
    Column('NOME', String(100)),
    Column('COD_PAIS', String(5)),
    Column('CNPJ', String(14), index=True),
    Column('CPF', String(11), index=True),
    Column('COD_MUN', String(7)),
    Column('ID_EFD_CTRL_REG_0000', INTEGER(11))
)


t_sped_pis_cofins_0150_ID_1052 = Table(
    'sped_pis_cofins_0150_ID_1052', metadata,
    Column('COD_PART', String(60), index=True),
    Column('NOME', String(100)),
    Column('COD_PAIS', String(5)),
    Column('CNPJ', String(14), index=True),
    Column('CPF', String(11), index=True),
    Column('COD_MUN', String(7)),
    Column('ID_EFD_CTRL_REG_0000', INTEGER(11))
)


t_sped_pis_cofins_0150_ID_1053 = Table(
    'sped_pis_cofins_0150_ID_1053', metadata,
    Column('COD_PART', String(60), index=True),
    Column('NOME', String(100)),
    Column('COD_PAIS', String(5)),
    Column('CNPJ', String(14), index=True),
    Column('CPF', String(11), index=True),
    Column('COD_MUN', String(7)),
    Column('ID_EFD_CTRL_REG_0000', INTEGER(11))
)


t_sped_pis_cofins_0150_ID_1054 = Table(
    'sped_pis_cofins_0150_ID_1054', metadata,
    Column('COD_PART', String(60), index=True),
    Column('NOME', String(100)),
    Column('COD_PAIS', String(5)),
    Column('CNPJ', String(14), index=True),
    Column('CPF', String(11), index=True),
    Column('COD_MUN', String(7)),
    Column('ID_EFD_CTRL_REG_0000', INTEGER(11))
)


t_sped_pis_cofins_0150_ID_1055 = Table(
    'sped_pis_cofins_0150_ID_1055', metadata,
    Column('COD_PART', String(60), index=True),
    Column('NOME', String(100)),
    Column('COD_PAIS', String(5)),
    Column('CNPJ', String(14), index=True),
    Column('CPF', String(11), index=True),
    Column('COD_MUN', String(7)),
    Column('ID_EFD_CTRL_REG_0000', INTEGER(11))
)


class SpedPisCofins0190(Base):
    __tablename__ = 'sped_pis_cofins_0190'

    ID_REG_0190 = Column(BIGINT(25), primary_key=True)
    ID_REG_0140 = Column(BIGINT(25), nullable=False)
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    UNID = Column(String(6))
    DESCR = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofins0200(Base):
    __tablename__ = 'sped_pis_cofins_0200'
    __table_args__ = (
        Index('IDX_DUPLO', 'COD_ITEM', 'ID_EFD_CTRL_REG_0000'),
    )

    ID_REG_0200 = Column(BIGINT(25), primary_key=True)
    ID_REG_0140 = Column(BIGINT(25), nullable=False)
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    COD_ITEM = Column(String(60))
    DESCR_ITEM = Column(String(255))
    COD_BARRA = Column(String(255))
    COD_ANT_ITEM = Column(String(60))
    UNID_INV = Column(String(6))
    TIPO_ITEM = Column(String(2))
    COD_NCM = Column(String(8))
    EX_IPI = Column(String(3))
    COD_GEN = Column(String(2))
    COD_LST = Column(String(6))
    ALIQ_ICMS = Column(String(60))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))
    CNPJ_FILIAL = Column(String(40))


class SpedPisCofins0205(Base):
    __tablename__ = 'sped_pis_cofins_0205'

    ID_REG_0205 = Column(BIGINT(25), primary_key=True)
    ID_REG_0200 = Column(BIGINT(25), nullable=False)
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4), nullable=False)
    DESCR_ANT_ITEM = Column(String(255))
    DT_INI = Column(String(255))
    DT_FIN = Column(String(255))
    COD_ANT_ITEM = Column(String(60))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofins0206(Base):
    __tablename__ = 'sped_pis_cofins_0206'

    ID_REG_0200 = Column(BIGINT(25), primary_key=True)
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    COD_COMB = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofins0208(Base):
    __tablename__ = 'sped_pis_cofins_0208'

    ID_REG_0200 = Column(BIGINT(25))
    ID_REG_0208 = Column(BIGINT(25), primary_key=True)
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    COD_TAB = Column(String(2))
    COD_GRU = Column(String(2))
    MARCA_COM = Column(String(60))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofins0400(Base):
    __tablename__ = 'sped_pis_cofins_0400'

    ID_REG_0400 = Column(BIGINT(25), primary_key=True)
    ID_REG_0140 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    COD_NAT = Column(String(10))
    DESCR_NAT = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofins0450(Base):
    __tablename__ = 'sped_pis_cofins_0450'

    ID_REG_0450 = Column(BIGINT(25), primary_key=True)
    ID_REG_0140 = Column(BIGINT(25), nullable=False)
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    COD_INF = Column(String(6))
    TXT = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofins0500(Base):
    __tablename__ = 'sped_pis_cofins_0500'

    ID_REG_0500 = Column(BIGINT(25), primary_key=True)
    ID_REG_0001 = Column(BIGINT(25), nullable=False)
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    DT_ALT = Column(String(100))
    COD_NAT_CC = Column(String(2))
    IND_CTA = Column(String(1))
    NIVEL = Column(String(5))
    COD_CTA = Column(String(60))
    NOME_CTA = Column(String(60))
    COD_CTA_REF = Column(String(60))
    CNPJ_EST = Column(String(14))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofins0600(Base):
    __tablename__ = 'sped_pis_cofins_0600'

    ID_REG_0600 = Column(BIGINT(25), primary_key=True)
    ID_REG_0001 = Column(BIGINT(25), nullable=False)
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    DT_ALT = Column(String(100))
    COD_CCUS = Column(String(60))
    CCUS = Column(String(60))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofins0990(Base):
    __tablename__ = 'sped_pis_cofins_0990'

    ID_REG_0990 = Column(BIGINT(25), primary_key=True)
    ID_REG_0000 = Column(BIGINT(25), nullable=False)
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    QTD_LIN_0 = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofins1001(Base):
    __tablename__ = 'sped_pis_cofins_1001'

    ID_REG_1001 = Column(BIGINT(25), primary_key=True)
    ID_REG_0000 = Column(BIGINT(25), nullable=False)
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    IND_MOV = Column(String(1))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofins1010(Base):
    __tablename__ = 'sped_pis_cofins_1010'

    ID_REG_1010 = Column(BIGINT(25), primary_key=True)
    ID_REG_1001 = Column(BIGINT(25), nullable=False)
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    NUM_PROC = Column(String(20))
    ID_SEC_JUD = Column(String(255))
    ID_VARA = Column(String(2))
    IND_NAT_ACAO = Column(String(2))
    DESC_DEC_JUD = Column(String(100))
    DT_SENT_JUD = Column(String(100))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofins1020(Base):
    __tablename__ = 'sped_pis_cofins_1020'

    ID_REG_1020 = Column(BIGINT(25), primary_key=True)
    ID_REG_1001 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    NUM_PROC = Column(String(20))
    IND_NAT_ACAO = Column(String(2))
    DT_DEC_ADM = Column(String(100))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofins1100(Base):
    __tablename__ = 'sped_pis_cofins_1100'

    ID_REG_1100 = Column(BIGINT(25), primary_key=True)
    ID_REG_1001 = Column(BIGINT(25), nullable=False)
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    PER_APU_CRED = Column(String(6))
    ORIG_CRED = Column(String(2))
    CNPJ_SUC = Column(String(14))
    COD_CRED = Column(String(3))
    VL_CRED_APU = Column(String(255))
    VL_CRED_EXT_APU = Column(String(255))
    VL_TOT_CRED_APU = Column(String(255))
    VL_CRED_DESC_PA_ANT = Column(String(255))
    VL_CRED_PER_PA_ANT = Column(String(255))
    VL_CRED_DCOMP_PA_ANT = Column(String(255))
    SD_CRED_DISP_EFD = Column(String(255))
    VL_CRED_DESC_EFD = Column(String(255))
    VL_CRED_PER_EFD = Column(String(255))
    VL_CRED_DCOMP_EFD = Column(String(255))
    VL_CRED_TRANS = Column(String(255))
    VL_CRED_OUT = Column(String(255))
    SLD_CRED_FIM = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofins1101(Base):
    __tablename__ = 'sped_pis_cofins_1101'

    ID_REG_1101 = Column(BIGINT(25), primary_key=True)
    ID_REG_1010 = Column(BIGINT(25), nullable=False)
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    COD_PART = Column(String(60))
    COD_ITEM = Column(String(60))
    COD_MOD = Column(String(2))
    SER = Column(String(4))
    SUB_SER = Column(String(3))
    NUM_DOC = Column(String(9))
    DT_OPER = Column(String(100))
    CHV_NFE = Column(String(44))
    VL_OPER = Column(String(255))
    CFOP = Column(String(4))
    NAT_BC_CRED = Column(String(2))
    IND_ORIG_CRED = Column(String(1))
    CST_PIS = Column(String(2))
    VL_BC_PIS = Column(String(60))
    ALIQ_PIS = Column(String(60))
    VL_PIS = Column(String(255))
    COD_CTA = Column(String(60))
    COD_CCUS = Column(String(60))
    DESC_COMPL = Column(String(255))
    PER_ESCRIT = Column(String(6))
    CNPJ = Column(String(14))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofins1102(Base):
    __tablename__ = 'sped_pis_cofins_1102'

    ID_REG_1102 = Column(BIGINT(25), primary_key=True)
    ID_REG_1101 = Column(BIGINT(25), nullable=False)
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    VL_CRED_PIS_TRIB_MI = Column(String(255))
    VL_CRED_PIS_NT_MI = Column(String(255))
    VL_CRED_PIS_EXP = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofins1200(Base):
    __tablename__ = 'sped_pis_cofins_1200'

    ID_REG_1200 = Column(BIGINT(25), primary_key=True)
    ID_REG_1001 = Column(BIGINT(25), nullable=False)
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    PER_APUR_ANT = Column(String(6))
    NAT_CONT_REC = Column(String(2))
    VL_CONT_APUR = Column(String(255))
    VL_CRED_PIS_DESC = Column(String(255))
    VL_CONT_DEV = Column(String(255))
    VL_OUT_DED = Column(String(255))
    VL_CONT_EXT = Column(String(255))
    VL_MUL = Column(String(255))
    VL_JUR = Column(String(255))
    DT_RECOL = Column(String(8))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofins1210(Base):
    __tablename__ = 'sped_pis_cofins_1210'

    ID_REG_1210 = Column(BIGINT(25), primary_key=True)
    ID_REG_1200 = Column(BIGINT(25), nullable=False)
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    CNPJ = Column(String(14))
    CST_PIS = Column(String(2))
    COD_PART = Column(String(60))
    DT_OPER = Column(String(100))
    VL_OPER = Column(String(255))
    VL_BC_PIS = Column(String(60))
    ALIQ_PIS = Column(String(60))
    VL_PIS = Column(String(255))
    COD_CTA = Column(String(60))
    DESC_COMPL = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofins1220(Base):
    __tablename__ = 'sped_pis_cofins_1220'

    ID_REG_1220 = Column(BIGINT(25), primary_key=True)
    ID_REG_1200 = Column(BIGINT(25), nullable=False)
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    PER_APU_CRED = Column(String(6))
    ORIG_CRED = Column(String(2))
    COD_CRED = Column(String(3))
    VL_CRED = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofins1300(Base):
    __tablename__ = 'sped_pis_cofins_1300'

    ID_REG_1300 = Column(BIGINT(25), primary_key=True)
    ID_REG_1001 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    IND_NAT_RET = Column(String(2))
    PR_REC_RET = Column(String(6))
    VL_RET_APU = Column(String(255))
    VL_RET_DED = Column(String(255))
    VL_RET_PER = Column(String(255))
    VL_RET_DCOMP = Column(String(255))
    SLD_RET = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofins1500(Base):
    __tablename__ = 'sped_pis_cofins_1500'

    ID_REG_1500 = Column(BIGINT(25), primary_key=True)
    ID_REG_1001 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    PER_APU_CRED = Column(String(6))
    ORIG_CRED = Column(String(2))
    CNPJ_SUC = Column(String(14))
    COD_CRED = Column(String(3))
    VL_CRED_APU = Column(String(255))
    VL_CRED_EXT_APU = Column(String(255))
    VL_TOT_CRED_APU = Column(String(255))
    VL_CRED_DESC_PA_ANT = Column(String(255))
    VL_CRED_PER_PA_ANT = Column(String(255))
    VL_CRED_DCOMP_PA_ANT = Column(String(255))
    SD_CRED_DISP_EFD = Column(String(255))
    VL_CRED_DESC_EFD = Column(String(255))
    VL_CRED_PER_EFD = Column(String(255))
    VL_CRED_DCOMP_EFD = Column(String(255))
    VL_CRED_TRANS = Column(String(255))
    VL_CRED_OUT = Column(String(255))
    SLD_CRED_FIM = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofins1501(Base):
    __tablename__ = 'sped_pis_cofins_1501'

    ID_REG_1501 = Column(BIGINT(25), primary_key=True)
    ID_REG_1010 = Column(BIGINT(25), nullable=False)
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    COD_PART = Column(String(60))
    COD_ITEM = Column(String(60))
    COD_MOD = Column(String(2))
    SER = Column(String(4))
    SUB_SER = Column(String(3))
    NUM_DOC = Column(String(9))
    DT_OPER = Column(String(100))
    CHV_NFE = Column(String(44))
    VL_OPER = Column(String(255))
    CFOP = Column(String(4))
    NAT_BC_CRED = Column(String(2))
    IND_ORIG_CRED = Column(String(1))
    CST_COFINS = Column(String(2))
    VL_BC_COFINS = Column(String(255))
    ALIQ_COFINS = Column(String(255))
    VL_COFINS = Column(String(255))
    COD_CTA = Column(String(60))
    COD_CCUS = Column(String(60))
    DESC_COMPL = Column(String(255))
    PER_ESCRIT = Column(String(6))
    CNPJ = Column(String(14))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofins1502(Base):
    __tablename__ = 'sped_pis_cofins_1502'

    ID_REG_1502 = Column(BIGINT(25), primary_key=True)
    ID_REG_1501 = Column(BIGINT(25), nullable=False)
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    VL_CRED_COFINS_TRIB_MI = Column(String(255))
    VL_CRED_COFINS_NT_MI = Column(String(255))
    VL_CRED_COFINS_EXP = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofins1600(Base):
    __tablename__ = 'sped_pis_cofins_1600'

    ID_REG_1600 = Column(BIGINT(25), primary_key=True)
    ID_REG_1001 = Column(BIGINT(25), nullable=False)
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    PER_APUR_ANT = Column(String(6))
    NAT_CONT_REC = Column(String(2))
    VL_CONT_APUR = Column(String(255))
    VL_CRED_COFINS_DESC = Column(String(255))
    VL_CONT_DEV = Column(String(255))
    VL_OUT_DED = Column(String(255))
    VL_CONT_EXT = Column(String(255))
    VL_MUL = Column(String(255))
    VL_JUR = Column(String(255))
    DT_RECOL = Column(String(100))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofins1610(Base):
    __tablename__ = 'sped_pis_cofins_1610'

    ID_REG_1610 = Column(BIGINT(25), primary_key=True)
    ID_REG_1600 = Column(BIGINT(25), nullable=False)
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    CNPJ = Column(String(14))
    CST_COFINS = Column(String(2))
    COD_PART = Column(String(60))
    DT_OPER = Column(String(100))
    VL_OPER = Column(String(255))
    VL_BC_COFINS = Column(String(255))
    ALIQ_COFINS = Column(String(255))
    VL_COFINS = Column(String(255))
    COD_CTA = Column(String(60))
    DESC_COMPL = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofins1620(Base):
    __tablename__ = 'sped_pis_cofins_1620'

    ID_REG_1620 = Column(BIGINT(25), primary_key=True)
    ID_REG_1600 = Column(BIGINT(25), nullable=False)
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    PER_APU_CRED = Column(String(6))
    ORIG_CRED = Column(String(2))
    COD_CRED = Column(String(3))
    VL_CRED = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofins1700(Base):
    __tablename__ = 'sped_pis_cofins_1700'

    ID_REG_1700 = Column(BIGINT(25), primary_key=True)
    ID_REG_1001 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    IND_NAT_RET = Column(String(2))
    PR_REC_RET = Column(String(6))
    VL_RET_APU = Column(String(255))
    VL_RET_DED = Column(String(255))
    VL_RET_PER = Column(String(255))
    VL_RET_DCOMP = Column(String(255))
    SLD_RET = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofins1800(Base):
    __tablename__ = 'sped_pis_cofins_1800'

    ID_REG_1800 = Column(BIGINT(25), primary_key=True)
    ID_REG_1001 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    INC_IMOB = Column(String(90))
    REC_RECEB_RET = Column(String(255))
    REC_FIN_RET = Column(String(255))
    BC_RET = Column(String(255))
    ALIQ_RET = Column(String(255))
    VL_REC_UNI = Column(String(255))
    DT_REC_UNI = Column(String(100))
    COD_REC = Column(String(4))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofins1809(Base):
    __tablename__ = 'sped_pis_cofins_1809'

    ID_REG_1809 = Column(BIGINT(25), primary_key=True)
    ID_REG_1800 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    NUM_PROC = Column(String(20))
    IND_PROC = Column(String(1))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofins1900(Base):
    __tablename__ = 'sped_pis_cofins_1900'

    ID_REG_1900 = Column(BIGINT(25), primary_key=True)
    ID_REG_1001 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    CNPJ = Column(String(14))
    COD_MOD = Column(String(2))
    SER = Column(String(4))
    SUB_SER = Column(String(20))
    COD_SIT = Column(String(2))
    VL_TOT_REC = Column(String(255))
    QUANT_DOC = Column(String(255))
    CST_PIS = Column(String(2))
    CST_COFINS = Column(String(2))
    CFOP = Column(String(4))
    INFO_COMPL = Column(String(255))
    COD_CTA = Column(String(60))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofins1990(Base):
    __tablename__ = 'sped_pis_cofins_1990'

    ID_REG_1990 = Column(BIGINT(25), primary_key=True)
    ID_REG_0000 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    QTD_LIN_1 = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofins9001(Base):
    __tablename__ = 'sped_pis_cofins_9001'

    ID_REG_9001 = Column(BIGINT(25), primary_key=True)
    ID_REG_0000 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    IND_MOV = Column(String(1))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofins9900(Base):
    __tablename__ = 'sped_pis_cofins_9900'

    ID_REG_9900 = Column(BIGINT(25), primary_key=True)
    ID_REG_9001 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    EFD_REG_BLC = Column(String(4))
    QTD_EFD_REG_BLC = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofins9990(Base):
    __tablename__ = 'sped_pis_cofins_9990'

    ID_REG_9990 = Column(BIGINT(25), primary_key=True)
    ID_REG_0000 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    QTD_LIN_9 = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofins9999(Base):
    __tablename__ = 'sped_pis_cofins_9999'

    ID_REG_9999 = Column(BIGINT(25), primary_key=True)
    ID_LOTES_ARQUIVOS = Column(BIGINT(25), nullable=False)
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    QTD_LIN = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsA001(Base):
    __tablename__ = 'sped_pis_cofins_A001'

    ID_REG_A001 = Column(BIGINT(25), primary_key=True)
    ID_REG_0000 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    IND_MOV = Column(String(1))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsA010(Base):
    __tablename__ = 'sped_pis_cofins_A010'

    ID_REG_A010 = Column(BIGINT(25), primary_key=True)
    ID_REG_A001 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    CNPJ = Column(String(14))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsA100(Base):
    __tablename__ = 'sped_pis_cofins_A100'

    ID_REG_A100 = Column(BIGINT(25), primary_key=True)
    ID_REG_A010 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    IND_OPER = Column(String(1))
    IND_EMIT = Column(String(1))
    COD_PART = Column(String(60))
    COD_SIT = Column(String(2))
    SER = Column(String(20))
    SUB = Column(String(20))
    NUM_DOC = Column(String(128))
    CHV_NFSE = Column(String(128))
    DT_DOC = Column(String(100))
    DT_EXE_SERV = Column(String(100))
    VL_DOC = Column(String(255))
    IND_PGTO = Column(String(1))
    VL_DESC = Column(String(255))
    VL_BC_PIS = Column(String(255))
    VL_PIS = Column(String(255))
    VL_BC_COFINS = Column(String(255))
    VL_COFINS = Column(String(255))
    VL_PIS_RET = Column(String(255))
    VL_COFINS_RET = Column(String(255))
    VL_ISS = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11), index=True)


class SpedPisCofinsA110(Base):
    __tablename__ = 'sped_pis_cofins_A110'

    ID_REG_A110 = Column(BIGINT(25), primary_key=True)
    ID_REG_A100 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    COD_INF = Column(String(6))
    TXT_COMPL = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsA111(Base):
    __tablename__ = 'sped_pis_cofins_A111'

    ID_REG_A111 = Column(BIGINT(25), primary_key=True)
    ID_REG_A100 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    NUM_PROC = Column(String(20))
    IND_PROC = Column(String(1))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsA120(Base):
    __tablename__ = 'sped_pis_cofins_A120'

    ID_REG_A120 = Column(BIGINT(25), primary_key=True)
    ID_REG_A100 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    VL_TOT_SERV = Column(String(255))
    VL_BC_PIS = Column(String(255))
    VL_PIS_IMP = Column(String(255))
    DT_PAG_PIS = Column(String(100))
    VL_BC_COFINS = Column(String(255))
    VL_COFINS_IMP = Column(String(255))
    DT_PAG_COFINS = Column(String(100))
    LOC_EXE_SERV = Column(String(1))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsA170(Base):
    __tablename__ = 'sped_pis_cofins_A170'

    ID_REG_A170 = Column(BIGINT(25), primary_key=True)
    ID_REG_A100 = Column(BIGINT(25), index=True)
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    NUM_ITEM = Column(String(4))
    COD_ITEM = Column(String(60))
    DESCR_COMPL = Column(String(255))
    VL_ITEM = Column(String(255))
    VL_DESC = Column(String(255))
    NAT_BC_CRED = Column(String(2))
    IND_ORIG_CRED = Column(String(1))
    CST_PIS = Column(String(2))
    VL_BC_PIS = Column(String(255))
    ALIQ_PIS = Column(String(255))
    VL_PIS = Column(String(255))
    CST_COFINS = Column(String(2))
    VL_BC_COFINS = Column(String(255))
    ALIQ_COFINS = Column(String(255))
    VL_COFINS = Column(String(255))
    COD_CTA = Column(String(60))
    COD_CCUS = Column(String(60))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsA990(Base):
    __tablename__ = 'sped_pis_cofins_A990'

    ID_REG_A990 = Column(BIGINT(25), primary_key=True)
    ID_REG_0000 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    QTD_LIN_A = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsC001(Base):
    __tablename__ = 'sped_pis_cofins_C001'

    ID_REG_C001 = Column(BIGINT(25), primary_key=True)
    ID_REG_0000 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    IND_MOV = Column(String(1))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsC010(Base):
    __tablename__ = 'sped_pis_cofins_C010'

    ID_REG_C010 = Column(BIGINT(25), primary_key=True)
    ID_REG_C001 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    CNPJ = Column(String(14))
    IND_ESCRI = Column(String(1))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsC100(Base):
    __tablename__ = 'sped_pis_cofins_C100'

    ID_REG_C100 = Column(BIGINT(25), primary_key=True)
    ID_REG_C010 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    IND_OPER = Column(String(1))
    IND_EMIT = Column(String(1))
    COD_PART = Column(String(60))
    COD_MOD = Column(String(2))
    COD_SIT = Column(String(2))
    SER = Column(String(3))
    NUM_DOC = Column(String(9))
    CHV_NFE = Column(String(44))
    DT_DOC = Column(String(100))
    DT_E_S = Column(String(100))
    VL_DOC = Column(String(255))
    IND_PGTO = Column(String(1))
    VL_DESC = Column(String(255))
    VL_ABAT_NT = Column(String(255))
    VL_MERC = Column(String(255))
    IND_FRT = Column(String(1))
    VL_FRT = Column(String(255))
    VL_SEG = Column(String(255))
    VL_OUT_DA = Column(String(255))
    VL_BC_ICMS = Column(String(255))
    VL_ICMS = Column(String(255))
    VL_BC_ICMS_ST = Column(String(255))
    VL_ICMS_ST = Column(String(255))
    VL_IPI = Column(String(255))
    VL_PIS = Column(String(255))
    VL_COFINS = Column(String(255))
    VL_PIS_ST = Column(String(255))
    VL_COFINS_ST = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11), index=True)


class SpedPisCofinsC110(Base):
    __tablename__ = 'sped_pis_cofins_C110'

    ID_REG_C110 = Column(BIGINT(25), primary_key=True)
    ID_REG_C100 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    COD_INF = Column(String(6))
    TXT_COMPL = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsC111(Base):
    __tablename__ = 'sped_pis_cofins_C111'

    ID_REG_C100 = Column(BIGINT(25))
    ID_REG_C111 = Column(BIGINT(25), primary_key=True)
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    NUM_PROC = Column(String(20))
    IND_PROC = Column(String(1))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsC120(Base):
    __tablename__ = 'sped_pis_cofins_C120'

    ID_REG_C100 = Column(BIGINT(25))
    ID_REG_C120 = Column(BIGINT(25), primary_key=True)
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    COD_DOC_IMP = Column(String(1))
    NUM_DOC_IMP = Column(String(10))
    VL_PIS_IMP = Column(String(255))
    VL_COFINS_IMP = Column(String(255))
    NUM_ACDRAW = Column(String(20))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsC170(Base):
    __tablename__ = 'sped_pis_cofins_C170'

    ID_REG_C170 = Column(BIGINT(25), primary_key=True)
    ID_REG_C100 = Column(BIGINT(25), index=True)
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    NUM_ITEM = Column(String(3))
    COD_ITEM = Column(String(60))
    DESCR_COMPL = Column(String(255))
    QTD = Column(String(255))
    UNID = Column(String(6))
    VL_ITEM = Column(String(255))
    VL_DESC = Column(String(255))
    IND_MOV = Column(String(1))
    CST_ICMS = Column(String(3))
    CFOP = Column(String(4))
    COD_NAT = Column(String(10))
    VL_BC_ICMS = Column(String(255))
    ALIQ_ICMS = Column(String(255))
    VL_ICMS = Column(String(255))
    VL_BC_ICMS_ST = Column(String(255))
    ALIQ_ST = Column(String(255))
    VL_ICMS_ST = Column(String(255))
    IND_APUR = Column(String(1))
    CST_IPI = Column(String(2))
    COD_ENQ = Column(String(3))
    VL_BC_IPI = Column(String(255))
    ALIQ_IPI = Column(String(255))
    VL_IPI = Column(String(255))
    CST_PIS = Column(String(2))
    VL_BC_PIS = Column(String(255))
    ALIQ_PIS = Column(String(255))
    QUANT_BC_PIS = Column(String(255))
    ALIQ_PIS_QUANT = Column(String(255))
    VL_PIS = Column(String(255))
    CST_COFINS = Column(String(2))
    VL_BC_COFINS = Column(String(255))
    ALIQ_COFINS = Column(String(255))
    QUANT_BC_COFINS = Column(String(255))
    ALIQ_COFINS_QUANT = Column(String(255))
    VL_COFINS = Column(String(255))
    COD_CTA = Column(String(60))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsC175(Base):
    __tablename__ = 'sped_pis_cofins_C175'

    ID_REG_C175 = Column(BIGINT(25), primary_key=True)
    ID_REG_C100 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    CFOP = Column(String(4))
    VL_OPER = Column(String(255))
    VL_DESC = Column(String(255))
    CST_PIS = Column(String(2))
    VL_BC_PIS = Column(String(255))
    ALIQ_PIS = Column(String(255))
    QUANT_BC_PIS = Column(String(255))
    ALIQ_PIS_QUANT = Column(String(255))
    VL_PIS = Column(String(255))
    CST_COFINS = Column(String(2))
    VL_BC_COFINS = Column(String(255))
    ALIQ_COFINS = Column(String(255))
    QUANT_BC_COFINS = Column(String(255))
    ALIQ_COFINS_QUANT = Column(String(255))
    VL_COFINS = Column(String(255))
    COD_CTA = Column(String(60))
    INFO_COMPL = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsC180(Base):
    __tablename__ = 'sped_pis_cofins_C180'

    ID_REG_C180 = Column(BIGINT(25), primary_key=True)
    ID_REG_C010 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    COD_MOD = Column(String(2))
    DT_DOC_INI = Column(String(100))
    DT_DOC_FIN = Column(String(100))
    COD_ITEM = Column(String(60))
    COD_NCM = Column(String(8))
    EX_IPI = Column(String(3))
    VL_TOT_ITEM = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsC181(Base):
    __tablename__ = 'sped_pis_cofins_C181'

    ID_REG_C181 = Column(BIGINT(25), primary_key=True)
    ID_REG_C180 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    CST_PIS = Column(String(2))
    CFOP = Column(String(4))
    VL_ITEM = Column(String(255))
    VL_DESC = Column(String(255))
    VL_BC_PIS = Column(String(255))
    ALIQ_PIS = Column(String(255))
    QUANT_BC_PIS = Column(String(255))
    ALIQ_PIS_QUANT = Column(String(255))
    VL_PIS = Column(String(255))
    COD_CTA = Column(String(60))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsC185(Base):
    __tablename__ = 'sped_pis_cofins_C185'

    ID_REG_C185 = Column(BIGINT(25), primary_key=True)
    ID_REG_C180 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    CST_COFINS = Column(String(2))
    CFOP = Column(String(4))
    VL_ITEM = Column(String(255))
    VL_DESC = Column(String(255))
    VL_BC_COFINS = Column(String(255))
    ALIQ_COFINS = Column(String(255))
    QUANT_BC_COFINS = Column(String(255))
    ALIQ_COFINS_QUANT = Column(String(255))
    VL_COFINS = Column(String(255))
    COD_CTA = Column(String(60))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsC188(Base):
    __tablename__ = 'sped_pis_cofins_C188'

    ID_REG_C188 = Column(BIGINT(25), primary_key=True)
    ID_REG_C180 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    NUM_PROC = Column(String(20))
    IND_PROC = Column(String(1))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsC190(Base):
    __tablename__ = 'sped_pis_cofins_C190'

    ID_REG_C190 = Column(BIGINT(25), primary_key=True)
    ID_REG_C010 = Column(BIGINT(25), index=True)
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    COD_MOD = Column(String(2))
    DT_REF_INI = Column(String(100))
    DT_REF_FIN = Column(String(100))
    COD_ITEM = Column(String(60))
    COD_NCM = Column(String(8))
    EX_IPI = Column(String(3))
    VL_TOT_ITEM = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsC191(Base):
    __tablename__ = 'sped_pis_cofins_C191'

    ID_REG_C191 = Column(BIGINT(25), primary_key=True)
    ID_REG_C190 = Column(BIGINT(25), index=True)
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    CNPJ_CPF_PART = Column(String(14))
    CST_PIS = Column(String(2))
    CFOP = Column(String(4))
    VL_ITEM = Column(String(255))
    VL_DESC = Column(String(255))
    VL_BC_PIS = Column(String(255))
    ALIQ_PIS = Column(String(255))
    QUANT_BC_PIS = Column(String(255))
    ALIQ_PIS_QUANT = Column(String(255))
    VL_PIS = Column(String(255))
    COD_CTA = Column(String(60))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsC195(Base):
    __tablename__ = 'sped_pis_cofins_C195'

    ID_REG_C195 = Column(BIGINT(25), primary_key=True)
    ID_REG_C190 = Column(BIGINT(25), index=True)
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    CNPJ_CPF_PART = Column(String(14))
    CST_COFINS = Column(String(2))
    CFOP = Column(String(4))
    VL_ITEM = Column(String(255))
    VL_DESC = Column(String(255))
    VL_BC_COFINS = Column(String(255))
    ALIQ_COFINS = Column(String(255))
    QUANT_BC_COFINS = Column(String(255))
    ALIQ_COFINS_QUANT = Column(String(255))
    VL_COFINS = Column(String(255))
    COD_CTA = Column(String(60))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsC198(Base):
    __tablename__ = 'sped_pis_cofins_C198'

    ID_REG_C198 = Column(BIGINT(25), primary_key=True)
    ID_REG_C190 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    NUM_PROC = Column(String(20))
    IND_PROC = Column(String(1))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsC199(Base):
    __tablename__ = 'sped_pis_cofins_C199'

    ID_REG_C199 = Column(BIGINT(25), primary_key=True)
    ID_REG_C190 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    COD_DOC_IMP = Column(String(1))
    NUM_DOC_IMP = Column(String(10))
    VL_PIS_IMP = Column(String(255))
    VL_COFINS_IMP = Column(String(255))
    NUM_ACDRAW = Column(String(20))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsC380(Base):
    __tablename__ = 'sped_pis_cofins_C380'

    ID_REG_C380 = Column(BIGINT(25), primary_key=True)
    ID_REG_C010 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    COD_MOD = Column(String(2))
    DT_DOC_INI = Column(String(100))
    DT_DOC_FIN = Column(String(100))
    NUM_DOC_INI = Column(String(6))
    NUM_DOC_FIN = Column(String(6))
    VL_DOC = Column(String(255))
    VL_DOC_CANC = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsC381(Base):
    __tablename__ = 'sped_pis_cofins_C381'

    ID_REG_C381 = Column(BIGINT(25), primary_key=True)
    ID_REG_C380 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    CST_PIS = Column(String(2))
    COD_ITEM = Column(String(60))
    VL_ITEM = Column(String(255))
    VL_BC_PIS = Column(String(255))
    ALIQ_PIS = Column(String(255))
    QUANT_BC_PIS = Column(String(255))
    ALIQ_PIS_QUANT = Column(String(255))
    VL_PIS = Column(String(255))
    COD_CTA = Column(String(60))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsC385(Base):
    __tablename__ = 'sped_pis_cofins_C385'

    ID_REG_C385 = Column(BIGINT(25), primary_key=True)
    ID_REG_C380 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    CST_COFINS = Column(String(2))
    COD_ITEM = Column(String(60))
    VL_ITEM = Column(String(255))
    VL_BC_COFINS = Column(String(255))
    ALIQ_COFINS = Column(String(255))
    QUANT_BC_COFINS = Column(String(255))
    ALIQ_COFINS_QUANT = Column(String(255))
    VL_COFINS = Column(String(255))
    COD_CTA = Column(String(60))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsC395(Base):
    __tablename__ = 'sped_pis_cofins_C395'

    ID_REG_C395 = Column(BIGINT(25), primary_key=True)
    ID_REG_C010 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    COD_MOD = Column(String(2))
    COD_PART = Column(String(60))
    SER = Column(String(3))
    SUB_SER = Column(String(3))
    NUM_DOC = Column(String(6))
    DT_DOC = Column(String(100))
    VL_DOC = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsC396(Base):
    __tablename__ = 'sped_pis_cofins_C396'

    ID_REG_C396 = Column(BIGINT(25), primary_key=True)
    ID_REG_C395 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    COD_ITEM = Column(String(60))
    VL_ITEM = Column(String(255))
    VL_DESC = Column(String(255))
    NAT_BC_CRED = Column(String(2))
    CST_PIS = Column(String(2))
    VL_BC_PIS = Column(String(255))
    ALIQ_PIS = Column(String(255))
    VL_PIS = Column(String(255))
    CST_COFINS = Column(String(2))
    VL_BC_COFINS = Column(String(255))
    ALIQ_COFINS = Column(String(255))
    VL_COFINS = Column(String(255))
    COD_CTA = Column(String(60))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsC400(Base):
    __tablename__ = 'sped_pis_cofins_C400'

    ID_REG_C400 = Column(BIGINT(25), primary_key=True)
    ID_REG_C010 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    COD_MOD = Column(String(2))
    ECF_MOD = Column(String(20))
    ECF_FAB = Column(String(20))
    ECF_CX = Column(String(3))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsC405(Base):
    __tablename__ = 'sped_pis_cofins_C405'

    ID_REG_C405 = Column(BIGINT(25), primary_key=True)
    ID_REG_C400 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    DT_DOC = Column(String(100))
    CRO = Column(String(3))
    CRZ = Column(String(6))
    NUM_COO_FIN = Column(String(6))
    GT_FIN = Column(String(255))
    VL_BRT = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsC481(Base):
    __tablename__ = 'sped_pis_cofins_C481'

    ID_REG_C481 = Column(BIGINT(25), primary_key=True)
    ID_REG_C405 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    CST_PIS = Column(String(2))
    VL_ITEM = Column(String(255))
    VL_BC_PIS = Column(String(255))
    ALIQ_PIS = Column(String(255))
    QUANT_BC_PIS = Column(String(255))
    ALIQ_PIS_QUANT = Column(String(255))
    VL_PIS = Column(String(255))
    COD_ITEM = Column(String(60))
    COD_CTA = Column(String(60))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsC485(Base):
    __tablename__ = 'sped_pis_cofins_C485'

    ID_REG_C485 = Column(BIGINT(25), primary_key=True)
    ID_REG_C405 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    CST_COFINS = Column(String(2))
    VL_ITEM = Column(String(255))
    VL_BC_COFINS = Column(String(255))
    ALIQ_COFINS = Column(String(255))
    QUANT_BC_COFINS = Column(String(255))
    ALIQ_COFINS_QUANT = Column(String(255))
    VL_COFINS = Column(String(255))
    COD_ITEM = Column(String(60))
    COD_CTA = Column(String(60))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsC489(Base):
    __tablename__ = 'sped_pis_cofins_C489'

    ID_REG_C489 = Column(BIGINT(25), primary_key=True)
    ID_REG_C400 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    NUM_PROC = Column(String(20))
    IND_PROC = Column(String(1))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsC490(Base):
    __tablename__ = 'sped_pis_cofins_C490'

    ID_REG_C490 = Column(BIGINT(25), primary_key=True)
    ID_REG_C010 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    DT_DOC_INI = Column(String(100))
    DT_DOC_FIN = Column(String(100))
    COD_MOD = Column(String(2))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsC491(Base):
    __tablename__ = 'sped_pis_cofins_C491'

    ID_REG_C491 = Column(BIGINT(25), primary_key=True)
    ID_REG_C490 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    COD_ITEM = Column(String(60))
    CST_PIS = Column(String(2))
    CFOP = Column(String(4))
    VL_ITEM = Column(String(255))
    VL_BC_PIS = Column(String(255))
    ALIQ_PIS = Column(String(255))
    QUANT_BC_PIS = Column(String(255))
    ALIQ_PIS_QUANT = Column(String(255))
    VL_PIS = Column(String(255))
    COD_CTA = Column(String(60))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsC495(Base):
    __tablename__ = 'sped_pis_cofins_C495'

    ID_REG_C495 = Column(BIGINT(25), primary_key=True)
    ID_REG_C490 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    COD_ITEM = Column(String(60))
    CST_COFINS = Column(String(2))
    CFOP = Column(String(4))
    VL_ITEM = Column(String(255))
    VL_BC_COFINS = Column(String(255))
    ALIQ_COFINS = Column(String(255))
    QUANT_BC_COFINS = Column(String(255))
    ALIQ_COFINS_QUANT = Column(String(255))
    VL_COFINS = Column(String(255))
    COD_CTA = Column(String(60))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsC499(Base):
    __tablename__ = 'sped_pis_cofins_C499'

    ID_REG_C499 = Column(BIGINT(25), primary_key=True)
    ID_REG_C490 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    NUM_PROC = Column(String(20))
    IND_PROC = Column(String(1))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsC500(Base):
    __tablename__ = 'sped_pis_cofins_C500'

    ID_REG_C500 = Column(BIGINT(25), primary_key=True)
    ID_REG_C010 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    COD_PART = Column(String(60))
    COD_MOD = Column(String(2))
    COD_SIT = Column(String(2))
    SER = Column(String(4))
    SUB = Column(String(3))
    NUM_DOC = Column(String(60))
    DT_DOC = Column(String(100))
    DT_E_S = Column(String(100))
    VL_DOC = Column(String(255))
    VL_ICMS = Column(String(255))
    COD_INF = Column(String(6))
    VL_PIS = Column(String(255))
    VL_COFINS = Column(String(255))
    CHV_DOCe = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsC501(Base):
    __tablename__ = 'sped_pis_cofins_C501'

    ID_REG_C501 = Column(BIGINT(25), primary_key=True)
    ID_REG_C500 = Column(BIGINT(25), index=True)
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    CST_PIS = Column(String(2))
    VL_ITEM = Column(String(255))
    NAT_BC_CRED = Column(String(2))
    VL_BC_PIS = Column(String(255))
    ALIQ_PIS = Column(String(255))
    VL_PIS = Column(String(255))
    COD_CTA = Column(String(60))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsC505(Base):
    __tablename__ = 'sped_pis_cofins_C505'

    ID_REG_C505 = Column(BIGINT(25), primary_key=True)
    ID_REG_C500 = Column(BIGINT(25), index=True)
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    CST_COFINS = Column(String(2))
    VL_ITEM = Column(String(255))
    NAT_BC_CRED = Column(String(2))
    VL_BC_COFINS = Column(String(255))
    ALIQ_COFINS = Column(String(255))
    VL_COFINS = Column(String(255))
    COD_CTA = Column(String(60))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsC509(Base):
    __tablename__ = 'sped_pis_cofins_C509'

    ID_REG_C509 = Column(BIGINT(25), primary_key=True)
    ID_REG_C500 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    NUM_PROC = Column(String(20))
    IND_PROC = Column(String(1))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsC600(Base):
    __tablename__ = 'sped_pis_cofins_C600'

    ID_REG_C600 = Column(BIGINT(25), primary_key=True)
    ID_REG_C010 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    COD_MOD = Column(String(2))
    COD_MUN = Column(String(7))
    SER = Column(String(4))
    SUB = Column(String(3))
    COD_CONS = Column(String(2))
    QTD_CONS = Column(String(255))
    QTD_CANC = Column(String(255))
    DT_DOC = Column(String(100))
    VL_DOC = Column(String(255))
    VL_DESC = Column(String(255))
    CONS = Column(String(255))
    VL_FORN = Column(String(255))
    VL_SERV_NT = Column(String(255))
    VL_TERC = Column(String(255))
    VL_DA = Column(String(255))
    VL_BC_ICMS = Column(String(255))
    VL_ICMS = Column(String(255))
    VL_BC_ICMS_ST = Column(String(255))
    VL_ICMS_ST = Column(String(255))
    VL_PIS = Column(String(255))
    VL_COFINS = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsC601(Base):
    __tablename__ = 'sped_pis_cofins_C601'

    ID_REG_C601 = Column(BIGINT(25), primary_key=True)
    ID_REG_C600 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    CST_PIS = Column(String(2))
    VL_ITEM = Column(String(255))
    VL_BC_PIS = Column(String(255))
    ALIQ_PIS = Column(String(255))
    VL_PIS = Column(String(255))
    COD_CTA = Column(String(60))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsC605(Base):
    __tablename__ = 'sped_pis_cofins_C605'

    ID_REG_C605 = Column(BIGINT(25), primary_key=True)
    ID_REG_C600 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    CST_COFINS = Column(String(2))
    VL_ITEM = Column(String(255))
    VL_BC_COFINS = Column(String(255))
    ALIQ_COFINS = Column(String(255))
    VL_COFINS = Column(String(255))
    COD_CTA = Column(String(60))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsC609(Base):
    __tablename__ = 'sped_pis_cofins_C609'

    ID_REG_C609 = Column(BIGINT(25), primary_key=True)
    ID_REG_C600 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    NUM_PROC = Column(String(20))
    IND_PROC = Column(String(1))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsC800(Base):
    __tablename__ = 'sped_pis_cofins_C800'

    ID_REG_C800 = Column(BIGINT(25), primary_key=True)
    ID_REG_C010 = Column(BIGINT(25), nullable=False)
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    COD_MOD = Column(String(2))
    COD_SIT = Column(String(2))
    NUM_CFE = Column(String(9))
    DT_DOC = Column(String(100))
    VL_CFE = Column(String(255))
    VL_PIS = Column(String(255))
    VL_COFINS = Column(String(255))
    CNPJ_CPF = Column(String(14))
    NR_SAT = Column(String(9))
    CHV_NFE = Column(String(44))
    VL_DESC = Column(String(255))
    VL_MERC = Column(String(255))
    VL_OUT_DA = Column(String(255))
    VL_ICMS = Column(String(255))
    VL_PIS_ST = Column(String(255))
    VL_COFINS_ST = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsC810(Base):
    __tablename__ = 'sped_pis_cofins_C810'

    ID_REG_C810 = Column(BIGINT(25), primary_key=True)
    ID_REG_C800 = Column(BIGINT(25), nullable=False)
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    CFOP = Column(String(4))
    VL_ITEM = Column(String(255))
    COD_ITEM = Column(String(60))
    CST_PIS = Column(String(2))
    VL_BC_PIS = Column(String(255))
    ALIQ_PIS = Column(String(255))
    VL_PIS = Column(String(255))
    CST_COFINS = Column(String(2))
    VL_BC_COFINS = Column(String(255))
    ALIQ_COFINS = Column(String(255))
    VL_COFINS = Column(String(255))
    COD_CTA = Column(String(60))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsC820(Base):
    __tablename__ = 'sped_pis_cofins_C820'

    ID_REG_C820 = Column(BIGINT(25), primary_key=True)
    ID_REG_C800 = Column(BIGINT(25), nullable=False)
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    CFOP = Column(String(4))
    VL_ITEM = Column(String(255))
    COD_ITEM = Column(String(60))
    CST_PIS = Column(String(2))
    QUANT_BC_PIS = Column(String(255))
    ALIQ_PIS_QUANT = Column(String(255))
    VL_PIS = Column(String(255))
    CST_COFINS = Column(String(2))
    QUANT_BC_COFINS = Column(String(255))
    ALIQ_COFINS_QUANT = Column(String(255))
    VL_COFINS = Column(String(255))
    COD_CTA = Column(String(60))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsC830(Base):
    __tablename__ = 'sped_pis_cofins_C830'

    ID_REG_C830 = Column(BIGINT(25), primary_key=True)
    ID_REG_C800 = Column(BIGINT(25), nullable=False)
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    NUM_PROC = Column(String(20))
    IND_PROC = Column(String(1))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsC860(Base):
    __tablename__ = 'sped_pis_cofins_C860'

    ID_REG_C860 = Column(BIGINT(25), primary_key=True)
    ID_REG_C010 = Column(INTEGER(20))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    COD_MOD = Column(String(2))
    NR_SAT = Column(String(9))
    DT_DOC = Column(String(100))
    DOC_INI = Column(String(9))
    DOC_FIM = Column(String(9))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsC870(Base):
    __tablename__ = 'sped_pis_cofins_C870'

    ID_REG_C870 = Column(BIGINT(25), primary_key=True)
    ID_REG_C860 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    COD_ITEM = Column(String(60))
    CFOP = Column(String(4))
    VL_ITEM = Column(String(255))
    VL_DESC = Column(String(255))
    CST_PIS = Column(String(2))
    VL_BC_PIS = Column(String(255))
    ALIQ_PIS = Column(String(255))
    VL_PIS = Column(String(255))
    CST_COFINS = Column(String(2))
    VL_BC_COFINS = Column(String(255))
    ALIQ_COFINS = Column(String(255))
    VL_COFINS = Column(String(255))
    COD_CTA = Column(String(60))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsC880(Base):
    __tablename__ = 'sped_pis_cofins_C880'

    ID_REG_C880 = Column(BIGINT(25), primary_key=True)
    ID_REG_C860 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    COD_ITEM = Column(String(60))
    CFOP = Column(String(4))
    VL_ITEM = Column(String(255))
    VL_DESC = Column(String(255))
    CST_PIS = Column(String(2))
    QUANT_BC_PIS = Column(String(255))
    ALIQ_PIS_QUANT = Column(String(255))
    VL_PIS = Column(String(255))
    CST_COFINS = Column(String(2))
    QUANT_BC_COFINS = Column(String(255))
    ALIQ_COFINS_QUANT = Column(String(255))
    VL_COFINS = Column(String(255))
    COD_CTA = Column(String(60))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsC890(Base):
    __tablename__ = 'sped_pis_cofins_C890'

    ID_REG_C890 = Column(BIGINT(25), primary_key=True)
    ID_REG_C860 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    NUM_PROC = Column(String(20))
    IND_PROC = Column(String(1))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsC990(Base):
    __tablename__ = 'sped_pis_cofins_C990'

    ID_REG_C990 = Column(BIGINT(25), primary_key=True)
    ID_REG_0000 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    QTD_LIN_C = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsD001(Base):
    __tablename__ = 'sped_pis_cofins_D001'

    ID_REG_D001 = Column(BIGINT(25), primary_key=True)
    ID_REG_0000 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    IND_MOV = Column(String(1))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsD010(Base):
    __tablename__ = 'sped_pis_cofins_D010'

    ID_REG_D010 = Column(BIGINT(25), primary_key=True)
    ID_REG_D001 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    CNPJ = Column(String(14))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsD100(Base):
    __tablename__ = 'sped_pis_cofins_D100'

    ID_REG_D100 = Column(BIGINT(25), primary_key=True)
    ID_REG_D010 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    IND_OPER = Column(String(1))
    IND_EMIT = Column(String(1))
    COD_PART = Column(String(60))
    COD_MOD = Column(String(2))
    COD_SIT = Column(String(2))
    SER = Column(String(4))
    SUB = Column(String(3))
    NUM_DOC = Column(String(9))
    CHV_CTE = Column(String(44))
    DT_DOC = Column(String(100))
    DT_A_P = Column(String(100))
    TP_CTE = Column(String(1))
    CHV_CTE_REF = Column(String(44))
    VL_DOC = Column(String(255))
    VL_DESC = Column(String(255))
    IND_FRT = Column(String(1))
    VL_SERV = Column(String(255))
    VL_BC_ICMS = Column(String(255))
    VL_ICMS = Column(String(255))
    VL_NT = Column(String(255))
    COD_INF = Column(String(6))
    COD_CTA = Column(String(60))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsD101(Base):
    __tablename__ = 'sped_pis_cofins_D101'

    ID_REG_D101 = Column(BIGINT(25), primary_key=True)
    ID_REG_D100 = Column(BIGINT(25), index=True)
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    IND_NAT_FRT = Column(String(1))
    VL_ITEM = Column(String(255))
    CST_PIS = Column(String(2))
    NAT_BC_CRED = Column(String(2))
    VL_BC_PIS = Column(String(255))
    ALIQ_PIS = Column(String(255))
    VL_PIS = Column(String(255))
    COD_CTA = Column(String(60))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsD105(Base):
    __tablename__ = 'sped_pis_cofins_D105'

    ID_REG_D105 = Column(BIGINT(25), primary_key=True)
    ID_REG_D100 = Column(BIGINT(25), index=True)
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    IND_NAT_FRT = Column(String(1))
    VL_ITEM = Column(String(255))
    CST_COFINS = Column(String(2))
    NAT_BC_CRED = Column(String(2))
    VL_BC_COFINS = Column(String(255))
    ALIQ_COFINS = Column(String(255))
    VL_COFINS = Column(String(255))
    COD_CTA = Column(String(60))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsD111(Base):
    __tablename__ = 'sped_pis_cofins_D111'

    ID_REG_D111 = Column(BIGINT(25), primary_key=True)
    ID_REG_D100 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    NUM_PROC = Column(String(20))
    IND_PROC = Column(String(1))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsD200(Base):
    __tablename__ = 'sped_pis_cofins_D200'

    ID_REG_D200 = Column(BIGINT(25), primary_key=True)
    ID_REG_D010 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    COD_MOD = Column(String(2))
    COD_SIT = Column(String(2))
    SER = Column(String(4))
    SUB = Column(String(3))
    NUM_DOC_INI = Column(String(9))
    NUM_DOC_FIN = Column(String(9))
    CFOP = Column(String(4))
    DT_REF = Column(String(100))
    VL_DOC = Column(String(255))
    VL_DESC = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsD201(Base):
    __tablename__ = 'sped_pis_cofins_D201'

    ID_REG_D201 = Column(BIGINT(25), primary_key=True)
    ID_REG_D200 = Column(BIGINT(25), index=True)
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    CST_PIS = Column(String(2))
    VL_ITEM = Column(String(255))
    VL_BC_PIS = Column(String(255))
    ALIQ_PIS = Column(String(255))
    VL_PIS = Column(String(255))
    COD_CTA = Column(String(60))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsD205(Base):
    __tablename__ = 'sped_pis_cofins_D205'

    ID_REG_D205 = Column(BIGINT(25), primary_key=True)
    ID_REG_D200 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    CST_COFINS = Column(String(2))
    VL_ITEM = Column(String(255))
    VL_BC_COFINS = Column(String(255))
    ALIQ_COFINS = Column(String(255))
    VL_COFINS = Column(String(255))
    COD_CTA = Column(String(60))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsD209(Base):
    __tablename__ = 'sped_pis_cofins_D209'

    ID_REG_D209 = Column(BIGINT(25), primary_key=True)
    ID_REG_D200 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    NUM_PROC = Column(String(20))
    IND_PROC = Column(String(1))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsD300(Base):
    __tablename__ = 'sped_pis_cofins_D300'

    ID_REG_D300 = Column(BIGINT(25), primary_key=True)
    ID_REG_D010 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    COD_MOD = Column(String(2))
    SER = Column(String(4))
    SUB = Column(String(3))
    NUM_DOC_INI = Column(String(6))
    NUM_DOC_FIN = Column(String(255))
    CFOP = Column(String(4))
    DT_REF = Column(String(100))
    VL_DOC = Column(String(255))
    VL_DESC = Column(String(255))
    CST_PIS = Column(String(2))
    VL_BC_PIS = Column(String(255))
    ALIQ_PIS = Column(String(255))
    VL_PIS = Column(String(255))
    CST_COFINS = Column(String(2))
    VL_BC_COFINS = Column(String(255))
    ALIQ_COFINS = Column(String(255))
    VL_COFINS = Column(String(255))
    COD_CTA = Column(String(60))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsD309(Base):
    __tablename__ = 'sped_pis_cofins_D309'

    ID_REG_D309 = Column(BIGINT(25), primary_key=True)
    ID_REG_D300 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    NUM_PROC = Column(String(20))
    IND_PROC = Column(String(1))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsD350(Base):
    __tablename__ = 'sped_pis_cofins_D350'

    ID_REG_D350 = Column(BIGINT(25), primary_key=True)
    ID_REG_D010 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    COD_MOD = Column(String(2))
    ECF_MOD = Column(String(20))
    ECF_FAB = Column(String(20))
    DT_DOC = Column(String(100))
    CRO = Column(String(3))
    CRZ = Column(String(6))
    NUM_COO_FIN = Column(String(6))
    GT_FIN = Column(String(255))
    VL_BRT = Column(String(255))
    CST_PIS = Column(String(2))
    VL_BC_PIS = Column(String(255))
    ALIQ_PIS = Column(String(255))
    QUANT_BC_PIS = Column(String(255))
    ALIQ_PIS_QUANT = Column(String(255))
    VL_PIS = Column(String(255))
    CST_COFINS = Column(String(2))
    VL_BC_COFINS = Column(String(255))
    ALIQ_COFINS = Column(String(255))
    QUANT_BC_COFINS = Column(String(255))
    ALIQ_COFINS_QUANT = Column(String(255))
    VL_COFINS = Column(String(255))
    COD_CTA = Column(String(60))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsD359(Base):
    __tablename__ = 'sped_pis_cofins_D359'

    ID_REG_D359 = Column(BIGINT(25), primary_key=True)
    ID_REG_D350 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    NUM_PROC = Column(String(20))
    IND_PROC = Column(String(1))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsD500(Base):
    __tablename__ = 'sped_pis_cofins_D500'

    ID_REG_D500 = Column(BIGINT(25), primary_key=True)
    ID_REG_D010 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    IND_OPER = Column(String(1))
    IND_EMIT = Column(String(1))
    COD_PART = Column(String(60))
    COD_MOD = Column(String(2))
    COD_SIT = Column(String(2))
    SER = Column(String(4))
    SUB = Column(String(3))
    NUM_DOC = Column(String(9))
    DT_DOC = Column(String(100))
    DT_A_P = Column(String(100))
    VL_DOC = Column(String(255))
    VL_DESC = Column(String(255))
    VL_SERV = Column(String(255))
    VL_SERV_NT = Column(String(255))
    VL_TERC = Column(String(255))
    VL_DA = Column(String(255))
    VL_BC_ICMS = Column(String(255))
    VL_ICMS = Column(String(255))
    COD_INF = Column(String(6))
    VL_PIS = Column(String(255))
    VL_COFINS = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsD501(Base):
    __tablename__ = 'sped_pis_cofins_D501'

    ID_REG_D501 = Column(BIGINT(25), primary_key=True)
    ID_REG_D500 = Column(BIGINT(25), index=True)
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    CST_PIS = Column(String(2))
    VL_ITEM = Column(String(255))
    NAT_BC_CRED = Column(String(2))
    VL_BC_PIS = Column(String(255))
    ALIQ_PIS = Column(String(255))
    VL_PIS = Column(String(255))
    COD_CTA = Column(String(60))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsD505(Base):
    __tablename__ = 'sped_pis_cofins_D505'

    ID_REG_D505 = Column(BIGINT(25), primary_key=True)
    ID_REG_D500 = Column(BIGINT(25), index=True)
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    CST_COFINS = Column(String(2))
    VL_ITEM = Column(String(255))
    NAT_BC_CRED = Column(String(2))
    VL_BC_COFINS = Column(String(255))
    ALIQ_COFINS = Column(String(255))
    VL_COFINS = Column(String(255))
    COD_CTA = Column(String(60))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsD509(Base):
    __tablename__ = 'sped_pis_cofins_D509'

    ID_REG_D509 = Column(BIGINT(25), primary_key=True)
    ID_REG_D500 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    NUM_PROC = Column(String(20))
    IND_PROC = Column(String(1))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsD600(Base):
    __tablename__ = 'sped_pis_cofins_D600'

    ID_REG_D600 = Column(BIGINT(25), primary_key=True)
    ID_REG_D010 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    COD_MOD = Column(String(2))
    COD_MUN = Column(String(7))
    SER = Column(String(4))
    SUB = Column(String(3))
    IND_REC = Column(String(1))
    QTD_CONS = Column(String(255))
    DT_DOC_INI = Column(String(100))
    DT_DOC_FIN = Column(String(100))
    VL_DOC = Column(String(255))
    VL_DESC = Column(String(255))
    VL_SERV = Column(String(255))
    VL_SERV_NT = Column(String(255))
    VL_TERC = Column(String(255))
    VL_DA = Column(String(255))
    VL_BC_ICMS = Column(String(255))
    VL_ICMS = Column(String(255))
    VL_PIS = Column(String(255))
    VL_COFINS = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsD601(Base):
    __tablename__ = 'sped_pis_cofins_D601'

    ID_REG_D601 = Column(BIGINT(25), primary_key=True)
    ID_REG_D600 = Column(INTEGER(20))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    COD_CLASS = Column(String(4))
    VL_ITEM = Column(String(255))
    VL_DESC = Column(String(255))
    CST_PIS = Column(String(2))
    VL_BC_PIS = Column(String(255))
    ALIQ_PIS = Column(String(255))
    VL_PIS = Column(String(255))
    COD_CTA = Column(String(60))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsD605(Base):
    __tablename__ = 'sped_pis_cofins_D605'

    ID_REG_D605 = Column(BIGINT(25), primary_key=True)
    ID_REG_D600 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    COD_CLASS = Column(String(4))
    VL_ITEM = Column(String(255))
    VL_DESC = Column(String(255))
    CST_COFINS = Column(String(2))
    VL_BC_COFINS = Column(String(255))
    ALIQ_COFINS = Column(String(255))
    VL_COFINS = Column(String(255))
    COD_CTA = Column(String(60))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsD609(Base):
    __tablename__ = 'sped_pis_cofins_D609'

    ID_REG_D609 = Column(BIGINT(25), primary_key=True)
    ID_REG_D600 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    NUM_PROC = Column(String(20))
    IND_PROC = Column(String(1))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsD990(Base):
    __tablename__ = 'sped_pis_cofins_D990'

    ID_REG_D990 = Column(BIGINT(25), primary_key=True)
    ID_REG_0000 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    QTD_LIN_D = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsF001(Base):
    __tablename__ = 'sped_pis_cofins_F001'

    ID_REG_F001 = Column(BIGINT(25), primary_key=True)
    ID_REG_0000 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    IND_MOV = Column(String(1))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsF010(Base):
    __tablename__ = 'sped_pis_cofins_F010'

    ID_REG_F010 = Column(BIGINT(25), primary_key=True)
    ID_REG_F001 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    CNPJ = Column(String(14))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsF100(Base):
    __tablename__ = 'sped_pis_cofins_F100'

    ID_REG_F100 = Column(BIGINT(25), primary_key=True)
    ID_REG_F010 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    IND_OPER = Column(String(1))
    COD_PART = Column(String(60))
    COD_ITEM = Column(String(60))
    DT_OPER = Column(String(100))
    VL_OPER = Column(String(255))
    CST_PIS = Column(String(2))
    VL_BC_PIS = Column(String(255))
    ALIQ_PIS = Column(String(255))
    VL_PIS = Column(String(255))
    CST_COFINS = Column(String(2))
    VL_BC_COFINS = Column(String(255))
    ALIQ_COFINS = Column(String(255))
    VL_COFINS = Column(String(255))
    NAT_BC_CRED = Column(String(2))
    IND_ORIG_CRED = Column(String(1))
    COD_CTA = Column(String(60))
    COD_CCUS = Column(String(60))
    DESC_DOC_OPER = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsF111(Base):
    __tablename__ = 'sped_pis_cofins_F111'

    ID_REG_F111 = Column(BIGINT(25), primary_key=True)
    ID_REG_F100 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    NUM_PROC = Column(String(20))
    IND_PROC = Column(String(1))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsF120(Base):
    __tablename__ = 'sped_pis_cofins_F120'

    ID_REG_F120 = Column(BIGINT(25), primary_key=True)
    ID_REG_F010 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    NAT_BC_CRED = Column(String(2))
    IDENT_BEM_IMOB = Column(String(2))
    IND_ORIG_CRED = Column(String(1))
    IND_UTIL_BEM_IMOB = Column(String(1))
    VL_OPER_DEP = Column(String(255))
    PARC_OPER_NAO_BC_CRED = Column(String(255))
    CST_PIS = Column(String(2))
    VL_BC_PIS = Column(String(255))
    ALIQ_PIS = Column(String(255))
    VL_PIS = Column(String(255))
    CST_COFINS = Column(String(2))
    VL_BC_COFINS = Column(String(255))
    ALIQ_COFINS = Column(String(255))
    VL_COFINS = Column(String(255))
    COD_CTA = Column(String(60))
    COD_CCUS = Column(String(60))
    DESC_BEM_IMOB = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsF129(Base):
    __tablename__ = 'sped_pis_cofins_F129'

    ID_REG_F129 = Column(BIGINT(25), primary_key=True)
    ID_REG_F120 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    NUM_PROC = Column(String(20))
    IND_PROC = Column(String(1))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsF130(Base):
    __tablename__ = 'sped_pis_cofins_F130'

    ID_REG_F130 = Column(BIGINT(25), primary_key=True)
    ID_REG_F010 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    NAT_BC_CRED = Column(String(2))
    IDENT_BEM_IMOB = Column(String(2))
    IND_ORIG_CRED = Column(String(1))
    IND_UTIL_BEM_IMOB = Column(String(1))
    MES_OPER_AQUIS = Column(String(6))
    VL_OPER_AQUIS = Column(String(255))
    PARC_OPER_NAO_BC_CRED = Column(String(255))
    VL_BC_CRED = Column(String(255))
    IND_NR_PARC = Column(String(1))
    CST_PIS = Column(String(2))
    VL_BC_PIS = Column(String(255))
    ALIQ_PIS = Column(String(255))
    VL_PIS = Column(String(255))
    CST_COFINS = Column(String(2))
    VL_BC_COFINS = Column(String(255))
    ALIQ_COFINS = Column(String(255))
    VL_COFINS = Column(String(255))
    COD_CTA = Column(String(60))
    COD_CCUS = Column(String(60))
    DESC_BEM_IMOB = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsF139(Base):
    __tablename__ = 'sped_pis_cofins_F139'

    ID_REG_F139 = Column(BIGINT(25), primary_key=True)
    ID_REG_F130 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    NUM_PROC = Column(String(20))
    IND_PROC = Column(String(1))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsF150(Base):
    __tablename__ = 'sped_pis_cofins_F150'

    ID_REG_F150 = Column(BIGINT(25), primary_key=True)
    ID_REG_F010 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    NAT_BC_CRED = Column(String(2))
    VL_TOT_EST = Column(String(255))
    EST_IMP = Column(String(255))
    VL_BC_EST = Column(String(255))
    VL_BC_MEN_EST = Column(String(255))
    CST_PIS = Column(String(2))
    ALIQ_PIS = Column(String(255))
    VL_CRED_PIS = Column(String(255))
    CST_COFINS = Column(String(2))
    ALIQ_COFINS = Column(String(255))
    VL_CRED_COFINS = Column(String(255))
    DESC_EST = Column(String(100))
    COD_CTA = Column(String(60))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsF200(Base):
    __tablename__ = 'sped_pis_cofins_F200'

    ID_REG_F200 = Column(BIGINT(25), primary_key=True)
    ID_REG_F010 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    IND_OPER = Column(String(2))
    UNID_IMOB = Column(String(2))
    IDENT_EMP = Column(String(255))
    DESC_UNID_IMOB = Column(String(90))
    NUM_CONT = Column(String(90))
    CPF_CNPJ_ADQU = Column(String(14))
    DT_OPER = Column(String(100))
    VL_TOT_VEND = Column(String(255))
    VL_REC_ACUM = Column(String(255))
    VL_TOT_REC = Column(String(255))
    CST_PIS = Column(String(2))
    VL_BC_PIS = Column(String(255))
    ALIQ_PIS = Column(String(255))
    VL_PIS = Column(String(255))
    CST_COFINS = Column(String(2))
    VL_BC_COFINS = Column(String(255))
    ALIQ_COFINS = Column(String(255))
    VL_COFINS = Column(String(255))
    PERC_REC_RECEB = Column(String(255))
    IND_NAT_EMP = Column(String(1))
    INF_COMP = Column(String(90))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsF205(Base):
    __tablename__ = 'sped_pis_cofins_F205'

    ID_REG_F205 = Column(BIGINT(25), primary_key=True)
    ID_REG_F200 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    VL_CUS_INC_ACUM_ANT = Column(String(255))
    VL_CUS_INC_PER_ESC = Column(String(255))
    VL_CUS_INC_ACUM = Column(String(255))
    VL_EXC_BC_CUS_INC_ACUM = Column(String(255))
    VL_BC_CUS_INC = Column(String(255))
    CST_PIS = Column(String(2))
    ALIQ_PIS = Column(String(255))
    VL_CRED_PIS_ACUM = Column(String(255))
    VL_CRED_PIS_DESC_ANT = Column(String(255))
    VL_CRED_PIS_DESC = Column(String(255))
    VL_CRED_PIS_DESC_FUT = Column(String(255))
    CST_COFINS = Column(String(2))
    ALIQ_COFINS = Column(String(255))
    VL_CRED_COFINS_ACUM = Column(String(255))
    VL_CRED_COFINS_DESC_ANT = Column(String(255))
    VL_CRED_COFINS_DESC = Column(String(255))
    VL_CRED_COFINS_DESC_FUT = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsF210(Base):
    __tablename__ = 'sped_pis_cofins_F210'

    ID_REG_F210 = Column(BIGINT(25), primary_key=True)
    ID_REG_F200 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    VL_CUS_ORC = Column(String(255))
    VL_EXC = Column(String(255))
    VL_CUS_ORC_AJU = Column(String(255))
    VL_BC_CRED = Column(String(255))
    CST_PIS = Column(String(2))
    ALIQ_PIS = Column(String(255))
    VL_CRED_PIS_UTIL = Column(String(255))
    CST_COFINS = Column(String(2))
    ALIQ_COFINS = Column(String(255))
    VL_CRED_COFINS_UTIL = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsF211(Base):
    __tablename__ = 'sped_pis_cofins_F211'

    ID_REG_F211 = Column(BIGINT(25), primary_key=True)
    ID_REG_F200 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    NUM_PROC = Column(String(20))
    IND_PROC = Column(String(1))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsF500(Base):
    __tablename__ = 'sped_pis_cofins_F500'

    ID_REG_F500 = Column(BIGINT(25), primary_key=True)
    ID_REG_F010 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    VL_REC_CAIXA = Column(String(255))
    CST_PIS = Column(String(2))
    VL_DESC_PIS = Column(String(255))
    VL_BC_PIS = Column(String(255))
    ALIQ_PIS = Column(String(255))
    VL_PIS = Column(String(255))
    CST_COFINS = Column(String(2))
    VL_DESC_COFINS = Column(String(255))
    VL_BC_COFINS = Column(String(255))
    ALIQ_COFINS = Column(String(255))
    VL_COFINS = Column(String(255))
    COD_MOD = Column(String(2))
    CFOP = Column(String(4))
    COD_CTA = Column(String(60))
    INFO_COMPL = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsF509(Base):
    __tablename__ = 'sped_pis_cofins_F509'

    ID_REG_F509 = Column(BIGINT(25), primary_key=True)
    ID_REG_F500 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    NUM_PROC = Column(String(20))
    IND_PROC = Column(String(1))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsF510(Base):
    __tablename__ = 'sped_pis_cofins_F510'

    ID_REG_F510 = Column(BIGINT(25), primary_key=True)
    ID_REG_F010 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    VL_REC_CAIXA = Column(String(255))
    CST_PIS = Column(String(2))
    VL_DESC_PIS = Column(String(255))
    QUANT_BC_PIS = Column(String(255))
    ALIQ_PIS_QUANT = Column(String(255))
    VL_PIS = Column(String(255))
    CST_COFINS = Column(String(2))
    VL_DESC_COFINS = Column(String(255))
    QUANT_BC_COFINS = Column(String(255))
    ALIQ_COFINS_QUANT = Column(String(255))
    VL_COFINS = Column(String(255))
    COD_MOD = Column(String(2))
    CFOP = Column(String(4))
    COD_CTA = Column(String(60))
    INFO_COMPL = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsF519(Base):
    __tablename__ = 'sped_pis_cofins_F519'

    ID_REG_F519 = Column(BIGINT(25), primary_key=True)
    ID_REG_F510 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    NUM_PROC = Column(String(20))
    IND_PROC = Column(String(1))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsF525(Base):
    __tablename__ = 'sped_pis_cofins_F525'

    ID_REG_F525 = Column(BIGINT(25), primary_key=True)
    ID_REG_F010 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    VL_REC = Column(String(255))
    IND_REC = Column(String(2))
    CNPJ_CPF = Column(String(14))
    NUM_DOC = Column(String(60))
    COD_ITEM = Column(String(60))
    VL_REC_DET = Column(String(255))
    CST_PIS = Column(String(2))
    CST_COFINS = Column(String(2))
    INFO_COMPL = Column(String(255))
    COD_CTA = Column(String(60))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsF550(Base):
    __tablename__ = 'sped_pis_cofins_F550'

    ID_REG_F550 = Column(BIGINT(25), primary_key=True)
    ID_REG_F010 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    VL_REC_COMP = Column(String(255))
    CST_PIS = Column(String(2))
    VL_DESC_PIS = Column(String(255))
    VL_BC_PIS = Column(String(255))
    ALIQ_PIS = Column(String(255))
    VL_PIS = Column(String(255))
    CST_COFINS = Column(String(2))
    VL_DESC_COFINS = Column(String(255))
    VL_BC_COFINS = Column(String(255))
    ALIQ_COFINS = Column(String(255))
    VL_COFINS = Column(String(255))
    COD_MOD = Column(String(2))
    CFOP = Column(String(4))
    COD_CTA = Column(String(60))
    INFO_COMPL = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsF559(Base):
    __tablename__ = 'sped_pis_cofins_F559'

    ID_REG_F559 = Column(BIGINT(25), primary_key=True)
    ID_REG_F550 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    NUM_PROC = Column(String(20))
    IND_PROC = Column(String(1))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsF560(Base):
    __tablename__ = 'sped_pis_cofins_F560'

    ID_REG_F560 = Column(BIGINT(25), primary_key=True)
    ID_REG_F010 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    VL_REC_COMP = Column(String(255))
    CST_PIS = Column(String(2))
    VL_DESC_PIS = Column(String(255))
    QUANT_BC_PIS = Column(String(255))
    ALIQ_PIS_QUANT = Column(String(255))
    VL_PIS = Column(String(255))
    CST_COFINS = Column(String(2))
    VL_DESC_COFINS = Column(String(255))
    QUANT_BC_COFINS = Column(String(255))
    ALIQ_COFINS_QUANT = Column(String(255))
    VL_COFINS = Column(String(255))
    COD_MOD = Column(String(2))
    CFOP = Column(String(4))
    COD_CTA = Column(String(60))
    INFO_COMPL = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsF569(Base):
    __tablename__ = 'sped_pis_cofins_F569'

    ID_REG_F569 = Column(BIGINT(25), primary_key=True)
    ID_REG_F560 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    NUM_PROC = Column(String(20))
    IND_PROC = Column(String(1))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsF600(Base):
    __tablename__ = 'sped_pis_cofins_F600'

    ID_REG_F600 = Column(BIGINT(25), primary_key=True)
    ID_REG_F010 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    IND_NAT_RET = Column(String(2))
    DT_RET = Column(String(100))
    VL_BC_RET = Column(String(255))
    VL_RET = Column(String(255))
    COD_REC = Column(String(4))
    IND_NAT_REC = Column(String(1))
    CNPJ = Column(String(14))
    VL_RET_PIS = Column(String(255))
    VL_RET_COFINS = Column(String(255))
    IND_DEC = Column(String(1))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsF700(Base):
    __tablename__ = 'sped_pis_cofins_F700'

    ID_REG_F700 = Column(BIGINT(25), primary_key=True)
    ID_REG_F010 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    IND_ORI_DED = Column(String(2))
    IND_NAT_DED = Column(String(1))
    VL_DED_PIS = Column(String(255))
    VL_DED_COFINS = Column(String(255))
    VL_BC_OPER = Column(String(255))
    CNPJ = Column(String(14))
    INF_COMP = Column(String(90))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsF800(Base):
    __tablename__ = 'sped_pis_cofins_F800'

    ID_REG_F800 = Column(BIGINT(25), primary_key=True)
    ID_REG_F010 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    IND_NAT_EVEN = Column(String(2))
    DT_EVEN = Column(String(100))
    CNPJ_SUCED = Column(String(14))
    PA_CONT_CRED = Column(String(6))
    COD_CRED = Column(String(3))
    VL_CRED_PIS = Column(String(255))
    VL_CRED_COFINS = Column(String(255))
    PER_CRED_CIS = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsF990(Base):
    __tablename__ = 'sped_pis_cofins_F990'

    ID_REG_F990 = Column(BIGINT(25), primary_key=True)
    ID_REG_0000 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    QTD_LIN_F = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsI001(Base):
    __tablename__ = 'sped_pis_cofins_I001'

    ID_REG_I001 = Column(BIGINT(25), primary_key=True)
    ID_REG_0000 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    IND_MOV = Column(String(1))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsI010(Base):
    __tablename__ = 'sped_pis_cofins_I010'

    ID_REG_I010 = Column(BIGINT(25), primary_key=True)
    ID_REG_I001 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    CNPJ = Column(String(14))
    IND_ATIV = Column(String(2))
    INFO_COMPL = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsI199(Base):
    __tablename__ = 'sped_pis_cofins_I199'

    ID_REG_I199 = Column(BIGINT(25), primary_key=True)
    ID_REG_I100 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    NUM_PROC = Column(String(20))
    IND_PROC = Column(String(1))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsI200(Base):
    __tablename__ = 'sped_pis_cofins_I200'

    ID_REG_I200 = Column(BIGINT(25), primary_key=True)
    ID_REG_I100 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    NUM_CAMPO = Column(String(2))
    COD_DET = Column(String(5))
    VL_DET = Column(String(255))
    COD_CTA = Column(String(60))
    INF_COMP = Column(String(90))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsI299(Base):
    __tablename__ = 'sped_pis_cofins_I299'

    ID_REG_I299 = Column(BIGINT(25), primary_key=True)
    ID_REG_I200 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    NUM_PROC = Column(String(20))
    IND_PROC = Column(String(1))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsI300(Base):
    __tablename__ = 'sped_pis_cofins_I300'

    ID_REG_I300 = Column(BIGINT(25), primary_key=True)
    ID_REG_I200 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    COD_COMP = Column(String(8))
    VL_COMP = Column(String(255))
    COD_CTA = Column(String(60))
    INF_COMP = Column(String(90))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsI399(Base):
    __tablename__ = 'sped_pis_cofins_I399'

    ID_REG_I399 = Column(BIGINT(25), primary_key=True)
    ID_REG_I300 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    NUM_PROC = Column(String(20))
    IND_PROC = Column(String(1))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsI990(Base):
    __tablename__ = 'sped_pis_cofins_I990'

    ID_REG_I990 = Column(BIGINT(25), primary_key=True)
    ID_REG_0000 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    QTD_LIN_I = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsM001(Base):
    __tablename__ = 'sped_pis_cofins_M001'

    ID_REG_M001 = Column(BIGINT(25), primary_key=True)
    ID_REG_0000 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    IND_MOV = Column(String(1))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsM100(Base):
    __tablename__ = 'sped_pis_cofins_M100'

    ID_REG_M100 = Column(BIGINT(25), primary_key=True)
    ID_REG_M001 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    COD_CRED = Column(String(3))
    IND_CRED_ORI = Column(String(1))
    VL_BC_CRED = Column(String(255))
    ALIQ_PIS = Column(String(255))
    QUANT_BC_PIS = Column(String(255))
    ALIQ_PIS_QUANT = Column(String(255))
    VL_CRED = Column(String(255))
    VL_AJUS_ACRES = Column(String(255))
    VL_AJUS_REDUC = Column(String(255))
    VL_CRED_DIF = Column(String(255))
    VL_CRED_DISP = Column(String(255))
    IND_DESC_CRED = Column(String(1))
    VL_CRED_DESC = Column(String(255))
    SLD_CRED = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsM105(Base):
    __tablename__ = 'sped_pis_cofins_M105'

    ID_REG_M105 = Column(BIGINT(25), primary_key=True)
    ID_REG_M100 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    NAT_BC_CRED = Column(String(2))
    CST_PIS = Column(String(2))
    VL_BC_PIS_TOT = Column(String(255))
    VL_BC_PIS_CUM = Column(String(255))
    VL_BC_PIS_NC = Column(String(255))
    VL_BC_PIS = Column(String(255))
    QUANT_BC_PIS_TOT = Column(String(255))
    QUANT_BC_PIS = Column(String(255))
    DESC_CRED = Column(String(60))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsM110(Base):
    __tablename__ = 'sped_pis_cofins_M110'

    ID_REG_M110 = Column(BIGINT(25), primary_key=True)
    ID_REG_M100 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    IND_AJ = Column(String(1))
    VL_AJ = Column(String(255))
    COD_AJ = Column(String(2))
    NUM_DOC = Column(String(255))
    DESCR_AJ = Column(String(255))
    DT_REF = Column(String(100))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsM115(Base):
    __tablename__ = 'sped_pis_cofins_M115'

    ID_REG_M115 = Column(BIGINT(25), primary_key=True)
    ID_REG_M110 = Column(BIGINT(25), nullable=False)
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    DET_VALOR_AJ = Column(String(255))
    CST_PIS = Column(String(2))
    DET_BC_CRED = Column(String(255))
    DET_ALIQ = Column(String(255))
    DT_OPER_AJ = Column(String(100))
    DESC_AJ = Column(String(255))
    COD_CTA = Column(String(60))
    INFO_COMPL = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsM200(Base):
    __tablename__ = 'sped_pis_cofins_M200'

    ID_REG_M200 = Column(BIGINT(25), primary_key=True)
    ID_REG_M001 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    VL_TOT_CONT_NC_PER = Column(String(255))
    VL_TOT_CRED_DESC = Column(String(255))
    VL_TOT_CRED_DESC_ANT = Column(String(255))
    VL_TOT_CONT_NC_DEV = Column(String(255))
    VL_RET_NC = Column(String(255))
    VL_OUT_DED_NC = Column(String(255))
    VL_CONT_NC_REC = Column(String(255))
    VL_TOT_CONT_CUM_PER = Column(String(255))
    VL_RET_CUM = Column(String(255))
    VL_OUT_DED_CUM = Column(String(255))
    VL_CONT_CUM_REC = Column(String(255))
    VL_TOT_CONT_REC = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsM205(Base):
    __tablename__ = 'sped_pis_cofins_M205'

    ID_REG_M205 = Column(BIGINT(25), primary_key=True)
    ID_REG_M200 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    NUM_CAMPO = Column(String(2))
    COD_REC = Column(String(6))
    VL_DEBITO = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsM210(Base):
    __tablename__ = 'sped_pis_cofins_M210'

    ID_REG_M210 = Column(BIGINT(25), primary_key=True)
    ID_REG_M200 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    COD_CONT = Column(String(2))
    VL_REC_BRT = Column(String(255))
    VL_BC_CONT = Column(String(255))
    VL_AJUS_ACRES_BC_PIS = Column(String(255))
    VL_AJUS_REDUC_BC_PIS = Column(String(255))
    VL_BC_CONT_AJUS = Column(String(255))
    ALIQ_PIS = Column(String(255))
    QUANT_BC_PIS = Column(String(255))
    ALIQ_PIS_QUANT = Column(String(255))
    VL_CONT_APUR = Column(String(255))
    VL_AJUS_ACRES = Column(String(255))
    VL_AJUS_REDUC = Column(String(255))
    VL_CONT_DIFER = Column(String(255))
    VL_CONT_DIFER_ANT = Column(String(255))
    VL_CONT_PER = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsM211(Base):
    __tablename__ = 'sped_pis_cofins_M211'

    ID_REG_M211 = Column(BIGINT(25), primary_key=True)
    ID_REG_M210 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    IND_TIP_COOP = Column(String(2))
    VL_BC_CONT_ANT_EXC_COOP = Column(String(255))
    VL_EXC_COOP_GER = Column(String(255))
    VL_EXC_ESP_COOP = Column(String(255))
    VL_BC_CONT = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsM220(Base):
    __tablename__ = 'sped_pis_cofins_M220'

    ID_REG_M220 = Column(BIGINT(25), primary_key=True)
    ID_REG_M210 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    IND_AJ = Column(String(1))
    VL_AJ = Column(String(255))
    COD_AJ = Column(String(2))
    NUM_DOC = Column(String(255))
    DESCR_AJ = Column(String(255))
    DT_REF = Column(String(100))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsM225(Base):
    __tablename__ = 'sped_pis_cofins_M225'

    ID_REG_M225 = Column(BIGINT(25), primary_key=True)
    ID_REG_M220 = Column(BIGINT(25), nullable=False)
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    DET_VALOR_AJ = Column(String(255))
    CST_PIS = Column(String(2))
    DET_BC_CRED = Column(String(255))
    DET_ALIQ = Column(String(255))
    DT_OPER_AJ = Column(String(100))
    DESC_AJ = Column(String(255))
    COD_CTA = Column(String(60))
    INFO_COMPL = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsM230(Base):
    __tablename__ = 'sped_pis_cofins_M230'

    ID_REG_M230 = Column(BIGINT(25), primary_key=True)
    ID_REG_M210 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    CNPJ = Column(String(14))
    VL_VEND = Column(String(255))
    VL_NAO_RECEB = Column(String(255))
    VL_CONT_DIF = Column(String(255))
    VL_CRED_DIF = Column(String(255))
    COD_CRED = Column(String(3))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsM300(Base):
    __tablename__ = 'sped_pis_cofins_M300'

    ID_REG_M300 = Column(BIGINT(25), primary_key=True)
    ID_REG_M001 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    COD_CONT = Column(String(2))
    VL_CONT_APUR_DIFER = Column(String(255))
    NAT_CRED_DESC = Column(String(2))
    VL_CRED_DESC_DIFER = Column(String(255))
    VL_CONT_DIFER_ANT = Column(String(255))
    PER_APUR = Column(String(6))
    DT_RECEB = Column(String(100))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsM350(Base):
    __tablename__ = 'sped_pis_cofins_M350'

    ID_REG_M350 = Column(BIGINT(25), primary_key=True)
    ID_REG_M001 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    VL_TOT_FOL = Column(String(255))
    VL_EXC_BC = Column(String(255))
    VL_TOT_BC = Column(String(255))
    ALIQ_PIS_FOL = Column(String(255))
    VL_TOT_CONT_FOL = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsM400(Base):
    __tablename__ = 'sped_pis_cofins_M400'

    ID_REG_M400 = Column(BIGINT(25), primary_key=True)
    ID_REG_M001 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    CST_PIS = Column(String(2))
    VL_TOT_REC = Column(String(255))
    COD_CTA = Column(String(60))
    DESC_COMPL = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsM410(Base):
    __tablename__ = 'sped_pis_cofins_M410'

    ID_REG_M410 = Column(BIGINT(25), primary_key=True)
    ID_REG_M400 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    NAT_REC = Column(String(3))
    VL_REC = Column(String(255))
    COD_CTA = Column(String(60))
    DESC_COMPL = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsM500(Base):
    __tablename__ = 'sped_pis_cofins_M500'

    ID_REG_M500 = Column(BIGINT(25), primary_key=True)
    ID_REG_M001 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    COD_CRED = Column(String(3))
    IND_CRED_ORI = Column(String(1))
    VL_BC_CRED = Column(String(255))
    ALIQ_COFINS = Column(String(255))
    QUANT_BC_COFINS = Column(String(255))
    ALIQ_COFINS_QUANT = Column(String(255))
    VL_CRED = Column(String(255))
    VL_AJUS_ACRES = Column(String(255))
    VL_AJUS_REDUC = Column(String(255))
    VL_CRED_DIF = Column(String(255))
    VL_CRED_DISP = Column(String(255))
    IND_DESC_CRED = Column(String(1))
    VL_CRED_DESC = Column(String(255))
    SLD_CRED = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsM505(Base):
    __tablename__ = 'sped_pis_cofins_M505'

    ID_REG_M505 = Column(BIGINT(25), primary_key=True)
    ID_REG_M500 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    NAT_BC_CRED = Column(String(2))
    CST_COFINS = Column(String(2))
    VL_BC_COFINS_TOT = Column(String(255))
    VL_BC_COFINS_CUM = Column(String(255))
    VL_BC_COFINS_NC = Column(String(255))
    VL_BC_COFINS = Column(String(255))
    QUANT_BC_COFINS_TOT = Column(String(255))
    QUANT_BC_COFINS = Column(String(255))
    DESC_CRED = Column(String(60))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsM510(Base):
    __tablename__ = 'sped_pis_cofins_M510'

    ID_REG_M510 = Column(BIGINT(25), primary_key=True)
    ID_REG_M500 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    IND_AJ = Column(String(1))
    VL_AJ = Column(String(255))
    COD_AJ = Column(String(2))
    NUM_DOC = Column(String(255))
    DESCR_AJ = Column(String(255))
    DT_REF = Column(String(100))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsM515(Base):
    __tablename__ = 'sped_pis_cofins_M515'

    ID_REG_M515 = Column(BIGINT(25), primary_key=True)
    ID_REG_M510 = Column(BIGINT(25), nullable=False)
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    DET_VALOR_AJ = Column(String(255))
    CST_COFINS = Column(String(2))
    DET_BC_CRED = Column(String(255))
    DET_ALIQ = Column(String(255))
    DT_OPER_AJ = Column(String(100))
    DESC_AJ = Column(String(255))
    COD_CTA = Column(String(60))
    INFO_COMPL = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsM600(Base):
    __tablename__ = 'sped_pis_cofins_M600'

    ID_REG_M600 = Column(BIGINT(25), primary_key=True)
    ID_REG_M001 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    VL_TOT_CONT_NC_PER = Column(String(255))
    VL_TOT_CRED_DESC = Column(String(255))
    VL_TOT_CRED_DESC_ANT = Column(String(255))
    VL_TOT_CONT_NC_DEV = Column(String(255))
    VL_RET_NC = Column(String(255))
    VL_OUT_DED_NC = Column(String(255))
    VL_CONT_NC_REC = Column(String(255))
    VL_TOT_CONT_CUM_PER = Column(String(255))
    VL_RET_CUM = Column(String(255))
    VL_OUT_DED_CUM = Column(String(255))
    VL_CONT_CUM_REC = Column(String(255))
    VL_TOT_CONT_REC = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsM605(Base):
    __tablename__ = 'sped_pis_cofins_M605'

    ID_REG_M605 = Column(BIGINT(25), primary_key=True)
    ID_REG_M600 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    NUM_CAMPO = Column(String(2))
    COD_REC = Column(String(6))
    VL_DEBITO = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsM610(Base):
    __tablename__ = 'sped_pis_cofins_M610'

    ID_REG_M610 = Column(BIGINT(25), primary_key=True)
    ID_REG_M600 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    COD_CONT = Column(String(2))
    VL_REC_BRT = Column(String(255))
    VL_BC_CONT = Column(String(255))
    VL_AJUS_ACRES_BC_COFINS = Column(String(255))
    VL_AJUS_REDUC_BC_COFINS = Column(String(255))
    VL_BC_CONT_AJUS = Column(String(255))
    ALIQ_COFINS = Column(String(255))
    QUANT_BC_COFINS = Column(String(255))
    ALIQ_COFINS_QUANT = Column(String(255))
    VL_CONT_APUR = Column(String(255))
    VL_AJUS_ACRES = Column(String(255))
    VL_AJUS_REDUC = Column(String(255))
    VL_CONT_DIFER = Column(String(255))
    VL_CONT_DIFER_ANT = Column(String(255))
    VL_CONT_PER = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsM611(Base):
    __tablename__ = 'sped_pis_cofins_M611'

    ID_REG_M611 = Column(BIGINT(25), primary_key=True)
    ID_REG_M610 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    IND_TIP_COOP = Column(String(2))
    VL_BC_CONT_ANT_EXC_COOP = Column(String(255))
    VL_EXC_COOP_GER = Column(String(255))
    VL_EXC_ESP_COOP = Column(String(255))
    VL_BC_CONT = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsM620(Base):
    __tablename__ = 'sped_pis_cofins_M620'

    ID_REG_M620 = Column(BIGINT(25), primary_key=True)
    ID_REG_M610 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    IND_AJ = Column(String(1))
    VL_AJ = Column(String(255))
    COD_AJ = Column(String(2))
    NUM_DOC = Column(String(255))
    DESCR_AJ = Column(String(255))
    DT_REF = Column(String(100))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsM625(Base):
    __tablename__ = 'sped_pis_cofins_M625'

    ID_REG_M625 = Column(BIGINT(25), primary_key=True)
    ID_REG_M620 = Column(BIGINT(25), nullable=False)
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    DET_VALOR_AJ = Column(String(255))
    CST_COFINS = Column(String(2))
    DET_BC_CRED = Column(String(255))
    DET_ALIQ = Column(String(255))
    DT_OPER_AJ = Column(String(100))
    DESC_AJ = Column(String(255))
    COD_CTA = Column(String(60))
    INFO_COMPL = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsM630(Base):
    __tablename__ = 'sped_pis_cofins_M630'

    ID_REG_M630 = Column(BIGINT(25), primary_key=True)
    ID_REG_M610 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    CNPJ = Column(String(14))
    VL_VEND = Column(String(255))
    VL_NAO_RECEB = Column(String(255))
    VL_CONT_DIF = Column(String(255))
    VL_CRED_DIF = Column(String(255))
    COD_CRED = Column(String(3))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsM700(Base):
    __tablename__ = 'sped_pis_cofins_M700'

    ID_REG_M700 = Column(BIGINT(25), primary_key=True)
    ID_REG_M001 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    COD_CONT = Column(String(2))
    VL_CONT_APUR_DIFER = Column(String(255))
    NAT_BC_CRED_DESC = Column(String(2))
    VL_CRED_DESC_DIFER = Column(String(255))
    VL_CONT_DIFER_ANT = Column(String(255))
    PER_APUR = Column(String(6))
    DT_RECEB = Column(String(100))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsM800(Base):
    __tablename__ = 'sped_pis_cofins_M800'

    ID_REG_M800 = Column(BIGINT(25), primary_key=True)
    ID_REG_M001 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    CST_COFINS = Column(String(2))
    VL_TOT_REC = Column(String(255))
    COD_CTA = Column(String(60))
    DESC_COMPL = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsM810(Base):
    __tablename__ = 'sped_pis_cofins_M810'

    ID_REG_M810 = Column(BIGINT(25), primary_key=True)
    ID_REG_M800 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    NAT_REC = Column(String(3))
    VL_REC = Column(String(255))
    COD_CTA = Column(String(60))
    DESC_COMPL = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsM990(Base):
    __tablename__ = 'sped_pis_cofins_M990'

    ID_REG_M990 = Column(BIGINT(25), primary_key=True)
    ID_REG_0000 = Column(BIGINT(25))
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    QTD_LIN_M = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsP001(Base):
    __tablename__ = 'sped_pis_cofins_P001'

    ID_REG_P001 = Column(BIGINT(25), primary_key=True)
    ID_REG_0000 = Column(BIGINT(25), nullable=False)
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(5))
    IND_MOV = Column(String(5))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsP010(Base):
    __tablename__ = 'sped_pis_cofins_P010'

    ID_REG_P010 = Column(BIGINT(25), primary_key=True)
    ID_REG_P001 = Column(BIGINT(25), nullable=False)
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    CNPJ = Column(String(14))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsP100(Base):
    __tablename__ = 'sped_pis_cofins_P100'

    ID_REG_P100 = Column(BIGINT(25), primary_key=True)
    ID_REG_P010 = Column(BIGINT(25), nullable=False)
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    DT_FIN = Column(String(15))
    DT_INI = Column(String(15))
    VL_REC_TOT_EST = Column(String(21))
    COD_ATIV_ECON = Column(String(8))
    VL_REC_ATIV_ESTAB = Column(String(21))
    VL_EXC = Column(String(21))
    VL_BC_CONT = Column(String(21))
    ALIQ_CONT = Column(String(12))
    VL_CONT_APU = Column(String(21))
    COD_CTA = Column(String(60))
    INFO_COMPL = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsP110(Base):
    __tablename__ = 'sped_pis_cofins_P110'

    ID_REG_P110 = Column(BIGINT(25), primary_key=True)
    ID_REG_P100 = Column(BIGINT(25), nullable=False)
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    NUM_CAMPO = Column(String(2))
    COD_DET = Column(String(8))
    DET_VALOR = Column(String(255))
    INF_COMPL = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsP199(Base):
    __tablename__ = 'sped_pis_cofins_P199'

    ID_REG_P199 = Column(BIGINT(25), primary_key=True)
    ID_REG_P100 = Column(BIGINT(25), nullable=False)
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    NUM_PROC = Column(String(20))
    IND_PROC = Column(String(1))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsP200(Base):
    __tablename__ = 'sped_pis_cofins_P200'

    ID_REG_P200 = Column(BIGINT(25), primary_key=True)
    ID_REG_P001 = Column(BIGINT(25), nullable=False)
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    PER_REF = Column(String(6))
    VL_TOT_CONT_APU = Column(String(255))
    VL_TOT_AJ_REDUC = Column(String(255))
    VL_TOT_AJ_ACRES = Column(String(255))
    VL_TOT_CONT_DEV = Column(String(255))
    COD_REC = Column(String(6))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsP210(Base):
    __tablename__ = 'sped_pis_cofins_P210'

    ID_REG_P210 = Column(BIGINT(25), primary_key=True)
    ID_REG_P200 = Column(BIGINT(25), nullable=False)
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    IND_AJ = Column(String(1))
    VL_AJ = Column(String(255))
    COD_AJ = Column(String(2))
    NUM_DOC = Column(String(255))
    DESCR_AJ = Column(String(255))
    DT_REF = Column(String(100))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsP990(Base):
    __tablename__ = 'sped_pis_cofins_P990'

    ID_REG_P990 = Column(BIGINT(25), primary_key=True)
    ID_REG_0000 = Column(BIGINT(25), nullable=False)
    LINHA = Column(INTEGER(20), nullable=False)
    REG = Column(String(4))
    QTD_LIN_P = Column(String(255))
    ID_EFD_CTRL_REG_0000 = Column(INTEGER(11))


class SpedPisCofinsCtrl(Base):
    __tablename__ = 'sped_pis_cofins_ctrl'
    __table_args__ = (
        Index('IDX_CANCELAMENTO', 'DATA_INI', 'DATA_FIM', 'CNPJ'),
    )

    ID = Column(INTEGER(11), primary_key=True)
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11), index=True)
    DATA_INI = Column(Date)
    DATA_FIM = Column(Date)
    CNPJ = Column(CHAR(14))
    DATA_HORA = Column(DateTime)
    TIPO = Column(String(20))
    ENVIO = Column(INTEGER(1))
    CANCELADO = Column(INTEGER(1))
    RAZAO_SOCIAL = Column(String(255))
    RETIFICADOR = Column(INTEGER(1))
    NOME_ARQUIVO = Column(String(255))
    DW_ENTRADAS = Column(INTEGER(1))
    DW_SAIDAS = Column(INTEGER(1))
    DW_NTOMADOS = Column(INTEGER(1))
    DW_TOMADOS = Column(INTEGER(1))
    TRANSMISSAO_PVA = Column(TIMESTAMP)


class SpedfisRegE310012017(Base):
    __tablename__ = 'spedfis_reg_E310_01_2017'

    ID_SPEDFIS_REG_E310 = Column(BIGINT(25), primary_key=True, nullable=False)
    ID_SPEDFIS_REG_E300 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    IND_MOV_FCP_DIFAL = Column(String(1))
    VL_SLD_CRED_ANT_DIFAL = Column(String(30), primary_key=True, nullable=False)
    VL_TOT_DEBITOS_DIFAL = Column(String(255))
    VL_OUT_DEB_DIFAL = Column(String(255))
    VL_TOT_CREDITOS_DIFAL = Column(String(255))
    VL_OUT_CRED_DIFAL = Column(String(255))
    VL_SLD_DEV_ANT_DIFAL = Column(String(255))
    VL_DEDUÇÕES_DIFAL = Column(String(255))
    VL_RECOL_DIFAL = Column(String(255))
    VL_SLD_CRED_TRANSPORTAR_DIFAL = Column(String(255))
    DEB_ESP_DIFAL = Column(String(255))
    VL_SLD_CRED_ANT_FCP = Column(String(255))
    VL_TOT_DEB_FCP = Column(String(255))
    VL_OUT_DEB_FCP = Column(String(255))
    VL_TOT_CRED_FCP = Column(String(255))
    VL_OUT_CRED_FCP = Column(String(255))
    VL_SLD_DEV_ANT_FCP = Column(String(255))
    VL_DEDUÇÕES_FCP = Column(String(255))
    VL_RECOL_FCP = Column(String(255))
    VL_SLD_CRED_TRANSPORTAR_FCP = Column(String(255))
    DEB_ESP_FCP = Column(String(255))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class SpedfisRegE310122016(Base):
    __tablename__ = 'spedfis_reg_E310_12_2016'

    ID_SPEDFIS_REG_E310 = Column(BIGINT(25), primary_key=True)
    ID_SPEDFIS_REG_E300 = Column(BIGINT(25), nullable=False, index=True)
    LINHA = Column(DECIMAL(20, 0), nullable=False)
    REG = Column(String(4))
    IND_MOV_DIFAL = Column(String(1))
    VL_SLD_CRED_ANT_DIFAL = Column(String(30))
    VL_TOT_DEBITOS_DIFAL = Column(String(30))
    VL_OUT_DEB_DIFAL = Column(String(30))
    VL_TOT_DEB_FCP = Column(String(30))
    VL_TOT_CREDITOS_DIFAL = Column(String(30))
    VL_TOT_CRED_FCP = Column(String(30))
    VL_OUT_CRED_DIFAL = Column(String(30))
    VL_SLD_DEV_ANT_DIFAL = Column(String(30))
    VL_DEDUCOES_DIFAL = Column(String(30))
    VL_RECOL = Column(String(30))
    VL_SLD_CRED_TRANSPORTAR = Column(String(30))
    DEB_ESP_DIFAL = Column(String(30))
    ID_SPEDFIS_CTRL_REG_0000 = Column(INTEGER(11))


class TbDctf(Base):
    __tablename__ = 'tb_dctf'

    id_dctf = Column(INTEGER(11), primary_key=True)
    id_arqui = Column(INTEGER(11), nullable=False)
    nom_cnpj = Column(String(25), nullable=False)
    nom_grupo_tribu = Column(String(255), nullable=False)
    nom_codig_recei = Column(String(255), nullable=False)
    nom_perio = Column(String(255), nullable=False)
    nom_perio_apura = Column(String(255), nullable=False)
    nom_pagam_darf = Column(String(255))
    nom_debit_apura = Column(String(255))
    nom_pagam = Column(String(255))
    nom_compe = Column(String(255))
    nom_parce = Column(String(255))
    nom_suspe = Column(String(255))
    num_pagin = Column(INTEGER(11), nullable=False)


class TbDctfArquivo(Base):
    __tablename__ = 'tb_dctf_arquivo'

    id_arqui = Column(INTEGER(11), primary_key=True)
    nom_arqui = Column(String(1000), nullable=False)
    dat_envio = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    tip_emp = Column(String(255))
    cnpj = Column(String(255))


class TbDctfCapa(Base):
    __tablename__ = 'tb_dctf_capa'

    id = Column(INTEGER(11), primary_key=True)
    nomeContribuinte = Column(String(50))
    ctCnpj = Column(INTEGER(14))
    perApuracao = Column(String(7))
    dataHoraTransmissao = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    numRecibo = Column(String(14))
    itemEFD = Column(String(50))
    classTrib = Column(Text)
    indRetificacao = Column(String(30))
    numReciboRetificacao = Column(BIGINT(14))
    tpLogradouro = Column(String(15))
    cadLogradouro = Column(String(50))
    cadNumero = Column(INTEGER(5))
    cadComplemento = Column(String(255))
    cadBairro = Column(String(50))
    cadMunicipio = Column(String(35))
    cadUF = Column(String(2))
    cadCep = Column(INTEGER(8), nullable=False)
    cadTelefone = Column(String(20))
    cadEmail = Column(String(30))
    respNome = Column(String(35))
    respCPF = Column(BIGINT(11), nullable=False)
    respTelefone = Column(String(20))
    respEmail = Column(String(30))
    contatoNome = Column(String(35))
    contatoCPF = Column(BIGINT(11), nullable=False)
    contatoTelefone = Column(String(20))
    contatoEmail = Column(String(30))


class TbDctfItem(Base):
    __tablename__ = 'tb_dctf_item'

    id = Column(INTEGER(11), primary_key=True)
    codReceita = Column(String(8))
    ctDescricaoTributo = Column(String(255))
    ctCnpj = Column(BIGINT(14))
    ctValor = Column(Float(asdecimal=True))
    vlTotalCred = Column(Float(asdecimal=True))
    saldoaPagar = Column(Float(asdecimal=True))
    suspensoesVinculadas = Column(Text)
    idDctfCapa = Column(INTEGER(11))


class TbDctfLog(Base):
    __tablename__ = 'tb_dctf_log'

    id_log = Column(INTEGER(11), primary_key=True)
    id_arqui = Column(INTEGER(11), nullable=False)
    nom_log = Column(String(500), nullable=False)
    num_pagin = Column(INTEGER(11), nullable=False)
