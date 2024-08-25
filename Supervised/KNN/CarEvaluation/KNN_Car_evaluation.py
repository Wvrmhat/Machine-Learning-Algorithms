#!/usr/bin/env python3

import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
from sklearn import linear_model, preprocessing

data = pd.read_csv("car.data")
print(data.head())

print("-"*100)

# converts non-numerical data into numberical data by using preprocessing library

LabelEn = preprocessing.LabelEncoder()
# Takes each non-numeric column, and turns them into a list which then is transformed into integer values
buying = LabelEn.fit_transform(list(data["buying"]))
maint = LabelEn.fit_transform(list(data["maint"]))
door = LabelEn.fit_transform(list(data["doors"]))
persons = LabelEn.fit_transform(list(data["persons"]))
lug_boot = LabelEn.fit_transform(list(data["lug_boot"]))
safety = LabelEn.fit_transform(list(data["safety"]))
cls = LabelEn.fit_transform(list(data["class"]))


predict ="class"

# create X and Y list, x is features / Y is labels.
# zip creates tuple objects with different values corresponding to list we give
X = list(zip(buying, maint, door, persons, lug_boot, safety))
y = list(cls)

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size = 0.1)

#converted_xtest = [int[x] for x in x_test]

#print(x_train, y_test)

model = KNeighborsClassifier(n_neighbors=10)  # specify the amount of neighbours

model.fit(x_train, y_train)
acc = model.score(x_test, y_test)
print("Accuracy: \n")
print(acc)
print("-" *100)

predicted = model.predict(x_test)
# used to get the datapoint, prediction, and what the actual value is
names = ["unacc", "acc", "good", "vgood"]

for x in range(len(predicted)):
    print("predicted: ", [predicted[x]], "Data: ", x_test[x], "Actual: ", [y_test[x]])
    n = model.kneighbors([x_test[x]], 9, True) # supposed to take 2D array, but we want 1 value. So we put it in another array so it comes out as 1 value
    print(f"N: {n}")