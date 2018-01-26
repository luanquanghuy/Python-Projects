#!/usr/bin/python3.6
import pymysql

dbcon = pymysql.connect(host= 'localhost', user = 'root', passwd = "Z'xpd[FKv5ZY", db = 'newdata', charset = 'utf8')
if dbcon:
    cur = dbcon.cursor()
    cur.execute("SELECT VERSION()")
    ver = cur.fetchone()
    print(ver)