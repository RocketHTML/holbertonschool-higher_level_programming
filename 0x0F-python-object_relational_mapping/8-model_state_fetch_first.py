#!/usr/bin/python3
from sys import argv
from model_state import State, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == '__main__':
    user = argv[1]
    passwd = argv[2]
    dbname = argv[3]
    port = 3306
    host = 'localhost'
    dialect = 'mysql+mysqldb'
    con = '{}://{}:{}@{}:{}/{}'
    # 'mysql+pymysql://username:password@host:port/database_name'
    formatted = con.format(dialect, user, passwd, host, port, dbname)
    engine = create_engine(formatted)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    s = session.query(State).order_by(State.id).first()
    print("{}: {}".format(s.id, s.name))
