from sqlalchemy.orm import Session
from .models import LocalityModel
from .schemas import LocalitySchema


def get_locality(db: Session, cep: str):
    return db.query(LocalityModel).filter(LocalityModel.cep == cep).first()


def get_all_places(db: Session, uf: str | None = None):
    query = db.query(LocalityModel)
    if uf:
        query = query.filter(LocalityModel.uf == uf)
    return {"localidades": query.all()}


def create_locality(db: Session, locality: LocalitySchema):
    exists_locality = get_locality(db, locality.cep)
    if exists_locality:
        return exists_locality
    db_locality = LocalityModel(**locality.dict())
    db.add(db_locality)
    db.commit()
    db.refresh(db_locality)
    return db_locality
