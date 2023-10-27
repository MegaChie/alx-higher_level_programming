#!/usr/bin/python3
""" a script that adds the State object “Louisiana” to the database
hbtn_0e_6_usa. """
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


def Fetch():
    """ 11. Add a new state. """
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    state = State(name='Louisiana')
    session.add(state)
    session.commit()
    print(state.id)
    session.close()


if __name__ == "__main__":
    Fetch()