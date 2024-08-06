#!/usr/bin/env python3

import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
from sklearn import linear_model, preprocessing

# for context this dataset was taken from a criminology study used to identify types of glass for evidence
# reads data, define attributes then print the headers of the table
def main():
        
    data = pd.read_csv("glass.data")
    data = data[["ID", "RI", "Na","Mg","Al","Si","K","Ca","Ba","Fe","Class"]]
    print(data.head())

    # predict from a label
    predict = "Class"

    # returns new data frame(training data), and it is then used to predict new unseen data
    X = np.array(data.drop([predict], axis = 1))
    y = np.array(data[predict])

    # we split 10% of our data into test samples, and train our model off of that

    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size = 0.1)

    # We classify our model with the specified amount of neighbours
    model = KNeighborsClassifier(n_neighbors=9)

    # fits the model on best-fit, then we return a value that represents the accuracy 
    model.fit(x_train, y_train)
    acc = model.score(x_test, y_test)
    print(f"Accuracy: {acc}\n")
    print("-" *100)

    # model is then used to predict
    predicted = model.predict(x_test)

    TypeOfGlass = ["building_windows_float_processed",
                "building_windows_non_float_processed",
                "vehicle_windows_float_processed",
                "vehicle_windows_non_float_processed",
                "containers",
                "tableware",
                "headlamps"]
                
    # we loop through the predicted list, and print the values of the actual value as well. We then match the 
    for x in range(len(predicted)):
        print("predicted: ", predicted[x], "\nData: ", x_test[x], "\nActual: ", y_test[x])
        if 0 <= y_test[x] < len(TypeOfGlass):                       # ensures index is within valid range
            print(f"Type of glass: ", TypeOfGlass[predicted[x]])
            if predicted[x] == y_test[x]:                           # if predicted value matches the actual value it is a match
                print("Match found\n")
       
        n = model.kneighbors([x_test[x]], 9, True) 
        print(f"N: {n}")
        print("-" * 100)
           
if __name__ == '__main__':
    print(main())
    