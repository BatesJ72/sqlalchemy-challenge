from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from pprint import pprint
import pandas as pd
from sqlalchemy import func, select, table, column


# Import Hawaii Measurement Data

from measurement_model import Hawaii_Measurement

measurement_engine = create_engine("sqlite:///hawaii.sqlite")
measurement_session = Session(bind=measurement_engine)

measurement_data = measurement_session.query(Hawaii_Measurement)
# for row in measurement_data:
#     pprint(row.__dict__)

    
# Import Hawaii Station Data

from station_model import Hawaii_Station

station_engine = create_engine("sqlite:///hawaii.sqlite")
station_session = Session(bind=station_engine)

station_data = station_session.query(Hawaii_Station)
# for row in station_data:
#     pprint(row.__dict__)




# Precipitation Analysis

# Get the last 12 months of data
# Date of trip: 7/1/2016 - 7/9/2016
conn_m = measurement_engine.connect()

## Should I drop all NULLs? May matter for the joined table
measurement_df1 = pd.read_sql("SELECT * FROM measurement", conn_m).dropna(how = 'any') 
# print(measurement_df1)
# print(measurement_df1.head())

# Get max date from table
max_df = pd.read_sql("SELECT max(date) FROM measurement", conn_m)
# print(max_df)

# Get pertinent data
measurement_df2 = pd.read_sql("SELECT date, prcp FROM measurement WHERE date between '2015-07-01' and '2016-07-01'", conn_m)
# print(measurement_df1)
# print(measurement_df1.head())

# Data Cleaning: set index, sort, drop NULLs
measurement_df3 = measurement_df2.sort_values(by = 'date').dropna(how = 'any') #set_index('date').
# print(measurement_df3)

# Plot data
measurement_plot = measurement_df3.plot(x = 'date', y = 'prcp', kind = 'bar')
# measurement_plot.show

# Summary Statistics
# print(measurement_df2.describe())




# Station Analysis

conn_s = station_engine.connect()
station_df1 = pd.read_sql("SELECT * FROM station",conn_s)
# print(station_df1)
# print(station_df1.head())

# Calculate the total number of stations
station_count = station_df1["station"].count()
# print(station_count)

# The most active stations

# Join the data together
all_df = pd.merge(measurement_df1, station_df1, on = "station", how = "left")
# print(all_df.head())

# List of stations and observation counts in descending order
# print(all_df.count())

station_q = station_session.query(Hawaii_Station)
station_q1 = station_session.query(func.min(Hawaii_Station.longitude))
pprint(station_q1.all())

