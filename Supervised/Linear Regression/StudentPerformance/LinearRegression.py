#!/usr/bin/env python3

# pandas allows you to read data sets, numpy allows support for arrays

import pandas
import numpy
import sklearn
from sklearn import linear_model
import sklearn.model_selection
from sklearn.utils import shuffle

data = pandas.read_csv("student-mat.csv", sep=";")



data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]   # these are all attributes
print(data.head())        # prints the headers of the dataset, from the selected attributes

# now we try to predict from a label

predict = "G3"

# returns a new data frame (which becomes the training data), and is used to predict new data
# pandas uses keywords, "(columns = [predict])" is the same as "([predict], axis = 1)". 
# If axis = 0 then we drop rows
# data.drop takes a column or row out of the array of attributes

X = numpy.array(data.drop([predict], axis = 1))
y = numpy.array(data[predict])

# Takes all our labels and attributes; and we split them up into 4 arrays.
# We use the _test data to check accuracy of model/algorithm we create.
# We don't train model off our testing data, otherwise we get inaccurate results since it knows the answer (It memorises the patterns)

# Therefore we split 10% of our data into test samples (it will be information it hasn't seen before)
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size = 0.1)

linear = linear_model.LinearRegression()
# fits the model, and finds the best-fit line
linear.fit(x_train, y_train)
# we then return a value that represents the accuracy of our model
accuracy = linear.score(x_test, y_test)
print("-" * 100)
print("Accuracy: \n", accuracy)
print("-" * 100)

print("Coefficient: \n", linear.coef_)
print("Intercept: \n", linear.intercept_)

print("-" * 100)

# We then use the model to predict
# So we take an array of arrays, and predicts based off the x_test data
predictions = linear.predict(x_test)

# We get the length of predictions
for x in range(len(predictions)):
    # prints out predictions, the input data, and the actual value
    print(predictions[x], x_test[x], y_test[x])


