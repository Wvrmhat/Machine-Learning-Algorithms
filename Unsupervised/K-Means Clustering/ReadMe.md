# K Means Clustering
K means how many clusters
Centroids determine which datapoint belongs to a specific cluster
---

## Centroids

We create two centroids in random positions on our graph/dataset

> e.g if k = 2, then we have 2 centroids
> Once we have two centroids, we draw a straight line between the two centroids
> We use the line to separate the datapoints, and classify the datapoint according to the centroid

Then we find the average of the points, to find the first coordinate of the centroid. Same is done to find second coordinate
The points are reassigned after finding the midpoint of the centroids

>This process is done until there are no changes between datapoints. Therefore the points are clustered

---

## Advantages/Disadvantages

 + If there are more features and datapoints, it takes longer to process
 + However it is faster than other unsupervised machine learning algorithms


