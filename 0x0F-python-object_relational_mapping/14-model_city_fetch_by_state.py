#!/usr/bin/python3
"""SQLAlchemy quering"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


if __name__ == "__main__":
    """task #15"""
    eng = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                        pool_pre_ping=True)
    Base.metadata.create_all(eng)
    sess = Session(eng)
    result = sess.query(State, City).join(City).all()
    for item in result:
        print("{}: ({}) {}".format(item[0].__dict__["name"],
              item[1].__dict__["id"], item[1].__dict__["name"]))
    sess.close()
