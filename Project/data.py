# coding=utf-8
import torch
import pickle
# import gensim
# model = gensim.models.KeyedVectors.load_word2vec_format('word_embd.pickle')
# weights = torch.FloatTensor(model.vectors)

weight = open("word_embd.pickle",'rb')
weights = pickle.load(weight)
w = torch.tensor(weights)
embedding = torch.nn.Embedding.from_pretrained(w)
# Get embeddings for index 1
input = torch.LongTensor([1])  #必须用Longtensor

print(embedding(input))