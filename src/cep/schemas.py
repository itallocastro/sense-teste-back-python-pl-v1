import datetime

from pydantic import BaseModel
from typing import List


class LocalidadeBaseSchema(BaseModel):
    cep: str


class LocalidadeSchema(LocalidadeBaseSchema):
    uf: str
    localidade: str
    logradouro: str
    data_consulta: datetime.datetime = datetime.datetime.now()

    class Config:
        orm_mode = True


class LocalidadesSchema(BaseModel):
    localidades: List[LocalidadeSchema]
    class Config:
        orm_mode = True
