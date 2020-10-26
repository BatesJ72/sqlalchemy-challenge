from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy import Column, Integer, String, Float
# from sqlalchemy import create_engine
# from pprint import pprint


class Hawaii_Measurement(Base):
    __tablename__ = "measurement"
    id = Column(Integer, primary_key=True)
    station = Column(String)
    date = Column(String)
    prcp = Column(Float)
    tobs = Column(Float)
    
# engine = create_engine(f"sqlite:///Resources/hawaii.sqlite")
# pprint(engine.execute("SELECT * FROM measurement LIMIT 10").fetchall())


