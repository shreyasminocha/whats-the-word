import numpy as np
from Bert_Model import Bert_Model
from Bert_Summarizer import Bert_Summarizer

path = 'Test_SRT.srt'
bert = Bert_Model(path)
bert_encode, sentences_list, lines, timestamps = bert.run()
print(len(sentences_list))
summary = Bert_Summarizer(sentences_list, bert_encode)
sentence_ind, kmeans, n_cluster = summary.get_indices()
print(sentence_ind, n_cluster)
notes = summary.indices_to_english(sentence_ind, toPrint=True)
