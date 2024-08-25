

import numpy as np
import sklearn
from sklearn.preprocessing import scale
from sklearn.datasets import load_digits
from sklearn.cluster import KMeans
from sklearn import metrics


# the data is the features, so we scale it down so that they are within the value -1 and 1
digits = load_digits()
# by scaling them down we save time, since by default the digits are large
data = scale(digits.data)

y = digits.target
# Set the amount of clusters/centroids we want to make. We could also use K = 10
k = len(np.unique(y))
# Getting the amount of instances and features
samples, features = data.shape  

# function for scoring the unsupervised algorithm
# estimator is the k-means clustering model. name is the string representing the name of the estimator. data is the dataset on which the model will be fitted
def bench_k_means(estimator, name, data):
    estimator.fit(data)                                         #fits the K-Means model to the provided data
    print('%-9s\t%i\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f'        # ensures output is aligned
          % (name, estimator.inertia_,                          # sum of squared distances of samples to closest midpoint
             metrics.homogeneity_score(y, estimator.labels_),   # Measures if each cluster has only members of a single class
             metrics.completeness_score(y, estimator.labels_),  # Checks if all points of a class are assigned to the same cluster
             metrics.v_measure_score(y, estimator.labels_),     # The mean of homogenity and completeness
             metrics.adjusted_rand_score(y, estimator.labels_), # Checks similarity between the true labels and predicted labels
             metrics.adjusted_mutual_info_score(y, estimator.labels_), # measure the agreement of true labels and predicted labels
             metrics.silhouette_score(data, estimator.labels_,  # checks how similar an object is to its own cluster compared to other clusters
                                      metric='euclidean')))

# init allows centroids to also be in 
clf = KMeans(n_clusters=k, init="random", n_init=10)
bench_k_means(clf, "1", data)
    

