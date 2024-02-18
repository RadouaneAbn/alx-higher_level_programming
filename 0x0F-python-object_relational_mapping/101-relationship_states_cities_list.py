#!/usr/bin/python3

""" This script lists all State objects and corresponding City objects
contained in the database hbtn_0e_101_usa
"""

if __name__ == "__main__":
    from sys import argv as av
    from relationship_state import State
    from relationship_city import City
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker
    engine_info = 'mysql+mysqldb://{}:{}@localhost:{}/{}'\
        .format(av[1], av[2], 3306, av[3])

    engine = create_engine(engine_info, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    total_states = session.query(State).all()
    for current_state in total_states:
        print(f"{current_state.id}: {current_state.name}")
        for city in current_state.cities:
            print(f"    {city.id}: {city.name}")
