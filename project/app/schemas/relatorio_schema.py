from datetime import datetime
from typing import Optional

from pydantic import BaseModel

class CtrlArqExcelContabilSchema(BaseModel):
    id : Optional[int] = None
    cliente : Optional[str]
    cnpj_conta : Optional[str]
    data_ini : Optional[str]
    data_fim : Optional[str]
    nome_arquivo : Optional[str]   
    total_registros : Optional[int] = None
    data_cadastrada : Optional[datetime] = None
    
    class Config:
        orm_mode = True
