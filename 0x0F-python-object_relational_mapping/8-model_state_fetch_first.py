#!/usr/bin/python3
""" Write a script that lists all State objects from the database
hbtn_0e_6_usa. """
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


def Fetch():
    """ 7. All states via SQLAlchemy. """
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    file = session.query(State).first()
    if file:
        print("{}: {}".format(file.__dict__['id'], file.__dict__['name']))
    else:
        print("Nothing")
    session.close()


if __name__ == "__main__":
    Fetch()
