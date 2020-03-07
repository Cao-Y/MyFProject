# -*- coding: utf-8 -*-
# from gensim.models import word2vec
# # from gensim.models import KeyedVectors
# # # model =KeyedVectors.load_word2vec_format(r'搜狗新闻.model', binary=True)
# # # model.save_word2vec_format(r'Vecc.txt', binary=False)
#
# model2 = word2vec.Word2Vec.load('02_jieba.model')
# print(model2.wv.get_vector('大叔'))
# list = model2.wv.get_vector('大叔')
# #model2.wv.save_word2vec_format('test.txt', binary=False)
# num = 0
# for i in range(len(list)):
#     num = num+list[i]
#
# print(num)
from gensim.models.word2vec import Word2Vec
model = Word2Vec.load("02_jieba.model")  #w2v_model是已经生成的模型
#print(model.wv.index2word())    #获得所有的词汇
data = model.wv.index2word
for word in data:
	print(word,model.wv[word])     #获得词汇及其对应的向量
