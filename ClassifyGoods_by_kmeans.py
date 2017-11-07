# coding=utf-8
# created by czc on 2017.7.18
import re

import gensim

from mysql_module import mysql_connector                        # 引入自定义 mysql 数据库操作模块
from gensim.models.doc2vec import Doc2Vec
import jieba                                                    # 引入 jieba 分词包
import Kmeans_module

mysql_conn = mysql_connector(host='127.0.0.1', user='root', password='1234', port='3306', database='tmall_comments4gift')
mysql_conn.connect()
result = mysql_conn.execute("select name from product")

stopwords = {}.fromkeys([line.rstrip() for line in open('stopwords_HIT.txt')])      # 导入哈工大中文停用词语库
goods_list = []
words_list_ofOne = []
i = 0
for good_name in result:
    good_name = good_name[0]                                # for 语句获得的 good_name 是元组
    seg_list = jieba.cut(good_name, cut_all=False)          # 分词，cut_all=true 时为精确模式，默认为精确模式; cut_all=false 时为全模式
    final_list = []
    for seg in seg_list:                                    # 剔除停用词
        if seg not in stopwords:
            if not re.match(r"\d+\w{0,2}\W*\d*$", seg) and not seg == " ":         # 去掉空格、纯数字以及表示质量或容量的词
                final_list.append(seg)
    TaggededDocument = gensim.models.doc2vec.TaggedDocument
    words_list_ofOne.append(final_list)
    document = TaggededDocument(final_list, tags=[i])
    goods_list.append(document)                             # 把商品名称依次加入集合中
    i += 1

print(words_list_ofOne)
# print(goods_list)

# size 为向量维度
# model_dm = Doc2Vec(goods_list, size=20, window=8, min_count=200, workers=4, iter=20)        # 目前效果较好
model_dm = Doc2Vec(goods_list, size=20, window=8, min_count=2, workers=4, iter=20)

model_dm.train(goods_list, total_examples=model_dm.corpus_count, epochs=70)

print("训练文档向量共 ", len(model_dm.docvecs), "条")

model_dm.docvecs.save('model/docvec_tmall')
model_dm.save('model/model_dm_tmall')

# 释放不需要的内存
model_dm.delete_temporary_training_data(keep_doctags_vectors=True, keep_inference=True)

clusterModel = Kmeans_module.kmeans(k=15, vec_set=model_dm.docvecs)
clusters_ofIndex = clusterModel.train()
print(clusters_ofIndex)
for i in range(0, len(clusters_ofIndex)):
    print("簇 ", i, ": ")
    for index in clusters_ofIndex[i]:
        print(result[index])
