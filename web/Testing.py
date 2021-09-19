import numpy as np
from Bert_Model import Bert_Model
from Bert_Summarizer import Bert_Summarizer
from speech_to_text import speech_to_text
from Output import Output

# path = 'Test_SRT.srt'
# bert = Bert_Model()
# sentences_list = bert.make_english_sentences(path)
# bert_encode = bert.run_bert_encoding(sentences_list)
# print(len(sentences_list))
# summary = Bert_Summarizer(sentences_list, bert_encode)
# sentence_ind, kmeans, n_cluster = summary.get_indices()
# print(sentence_ind, n_cluster)
# notes = summary.indices_to_english(sentence_ind, toPrint=True)

# mp3_path = "gs://lecture_audio_files/Phil Lempert's 2 minute Speech Demo.mp3"
# sentences = speech_to_text(mp3_path)
# out = Output()
# out.set_sentences(sentences)
# print(out.compute_notes())

# srt_path = "Intro-to-Psychology-Crash-Course-Psychology-1.srt"
# out = Output()
# out.set_sentences_using_srt_path(srt_path)
# print(out.compute_notes())

mp3_path = "gs://lecture_audio_files/videoplayback.mp3"
sentences = speech_to_text(mp3_path)
out = Output()
out.set_sentences(sentences)
print(out.compute_notes())

