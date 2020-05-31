import pymysql
db = pymysql.connect(host = 'localhost', user = 'admin', password = '1234', db = 'testdb')
cursor = db.cursor()
cursor.execute("select version();")
data = cursor.fetchone()
print("database version %s" % data)
db.close()