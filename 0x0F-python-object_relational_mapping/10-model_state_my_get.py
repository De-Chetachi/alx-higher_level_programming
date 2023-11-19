#!/usr/bin/python3
'''contains the class definition of a State and an instance'''

from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sys import argv

if __name__ == "__main__":
    db_user = argv[1]
    db_pass = argv[2]
    db_name = argv[3]
    match = argv[4]
    url_ = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    url = url_.format(db_user, db_pass, db_name)
    engine = create_engine(url, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    state = session.query(State).filter(State.name == match).first()
    if state:
        print("{}".format(state.id))
    else:
        print("Not found")
    session.close()
