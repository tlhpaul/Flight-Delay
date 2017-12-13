import requests 
import quandl
import pandas as pd
from auth import quandl_key

start_date = "2016-12-30"
end_date = "2016-01-01"

prices_df = quandl.get("OPEC/ORB", authtoken=quandl_key)
prices_df.index = pd.to_datetime(prices_df.index, infer_datetime_format=True)

# Sort from most recent to least
prices_df = prices_df.iloc[::-1]
prices_df.columns = ["Price"]

# Slice based on desired date range
prices_df = prices_df.loc[start_date: end_date]
prices_df.to_csv("data/oilprices.csv")

prices_df['DATE'] = prices_df.index.astype(str)
print prices_df.tail()

flight_df = pd.read_csv('data/parsed_flights.csv')
flight_df['OIL_PRICE'] = 0
flight_df['FL_DATE'] = flight_df['FL_DATE'].astype(str)

print prices_df['DATE'].dtype
print flight_df['FL_DATE'].dtype

for ind, row in prices_df.iterrows():
	flight_df[flight_df.FL_DATE == row['DATE']].OIL_PRICE = row['Price']


print flight_df.tail()

