import pymysql

conn = pymysql.connect("localhost", "root", "rootpass", "registration_form")
cur = conn.cursor()
sql = "SELECT * FROM students"
cur.execute(sql)
data = cur.fetchall()
for record in data:
    print(record)
