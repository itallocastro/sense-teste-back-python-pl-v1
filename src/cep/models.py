from sqlalchemy import Column, String, DateTime
from ..config.database import Base


class LocalityModel(Base):
    __tablename__ = 'localidades'

    cep = Column(String, primary_key=True, index=True)
    uf = Column(String, index=True)
    localidade = Column(String, index=True)
    logradouro = Column(String, index=True)
    data_consulta = Column(DateTime, index=True)
