#!/usr/bin/python3
"""
Script that lists all City objects and their corresponding State objects
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City, Base
from relationship_state import State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(City).order_by(City.id).all()
    for city in result:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
