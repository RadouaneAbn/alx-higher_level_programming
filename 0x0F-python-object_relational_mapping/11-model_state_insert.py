#!/usr/bin/python3
""" This script adds the state object 'Louisiana' to a database
"""
from model_state import Base, State
from sys import argv as av
from sqlalchemy import (create_engine)
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    new_state_name = 'Louisiana'
    engine_info = 'mysql+mysqldb://{}:{}@localhost:{}/{}'\
        .format(av[1], av[2], 3306, av[3])

    engine = create_engine(engine_info, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(new_state_name)
    session.add(new_state)
    session.commit()

    st = session.query(State.id)\
        .filter(func.binary(State.name) == new_state_name)

    print(st[0][0])
