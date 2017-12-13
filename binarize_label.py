import pandas as pd 

df = pd.read_csv('data/parsed_flights.csv', low_memory=False)


AA = df[df['UNIQUE_CARRIER'].isin({'AA'})]
UA = df[df['UNIQUE_CARRIER'].isin({'UA'})]

AA.to_csv('parsed_labels_AA.csv', columns = ["DEP_DELAY", "ARR_DELAY"])
UA.to_csv('parsed_labels_UA.csv', columns = ["DEP_DELAY", "ARR_DELAY"])

AA = pd.read_csv('parsed_labels_AA.csv', low_memory=False, index_col=0)
UA = pd.read_csv('parsed_labels_UA.csv', low_memory=False, index_col=0)

data = []
data1 = []

for index, row in AA.iterrows():
	if (row['DEP_DELAY'] > 0):
		#Delay
		data.append(0)
	else:
		#Ontime
		data.append(1)


for index, row in UA.iterrows():
	if (row['DEP_DELAY'] > 0):
		#Delay
		data1.append(0)
	else:
		#Ontime
		data1.append(1)

data = pd.DataFrame(data)
data1 = pd.DataFrame(data1)
data.to_csv('binarized_parsed_labels_AA_DEP_DELAY.csv')
data1.to_csv('binarized_parsed_labels_UA_DEP_DELAY.csv')

