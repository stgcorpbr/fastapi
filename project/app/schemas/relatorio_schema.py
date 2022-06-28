from datetime import datetime
from typing import Optional

from pydantic import BaseModel

class CtrlArqExcelContabilSchema(BaseModel):
    id : Optional[int] = None
    id_user : Optional[int] = None
    user_name : Optional[str]
    email : Optional[str]
    cliente : Optional[str]
    cnpj_conta : Optional[str]
    data_ini : Optional[str]
    data_fim : Optional[str]
    cod_natureza : Optional[str]
    cod_conta : Optional[str]
    sheet : Optional[str]
    nome_arquivo : Optional[str]   
    total_registros : Optional[int] = None
    data_cadastrada : Optional[datetime] = None
    
    class Config:
        orm_mode = True

