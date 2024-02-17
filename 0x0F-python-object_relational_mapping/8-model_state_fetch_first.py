#!/usr/bin/python3
""" This script prints the first object from a database
"""
from model_state import Base, State
from sys import argv as av
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine_info = 'mysql+mysqldb://{}:{}@localhost:{}/{}'.format(
                   av[1], av[2], 3306, av[3])
    engine = create_engine(engine_info, pool_pre_ping=True)
    # Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).order_by(State.id).first()
    if state:
        print(state)
    else:
        print('Nothing')
