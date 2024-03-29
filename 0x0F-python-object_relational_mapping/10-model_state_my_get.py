#!/usr/bin/python3
"""
Script that prints the State object with the name passed as an argument
from the database hbtn_0e_6_usa
Usage: ./10-model_state_my_get.py <mysql_username>
                                   <mysql_password>
                                   <database_name>
                                   <state_name>
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).filter_by(name=argv[4]).first()
    if result is None:
        print("Not found")
    else:
        print("{0}".format(result.id))
