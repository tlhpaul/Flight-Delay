import pandas as pd 
from sklearn.utils import shuffle

data = pd.read_csv('data/parsed_flights.csv', low_memory=False)


AA = data[data['UNIQUE_CARRIER'].isin({'AA'})]
UA = data[data['UNIQUE_CARRIER'].isin({'UA'})]


AA.to_csv('parsed_flights_AA.csv')
UA.to_csv('parsed_flights_UA.csv')