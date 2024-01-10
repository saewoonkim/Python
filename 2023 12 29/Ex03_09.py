"""
import urllib.request
def get_wikidocs(page):
    resource = "https://wikidocs.net/{}".format(page)
    with urllib.request.urlopen(resource) as s:
        with open('wiki_%s.html' % page, 'wb') as f:
            f.write(s.read())

get_wikidocs(1)

import urllib.request
def get_wikidocs(page):
    resource = "https://wikidocs.net/{}".format(page)
    with urllib.request.urlopen(resource) as s:
        with open('wiki_%s.html' % page, 'wb') as f:
            f.write(s.read())

get_wikidocs(2)


from faker import Faker
fake = Faker('ko-KR')
#print(fake.name())
#print(fake.address())

test_data = [(fake.name(), fake.address(), fake.phone_number()) for i in range(5)]
print(test_data)


from fractions import Fraction
import sympy

x = sympy.symbols("x")
f = sympy.Eq(x*Fraction('2/5'), 1760)

result = sympy.solve(f)

remains = result[0] - 1760

print("남은 돈 {}".format(remains))




            
/////////되새김문제

//1
class Calculator:
    def __init__(self):
        self.value = 0
    def add(self, val):
        self.value += val

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)
print(cal.value)




//2
class Calculator:
    def __init__(self):
        self.value = 0
    def add(self, val):
        self.value += val
        
class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100
            
cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)
print(cal.value)


//3

print(all([1,2,abs(-3)-3]))

print(chr(ord('a')) == 'a')


//4
print(list(filter(lambda x: x>0, [1,-2,3,-5,8,-3])))

//5

print(int(0xea))

//6

print(list(map(lambda x:x*3, [1,2,3,4])))

//7

a = [-8, 2, 7, 5, -3, 5, 0, 1]
print(max(a)+min(a))

//8

print(round(17/3, 4))

//9

import os
os.chdir("C:/Users/ds/Desktop/파이썬/예제") // 디렉토리 이동
result = os.popen("dir") // dir 디렉토리 (이명령어로 출력하겠다)
print(result.read())

//9

import os

os.chdir('C:/Users/ds/Desktop/파이썬/예제')
result = os.popen("dir")
dirStr = list(result)

//10
import glob
print(glob.glob("C:/Users/ds/Desktop/파이썬/예제/*.py"))//디렉토리 설정해주고
                                                      //"k"넣으면 찾을수있음
result1 = glob.glob('C:/Users/ds/Desktop/파이썬/예제/*k*')
print(result1)

result2 = glob.glob('C:/Users/ds/Desktop/파이썬/예제/*k*')
print(result2)

//11
import time
print(time.strftime("%Y/%m/%d %H:%M:%S"))

//12
import random
lotto = []
for i in range(6):
    num = random.randint(1,45)
    if num in lotto:
        continue //수행하지 말고 계속 지나가라는 용어
    lotto.append(num)        
print(lotto)
    
//13
import datetime
sister = datetime.date(1995,11,20)
youngchul = datetime.date(1998,10,6)
diff = youngchul - sister
print(diff.days)
   
//14
import operator
from faker import Faker
fake = Faker('ko-KR')
data = [(fake.name(), fake.pyint(min_value=0, max_value=100)) for i in range(20)]
data = sorted(data, key=operator.itemgetter(1))
for i in data:
    print(i, end=" ")

//15
import itertools //이터레이터 툴 (반복되는 )이터 툴스 
from faker import Faker
fake = Faker('ko-KR')
student = list(fake.name() for i in range(4))
result = itertools.combinations(student, 2)
print(list(result))


//16
import itertools // 모든 경우의 수

a = "abcd"
result = itertools.permutations(a,4)
print(list(result))


"""

