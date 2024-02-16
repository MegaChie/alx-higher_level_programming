#!/usr/bin/python3
"""SQLAlchemy quering"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import delete
from model_state import Base, State


if __name__ == "__main__":
    """task #14"""
    eng = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                        pool_pre_ping=True)
    Base.metadata.create_all(eng)
    sess = Session(eng)
    dele = delete(State)
    dele = replace.where("a" in State.name)
    sess.execute(dele)
    sess.commit()
    sess.close()
