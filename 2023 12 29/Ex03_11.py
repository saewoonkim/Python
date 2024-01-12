"""
import turtle
import random

##변수 선언
pSize = 10
r, g, b = 0.0, 0.0, 0.0

##함수

def screenLeftClick(x, y):
    global r, g, b
    turtle.pencolor((r,g,b))
    turtle.pendown()
    turtle.goto(x, y)

def screenRightClick(x, y):
    turtle.penup()
    turtle.goto(x,y)

def screenMidClick(x,y):
    global r, g, b
    tSize = random.randrange(1,10)
    turtle.shapesize(tSize)
    r = random.random()
    g = random.random()
    b = random.random()

##메인
turtle.title('거북이로 그림 그리기')
turtle.shape('turtle')
turtle.pensize(pSize)

turtle.onscreenclick(screenLeftClick, 1)##왼쪽 클릭은 1
turtle.onscreenclick(screenMidClick, 2)##가운데 클릭은 2
turtle.onscreenclick(screenRightClick, 3)##오른쪾 클린은 3

turtle.done()







from time import *
from tkinter import *

##전역 변수
fnameList = ['a.gif', 'b.gif', 'c.gif']
photoList = [None]*3
num = 0

##함수 선언

def clickNext():
    global num
    num += 1
    if num > 2:
        num = 0
    photo = PhotoImage(file = fnameList[num])
    pLabel.configure(image = photo)
    pLabel.image = photo

def clickPrev():
    global num
    num -= 1
    if num < 0:
        num = 2
    photo = PhotoImage(file = fnameList[num])
    pLabel.configure(image = photo)
    pLabel.image = photo

##메인

window = Tk()
window.geometry("700x500")
window.title("사진앨범보기")

btnPrev = Button(window, text = "<< 이전", command = clickPrev)
btnNext = Button(window, text = "다음 >>", command = clickNext)

photo = PhotoImage(file = fnameList[0])
pLabel = Label(window, image = photo)

btnPrev.place(x = 250, y = 10)
btnNext.place(x = 400, y = 10)
pLabel.place(x = 15, y = 50)

window.mainloop()





import turtle
import random

class Shape:
    myTurtle = None
    cx, cy = 0, 0

    def __init__(self):
        self.myTurtle =  turtle.Turtle("turtle")

    def setPen(self):
        r = random.random()
        g = random.random()
        b = random.random()
        self.myTurtle.pencolor(r,g,b)
        pSize = random.randrange(1,10)
        self.myTurtle.pensize(pSize)

    def drawShape(self):
        pass

class Rectangle(Shape):
    width, height = [0] * 2

    def __init__(self, x, y):
        Shape.__init__(self)
        self.cx = x
        self.cy = y
        self.width = random.randrange(20, 100)
        self.height = random.randrange(20, 100)

    def drawShape(self):
        lx, ly, rx, ry = [0] * 4
        lx = self.cx - self.width / 2
        ly = self.cy - self.height / 2
        rx = self.cx + self.width / 2
        ry = self.cy + self.height / 2

        self.setPen()
        self.myTurtle.penup()
        self.myTurtle.goto(lx, ly)
        self.myTurtle.pendown()
        self.myTurtle.goto(lx, ry)
        self.myTurtle.goto(rx, ry)
        self.myTurtle.goto(rx, ly)
        self.myTurtle.goto(lx, ly)

def screenLeftClick(x, y):
    rect = Rectangle(x,y)
    rect.drawShape()
    
##메인
turtle.title("객체지향 거북이")
turtle.onscreenclick(screenLeftClick, 1)
turtle.done()


"""





