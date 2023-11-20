#!/usr/bin/python3
"""Module containing the State class"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    from sqlalchemy import create_engine
    from os import getenv

    db = {
        'host': 'localhost',
        'port': 3306,
        'user': getenv('HBNB_MYSQL_USER'),
        'pwd': getenv('HBNB_MYSQL_PWD'),
        'db': getenv('HBNB_MYSQL_DB')
    }

    engine = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}'
                           .format(db['user'], db['pwd'], db['host'],
                                   db['port'], db['db']))

    Base.metadata.create_all(engine)
