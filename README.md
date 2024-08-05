# Machine-Learning-Algorithms
>Algorithms that take a dataset, and trains off of it to create models. The algorithm can then be used to predict values based on the dataset.
---
## Categories of Machine Learning

### Supervised
Algorithms trained on labeled datasets. Each trained set is paired with an output label.
>Used to predict the output of new unseen data
Types of **Supervised** algorithms:
1. Regression:
   + Linear Regression
   + Polynomial Regression

2. Classification:
   + Support Vector Machines (SVM)
   + Neural Networks
   + Decision Trees
   + Logistic Regression
>K-Nearest Neighbours is an algorithm that falls under both Regression and Classification, but it is often used more for Classification.
<details>
   <summary>Advantages and Disadvantages</summary>
   
   ### Advantages
   + Highly accurate with enough labeled data
   + Clear results
   ### Disadvantages
   + Reguires large amount of data, often hard to obtain
   + Does not perform well on unseen data 
</details>

---
### Unsupervised
>Algorithm receives data without exact instructions, it then finds patterns to analyze and cluster the unlabeled datasets.

Types of **Unsupervised** algorithms:
1. **Clustering:**
   + K-Means Clustering
   + Hierarchical Clustering
   + DBSCAN (Density-Based Spatial Clustering of Applications with Noise)
   
2. **Associations:**
   + Apriori Algorithm
   + Eclat Algorithm
     
3. **Dimensionality Reduction**
   + PCA (Principal Component Analysis)
   + t-SNE (t-Distributed Stochastic Neighbor Embedding)

<details>
   <summary>Advantages and Disadvantages</summary>
   
   ### Advantages
   + Works with unlabled data, which is easier to gather
   + Useful for finding general patterns in data
   ### Disadvantages
   + Hard to evaluate as there are no labels
   + Requires domain knowledge to interpret results
</details>

   
