import Clustering
import numpy as np

class Bert_Summarizer:

    def __init__(self, english_sentences_input, bert_embed_input):
        '''
        Constructor for Bert_Summarizer class.
        In
            english_sentences_input; array-like of strings representing english sentences
            bert_embed_input; sentence embedding array output by BERT
                                array-like of shape (n_samples, n_features)
        '''
        self.english_sentences = np.array(english_sentences_input, copy=True)
        self.bert_embed = np.array(bert_embed_input, copy=True)

    def summarize(self):
        '''
        Summarizes the content in self.english_sentences using Clustering and BERT
        Out
            english; array of english sentences that summarize the main points
            sentence_ind; array of the indices of english found in self.english_sentences
            kmeans; sklearn.cluster.KMeans object representing the fitted cluster of bert embeds
            n_cluster; number of clusters, equivalent to number of returned english sentences
        '''
        n_cluster_max = 10
        cluster = Clustering(self.bert_embed)
        n_cluster, kmeans = cluster.compute_optimal_custer(n_cluster_max)
        sentence_ind = cluster.get_central_sentences(n_cluster, kmeans)
        english = self.indices_to_english(sentence_ind, toPrint=False)
        return english, sentence_ind, kmeans, n_cluster

    def indices_to_english(self, indices, toPrint):
        '''
        Returns the english sentences in self.english_sentences located at indices
        In
            indices; array of indices from self.english_sentences to return as english
            toPrint; boolean of whether to print to terminal the returned english
        Out
            array of the english sentences located at indices within self.english_sentences
        '''
        english = np.chararray(indices.shape)
        for ind in indices:
            english[ind] = self.english_sentences[ind]
        if toPrint:
            print(english)
        return english


