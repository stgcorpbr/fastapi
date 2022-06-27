from datetime import datetime
from typing import Optional

from pydantic import BaseModel

class OnlyClienteSchema(BaseModel):
    id_cliente : Optional[int] = None
    razao_social : str
    cnpj : str
    
    class Config:
        orm_mode = True

class ClienteSchema(BaseModel):
    id_cliente : Optional[int] = None
    razao_social : str
    cnpj_compl : str
    apelido : str
    cnpj : str
    dt_final : Optional[str]
    dt_inicial : Optional[str]
    qtd_analise : Optional[str]
    ativo : Optional[int] = None
    dt_criacao : Optional[datetime] = None
    grupo : Optional[str]

    class Config:
        orm_mode = True


        