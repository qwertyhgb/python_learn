import pymysql

db = pymysql.connect(host="localhost", user="root", passwd="2168884970", database="mysqltest")
# 使用cursor()方法创建一个游标对象cursor
cursor = db.cursor()
# 使用execute()方法执行SQL查询
cursor.execute("DROP TABLE IF EXISTS books")
sql = """
CREATE TABLE books (
	id INT ( 8 ) NOT NULL auto_increment,
	NAME VARCHAR ( 50 ) NOT NULL,
	category VARCHAR ( 50 ) NOT NULL,
	price DECIMAL ( 10, 2 ) DEFAULT NULL,
	publish_time date DEFAULT NULL,
PRIMARY KEY ( id ) 
) ENGINE = MyISam auto_increment = 1 DEFAULT charset = utf8;
"""
# 执行sql语句
cursor.execute(sql)
db.close()