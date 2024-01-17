import sqlite3

con = sqlite3.connect("C:/Users/ds/Desktop/2023 12 29/DBtest")
cur = con.cursor()


cur.execute("create table userTable (id char(4), username char(15), email char(20), birthyear char(4))")
con.commit()

