# Glass Identification
For context the dataset was taken from a criminology study used to identify the types of glass for evidence

## Steps on training this model:
First the data is read and then we define the attributes in an array
```
data = pd.read_csv("glass.data")
```

We then predict from the classification label and return a new dataframe
> pandas uses keywords, "(columns = [predict])" is the same as "([predict], axis = 1"

> If axis = 0 then we drop rows

> data.drop takes a column or row of of the array of attributes
```
X = numpy.array(data.drop([predict], axis = 1))
y = numpy.array(data[predict])
```
Take all our labels and attributes, and we split them up into 4 arrays. We use the _test data to check accuracy of model/algorithm we create.
> We train model off sample data to get more accurate results

> Therefore we split 10% of our data into test samples 
```
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size = 0.1)
```
We create a classification model that implements the KNN algorthim. A hyperparameter is specified for our model to consider when making a decision. In the example it looks at 9 nearest neighbors to determine the class of a new data point
```
model = KNeighborsClassifier(n_neighbors=9)
```

We then fit the model to a line of best-fit. Which allows us to return a value that represents the accuracy. Our model is then used to predict based off the test data.
```
predicted = model.predict(x_test)
```

We can then check the predictions, input data, and actual value by looping throught the predicted list.
```
for x in range(len(predicted)):
     prints out predicted, the input data, and the actual value
     print(predicted[x], x_test[x], y_test[x])
```

---
> [!WARNING]
> To run the file you will need to install the libraries in the requirements.txt file.

> pip install -r requirements.txt

> [!NOTE]
> Don't forget to import sklearn, pandas and numpy.


