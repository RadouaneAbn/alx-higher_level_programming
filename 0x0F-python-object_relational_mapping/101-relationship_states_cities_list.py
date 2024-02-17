#!/usr/bin/python3
""" This script lists all State objects and corresponding City objects
"""
from relationship_state import State
from relationship_city import City
from sys import argv as av
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine_info = 'mysql+mysqldb://{}:{}@localhost:{}/{}'\
        .format(av[1], av[2], 3306, av[3])

    engine = create_engine(engine_info, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for current_state in session.query(State).order_by(State.id):
        print("{}: {}".format(current_state.id, current_state.name))
        for city in current_state.cities:
            print("    {}: {}".format(city.id, city.name))
