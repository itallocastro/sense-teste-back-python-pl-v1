from fastapi import HTTPException
from sqlalchemy.orm import Session
from .schemas import LocalityCreateSchema
from .repository import create_locality, get_all_places
import os
import httpx

URL_VIA_CEP = os.environ["URL_VIA_CEP"]


def get_all_places_service(db: Session, uf: str | None):
    try:
        return get_all_places(db, uf)
    except Exception as e:
        raise HTTPException(status_code=400, detail='Houve um problema, tente novamente!')


def get_locality_service(db: Session, cep: str):
    try:
        r = httpx.get(f'{URL_VIA_CEP}/{cep}/json')
        result = r.json()
        if "erro" in result:
            raise HTTPException(status_code=404, detail='Cep não encontrado')
        locality = create_locality(db, LocalityCreateSchema(**result))
        return locality
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except Exception as e:
        raise HTTPException(status_code=400, detail='Houve um problema, tente novamente!')
