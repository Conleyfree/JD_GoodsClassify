# coding=utf-8
# created by czc on 2017.7.18

from mysql_module import mysql_connector
import difflib
import jieba                                                # 引入结巴分词（中文分词）模块

mysql_conn = mysql_connector(host='127.0.0.1', user='root', password='1234', port='3306', database='tmall_comments')
mysql_conn.connect()
result = mysql_conn.execute("select name from product")

goods_list = []
for good_name in result:
    goods_list.append(good_name)                            # 把商品名称依次加入集合中


