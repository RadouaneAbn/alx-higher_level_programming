#!/usr/bin/python3
""" This script prints the state id of a given state 'name'
"""
from model_state import Base, State
from sys import argv as av
from sqlalchemy import (create_engine)
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine_info = 'mysql+mysqldb://{}:{}@localhost:{}/{}'\
            .format(av[1], av[2], 3306, av[3])
    engine = create_engine(engine_info, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    st = session.query(State.id)\
        .filter(func.binary(State.name) == av[4])\
        .one_or_none()

    if st:
        print(st[0])
    else:
        print('Not found')
