import datetime

from pydantic import BaseModel
from typing import List


class LocalityBaseSchema(BaseModel):
    cep: str


class LocalitySchema(LocalityBaseSchema):
    uf: str
    localidade: str
    logradouro: str
    data_consulta: datetime.datetime = datetime.datetime.now()

    class Config:
        orm_mode = True


class PlacesSchema(BaseModel):
    localidades: List[LocalitySchema]

    class Config:
        orm_mode = True
