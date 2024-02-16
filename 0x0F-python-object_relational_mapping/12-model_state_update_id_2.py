#!/usr/bin/python3
"""SQLAlchemy quering"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


if __name__ == "__main__":
    """task #11"""
    eng = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                        pool_pre_ping=True)
    Base.metadata.create_all(eng)
    sess = Session(eng)
    replace = update(State)
    replace = replace.values({"name": "New Mexico"})
    replace = replace.where(State.id == 2)
    sess.execute(replace)
    sess.close()
