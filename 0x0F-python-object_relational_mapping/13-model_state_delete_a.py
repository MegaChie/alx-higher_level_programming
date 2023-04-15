#!/usr/bin/python3
""" a script that deletes all State objects with a name containing the letter a
from the database hbtn_0e_6_usa. """
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


def Fetch():
    """ 13. Delete states. """
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    file = session.query(State).all()
    for line in file:
        if 'a' in line.__dict__['name']:
            session.delete(line)
    session.commit()
    session.close()


if __name__ == "__main__":
    Fetch()
