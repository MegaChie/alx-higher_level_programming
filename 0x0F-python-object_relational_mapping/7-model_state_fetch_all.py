#!/usr/bin/python3
""" a script that lists all State objects from the database hbtn_0e_6_usa. """
import sqlalchemy
from model_state import Base, State
import sys
import sqlalchemy.orm


def Fetch():
    """ 7. All states via SQLAlchemy. """
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    file = session.query(State).all()
    for line in file:
        print("{}: {}".format(line.__dict__['id'], line.__dict__['name']))
    session.close()


if __name__ == "__main__":
    list_state_obj()
