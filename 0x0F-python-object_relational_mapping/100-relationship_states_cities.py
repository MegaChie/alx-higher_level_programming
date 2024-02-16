#!/usr/bin/python3
"""SQLAlchemy quering"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    """task #16"""
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                        pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    newState = State(name='California')
    newCity = City(name='San Francisco')
    newState.cities.append(newCity)
    session.add(newState)
    session.add(newCity)
    session.commit()
