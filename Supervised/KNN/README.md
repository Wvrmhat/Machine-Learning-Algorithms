# K Nearest Neighbors

Given a datapoint, it classifies that point according to a class it knows
> Looks for groupings and picks closest ppoint
> K is a hyperparameter, meaning we change the value as we train the model

---
**Magnitude** is the distance between two points
We use euclidean distance, which is the absolute distance

> d = = sqr((x2 - x1)^2 + (y2 - y1)^2) = sqr(4^2) = 4

However we usually have multiple attributes, meaning we plot in 3-Dimensions
If K is too high/too many values, it increases the range and reduces accuracy

> [!NOTE]
> Saving the model is very computation heavy especiall with many datapoints

