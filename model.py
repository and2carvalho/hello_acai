from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Acai(Base):

    __tablename__ = 'acai'

    codigo = Column(Integer, primary_key=True)
    tamanho = Column(String(50))
    sabor = Column(String(50))
    adicional = Column(String(50))
    tempo_preparo = Column(Integer)
    valor_total = Column(Integer)

