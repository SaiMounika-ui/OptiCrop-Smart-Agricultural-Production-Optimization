# K-Means Clustering

## Overview

K-Means Clustering is an unsupervised machine learning algorithm used to group similar agricultural conditions based on environmental and soil parameters. In the OptiCrop system, K-Means is applied to identify natural groupings within the agricultural dataset, enabling better analysis of crop patterns and environmental similarities.

Before training the clustering model, the Elbow Method is used to determine the optimal number of clusters by analyzing the Within-Cluster Sum of Squares (WCSS). The selected number of clusters is then used to train the K-Means model and categorize crops into meaningful groups.

---

## Objective

The objectives of this phase are to:

- Group similar agricultural conditions into clusters.
- Identify hidden patterns in the crop dataset.
- Determine the optimal number of clusters using the Elbow Method.
- Improve agricultural analysis through unsupervised learning.

---

## Python Code

### Import Library

```python
from sklearn.cluster import KMeans
```

### Finding the Optimal Number of Clusters (Elbow Method)

```python
wcss = []

for i in range(1, 11):
    km = KMeans(
        n_clusters=i,
        init='k-means++',
        max_iter=300,
        n_init=10,
        random_state=0
    )

    km.fit(X)
    wcss.append(km.inertia_)

plt.figure(figsize=(10,4))
plt.plot(range(1,11), wcss)

plt.title("The Elbow Method")
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.show()
```

---

### Training the K-Means Model

```python
km = KMeans(
    n_clusters=4,
    init='k-means++',
    max_iter=300,
    n_init=10,
    random_state=0
)

y_means = km.fit_predict(X)
```

---

### Displaying Cluster Results

```python
crop = data['label']

cluster = pd.DataFrame(y_means)

result = pd.concat([cluster, crop], axis=1)

result = result.rename(columns={0:'cluster'})

print(result.head())
```

---

## Elbow Method

The Elbow Method helps determine the optimal number of clusters by plotting the **Within-Cluster Sum of Squares (WCSS)** against different values of **K**.

As the number of clusters increases, WCSS decreases. The point where the decrease begins to slow significantly is called the **Elbow Point**, which represents the optimal number of clusters.

In this project, the elbow graph indicates that **4 clusters** provide the best balance between accuracy and computational efficiency.

---

## Analysis

After selecting **K = 4**, the K-Means algorithm groups agricultural records into four distinct clusters based on:

- Nitrogen (N)
- Phosphorous (P)
- Potassium (K)
- Temperature
- Humidity
- pH
- Rainfall

Each cluster contains crops that share similar environmental characteristics.

---

## Sample Cluster Output

```
Cluster 0:
Rice, Pigeonpeas, Apple, Orange, Papaya,
Coconut, Cotton, Jute

----------------------------------------

Cluster 1:
Maize, Banana, Grapes, Watermelon,
Muskmelon, Orange, Papaya

----------------------------------------

Cluster 2:
Maize, Chickpea, Kidneybeans,
Pigeonpeas, Mothbeans, Mungbean,
Blackgram, Lentil, Pomegranate,
Mango, Muskmelon, Apple

----------------------------------------

Cluster 3:
Grapes, Muskmelon
```

---

## Observations

- The Elbow Method identifies **4** as the optimal number of clusters.
- Similar agricultural conditions are grouped together.
- Crops within the same cluster share common soil and climatic characteristics.
- Clustering helps discover hidden relationships in the dataset.
- These groups can support intelligent crop recommendation and agricultural planning.

---

## Benefits

- Identifies natural groupings in agricultural data.
- Improves understanding of crop-environment relationships.
- Supports precision agriculture.
- Helps visualize agricultural patterns.
- Enhances data exploration before supervised model training.

---

## Conclusion

K-Means Clustering is used in the OptiCrop system to group crops with similar agricultural characteristics. The Elbow Method is first applied to determine the optimal number of clusters, after which the K-Means algorithm is trained using four clusters. The resulting groups reveal meaningful agricultural patterns that support crop recommendation, data analysis, and intelligent farming decisions.
