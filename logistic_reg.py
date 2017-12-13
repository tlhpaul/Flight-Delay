import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import OneHotEncoder, Imputer
import csv

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

#data import
datafile = open("data/test.csv", 'r')
X = csv.reader(datafile, delimiter=",")

#skip header
next(X, None)

Y = np.genfromtxt("data/test1.csv", delimiter = ",")
y = []
for i in range(len(Y)):
    hold = 0
    neg = False
    for label in Y[i]:
        if label < 0:
            neg = True
    if neg:
        y.append(0)
    else:
        y.append(1)
Y = y
#replace missing value with 'n/a' first, then with mean 
X = [[float(x) if isfloat(x) else x if x else np.nan for x in item] for item in X]
df = pd.DataFrame(X)
df = df.fillna(df.mean())
X = []
for i, row in enumerate(df.values):
    X.append(row.tolist())

Y = Y[:99]  
#enc.n_values_
fDict = {}
for i in range(len(X)):
    instance = X[i]
    for j in range(len(instance)):
        feature = instance[j]
        if isinstance(feature, float):
            continue
        if j in fDict:
            if feature not in fDict[j]:
                fDict[j].append(feature)
        else:
            fDict[j] = [feature]
        X[i][j] = fDict[j].index(feature)


X = np.asarray(X)
Y = np.asarray(Y)

df1 = pd.DataFrame(X)
df1.to_csv("X.csv")

df2 = pd.DataFrame(Y)
df2.to_csv("Y.csv")

clf = LogisticRegression()

x_train, x_test, y_train, y_test = train_test_split(
      X, Y, test_size=0.2, random_state=42)


clf.fit(x_train, y_train)
p = clf.predict(x_test)
print(accuracy_score(y_test, p))
