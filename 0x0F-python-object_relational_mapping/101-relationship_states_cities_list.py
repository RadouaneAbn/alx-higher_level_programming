#!/usr/bin/python3
""" This script lists all State objects and corresponding City objects
"""
from relationship_state import State, Base
from relationship_city import City
from sys import argv as av
from sqlalchemy import (create_engine)
from sqlalchemy import func, select
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine_info = 'mysql+mysqldb://{}:{}@localhost:{}/{}'\
        .format(av[1], av[2], 3306, av[3])

    engine = create_engine(engine_info, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    total_states = session.query(State).order_by(State.id)
    for state in total_states:
        print(state)

        cities_in_state = session.query(City)\
            .filter(City.state_id == state.id).order_by(City.id)
        for city in cities_in_state:
            print("\t{}".format(city))
