#!/usr/bin/python3
""" This script changes the name of a State object from a database
"""
from model_state import Base, State
from sys import argv as av
from sqlalchemy import (create_engine)
from sqlalchemy import select, func
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine_info = 'mysql+mysqldb://{}:{}@localhost:{}/{}'\
        .format(av[1], av[2], 3306, av[3])

    engine = create_engine(engine_info, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    st = select(State).where(func.binary(State.name).like('%a%'))
    states = session.scalars(st)
    for state in states:
        session.delete(state)

    session.commit()
