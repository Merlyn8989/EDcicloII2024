from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class Autor(Base):
    __tablename__ = 'tbl_autor'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    libro = relationship('Libro', back_populates='Autor') 


class Categoria(Base):
    __tablename__ = 'tbl_categoria'
    id = Column(Integer, primary_key=True)
    nombreCategoria = Column(String, nullable=False)
    libro = relationship('Libro', back_populates='Categoria')

class Libro(Base):
    __tablename__ = 'tbl_libro'
    id = Column(Integer, primary_key=True)  
    titulo = Column(String, nullable=False)
    paginas = Column(Integer, nullable=False)
    autor_id = Column(Integer, ForeignKey('tbl_autor.id'))
    categoria_id = Column(Integer, ForeignKey('tbl_categoria.id'))


engine = create_engine('sqlite:///libro.db', echo=True)
Base.metadata.create_all(engine)