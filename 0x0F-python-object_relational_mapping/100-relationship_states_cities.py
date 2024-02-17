#!/usr/bin/python3
""" creates the State "California" with the City "San Francisco"
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
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State("California")
    new_city = City("San Francisco")
    new_state.cities.append(new_city)
    session.add(new_state)
    session.commit()
