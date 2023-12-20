# from sqlalchemy import create_engine
# from models import *

# Base = declarative_base()
# engine = create_engine('sqlite:///session.db')

# def create_table(base, engine):
#     class Session(base):
#         __tablename__ = 'session'

#         id = Column(Integer, primary_key = True)
#         name = Column(String)
#         breed = Column(String)

#         Base.metadata.create_all(engine)

# create_table(Base, engine)

from models import Dog

def create_table(base, engine):
    base.metadata.create_all(engine)


def save(session, dog):
    session.add(dog)
    session.commit()

def get_all(session):
    return session.query(Dog).all()

def find_by_name(session, name):
    return session.query(Dog).filter(Dog.name == name).first()

def find_by_id(session, id):
    return session.query(Dog).filter(Dog.id == id).first()

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter(Dog.name == name and Dog.breed == breed).first()

def update_breed(session, dog, breed):
    dog.breed = breed
    session.add(dog)
    session.commit()