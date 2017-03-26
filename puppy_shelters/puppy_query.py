from sqlalchemy import create_engine
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker

from puppies import Base, Shelter, Puppy
import datetime


engine = create_engine('sqlite:///puppyshelter.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()


def query_one():
    """Query all of the puppies and return the results in ascending alphabetical order"""
    result = session.query(Puppy.name).order_by(Puppy.name.asc()).all()

    # print the result with puppy name only
    # print len(result)
    for item in result:
        print item[0]

