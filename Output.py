import numpy as np
from Bert_Model import Bert_Model
from Bert_Summarizer import Bert_Summarizer


class Output:

    def __init__(self, path_input):
        self.path = path_input

    def compute_notes(self):
        bert = Bert_Model(self.path)
        bert_encode, sentences_list, lines, timestamps = bert.run()
        summary = Bert_Summarizer(sentences_list, bert_encode)
        sentence_ind, kmeans, n_cluster = summary.get_indices()
        return summary.indices_to_english(sentence_ind, toPrint=True)