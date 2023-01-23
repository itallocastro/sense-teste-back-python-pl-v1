import datetime

from pydantic import BaseModel
from typing import List


class LocalityBaseSchema(BaseModel):
    cep: str
    uf: str
    localidade: str
    logradouro: str
    data_consulta: datetime.datetime = datetime.datetime.now()


class LocalityCreateSchema(LocalityBaseSchema):
    pass


class LocalitySchema(LocalityBaseSchema):
    class Config:
        orm_mode = True


class PlacesSchema(BaseModel):
    localidades: List[LocalitySchema]

    class Config:
        orm_mode = True
