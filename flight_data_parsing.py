import pandas as pd 

airports = {'ATL':None,
			'DEN':None,
			'PHL':None,
			'ORD':None,
			'IAH':None,
			'SFO':None,
			'SEA':None,
			'MIA':None,
			'BOS':None,
			'LGA':None,
			'JFK':None,
			'IAD':None,
}


unneeded_features = ['QUARTER', 'FL_NUM', 'ORIGIN_AIRPORT_SEQ_ID','ORIGIN_STATE_ABR', 'ORIGIN_STATE_NM', 'DEST_AIRPORT_SEQ_ID',
					 'DEST_STATE_ABR', 'DEST_STATE_NM', 'CRS_DEP_TIME', 'CRS_ARR_TIME', 'CRS_ELAPSED_TIME','CARRIER_DELAY',
					 'WEATHER_DELAY', 'NAS_DELAY', 'SECURITY_DELAY', 'LATE_AIRCRAFT_DELAY', 'FIRST_DEP_TIME']

df = pd.read_csv('data/flight_data2016.csv', low_memory=False)
df = df.drop(unneeded_features, axis=1)

#Remove comma in ORIGIN_CITY_NAME and DEST_CITY_NAME
df['ORIGIN_CITY_NAME'] = df['ORIGIN_CITY_NAME'].str.replace(',', '')
df['DEST_CITY_NAME'] = df['DEST_CITY_NAME'].str.replace(',', '')


# Only keep rows where cities match ones in airports dict
orig_df = df[df.ORIGIN.isin(airports.keys())]
dest_df = df[df.DEST.isin(airports.keys())]


#Drop rows where destination city is in airports to avoid duplicates
orig_df = orig_df[~orig_df.DEST.isin(airports.keys())]
dest_df = dest_df[~dest_df.ORIGIN.isin(airports.keys())]

combined_df = pd.concat([orig_df, dest_df], ignore_index=True)
combined_df.to_csv('data/parsed_flights.csv')

print len(combined_df)
print combined_df.tail()