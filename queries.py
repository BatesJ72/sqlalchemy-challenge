from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from pprint import pprint
import pandas as pd


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




# Precipitation Analysis

# Get the last 12 months of data
# Date of trip: 7/1/2016 - 7/9/2016
conn_m = measurement_engine.connect()

# Get max date from table
max_df = pd.read_sql("SELECT max(date) FROM measurement", conn_m)
# print(max_df)

# Get pertinent data
measurement_df1 = pd.read_sql("SELECT date, prcp FROM measurement WHERE date between '2015-07-01' and '2016-07-01'", conn_m)
# print(measurement_df1.head())

# Data Cleaning: set index, sort, drop NULLs
measurement_df2 = measurement_df1.sort_values(by = 'date').dropna(how = 'any') #set_index('date').
# print(measurement_df2)

# Plot data
measurement_plot = measurement_df2.plot(x = 'date', y = 'prcp', kind = 'bar')
# measurement_plot.show




git stat
