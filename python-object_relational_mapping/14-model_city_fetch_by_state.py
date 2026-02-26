#!/usr/bin/python3
"""Prints all City objects from the database, with their corresponding State."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City


def main():
    """Connects to the database and prints cities ordered by cities.id."""
    if len(sys.argv) != 4:
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(username, password, db_name),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    results = (session.query(State.name, City.id, City.name)
               .join(State, City.state_id == State.id)
               .order_by(City.id)
               .all())

    for state_name, city_id, city_name in results:
        print("{}: ({}) {}".format(state_name, city_id, city_name))

    session.close()


if __name__ == "__main__":
    main()
