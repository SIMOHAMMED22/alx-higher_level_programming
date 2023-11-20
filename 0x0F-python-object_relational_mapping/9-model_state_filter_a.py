#!/usr/bin/python3
"""Script to print specific State objects from the database hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State)
    query = query.filter(State.id.in_([1, 2, 3, 5]))
    query = query.order_by(State.id)
    states = query.all()

    if states:
        for state in states:
            print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")

    session.close()
