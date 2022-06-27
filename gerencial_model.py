# coding: utf-8
from sqlalchemy import CHAR, Column, DECIMAL, Date, DateTime, Float, JSON, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import BIGINT, CHAR, INTEGER, LONGTEXT, TEXT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class APURACAOCREDITOSPISCOFINS(Base):
    __tablename__ = 'APURACAO_CREDITOS_PIS_COFINS'

    DATA_INI = Column(Date)
    CNPJ = Column(CHAR(14))
    M100_M500 = Column(VARCHAR(4), nullable=False, server_default=text("''"))
    COD_CRED = Column(VARCHAR(3))
    DESC_COD_CRED = Column(VARCHAR(512))
    IND_CRED_ORI = Column(VARCHAR(1))
    VL_BC_CRED = Column(VARCHAR(255))
    ALIQ_PIS = Column(VARCHAR(255))
    QUANT_BC_PIS = Column(VARCHAR(255))
    ALIQ_PIS_QUANT = Column(VARCHAR(255))
    VL_CRED = Column(VARCHAR(255))
    VL_AJUS_ACRES = Column(VARCHAR(255))
    VL_AJUS_REDUC = Column(VARCHAR(255))
    VL_CRED_DIF = Column(VARCHAR(255))
    VL_CRED_DISP = Column(VARCHAR(255))
    IND_DESC_CRED = Column(VARCHAR(1))
    VL_CRED_DESC = Column(VARCHAR(255))
    SLD_CRED = Column(VARCHAR(255))
    ID = Column(INTEGER(11), primary_key=True)


t_APURACAO_DEBITOS_PIS_COFINS = Table(
    'APURACAO_DEBITOS_PIS_COFINS', metadata,
    Column('CNPJ', CHAR(14)),
    Column('DATA_INI', Date),
    Column('M200_M600', VARCHAR(4), nullable=False, server_default=text("''")),
    Column('VL_TOT_CONT_NC_PER', VARCHAR(255)),
    Column('VL_TOT_CRED_DESC', VARCHAR(255)),
    Column('VL_TOT_CRED_DESC_ANT', VARCHAR(255)),
    Column('VL_TOT_CONT_NC_DEV', VARCHAR(255)),
    Column('VL_RET_NC', VARCHAR(255)),
    Column('VL_OUT_DED_NC', VARCHAR(255)),
    Column('VL_CONT_NC_REC', VARCHAR(255)),
    Column('VL_TOT_CONT_CUM_PER', VARCHAR(255)),
    Column('VL_RET_CUM', VARCHAR(255)),
    Column('VL_OUT_DED_CUM', VARCHAR(255)),
    Column('VL_CONT_CUM_REC', VARCHAR(255)),
    Column('VL_TOT_CONT_REC', VARCHAR(255))
)


t_BALANCETE_GERAL_ONCO = Table(
    'BALANCETE_GERAL_ONCO', metadata,
    Column('ID_BALANCETE_GERAL', INTEGER(11), nullable=False, server_default=text("'0'")),
    Column('DT_FIN', Date),
    Column('DT_ESCRIT', VARCHAR(10)),
    Column('COD_NAT', VARCHAR(2)),
    Column('COD_CTA', VARCHAR(255)),
    Column('CTA', VARCHAR(255)),
    Column('COD_CCUS', VARCHAR(255)),
    Column('VL_SLD_INI', VARCHAR(30)),
    Column('IND_DC_INI', VARCHAR(1)),
    Column('VL_DEB', VARCHAR(30)),
    Column('VL_CRED', VARCHAR(30)),
    Column('VL_SLD_FIN', VARCHAR(30)),
    Column('VL_SLD_FIN_I355', VARCHAR(30)),
    Column('IND_DC_FIN', VARCHAR(1)),
    Column('ID_SPEDCONT_CTRL_REG_0000', INTEGER(11)),
    Column('CNPJ', String(255))
)


t_CTRL_PIS_COFINS = Table(
    'CTRL_PIS_COFINS', metadata,
    Column('DATA_INI', Date),
    Column('CNPJ', CHAR(14))
)


t_DCTF_GERAL_ONCO = Table(
    'DCTF_GERAL_ONCO', metadata,
    Column('ID_ARQUIVO', INTEGER(11), nullable=False),
    Column('CNPJ', VARCHAR(25), nullable=False),
    Column('GRUPO_TRIBUTO', VARCHAR(255)),
    Column('CODIGO_RECEITA', VARCHAR(255)),
    Column('CODIGO_RECEITA_TB_DARF', String(255)),
    Column('PERIODICIDADE', VARCHAR(255)),
    Column('PERIODICIDADE_APUCARACAO', VARCHAR(255)),
    Column('TOTAL_DARF', Float(asdecimal=True)),
    Column('DEBITO_APURACAO', VARCHAR(255)),
    Column('TOTAL_PAGAMENTO', Float(asdecimal=True)),
    Column('COMPENSACOES', DECIMAL(15, 2)),
    Column('PARCELAMENTO', DECIMAL(15, 2)),
    Column('SUSPENSAO', DECIMAL(15, 2))
)


t_EFD_GERAL_ONCO = Table(
    'EFD_GERAL_ONCO', metadata,
    Column('ID', INTEGER(11), nullable=False, server_default=text("'0'")),
    Column('DATA_INI', Date),
    Column('IND_OPER', String(1)),
    Column('REGISTRO', VARCHAR(4), nullable=False, server_default=text("''")),
    Column('CNPJ_FILIAL', String(14)),
    Column('COD_PART', String(60)),
    Column('CNPJ_PART', String(125)),
    Column('RAZAO_PART', String(125)),
    Column('UF_PART', String(2)),
    Column('CHV_NFE', String(44)),
    Column('VL_DOC', DECIMAL(30, 2)),
    Column('DT_DOC', String(80)),
    Column('NUM_DOC', String(200)),
    Column('DT_E_S', String(80)),
    Column('VL_ITEM', DECIMAL(30, 2)),
    Column('DESCR_COMPL', String(255)),
    Column('COD_ITEM', String(60)),
    Column('DESCR_0200', String(265)),
    Column('COD_NCM_REG_0200', String(265)),
    Column('CFOP', String(4)),
    Column('INF_CFOP', String(267)),
    Column('VL_BC_PIS', String(255)),
    Column('ALIQ_PIS', String(255)),
    Column('VL_PIS', String(255)),
    Column('CST_PIS', String(50)),
    Column('VL_BC_COFINS', String(80)),
    Column('ALIQ_COFINS', String(80)),
    Column('VL_COFINS', String(80)),
    Column('CST_COFINS', String(50)),
    Column('COD_CTA', String(60)),
    Column('DESC_CONTA_ECD', String(100)),
    Column('ID_EFD_CTRL_REG_0000', String(255))
)


t_F500_GERAL_ONCO = Table(
    'F500_GERAL_ONCO', metadata,
    Column('DATA_INI', Date),
    Column('CNPJ', VARCHAR(14)),
    Column('REG', VARCHAR(4)),
    Column('VL_REC_CAIXA', VARCHAR(255)),
    Column('CST_PIS', VARCHAR(2)),
    Column('VL_DESC_PIS', VARCHAR(255)),
    Column('VL_BC_PIS', VARCHAR(255)),
    Column('ALIQ_PIS', VARCHAR(255)),
    Column('VL_PIS', VARCHAR(255)),
    Column('CST_COFINS', VARCHAR(2)),
    Column('VL_DESC_COFINS', VARCHAR(255)),
    Column('VL_BC_COFINS', VARCHAR(255)),
    Column('ALIQ_COFINS', VARCHAR(255)),
    Column('VL_COFINS', VARCHAR(255)),
    Column('COD_MOD', VARCHAR(2)),
    Column('CFOP', VARCHAR(4)),
    Column('COD_CTA', VARCHAR(60)),
    Column('INFO_COMPL', VARCHAR(255))
)


t_RAZAO_GERAL_ONCO = Table(
    'RAZAO_GERAL_ONCO', metadata,
    Column('ID_RAZAO_04', INTEGER(15), nullable=False, server_default=text("'0'")),
    Column('CNPJ', String(20)),
    Column('DATA_LCTO_CONT', Date),
    Column('IND_LCTO', VARCHAR(12), server_default=text("''")),
    Column('COD_CONTA_CONT', VARCHAR(255)),
    Column('DESCRICAO_CTA_CONT', VARCHAR(255)),
    Column('COD_CENTRO_CUSTO', VARCHAR(255)),
    Column('DESCRICAO_CENTRO_CUSTO', VARCHAR(255)),
    Column('VALOR_PARTIDA', DECIMAL(15, 2)),
    Column('NATUREZA_PARTIDA', VARCHAR(1)),
    Column('NUMERO_LOC_LANCAMENTOS', VARCHAR(255)),
    Column('COD_HIST_PADRAO', VARCHAR(255)),
    Column('DESCR_HISTORICO_PADRAO', VARCHAR(255)),
    Column('HISTORIO_PARTIDA', LONGTEXT),
    Column('COD_PARTICIPANTE', VARCHAR(255)),
    Column('COD_CTA', VARCHAR(255), index=True),
    Column('COD_NAT', VARCHAR(2)),
    Column('DEB./CRED.', VARCHAR(255), server_default=text("''")),
    Column('ACHEI_NO_DEB', INTEGER(1)),
    Column('ACHEI_NO_CRED', INTEGER(1)),
    Column('ID_SPEDCONT_CTRL_REG_0000', INTEGER(11))
)


t_TEMP_ZERAR_RAZAO_04 = Table(
    'TEMP_ZERAR_RAZAO_04', metadata,
    Column('ID_RAZAO_04', INTEGER(15)),
    Column('VALOR_PARTIDA', DECIMAL(15, 2)),
    Column('NATUREZA_PARTIDA', VARCHAR(1), index=True),
    Column('COD_CTA', VARCHAR(255), index=True),
    Column('ID_SPEDCONT_CTRL_REG_0000', INTEGER(15))
)


t_TESTE_DW_ENTRADAS_ICMS = Table(
    'TESTE_DW_ENTRADAS_ICMS', metadata,
    Column('ID_ITEM', BIGINT(25), nullable=False),
    Column('CHV_PK', VARCHAR(55)),
    Column('DATA_INI', Date),
    Column('CNPJ_FILIAL', CHAR(14)),
    Column('RAZAO_FILIAL', VARCHAR(255)),
    Column('UF_FILIAL', CHAR(2)),
    Column('REGISTRO', VARCHAR(4)),
    Column('CHV_NFE_CTE', VARCHAR(44)),
    Column('VL_BC_ICMS', VARCHAR(30)),
    Column('VL_ICMS', VARCHAR(30)),
    Column('VL_DOC', DECIMAL(15, 2)),
    Column('COD_PART', VARCHAR(65)),
    Column('D_PART_REG_0150', VARCHAR(255)),
    Column('RAZAO_PART', VARCHAR(255)),
    Column('CNPJ_PART', VARCHAR(14)),
    Column('UF_PART', VARCHAR(2)),
    Column('NUM_DOC', INTEGER(9)),
    Column('DT_DOC', VARCHAR(10)),
    Column('DT_E_S', VARCHAR(10)),
    Column('IND_EMIT', VARCHAR(1)),
    Column('COD_MOD', VARCHAR(2)),
    Column('COD_SIT', VARCHAR(2)),
    Column('SER', VARCHAR(3)),
    Column('COD_ITEM', VARCHAR(60)),
    Column('NUM_ITEM', INTEGER(3)),
    Column('DESCR_COMPL', VARCHAR(255)),
    Column('D_ITEM_REG_0200', VARCHAR(255)),
    Column('COD_NCM_REG_0200', VARCHAR(10)),
    Column('TIPO_ITEM_REG_0200', VARCHAR(3)),
    Column('VL_ITEM', DECIMAL(15, 2)),
    Column('CFOP', VARCHAR(4)),
    Column('VL_BC_ICMS_ITEM', DECIMAL(21, 2)),
    Column('ALIQ_ICMS_ITEM', DECIMAL(8, 2)),
    Column('VL_ICMS_ITEM', DECIMAL(21, 2)),
    Column('CST_ICMS', VARCHAR(3)),
    Column('VL_BC_ICMS_ST', DECIMAL(21, 2)),
    Column('ALIQ_ST', DECIMAL(8, 2)),
    Column('VL_ICMS_ST', DECIMAL(21, 2)),
    Column('VL_BC_IPI', DECIMAL(21, 2)),
    Column('ALIQ_IPI', DECIMAL(8, 2)),
    Column('VL_IPI', DECIMAL(21, 2)),
    Column('CST_IPI', VARCHAR(2)),
    Column('CONCILIADO_PISCOFINS', VARCHAR(150)),
    Column('CONCILIADO_XML', VARCHAR(150)),
    Column('ID_SPEDFIS_CTRL_REG_0000', INTEGER(11))
)


t_TESTE_DW_ENTRADAS_PIS_COFINS = Table(
    'TESTE_DW_ENTRADAS_PIS_COFINS', metadata,
    Column('ID_ITEM', BIGINT(25), nullable=False),
    Column('PK', VARCHAR(65)),
    Column('DATA_INI', Date),
    Column('CNPJ_FILIAL', VARCHAR(14)),
    Column('REGISTRO', VARCHAR(4), server_default=text("''")),
    Column('IND_ESCRI', VARCHAR(1)),
    Column('IND_OPER', VARCHAR(1)),
    Column('IND_EMIT', VARCHAR(1)),
    Column('COD_PART', VARCHAR(60)),
    Column('D_PART_REG_0150', VARCHAR(140)),
    Column('RAZAO_PART', String(140)),
    Column('CNPJ_PART', String(14)),
    Column('UF_PART', String(2)),
    Column('COD_MOD', VARCHAR(2)),
    Column('COD_SIT', VARCHAR(2)),
    Column('SER', VARCHAR(3)),
    Column('NUM_DOC', INTEGER(9)),
    Column('CHV_NFE', VARCHAR(44)),
    Column('DT_DOC', VARCHAR(100)),
    Column('DT_E_S', VARCHAR(100)),
    Column('VL_DOC', DECIMAL(15, 2)),
    Column('IND_PGTO', VARCHAR(1)),
    Column('VL_DESC', DECIMAL(15, 2)),
    Column('VL_ABAT_NT', DECIMAL(15, 2)),
    Column('VL_MERC', DECIMAL(15, 2)),
    Column('IND_FRT', VARCHAR(1)),
    Column('VL_FRT', DECIMAL(15, 2)),
    Column('VL_SEG', DECIMAL(15, 2)),
    Column('VL_OUT_DA', DECIMAL(15, 2)),
    Column('VL_BC_ICMS', DECIMAL(15, 2)),
    Column('VL_ICMS', DECIMAL(15, 2)),
    Column('VL_BC_ICMS_ST', DECIMAL(15, 2)),
    Column('VL_ICMS_ST', DECIMAL(15, 2)),
    Column('VL_IPI', DECIMAL(15, 2)),
    Column('VL_PIS', DECIMAL(15, 2)),
    Column('VL_COFINS', DECIMAL(15, 2)),
    Column('VL_PIS_ST', DECIMAL(15, 2)),
    Column('VL_COFINS_ST', DECIMAL(15, 2)),
    Column('NUM_ITEM', INTEGER(3)),
    Column('COD_ITEM', VARCHAR(60)),
    Column('DESCR_COMPL', VARCHAR(255)),
    Column('D_ITEM_REG_0200', VARCHAR(273)),
    Column('COD_NCM_REG_0200', String(10)),
    Column('TIPO_ITEM_REG_0200', String(3)),
    Column('QTD', VARCHAR(12)),
    Column('UNID', VARCHAR(6)),
    Column('VL_ITEM', DECIMAL(15, 2)),
    Column('VL_DESC_ITEM', DECIMAL(15, 2)),
    Column('IND_MOV', VARCHAR(1)),
    Column('CST_ICMS', VARCHAR(3)),
    Column('CFOP', VARCHAR(4)),
    Column('COD_NAT', VARCHAR(10)),
    Column('VL_BC_ICMS_ITEM', DECIMAL(15, 2)),
    Column('ALIQ_ICMS', DECIMAL(8, 2)),
    Column('VL_ICMS_ITEM', DECIMAL(15, 2)),
    Column('VL_BC_ICMS_ST_ITEM', DECIMAL(15, 2)),
    Column('ALIQ_ST', DECIMAL(8, 2)),
    Column('VL_ICMS_ST_ITEM', DECIMAL(15, 2)),
    Column('IND_APUR', VARCHAR(1)),
    Column('CST_IPI', VARCHAR(2)),
    Column('COD_ENQ', VARCHAR(3)),
    Column('VL_BC_IPI', DECIMAL(15, 2)),
    Column('ALIQ_IPI', DECIMAL(15, 2)),
    Column('VL_IPI_ITEM', DECIMAL(15, 2)),
    Column('CST_PIS', VARCHAR(2)),
    Column('VL_BC_PIS', DECIMAL(15, 2)),
    Column('ALIQ_PIS', DECIMAL(8, 2)),
    Column('QUANT_BC_PIS', DECIMAL(15, 2)),
    Column('ALIQ_PIS_QUANT', DECIMAL(8, 2)),
    Column('VL_PIS_ITEM', DECIMAL(15, 2)),
    Column('CST_COFINS', VARCHAR(2)),
    Column('VL_BC_COFINS', DECIMAL(15, 2)),
    Column('ALIQ_COFINS', DECIMAL(8, 2)),
    Column('QUANT_BC_COFINS', DECIMAL(15, 2)),
    Column('ALIQ_COFINS_QUANT', DECIMAL(8, 2)),
    Column('VL_COFINS_ITEM', DECIMAL(15, 2)),
    Column('COD_CTA', VARCHAR(60)),
    Column('CONCILIADO_PISCOFINS', String(150)),
    Column('ID_EFD_CTRL_REG_0000', INTEGER(11))
)


t_TESTE_DW_saidas_ICMS = Table(
    'TESTE_DW_saidas_ICMS', metadata,
    Column('ID_ITEM', BIGINT(25), nullable=False),
    Column('CHV_PK', VARCHAR(55)),
    Column('DATA_INI', Date),
    Column('CNPJ_FILIAL', CHAR(14)),
    Column('RAZAO_FILIAL', VARCHAR(255)),
    Column('UF_FILIAL', CHAR(2)),
    Column('REGISTRO', VARCHAR(4)),
    Column('CHV_NFE_CTE', VARCHAR(44)),
    Column('VL_BC_ICMS', VARCHAR(30)),
    Column('VL_ICMS', VARCHAR(30)),
    Column('VL_DOC', DECIMAL(15, 2)),
    Column('COD_PART', VARCHAR(65)),
    Column('D_PART_REG_0150', VARCHAR(255)),
    Column('RAZAO_PART', VARCHAR(255)),
    Column('CNPJ_PART', VARCHAR(14)),
    Column('UF_PART', VARCHAR(2)),
    Column('NUM_DOC', INTEGER(9)),
    Column('DT_DOC', VARCHAR(10)),
    Column('DT_E_S', VARCHAR(10)),
    Column('IND_EMIT', VARCHAR(1)),
    Column('COD_MOD', VARCHAR(2)),
    Column('COD_SIT', VARCHAR(2)),
    Column('SER', VARCHAR(3)),
    Column('COD_ITEM', VARCHAR(60)),
    Column('NUM_ITEM', INTEGER(3)),
    Column('DESCR_COMPL', VARCHAR(255)),
    Column('D_ITEM_REG_0200', VARCHAR(255)),
    Column('COD_NCM_REG_0200', VARCHAR(10)),
    Column('TIPO_ITEM_REG_0200', VARCHAR(3)),
    Column('VL_ITEM', DECIMAL(15, 2)),
    Column('CFOP', VARCHAR(4)),
    Column('VL_BC_ICMS_ITEM', DECIMAL(21, 2)),
    Column('ALIQ_ICMS_ITEM', DECIMAL(8, 2)),
    Column('VL_ICMS_ITEM', DECIMAL(21, 2)),
    Column('CST_ICMS', VARCHAR(3)),
    Column('VL_BC_ICMS_ST', DECIMAL(21, 2)),
    Column('ALIQ_ST', DECIMAL(8, 2)),
    Column('VL_ICMS_ST', DECIMAL(21, 2)),
    Column('VL_BC_IPI', DECIMAL(21, 2)),
    Column('ALIQ_IPI', DECIMAL(8, 2)),
    Column('VL_IPI', DECIMAL(21, 2)),
    Column('CST_IPI', VARCHAR(2)),
    Column('CONCILIADO_PISCOFINS', VARCHAR(150)),
    Column('CONCILIADO_XML', VARCHAR(150)),
    Column('ID_SPEDFIS_CTRL_REG_0000', INTEGER(11))
)


t_TESTE_DW_saidas_PIS_COFINS = Table(
    'TESTE_DW_saidas_PIS_COFINS', metadata,
    Column('ID_ITEM', BIGINT(25), nullable=False),
    Column('PK', VARCHAR(65)),
    Column('DATA_INI', Date),
    Column('CNPJ_FILIAL', VARCHAR(14)),
    Column('REGISTRO', VARCHAR(4), server_default=text("''")),
    Column('IND_ESCRI', VARCHAR(1)),
    Column('IND_OPER', VARCHAR(1)),
    Column('IND_EMIT', VARCHAR(1)),
    Column('COD_PART', VARCHAR(60)),
    Column('D_PART_REG_0150', VARCHAR(140)),
    Column('RAZAO_PART', String(140)),
    Column('CNPJ_PART', String(14)),
    Column('UF_PART', String(2)),
    Column('COD_MOD', VARCHAR(2)),
    Column('COD_SIT', VARCHAR(2)),
    Column('SER', VARCHAR(3)),
    Column('NUM_DOC', INTEGER(9)),
    Column('CHV_NFE', VARCHAR(44)),
    Column('DT_DOC', VARCHAR(100)),
    Column('DT_E_S', VARCHAR(100)),
    Column('VL_DOC', DECIMAL(15, 2)),
    Column('IND_PGTO', VARCHAR(1)),
    Column('VL_DESC', DECIMAL(15, 2)),
    Column('VL_ABAT_NT', DECIMAL(15, 2)),
    Column('VL_MERC', DECIMAL(15, 2)),
    Column('IND_FRT', VARCHAR(1)),
    Column('VL_FRT', DECIMAL(15, 2)),
    Column('VL_SEG', DECIMAL(15, 2)),
    Column('VL_OUT_DA', DECIMAL(15, 2)),
    Column('VL_BC_ICMS', DECIMAL(15, 2)),
    Column('VL_ICMS', DECIMAL(15, 2)),
    Column('VL_BC_ICMS_ST', DECIMAL(15, 2)),
    Column('VL_ICMS_ST', DECIMAL(15, 2)),
    Column('VL_IPI', DECIMAL(15, 2)),
    Column('VL_PIS', DECIMAL(15, 2)),
    Column('VL_COFINS', DECIMAL(15, 2)),
    Column('VL_PIS_ST', DECIMAL(15, 2)),
    Column('VL_COFINS_ST', DECIMAL(15, 2)),
    Column('NUM_ITEM', INTEGER(3)),
    Column('COD_ITEM', VARCHAR(60)),
    Column('DESCR_COMPL', VARCHAR(255)),
    Column('D_ITEM_REG_0200', VARCHAR(273)),
    Column('COD_NCM_REG_0200', String(10)),
    Column('TIPO_ITEM_REG_0200', String(3)),
    Column('QTD', VARCHAR(12)),
    Column('UNID', VARCHAR(6)),
    Column('VL_ITEM', DECIMAL(15, 2)),
    Column('VL_DESC_ITEM', DECIMAL(15, 2)),
    Column('IND_MOV', VARCHAR(1)),
    Column('CST_ICMS', VARCHAR(3)),
    Column('CFOP', VARCHAR(4)),
    Column('COD_NAT', VARCHAR(10)),
    Column('VL_BC_ICMS_ITEM', DECIMAL(15, 2)),
    Column('ALIQ_ICMS', DECIMAL(8, 2)),
    Column('VL_ICMS_ITEM', DECIMAL(15, 2)),
    Column('VL_BC_ICMS_ST_ITEM', DECIMAL(15, 2)),
    Column('ALIQ_ST', DECIMAL(8, 2)),
    Column('VL_ICMS_ST_ITEM', DECIMAL(15, 2)),
    Column('IND_APUR', VARCHAR(1)),
    Column('CST_IPI', VARCHAR(2)),
    Column('COD_ENQ', VARCHAR(3)),
    Column('VL_BC_IPI', DECIMAL(15, 2)),
    Column('ALIQ_IPI', DECIMAL(15, 2)),
    Column('VL_IPI_ITEM', DECIMAL(15, 2)),
    Column('CST_PIS', VARCHAR(2)),
    Column('VL_BC_PIS', DECIMAL(15, 2)),
    Column('ALIQ_PIS', DECIMAL(8, 2)),
    Column('QUANT_BC_PIS', DECIMAL(15, 2)),
    Column('ALIQ_PIS_QUANT', DECIMAL(8, 2)),
    Column('VL_PIS_ITEM', DECIMAL(15, 2)),
    Column('CST_COFINS', VARCHAR(2)),
    Column('VL_BC_COFINS', DECIMAL(15, 2)),
    Column('ALIQ_COFINS', DECIMAL(8, 2)),
    Column('QUANT_BC_COFINS', DECIMAL(15, 2)),
    Column('ALIQ_COFINS_QUANT', DECIMAL(8, 2)),
    Column('VL_COFINS_ITEM', DECIMAL(15, 2)),
    Column('COD_CTA', VARCHAR(60)),
    Column('CONCILIADO_PISCOFINS', String(150)),
    Column('ID_EFD_CTRL_REG_0000', INTEGER(11))
)


t_base = Table(
    'base', metadata,
    Column('DATA_REC', String(255)),
    Column('CNPJ', String(255)),
    Column('RAZAO', String(255)),
    Column('CNPJ_TMP', String(255)),
    Column('RAIZ', String(255)),
    Column('BASE', String(255)),
    Column('RECEITA_NETBX', String(255)),
    Column('DCTF', String(255)),
    Column('DCTF_WEB', String(255))
)


t_base_guarde = Table(
    'base_guarde', metadata,
    Column('DATA_REC', String(255)),
    Column('CNPJ', String(255)),
    Column('RAZAO', String(255)),
    Column('CNPJ_TMP', String(255)),
    Column('RAIZ', String(255)),
    Column('BASE', String(255)),
    Column('RECEITA_NETBX', String(255)),
    Column('DCTF', String(255)),
    Column('DCTF_WEB', String(255))
)


class CfopCredito(Base):
    __tablename__ = 'cfop_credito'

    id_esct = Column(BIGINT(15), primary_key=True)
    cfop = Column(VARCHAR(30), nullable=False, index=True)
    descricao = Column(VARCHAR(512), nullable=False)
    dt_ini = Column(Date, index=True)
    dt_fin = Column(Date)
    nat_bc_cred = Column(VARCHAR(2))
    hash = Column(BIGINT(20), nullable=False)


t_controle_aliq_onco = Table(
    'controle_aliq_onco', metadata,
    Column('DADOS_FILIAL', String(14)),
    Column('ALIQ_PIS', String(255)),
    Column('ALIQ_COFINS', String(80)),
    Column('ALIQ_COFINS_COFINS', Float(asdecimal=True)),
    Column('TOTAL_PIS', Float(19, True)),
    Column('TOTAL_COFINS', Float(19, True)),
    Column('total', Float(19, True))
)


t_controle_movimento_onco = Table(
    'controle_movimento_onco', metadata,
    Column('CNPJ', VARCHAR(14)),
    Column('ID_EFD_CTRL_REG_0000', INTEGER(11)),
    Column('DATA_INI', Date)
)


class CtrlArqExcelContabil(Base):
    __tablename__ = 'ctrl_arq_excel_contabil'

    id = Column(BIGINT(20), primary_key=True, index=True)
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


class CtrlArqExcelPrevidenciario(Base):
    __tablename__ = 'ctrl_arq_excel_previdenciario'

    id = Column(BIGINT(20), primary_key=True, index=True)
    cliente = Column(Text)
    id_user = Column(Text)
    user_name = Column(Text)
    cnpj_conta = Column(Text)
    tipo_relatorio = Column(Text)
    nome_arquivo = Column(Text)
    data_cadastrada = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))
    json = Column(JSON)


t_esocial_tabela_03_nat_rub_fopag = Table(
    'esocial_tabela_03_nat_rub_fopag', metadata,
    Column('CODIGO', INTEGER(5)),
    Column('NOME_ NATUREZA_RUBRICA', String(150)),
    Column('DESCR_NATUREZA_RUBRICA', String(800)),
    Column('INICIO', Date),
    Column('FIM', Date)
)


t_regime_g_bringel = Table(
    'regime_g_bringel', metadata,
    Column('DATA_INI', Date),
    Column('CNPJ', CHAR(14)),
    Column('incidencia_tributaria_periodo', VARCHAR(255), server_default=text("''")),
    Column('metodo_apropriacao', VARCHAR(255), server_default=text("''")),
    Column('tp_contribuicao', VARCHAR(255), server_default=text("''")),
    Column('criterio_ecrituracao', VARCHAR(255), server_default=text("''"))
)


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


class TbAjContribCred(Base):
    __tablename__ = 'tb_aj_contrib_cred'

    id_esct = Column(BIGINT(15), primary_key=True)
    codigo = Column(String(30, 'latin1_general_ci'), nullable=False)
    descricao = Column(String(512, 'latin1_general_ci'), nullable=False)
    dt_ini = Column(Date)
    dt_fin = Column(Date)
    hash = Column(BIGINT(20), nullable=False)


class TbCfop(Base):
    __tablename__ = 'tb_cfop'

    ID = Column(INTEGER(11), primary_key=True)
    CFOP = Column(VARCHAR(10), index=True)
    DESCRICAO = Column(VARCHAR(255))
    ICMS = Column(VARCHAR(10))
    PIS_COFINS = Column(VARCHAR(10))
    IPI = Column(VARCHAR(10))


class TbClassificacao(Base):
    __tablename__ = 'tb_classificacao'

    id_classificacao = Column(INTEGER(10), primary_key=True)
    descricao = Column(String(150))


class TbClientes(Base):
    __tablename__ = 'tb_clientes'

    id_cliente = Column(INTEGER(11), primary_key=True)
    razao_social = Column(TEXT)
    cnpj_compl = Column(TEXT)
    apelido = Column(TEXT)
    cnpj = Column(TEXT)
    dt_final = Column(TEXT)
    dt_inicial = Column(TEXT)
    qtd_analise = Column(TEXT)
    ativo = Column(TEXT)
    dt_criacao = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))
    grupo = Column(TEXT)


t_tb_clientes_2 = Table(
    'tb_clientes_2', metadata,
    Column('id_cliente', Text),
    Column('razao_social', Text),
    Column('cnpj_compl', Text),
    Column('apelido', Text),
    Column('cnpj', Text),
    Column('dt_final', Text),
    Column('dt_inicial', Text),
    Column('qtd_analise', Text),
    Column('ativo', Text),
    Column('dt_criacao', Text),
    Column('grupo', Text)
)


t_tb_cod_ajuste_apur_icms = Table(
    'tb_cod_ajuste_apur_icms', metadata,
    Column('COD_AJ_APUR', String(255), index=True),
    Column('DESC', String(900)),
    Column('DT_INI', String(255)),
    Column('DT_FIM', String(255)),
    Column('UF', String(255))
)


class TbDarf(Base):
    __tablename__ = 'tb_darf'

    id_item = Column(INTEGER(255), primary_key=True)
    codig_varia = Column(String(255))
    perio = Column(String(255))
    perio_apura_fato_gerad = Column(String(255))
    denom = Column(String(255))


t_tb_monofasia = Table(
    'tb_monofasia', metadata,
    Column('NCM', String(255)),
    Column('DESCRICAO', String(255)),
    Column('MERCADORIA', String(1500))
)


class TbTipi(Base):
    __tablename__ = 'tb_tipi'

    ID = Column(INTEGER(11), primary_key=True)
    NCM = Column(String(255), index=True)
    DESCRICAO = Column(String(255))
    ALIQ = Column(String(255))
    STATUS = Column(String(255))
    NCM_REPLACE = Column(String(20), index=True)


class TbTipoCred(Base):
    __tablename__ = 'tb_tipo_cred'

    id_esct = Column(BIGINT(15), primary_key=True)
    codigo = Column(String(30, 'latin1_general_ci'), nullable=False)
    descricao = Column(String(512, 'latin1_general_ci'), nullable=False)
    dt_ini = Column(Date)
    dt_fin = Column(Date)
    hash = Column(BIGINT(20), nullable=False)


class TbUfCodigoSigla(Base):
    __tablename__ = 'tb_uf_codigo_sigla'

    id_esct = Column(BIGINT(15), primary_key=True)
    codigo = Column(String(30, 'latin1_general_ci'), nullable=False)
    descricao = Column(String(512, 'latin1_general_ci'), nullable=False)
    dt_ini = Column(Date)
    dt_fin = Column(Date)
    hash = Column(BIGINT(20), nullable=False)


class TbUfesp(Base):
    __tablename__ = 'tb_ufesp'

    ID = Column(INTEGER(5), primary_key=True)
    ANO = Column(INTEGER(4))
    VALOR = Column(DECIMAL(15, 2))


class TbUsuarioAdmin(Base):
    __tablename__ = 'tb_usuario_admin'

    id_user = Column(INTEGER(11), primary_key=True)
    nome = Column(String(150))
    ativo = Column(CHAR(1))
    usuario = Column(String(50))
    senha = Column(String(30))
    email = Column(String(80))
    categoria = Column(String(50))
    ids_clientes = Column(String(1500))
    ids_grupos = Column(String(255))
    cpf = Column(String(16))
    banco = Column(String(100))
    ag = Column(String(20))
    conta = Column(String(80))
    img_src = Column(String(1500))


class TesteSpedContabilCtrl(Base):
    __tablename__ = 'teste_sped_contabil_ctrl'

    ID = Column(BIGINT(20), primary_key=True)
    ID_SPEDFIS_CTRL_REG_0000 = Column(BIGINT(20))
    DATA_INI = Column(Date)
    DATA_FIM = Column(Date)
    CNPJ = Column(Text)
    DATA_HORA = Column(DateTime)
    TIPO = Column(Text)
    ENVIO = Column(BIGINT(20))
    CANCELADO = Column(Text)
    RAZAO_SOCIAL = Column(Text)
    RETIFICADOR = Column(BIGINT(20))
    NOME_ARQUIVO = Column(Text)
    DW_BALANCETE_GERAL = Column(BIGINT(20))
    DW_RAZAO_04 = Column(BIGINT(20))
    SPR_ZERAMENTO_RAZAO_04 = Column(Text)


class TipoCdResposta(Base):
    __tablename__ = 'tipo_cdResposta'

    id = Column(INTEGER(11), primary_key=True, index=True)
    cod = Column(String(3))
    descricao = Column(Text)


t_tipo_codIncFGTS = Table(
    'tipo_codIncFGTS', metadata,
    Column('id', INTEGER(11), nullable=False, index=True),
    Column('cod', String(2)),
    Column('descricao', Text)
)


class TipoCodIncIRRF(Base):
    __tablename__ = 'tipo_codIncIRRF'

    ID = Column(INTEGER(11), primary_key=True)
    CODIGO = Column(INTEGER(20), index=True)
    DESCRIÇÃO = Column(Text)
    INÍCIO = Column(Date)
    TÉRMINO = Column(Date)


t_tipo_codIncSIND = Table(
    'tipo_codIncSIND', metadata,
    Column('id', INTEGER(11), nullable=False, index=True),
    Column('cod', String(2)),
    Column('descricao', Text)
)


class TipoProcEmi(Base):
    __tablename__ = 'tipo_proc_Emi'

    id = Column(INTEGER(11), primary_key=True, index=True)
    cod = Column(INTEGER(1))
    descricao = Column(Text)


class TipoTpAmbRecepcao(Base):
    __tablename__ = 'tipo_tpAmb_recepcao'

    id = Column(INTEGER(11), primary_key=True, index=True)
    cod = Column(INTEGER(1))
    descricao = Column(Text)


class TipoTpInscIdeEmpregador(Base):
    __tablename__ = 'tipo_tpInsc_ideEmpregador'

    id = Column(INTEGER(11), primary_key=True, index=True)
    cod = Column(INTEGER(1))
    descricao = Column(Text)


class TipoTpRubr(Base):
    __tablename__ = 'tipo_tpRubr'

    id = Column(INTEGER(11), primary_key=True, index=True)
    cod = Column(INTEGER(1))
    descricao = Column(Text)


class UfCodigoSigla(Base):
    __tablename__ = 'uf_codigo_sigla'

    id_esct = Column(BIGINT(15), primary_key=True)
    codigo = Column(String(30, 'latin1_general_ci'), nullable=False)
    descricao = Column(String(512, 'latin1_general_ci'), nullable=False)
    dt_ini = Column(Date)
    dt_fin = Column(Date)
    hash = Column(BIGINT(20), nullable=False)
