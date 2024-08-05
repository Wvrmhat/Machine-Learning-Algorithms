# Machine-Learning-Algorithms
>Algorithms that take a dataset, and trains off of it to create models. The algorithm can then be used to predict values based on the dataset.
---
## Categories of Machine Learning

### Supervised
Algorithms trained on labeled datasets. Each trained set is paired with an output label.
>Used to predict the output of new unseen data

<details>
   
   Types of **Supervised** algorithms
   
1. Regression:
   + Linear Regression
   + Polynomial Regression

2. Classification:
   + Support Vector Machines (SVM)
   + Neural Networks
   + Decision Trees
   + Logistic Regression
>[K-Nearest Neighbours](Supervised/KNN) is an algorithm that falls under both Regression and Classification, but it is often used more for Classification.
<details>
   
   <summary>Advantages and Disadvantages</summary>
   
   ### Advantages
   + Highly accurate with enough labeled data
   + Clear results
   ### Disadvantages
   + Reguires large amount of data, often hard to obtain
   + Does not perform well on unseen data 
</details>

</details>

   ---
   ### Unsupervised
   >Algorithm receives data without exact instructions, it then finds patterns to analyze and cluster the unlabeled datasets.

<details>
   
   <summary> Types of **Unsupervised** algorithms </summary>
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
  
</details>

---
### Reinforcment
Agent learns to make decisions by performing actions and getting feedback from environment.
> Goal is to learn policies that bring the highest reward over time

<details>
Types of **Reinforcment** algorithms:
1. **Model-Free Methods:
   + Q-Learning
   + SARSA (State-Action-Reward-State-Action)

2. **Model-Based Methods**
   + Dynamic Programming
   + Monte Carlo Methods

<Details>
   <summary>Advantages and Disadvantages</summary>

   ### Advantages
   + Handles complex, multi-dimensional environments
   + Learns through trial and error
   ### Disadvantages
   + Requires a lot of data and computation power
   + Can be hard to tune/debeug
</Details>

</details>

---

   
