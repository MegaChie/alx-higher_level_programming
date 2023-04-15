#!/usr/bin/python3
""" a Python file similar to model_state.py named model_city.py that contains
the class definition of a City. """
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import City


def Fetch():
    """ 14. Cities in state. """
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    file = session.query(State, City).join(City).all()
    for line in file:
        print("{}: ({}) {}".format(line[0].__dict__['name'],
                                   line[1].__dict__['id'],
                                   line[1].__dict__['name']))
    session.close()


if __name__ == "__main__":
    Fetch()
