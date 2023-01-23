from sqlalchemy.orm import Session
from .models import LocalidadeModel
from .schemas import LocalidadeSchema, LocalidadesSchema


def existe_localidade(db: Session, cep: str):
    return db.query(LocalidadeModel).filter(LocalidadeModel.cep == cep).first()


def pegar_localidades(db: Session, uf: str | None = None):
    query = db.query(LocalidadeModel)
    if uf:
        query = query.filter(LocalidadeModel.uf == uf)
    return {"localidades": query.all()}


def criar_localidade(db: Session, localidade: LocalidadeSchema):
    localidade_existe = existe_localidade(db, localidade.cep)
    if localidade_existe:
        return localidade_existe
    db_localidade = LocalidadeModel(**localidade.dict())
    db.add(db_localidade)
    db.commit()
    db.refresh(db_localidade)
    return db_localidade
