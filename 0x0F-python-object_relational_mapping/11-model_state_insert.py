#!/usr/bin/python3
"""SQLAlchemy quering"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


if __name__ == "__main__":
    """task #12"""
    eng = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                        pool_pre_ping=True)
    Base.metadata.create_all(eng)
    sess = Session(eng)
    stat = State(name="Louisiana")
    sess.add(stat)
    sess.commit()
    result = sess.query(State).all()
    for item in result:
        if "Louisiana" in item.__dict__["name"]:
            print(item.__dict__["id"])
    sess.close()
