from fastapi import HTTPException
from sqlalchemy.orm import Session
from .schemas import LocalidadeSchema
from .repository import criar_localidade, pegar_localidades
import os
import httpx

URL_VIA_CEP = os.environ["URL_VIA_CEP"]


def get_todas_localidades_service(db: Session, uf: str | None):
    return pegar_localidades(db, uf)

def get_localidade_service(db: Session, cep: str):
    try:
        r = httpx.get(f'{URL_VIA_CEP}/{cep}/json')
        result = r.json()
        if "erro" in result:
            raise HTTPException(status_code=404, detail='Cep não encontrado')
        localidade = criar_localidade(db, LocalidadeSchema(**result))
        return localidade
    except Exception as e:
        raise HTTPException(status_code=400, detail='Houve um problema, tente novamente!')
