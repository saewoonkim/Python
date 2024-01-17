"""
import sqlite3

##변수 선언
con, cur = None, None
data1, data2, data3, data4 = "", "", "", ""

##메인 코드
con = sqlite3.connect("C:/Users/ds/Desktop/2023 12 29/myDB")
cur = con.cursor()
루틴한거 무조건 기억 콘 커서 디비 연결
sql = ""
while True:
    data1 = input("아이디 : ")
    if data1 == "":
        break
    data2 = input("이름 : ")
    data3 = input("이메일 : ")
    data4 = input("년도: ")
    sql = "insert into userTable1 values(' "+data1+" ',  ' "+data2+" ' , ' "+data3+" ', ' " +data4+ " ' )"
    cur.execute(sql)
    
con.commit()
con.close()

"""

cur.execute("create table userTable1 (id char(4), userName char(15), email char(20), birth int)")
cur.execute("insert into userTable1 values('john', 'john Lee', 'abc@naver.com', 1999)")
cur.execute("insert into userTable1 values('kang', 'Jihoon', 'def@naver.com', 2000)")
cur.execute("insert into userTable1 values('Kim', 'Seondal', 'ghi@naver.com', 1988)")






