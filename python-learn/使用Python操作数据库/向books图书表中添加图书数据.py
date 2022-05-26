import pymysql

db = pymysql.connect(host="localhost", user="root", passwd="2168884970", database="mysqltest", charset="utf8")
# 使用cursor()方法创建一个游标对象cursor
cursor = db.cursor()
data = [
    ("零基础学python", "Python", "89.5", "2018-5-20"),
    ("Python从基础到精通", "Python", "56.5", "2018-09-27"),
]
try:
    # 执行SQL语句，插入多条数据。
    cursor.executemany("insert into books(name, category, price, publish_time) values (%s,%s,%s,%s)", data)
    # 提交数据
    db.commit()
except:
    # 放生错误时回滚
    db.rollback()

db.close()
