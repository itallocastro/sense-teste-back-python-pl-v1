from fastapi import APIRouter, Depends, Path
from sqlalchemy.orm import Session
from ..utils.get_db import get_db
from .schemas import LocalidadeSchema, LocalidadesSchema
from .service import get_localidade_service, get_todas_localidades_service

router = APIRouter()

BASE_URL = '/api/localidades'


@router.get(f'{BASE_URL}/', response_model=LocalidadesSchema)
def get_todas_localidades(db: Session = Depends(get_db), uf: str | None = None):
    return get_todas_localidades_service(db, uf)


@router.get(BASE_URL + '/{cep}', response_model=LocalidadeSchema)
def get_localidade(db: Session = Depends(get_db), cep: str = Path(regex=r'(\d){5}(\d){3}')):
    return get_localidade_service(cep, db)
