# Glass Identification
For context the dataset was taken from a criminology study used to identify the types of glass for evidence

## Steps on training this model:
First the data is read and then we define the attributes in an array
```
data = pd.read_csv("glass.data")
```

We then predict from the classificat label and return a new dataframe
> pandas uses keywords, "(columns = [predict])" is the same as "([predict], axis = 1"
> If axis = 0 then we drop rows
> data.drop takes a column or row of of the array of attributes
```
X = numpy.array(data.drop([predict], axis = 1))
y = numpy.array(data[predict])
```
Take all our labels and attributes, and we split them up into 4 arrays. We use the _test data to check accuracy of model/algorithm we create.
> 


