from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql+psycopg2://postgres@/postgres', echo=True)
Base = declarative_base()



class User(Base):
    __tablename__ = 'users'


    name = Column(String, primary_key=True)
    lastname = Column(String)

Base.metadata.create_all(engine)


#\d
#\d+
#