# coding=utf-8
# created by czc on 2017.7.18

import mysql.connector


class mysql_connector:

    config={'host': '127.0.0.1',    # 默认127.0.0.1
            'user': 'root',         # 用户名
            'password': '123456',   # 密码
            'port': 3306,           # 默认即为3306
            'database': 'test',     # 数据库名
            'charset': 'utf8'       # 默认即为utf8
            }
    conn = None

    # 初始化
    def __init__(self, host, user, password, port, database):
        self.config['host'] = host
        self.config['user'] = user
        self.config['password'] = password
        self.config['port'] = port
        self.config['database'] = database

    # 建立连接
    def connect(self):
        try:
            self.conn = mysql.connector.connect(**self.config)
        except mysql.connector.Error as e:
            print('connect fails!{}'.format(e))

    # 执行语句
    def execute(self, sql_query):
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql_query)
            values = cursor.fetchall()
            return values
        except mysql.connector.Error as e:
            print('execute error!{}'.format(e))
        finally:
            cursor.close()
            self.conn.close()


