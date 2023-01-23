from fastapi import APIRouter, Depends, Path, Query
from sqlalchemy.orm import Session
from ..utils.get_db import get_db
from .schemas import LocalitySchema, PlacesSchema
from .service import get_all_places_service, get_locality_service

router = APIRouter()

BASE_URL = '/api/localidades'


@router.get(f'{BASE_URL}/', response_model=PlacesSchema)
def get_all_places(db: Session = Depends(get_db), uf: str | None = Query(default=None, regex=r'\b[A-Z]{2}\b')):
    return get_all_places_service(db, uf)


@router.get(BASE_URL + '/{cep}', response_model=LocalitySchema)
def get_locality(db: Session = Depends(get_db), cep: str = Path(regex=r'(\d){5}(\d){3}')):
    return get_locality_service(db, cep)
