#!/usr/bin/python3

"""script that lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa"""

if __name__ == "__main__":
    import sys
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)

    # Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    # count = 1
    result = session.query(State).all()
    for res in result:
        print(f"{res.id}: {res.name}")
        for r in res.cities:
            print(f"    {r.id}: {r.name}")
            # count += 1
