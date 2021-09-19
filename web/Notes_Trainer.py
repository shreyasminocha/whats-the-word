import Clustering
import numpy as np

def get_all_vectors(embed_list):
    '''
    list of bert_embed arrays
    '''
    for sheet in (embed_list):
        english_sentences = np.array(english_sentences_input, copy=True)
        bert_embed = np.array(bert_embed_input, copy=True)


        n_cluster_max = 100
        cluster = Clustering(self.bert_embed)
        n_cluster, kmeans = cluster.compute_optimal_custer(n_cluster_max)
        sentence_ind = cluster.get_central_sentences(n_cluster, kmeans)
        



    