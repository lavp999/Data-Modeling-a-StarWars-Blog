import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False)
    email = Column(String(120), nullable=False)
    password = Column(String(45), nullable=False)

class Planet(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)

class Character(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)

class FavoritChar(Base):
    __tablename__ = 'favorits_characters'
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('users.id'), nullable=False)
    id_character = Column(Integer, ForeignKey('characters.id'), nullable=True)
    user = relationship(User)
    character = relationship(Character)


class FavoritPla(Base):
    __tablename__ = 'favorits_planets'
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('users.id'), nullable=False)
    id_planet = Column(Integer, ForeignKey('planets.id'), nullable=True)
    user = relationship(User)
    planet = relationship(Planet)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
