import numpy as np
import pandas as pd
from sklearn import svm
from sklearn.model_selection import train_test_split
import csv
import numpy as np


def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False


decision_tree_model_pkl = open("svm_model_UA_DEP_DELAY.sav", 'rb')
clf = pickle.load(decision_tree_model_pkl)
print "Loaded Decision tree model :: ", clf


datafile = open("parsed_flights_UA.csv", 'r')
airport_data = open("data/airports.csv", 'r')
carrier_data = open("data/airlines.csv", 'r')
Y = open("binarized_parsed_labels_UA_DEP_DELAY.csv", 'r')

X = csv.reader(datafile, delimiter=",")
airport_data = csv.reader(airport_data, delimiter=",")
carrier_data = csv.reader(carrier_data, delimiter=",")
y = csv.reader(Y, delimiter=",")
airports = {}
carriers = {}


print "load" 


#skip header
next(X, None)
next(y, None)
next(airport_data, None)
next(carrier_data, None)

#Build airport and airline dictionary
for i, airport in enumerate(airport_data):
	airports[airport[0]] = i
for i, carrier in enumerate(carrier_data):
	carriers[carrier[0]] = i 

my_dict2 = {y:x for x,y in airports.iteritems()}
        
#Replace missing value with 'n/a' first,
X = [[float(x) if isfloat(x) else x if x else np.nan for x in item] for item in X]
y = [item for item in y]


y = np.array(y)
n, d = y.shape
print n , d
y = y.reshape(n,)
print y
df = pd.DataFrame(X)

date_data = df.iloc[:,3].tolist()

#Build date dictionary
date = {}
for i, date_entry in enumerate(date_data):
	if date_entry not in date:
		date[date_entry] = i

df = df.drop(df.columns[5], 1).drop(df.columns[6], 1).drop(df.columns[8], 1).drop(df.columns[9], 1).drop(df.columns[12], 1)
df = df.drop(df.columns[0], 1).drop(df.columns[1], 1).drop(df.columns[2], 1).drop(df.columns[3], 1)
df = df.drop(df.columns[2], 1)
df = df.drop(df.columns[0], 1).drop(df.columns[4], 1).drop(df.columns[5], 1).drop(df.columns[6], 1).drop(df.columns[7], 1).drop(df.columns[9], 1).drop(df.columns[10], 1)
df = df.drop(df.columns[6], 1)

n, d = df.shape

print "drop"

#Replace airport, carriers, date to int value, and replace missing value with mean 
df = df.replace(airports)
df = df.fillna(df.mean())
p = clf.predict(df)

print "Accuracy: ", accuracy_score(y, p)
