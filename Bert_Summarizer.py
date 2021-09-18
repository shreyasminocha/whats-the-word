import Clustering


english_sentences = None
bert_embed = None

cluster = Clustering(bert_embed)
n_cluster, kmeans = cluster.compute_optimal_cluster(10)
sentence_ind = cluster.get_central_sentences(n_cluster, kmeans)

for ind in sentence_ind:
    print(english_sentences[ind])


