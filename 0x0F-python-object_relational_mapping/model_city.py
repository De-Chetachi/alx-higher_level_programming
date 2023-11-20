#!/usr/bin/python3
'''contains the class definition of a State and an instance'''

from sqlalchemy import Column, String, Integer, ForeignKey
from model_state import Base, State


class City(Base):
    '''a class state'''
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True,
                unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
