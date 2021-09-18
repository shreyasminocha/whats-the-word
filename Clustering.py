from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

class Clustering:

    def __init__(self, bert_embed_input):
        '''
        Initializes this instance of Clustering class.
        In
            bert_embed_input; sentence embedding array output by BERT
        '''
        self.bert_embed = bert_embed_input
    
    def fit_cluster(self, n_cluster):
        '''
        Creates KMeans class.
        In
            n_cluster; integer number of clusters
        Out
            KMeans class fit to self.bert_embed data on n_cluster clusters
        '''
        return KMeans(n_cluster).fit(self.bert_embed)
    
    def get_silh(self, KMeans_fitted):
        '''
        Returns average silhouette score for a fitted KMeans class
        In
            KMeans_fitted; KMeans instance fitted by fit_cluster
        Out
            average silouette score for this instance
        '''
        return silhouette_score(self.bert_embed, KMeans_fitted.labels_)

    def optimal_cluster(self, n_cluster_range):
        '''
        Finds the optimal number of clusters
        In
            n_cluster_range; the range of # of clusters to be inspecteds
        Out
            optimal # of clusters    
        '''
        
    
X = np.array([[1, 2], [1, 4], [1, 0], [10, 2], [10, 4], [10, 0]])
kmeans = kmeans_plusplus(n_clusters=2, random_state=0).fit(X)
print(kmeans.labels_)
kmeans.predict([[0, 0], [12, 3]])
print(kmeans.cluster_centers_)

