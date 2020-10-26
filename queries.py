from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from pprint import pprint


# Import Hawaii Measurement Data

from measurement_model import Hawaii_Measurement

measurement_engine = create_engine("sqlite:///hawaii.sqlite")
measurement_session = Session(bind=measurement_engine)

measurement_data = measurement_session.query(Hawaii_Measurement).limit(10).all()
# for row in measurement_data:
#     pprint(row.__dict__)

    
# Import Hawaii Station Data

from station_model import Hawaii_Station

station_engine = create_engine("sqlite:///hawaii.sqlite")
station_session = Session(bind=station_engine)

station_data = station_session.query(Hawaii_Station).limit(10).all()
# for row in station_data:
#     pprint(row.__dict__)
