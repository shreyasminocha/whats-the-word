from sklearn.cluster import KMeans
import numpy as np


class Clustering:
    
    def __init__(self, bert_embed_input):
        self.bert_embed = bert_embed_input
    
    def make_cluster(self, n_cluster):
        kmeans = kmeans_plusplus(n_cluster, )

    
X = np.array([[1, 2], [1, 4], [1, 0], [10, 2], [10, 4], [10, 0]])
kmeans = kmeans_plusplus(n_clusters=2, random_state=0).fit(X)
print(kmeans.labels_)
kmeans.predict([[0, 0], [12, 3]])
print(kmeans.cluster_centers_)

