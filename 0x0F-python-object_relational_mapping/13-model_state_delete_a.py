#!/usr/bin/python3
"""deletes all State objs with name containing 'a'
from database hbtn_0e_6_usa"""

if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    user_name = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user_name, password, db_name),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    a_states = session.query(State).filter(State.name.like(
        '%a%')).delete(synchronize_session='fetch')
    session.commit()
