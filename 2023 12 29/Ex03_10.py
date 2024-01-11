"""

import random
import itertools
student = ['김승현', '김진호', '강춘자', '이예준', '김현주']
work = ['청소','빨래','설거지' ]

student = random.sample(student, len(student))
result = list(itertools.zip_longest(student, work, fillvalue="rest"))

print(result)
print(len(result))


import math

width = 200
height = 80

size = math.gcd(200, 80)

print("길이 %d" % size)

width_count = width / size
height_count = height / size
print("개수 %d" % (width_count * height_count))

num = int(input("1~1000사이의 정수 입력 : "))
result = 0

for i in range(1, num+1):
    if i % 3 == 0 or i % 5 == 0:
        result += i
print(result)


def page_count(total, perPage):
    count = 0
    if total % perPage == 0:
        return total // perPage
    else :
        return (total // perPage) + 1

print("필요 페이지 수 %d 개" % page_count(5, 10))
print("필요 페이지 수 %d 개" % page_count(50, 10))
print("필요 페이지 수 %d 개" % page_count(70, 10))


import turtle
import random

myTurtle, tX, tY, tColor, tSize, tShape = [None]*6

shapeList = []
playerTurtles = []

swidth, sheight = 500, 500

if  __name__  ==  "__main__":
    turtle.title('거북 리스트 활용')
    turtle.setup(width = swidth + 50, height = sheight + 50)
    turtle.screensize(swidth, sheight)

    shapeList = turtle.getshapes()
    for i in range(0,100):
        random.shuffle(shapeList)
        myTurtle = turtle.Turtle(shapeList[0])
        tX = random.randrange(-swidth // 2, swidth // 2)
        tY = random.randrange(-sheight // 2, sheight // 2)
        r = random.random(); g = random.random(); b = random.random()
        tSize = random.randrange(1,3)
        playerTurtles.append([myTurtle, tX, tY, tSize, r, g, b])

    for tList in playerTurtles:
        myTurtle = tList[0]
        myTurtle.color((tList[4], tList[5], tList[6]))
        myTurtle.pencolor((tList[4], tList[5], tList[6]))
        myTurtle.turtlesize(tList[3])
        myTurtle.goto(tList[1], tList[2])

    turtle.done()
        
        
import turtle
import random

myTurtle, tX, tY, tColor, tSize, tShape = [None]*6

shapeList = []
playerTurtles = []

swidth, sheight = 500, 500

if  __name__  ==  "__main__":
    turtle.title('거북 리스트 활용')
    turtle.setup(width = swidth+50, height = sheight+50)
    turtle.screensize(swidth, sheight)

    shapeList = turtle.getshapes()
    for i in range(0,100):
        c = random.choice(shapeList)
        myTurtle = turtle.Turtle(c)
        tX = random.randrange(-swidth // 2, swidth // 2)
        tY = random.randrange(-sheight // 2, sheight // 2)
        r = random.random(); g = random.random(); b = random.random()
        tSize = random.randrange(1,3)
        playerTurtles.append([myTurtle, tX, tY, tSize, r, g, b])

    for tList in playerTurtles:
        myTurtle = tList[0]
        myTurtle.color(tList[4], tList[5], tList[6])
        myTurtle.pencolor('red')
        myTurtle.turtlesize(tList[3])
        myTurtle.goto(tList[1], tList[2])

    turtle.done()
 

foods = {"떡볶이":"오뎅",
             "짜장면":"단무지",
             "라면":"김치",
             "피자":"피클",
             "맥주":"땅콩",
             "치킨":"치킨무",
             "삼겹살":"상추"
         }
while True:
    myfood = input(str(list(foods.keys())) + " 중 좋아하는 음식은?")
    if myfood in foods:
        print("<%s>의 궁합음식은 <%s>입니다." % (myfood, foods.get(myfood)))
    elif myfood  == "끝":
        break
    else :
        print("그런 음식 없어요")

import sys

option = sys.argv[1]

if option == '-a':
    memo = sys.argv[2]
    f = open('memo.txt', 'a')
    f.write(memo)
    f.write('\n')
    f.close()

elif option == '-v':
    f = open('memo.txt', 'r')
    memo = f.read()
    f.close()
    print(memo)

import sys

src = sys.argv[1]
dst = sys.argv[2]

f = open(src)
tab_content = f.read()
f.close()

space_content = tab_content.replace("\t", " "*4)

f = open(dst, 'w')
f.write(space_content)
f.close()





import os

def search(dirname):
    try:
        filenames = os.listdir(dirname)
        for i in filenames:
            full_filename = os.path.join(dirname, i)
            if os.path.isdir(full_filename):
                search(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]
                if ext == '.py':
                    print(full_filename)
                    
    except PermissionError:
        pass

search('C:/Users/ds/Desktop/파이썬/예제')


"""

        


