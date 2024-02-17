#!/usr/bin/python3
""" This script prints all City objects from a database
"""

from model_state import Base, State
from model_city import City
from sys import argv as av
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine_info = 'mysql+mysqldb://{}:{}@localhost:{}/{}'.format(
                   av[1], av[2], 3306, av[3])
    engine = create_engine(engine_info, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State.name, City.id, City.name)\
        .join(State).where(City.state_id == State.id).order_by(City.id)
    result_1 = result.all()

    for st_name, ct_id, ct_name in result:
        print(f"{st_name}: ({ct_id}) {ct_name}")
