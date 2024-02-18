#!/usr/bin/python3
"""SQLAlchemy classes"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """A class that defines State insatnces"""

    __tablename__ = "states"
    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
