#!/usr/bin/python3
""" a script that prints the State object with the name passed as argument from
the database hbtn_0e_6_usa.  """
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


def Fetch():
    """ 10. Get a state. """
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    File = session.query(State).all()
    result = ""
    for line in File:
        if sys.argv[4] in line.__dict__['name']:
            result = line.__dict__['id']
    if result != "":
        print(result)
    else:
        print("Not Found")
    session.close()


if __name__ == "__main__":
    Fetch()
