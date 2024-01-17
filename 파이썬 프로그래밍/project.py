import sqlite3
from tkinter import *
from tkinter import messagebox

##함수선언##

def insertData():
    con, cur = None, None
    data1, data2, data3, data4 = "", "", "", ""
    sql = ""

    con = sqlite3.connect("C:/Users/ds/Desktop/2023 12 29/DBtest")
    cur = con.cursor()

    data1 = edt1.get()
    data2 = edt2.get()
    data3 = edt3.get()
    data4 = edt4.get()
    
    try :
        sql = "insert into userTable values('"+data1+"','"+data2+"','"+data3+"','"+data4+"')"
        cur.execute(sql)
        
    except :
        messagebox.showerror('오류', '데이터 입력 오류')
        
    else :
        messagebox.showinfo('성공', '데이터 입력 성공')
        
    con.commit()
    selectData()
    con.close()


def selectData():
    strData1, strData2, strData3, strData4 = [], [], [], []
    con, cur = None, None
    data1, data2, data3, data4 = "", "", "", ""
    con = sqlite3.connect("C:/Users/ds/Desktop/2023 12 29/DBtest")
    cur = con.cursor()
    
    sql = "select * from userTable"
    cur.execute(sql)
    
    strData1.append("사용자 ID")
    strData2.append("이름")
    strData3.append("이메일")
    strData4.append("생일")
    
    strData1.append("----------------------------------")
    strData2.append("----------------------------------")
    strData3.append("----------------------------------")
    strData4.append("----------------------------------")

    while True:
        row = cur.fetchone()
        if row == None:
            break
        strData1.append(row[0])
        strData2.append(row[1])
        strData3.append(row[2])
        strData4.append(row[3])    

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
    data1, data2, data3, data4 = "", "", "", ""
    sql = ""
    
    con = sqlite3.connect("C:/Users/ds/Desktop/2023 12 29/DBtest")
    cur = con.cursor()
    
    data1 = edt1.get()
    data2 = edt2.get()
    data3 = edt3.get()
    data4 = edt4.get()

    try:
        sql = "delete from userTable where id = '"+data1+"'"
        cur.execute(sql)
    
    except :
        messagebox.showerror('오류', '데이터 입력 오류')
        
    else :
        messagebox.showinfo('성공', '데이터 삭제 성공')
    
     
    con.commit()
    print(cur.rowcount, "삭제")
    con.close()


def updateData():
    
    con, cur = None, None
    data1, data2, data3, data4 = "", "", "", ""
    sql = ""
    
    con = sqlite3.connect("C:/Users/ds/Desktop/2023 12 29/DBtest")
    cur = con.cursor()

    data1 = edt1.get()
    data2 = edt2.get()
    data3 = edt3.get()
    data4 = edt4.get()


    try:
        sql = "UPDATE userTable SET username = '"+data2+"',email ='"+data3+"' ,birthyear = '"+data4+"' WHERE id = '"+data1+"'" 
        cur.execute(sql)

    except :
        messagebox.showerror('오류', '데이터 입력 오류')
        
    else :
        messagebox.showinfo('성공', '데이터 수정 성공')

    con.commit()
    print(cur.rowcount, "수정")
    con.close()


def allDeleteData():
    con = sqlite3.connect("C:/Users/ds/Desktop/2023 12 29/DBtest")
    cur = con.cursor()

    try:
        sql = "delete from userTable"
        cur.execute(sql)
        
    except :
        messagebox.showerror('오류', '데이터 입력 오류')
        
    else :
        messagebox.showinfo('성공', '데이터 전체 삭제 성공')

    
    con.commit()
    print(cur.rowcount, "모든 DB삭제")
    con.close()
    
##메인코드##
window = Tk()
window.geometry("700x300")
window.title("DataBase 관리")

edtFrame = Frame(window)
edtFrame.pack()
listFrame = Frame(window)
listFrame.pack(side = BOTTOM, fill = BOTH, expand = 1)

edt1 = Entry(edtFrame, width = 10)
edt1.pack(side=LEFT, padx = 10, pady = 10)
edt2 = Entry(edtFrame, width = 10)
edt2.pack(side=LEFT, padx = 10, pady = 10)
edt3 = Entry(edtFrame, width = 10)
edt3.pack(side=LEFT, padx = 10, pady = 10)
edt4 = Entry(edtFrame, width = 10)
edt4.pack(side=LEFT, padx = 10, pady = 10)

btnInsert = Button(edtFrame, text = "입력", command = insertData)
btnInsert.pack(side=LEFT, padx = 10, pady = 10)
btnSelect = Button(edtFrame, text = "조회", command = selectData)
btnSelect.pack(side=LEFT, padx = 10, pady = 10)
btnselect = Button(edtFrame, text = "삭제", command = deleteData)
btnselect.pack(side = LEFT, padx = 10, pady = 10)
btnselect = Button(edtFrame, text = "수정", command = updateData)
btnselect.pack(side = LEFT, padx = 10, pady = 10)
btnselect = Button(edtFrame, text = "전체삭제", command = allDeleteData)
btnselect.pack(side = LEFT, padx = 10, pady = 10)

listData1 = Listbox(listFrame, bg = 'lightgrey')
listData1.pack(side=LEFT, fill = BOTH, expand = 1)
listData2 = Listbox(listFrame, bg = 'lightgrey')
listData2.pack(side=LEFT, fill = BOTH, expand = 1)
listData3 = Listbox(listFrame, bg = 'lightgrey')
listData3.pack(side=LEFT, fill = BOTH, expand = 1)
listData4 = Listbox(listFrame, bg = 'lightgrey')
listData4.pack(side=LEFT, fill = BOTH, expand = 1)

window.mainloop()







