import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class usuario(Base):
    __tablename__ = 'usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    userCode = Column(String(100), nullable=False)
    userName = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    bio = Column(String(1000), nullable=True)
    clave = Column(String(20), nullable=False)
    foto = Column(String(500), nullable=True)
    sexo = Column(String(1), nullable=False)
    
class seguidor(Base):
    __tablename__ = 'seguidor'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    usuarioID = Column(Integer,  ForeignKey('usuario.id'))
    usuarioSeguidorID = Column(Integer, ForeignKey('usuario.id'))

class post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    usuarioID = Column(Integer, ForeignKey('usuario.id'))
    fecha = Column(Datetime, nullable=False)
    foto = Column(String(500), nullable=False)
    caption = Column(String(500), nullable=True)

class comment(Base):
    __tablename__ = 'comment'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    postID = Column(Integer, ForeignKey('post.id'))
    fechaComentario = Column(Datetime, nullable=False)
    foto = Column(String(500), nullable=False)
    caption = Column(String(500), nullable=True)
    usuarioID = Column(Integer, ForeignKey('usuario.id'))
    textoComment = Column(String(500), nullable=False)


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e