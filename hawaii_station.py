from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import create_engine
from pprint import pprint

    
class Hawaii_Station(Base):
    __tablename__ = "station"
    id = Column(Integer, primary_key=True)
    station = Column(String)
    name = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    elevation = Column(Float)
    
engine = create_engine(f"sqlite:///Resources/hawaii.sqlite")

# pprint(engine.execute("SELECT * FROM station LIMIT 10").fetchall())

