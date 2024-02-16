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
    result = sess.query(State).all()
    stateList = []
    for item in result:
        if sys.argv[4] in item.__dict__["name"]:
            stateList.append(item.__dict__["id"])
    if len(stateList) == 0:
        print("Not found")
    else:
        for elem in stateList:
            print(elem)
    sess.close()
