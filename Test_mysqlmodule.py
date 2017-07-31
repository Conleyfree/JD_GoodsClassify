# coding=utf-8
# created by czc on 2017.7.18

from mysql_module import mysql_connector

print("test..")
mysql_conn = mysql_connector(host='127.0.0.1', user='root', password='1234', port='3306', database='tmall_comments')
mysql_conn.connect()
result = mysql_conn.execute("select * from product")
print(result)