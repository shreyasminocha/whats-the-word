from transformers import BertTokenizer, BertModel
import numpy as np
import torch
from pysubparser import parser
import re

class Bert_Model:

  def __init__(self):
    '''
    Initializer for Bert_Model class.
    In
      path; string filepath of the srt file of lecture transcript
    '''
    self.model = BertModel.from_pretrained('bert-base-uncased', output_hidden_states = True)
    self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')


  def make_english_sentences(self, transcript_path):
    '''
    Converts srt file to list of separate full english sentences.
    In
      transcript_path, string filepath of the srt file of lecture transcript
    Out
      sentences_list; list of separate full sentences within transcript
    '''
    transcript = parser.parse(transcript_path)
    timestamps = []
    lines = []
    for line in transcript:
        timestamps.append(str(line.start))
        lines.append(str(line))


    lines_len = len(lines)

    for line_ind in range(lines_len):
      cur_line = lines[line_ind]
      try:
        cur_line_index = cur_line.index('>')
        new_line = cur_line[cur_line_index+2:]
        lines[line_ind] = new_line
      except:
        pass


    sentences_list = []
    past_line_fragment = ''
    for ind_line in range(lines_len):
      cur_line = lines[ind_line]
      cur_line_arr = re.split('[\.?!]', cur_line)
      cur_line_arr_len = len(cur_line_arr)

      # Remove (possibly) some elements in the end of cur_line_arr
      # such that the last element in cur_line_arr is not empty
      ind_cur_line_arr = cur_line_arr_len-1
      last_ele_is_empty = not cur_line_arr[cur_line_arr_len-1];
      cur_line_ends_with_period = False

      while last_ele_is_empty:
        cur_line_ends_with_period = True
        last_ele_is_empty = not cur_line_arr[cur_line_arr_len-1]
        if (last_ele_is_empty):
          cur_line_arr.pop()
          cur_line_arr_len -= 1

      cur_line_arr_len = len(cur_line_arr)

      ind_sentence_start = 0
      if past_line_fragment:
        if (cur_line_ends_with_period) or not cur_line_arr_len <= 1:
          sentences_list.append(past_line_fragment+' '+cur_line_arr[0])
          past_line_fragment = ''
          ind_sentence_start = 1

      for ind_sentence in range(ind_sentence_start, cur_line_arr_len):
        if (not cur_line_ends_with_period) and ind_sentence == cur_line_arr_len-1:
          add_space = True if past_line_fragment else False
          if add_space:
            past_line_fragment += ' '
          past_line_fragment += (cur_line_arr[cur_line_arr_len-1])
          break
        sentences_list.append(cur_line_arr[ind_sentence])

    return sentences_list #, lines, timestamps

    # Don't append the past_line_fragment after the for loop because
    # the past_line_fragment (represents the last line fragment that doesn't make a complete sentence)
    # may not be a complete sentence.


  def bert_text_preparation(self, text, tokenizer):
    """Preparing the input for BERT

    Takes a string argument and performs
    pre-processing like adding special tokens,
    tokenization, tokens to ids, and tokens to
    segment ids. All tokens are mapped to seg-
    ment id = 1.

    Args:
        text (str): Text to be converted
        tokenizer (obj): Tokenizer object
            to convert text into BERT-re-
            adable tokens and ids

    Returns:
        list: List of BERT-readable tokens
        obj: Torch tensor with token ids
        obj: Torch tensor segment ids


    """
    marked_text = "[CLS] " + text + " [SEP]"
    tokenized_text = tokenizer.tokenize(marked_text)
    indexed_tokens = tokenizer.convert_tokens_to_ids(tokenized_text)
    segments_ids = [1]*len(indexed_tokens)

    # Convert inputs to PyTorch tensors
    tokens_tensor = torch.tensor([indexed_tokens])
    segments_tensors = torch.tensor([segments_ids])

    return tokenized_text, tokens_tensor, segments_tensors

  def get_bert_embeddings(self, tokens_tensor, segments_tensors, model):
    """Get embeddings from an embedding model

    Args:
        tokens_tensor (obj): Torch tensor size [n_tokens]
            with token ids for each token in text
        segments_tensors (obj): Torch tensor size [n_tokens]
            with segment ids for each token in text
        model (obj): Embedding model to generate embeddings
            from token and segment ids

    Returns:
        list: List of list of floats of size
            [n_tokens, n_embedding_dimensions]
            containing embeddings for each token

    """

    # Gradient calculation id disabled
    # Model is in inference mode
    with torch.no_grad():
        outputs = model(tokens_tensor, segments_tensors)
        # Removing the first hidden state
        # The first state is the input state
        hidden_states = outputs[2][1:]

    # Getting embeddings from the final BERT layer
    token_embeddings = hidden_states[-1]
    # Collapsing the tensor into 1-dimension
    token_embeddings = torch.squeeze(token_embeddings, dim=0)
    # Converting torchtensors to lists
    list_token_embeddings = [token_embed.tolist() for token_embed in token_embeddings]

    return list_token_embeddings


  def run_bert_encoding(self, sentences_list, num_attributes=768):
    # Getting embeddings for the target
    # word in all given contexts
    sentences_list_len = len(sentences_list)
    target_word_embeddings = np.empty((sentences_list_len, num_attributes))

    sentence_ind = 0
    for text in sentences_list:
        tokenized_text, tokens_tensor, segments_tensors = self.bert_text_preparation(text, self.tokenizer)
        list_token_embeddings = self.get_bert_embeddings(tokens_tensor, segments_tensors, self.model)

        #if (sentence_ind > 100):
        #  break

        # if (sentence_ind < 3):
        #   print(len(tokenized_text))
        #   print(tokenized_text[0])
        #   print(tokenized_text)
        #   print(len(list_token_embeddings))
        #   print(len(list_token_embeddings[0]))
        #   print("after one list token embeddings")


        # Find the position 'bank' in list of tokens
        #word_index = tokenized_text.index('bank')
        # Get the embedding for bank

        token_len = len(tokenized_text)

        # for ind_token in range(token_len):
        #   word_embedding = list_token_embeddings[ind_token]
        #   target_word_embeddings.append(word_embedding)

        a = np.array(list_token_embeddings)
        res = np.average(a, axis=0)
        target_word_embeddings[sentence_ind:] = res

        #target_word_embeddings.append(word_embedding)
        sentence_ind += 1
    return target_word_embeddings



