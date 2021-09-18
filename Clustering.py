import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

class Clustering:

    def __init__(self, bert_embed_input):
        '''
        Initializes this instance of Clustering class.
        In
            bert_embed_input; sentence embedding array output by BERT
                                array-like of shape (n_samples, n_features)
        '''
        self.bert_embed = np.array(bert_embed_input, copy=True)

    def apply_embed_weights(self, weights):
        '''
        Assigns user-defined weights to each element of the embedding vectors.
        In
            weights; numerical weights to apply to self.bert_embed across the features
        '''
        for sentence_ind in range(self.bert_embed.length):
            self.bert_embed[sentence_ind:] = np.multiply(self.bert_embed[sentence_ind:], weights)
    
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

    def compute_optimal_cluster(self, n_cluster_max):
        '''
        Finds the optimal number of clusters
        In
            n_cluster_max; the max # of clusters to be inspected
        Out
            # clusters that yields the maximum silhouette score
            fitted KMeans instance with the optimal # clusters
        '''
        best_silh = -1
        best_n_cluster = None
        best_KMeans = None
        for n_cluster in range(5, n_cluster_max):
            KMeans_fitted = self.fit_cluster(n_cluster)
            silh = self.get_silh(KMeans_fitted)
            if silh > best_silh:
                print("here")
                best_silh = silh
                best_n_cluster = n_cluster
                best_KMeans = KMeans_fitted
        return best_n_cluster, best_KMeans

    def get_central_sentences(self, n_cluster, KMeans_fitted):
        '''
        Find the best sentence for each cluster "main idea"
        In
            n_cluster; number of clusters
            KMeans_fitted; fitted KMeans instance
        Out
            Array of the indices of each central sentence within self.bert_embed
        '''
        main_sentences = np.empty((n_cluster, 1), dtype=np.int16)
        for cluster_id in range(n_cluster):
            clustered_sentences = self.get_clustered_sentences(cluster_id, KMeans_fitted)
            centroid = KMeans_fitted.cluster_centers_[cluster_id]
            lowest_dist = float('inf')
            best_sentence = -1
            for sentence_ind in clustered_sentences:
                dist = self.distance(self.bert_embed[sentence_ind], centroid)
                if dist < lowest_dist:
                    lowest_dist = dist
                    best_sentence = sentence_ind
            main_sentences[cluster_id, 0] = best_sentence
        return main_sentences

    def distance(self, vec1, vec2):
        return np.linalg.norm(vec1 - vec2)

    def get_clustered_sentences(self, cluster_id, KMeans_fitted):
        '''
        Returns indices of the self.bert_embed sentences that belong to specified cluster
        In
            cluster_id; integer identifier of the cluster of interest
            KMeans_fitted; fitted KMeans model instance
        Out
            array of the indices of self.bert_embed sentences of cluster cluster_id
        '''
        indices = np.where(KMeans_fitted.labels_ == cluster_id)
        print("indices")
        print(indices)
        print("_____")
        return indices[0]


