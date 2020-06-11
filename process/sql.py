#!/usr/bin/env python3
import pymysql

db = pymysql.connect("localhost", "root", "123456", "stbweb")

cus = db.cursor()
cus.execute("select * from user")
data = cus.fetchall()
print(len(data))
for da in data:
    print(da)
# print(da[len(data)-1])
db.close()
