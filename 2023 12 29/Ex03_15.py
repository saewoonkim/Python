import sqlite3
from tkinter import * 
"""
윈도우창
"""
from tkinter import messagebox

def insertData():
    con, cur = None, None
    data1, data2, data3, data4 = "", "", "", ""
    sql = ""

    con = sqlite3.connect()
    cur = con.cursor()

    data1 = edt1.get(); data2 = edt2.get(); data3 = edt3.get(); data4 = edt4.get()

    """
    이어 쓸꺼면 ;넣어줘야됨 get 문으로 데이터를 가져올수있음
    """
    try :
        sql = "insert into userTable1 values(' "+data1+" ',  ' "+data2+" ' , ' "+data3+" ', ' " +data4+ " ' )"
        cur.execute(sql)
    except :
        messagebox.showerror('오류', '데이터 입력 오류')
    else :
        messagebox.showinfo('성공', '데이터 입력 성공')
    con.commit()
    con.close()
    
def selectData():
    strData1, strData2, strData3, strData4 = [], [], [], []
    con = sqlite3.connect("C:/Users/ds/Desktop/2023 12 29/myDB")
    cur = con.cursor()
    cur.execute("select * from userTable1")
    strData1.append("사용자 ID"); strData2.append("이름");
    strData3.append("이메일"); strData4.append("생일");
    strData1.append("-------------"); strData2.append("-------------");
    strData3.append("-------------"); strData4.append("-------------");
    while True:
        row = cur.fetchone()
        if row == None:
            break
        strData1.append(row[0]); strData2.append(row[1])
        strData3.append(row[2]); strData4.append(row[3])

    listData1.delete(0, listData1.size() - 1)
    listData2.delete(0, listData2.size() - 1)
    listData3.delete(0, listData3.size() - 1)
    listData4.delete(0, listData4.size() - 1)

    for item1, item2, item3, item4 in zip(strData1, strData2, strData3, strData4):
        listData1.insert(END, item1)
        listData2.insert(END, item2)
        listData3.insert(END, item3)
        listData4.insert(END, item4)
    con.close()

def deleteData():
    con, cur = None, None
    con = sqlite3.connect("C:/Users/ds/Desktop/2023 12 29/myDB")
    cur = con.cursor()
    delid = edt1.get()
    print(delid)
    sql = "delete from userTable1 where id = 'john' "
    cur.execute(sql)
     
    con.commit()
    con.close()
        
##메인

window = Tk()
"""
윈도우창
"""
window.geometry("600x300")
window.title("데이터관리")

edtFrame = Frame(window)
edtFrame.pack()
listFrame = Frame(window)
listFrame.pack(side = BOTTOM, fill = BOTH, expand = 1)

edt1= Entry(edtFrame, width=10); edt1.pack(side = LEFT, padx = 10, pady = 10)
"""
pack 안에 들어가야 버튼 간격 조정
padx 간격 pady 간격 이만큼씩 서로 띄우자
"""
edt2= Entry(edtFrame, width=10); edt2.pack(side = LEFT, padx = 10, pady = 10)
edt3= Entry(edtFrame, width=10); edt3.pack(side = LEFT, padx = 10, pady = 10)
edt4= Entry(edtFrame, width=10); edt4.pack(side = LEFT, padx = 10, pady = 10)

btnInsert = Button(edtFrame, text = "입력", command = insertData)
btnInsert.pack(side = LEFT, padx = 10, pady = 10)
btnselect = Button(edtFrame, text = "조회", command = selectData)
btnselect.pack(side = LEFT, padx = 10, pady = 10)
btnselect = Button(edtFrame, text = "삭제", command = deleteData)
btnselect.pack(side = LEFT, padx = 10, pady = 10)

listData1 = Listbox(listFrame, bg = 'yellow')
listData1.pack(side = LEFT, fill = BOTH, expand = 1)
"""
expand = 1 꽉체워지는 효과
"""
listData2 = Listbox(listFrame, bg = 'yellow')
listData2.pack(side = LEFT, fill = BOTH, expand = 1)
listData3 = Listbox(listFrame, bg = 'yellow')
listData3.pack(side = LEFT, fill = BOTH, expand = 1)
listData4 = Listbox(listFrame, bg = 'yellow')
listData4.pack(side = LEFT, fill = BOTH, expand = 1)

window.mainloop()











