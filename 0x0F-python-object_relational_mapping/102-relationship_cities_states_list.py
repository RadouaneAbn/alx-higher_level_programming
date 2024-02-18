#!/usr/bin/python3
""" This script lists all City objects from a data base
"""
from relationship_state import State, Base
from relationship_city import City
from sys import argv as av
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine_info = 'mysql+mysqldb://{}:{}@localhost:{}/{}'\
        .format(av[1], av[2], 3306, av[3])

    engine = create_engine(engine_info, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    total_states = session.query(State).order_by(State.id)

    for state in total_states:
        for city in state.cities:
            print(f"{city.id}: {city.name} -> {state.name}")
