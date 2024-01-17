import sqlite3

con, cur = None, None
data1, data2, data3, data4 = "", "", "", ""
row = None

con = sqlite3.connect("C:/Users/ds/Desktop/2023 12 29/myDB")
cur = con.cursor()

cur.execute("select * from userTable1")
print("id \t name \t email \t year \t ")
while True:
    row = cur.fetchone()
    if row == None:
        break
    data1 = row[0]
    data2 = row[1]
    data3 = row[2]
    data4 = row[3]
    print("%s \t %s \t %s \t %s" % (data1, data2, data3, data4))

con.close()



    
