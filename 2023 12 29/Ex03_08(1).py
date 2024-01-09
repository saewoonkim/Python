Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import datetime
day1 = datetime.date(2024,1,9))
SyntaxError: unmatched ')'
day1 = datetime.date(2024,1,9)
day1
datetime.date(2024, 1, 9)
day2 = datetime(2023,4,5)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    day2 = datetime(2023,4,5)
TypeError: 'module' object is not callable. Did you mean: 'datetime.datetime(...)'?
day2 = datetime.date(2023,4,5)
diff = day1 - day2
diff
datetime.timedelta(days=279)
diff.days
279
day = datetime.date(2024.1.9)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
day = datetime.date(2024,1,9)
day.weekday()
1
day = datetime.date(2023,10,3)
day.weekday()
1
import time
time.time()
1704777429.4518151
time.localtime(time.time())
time.struct_time(tm_year=2024, tm_mon=1, tm_mday=9, tm_hour=14, tm_min=18, tm_sec=4, tm_wday=1, tm_yday=9, tm_isdst=0)
time.acstime(time.localtime(time.time()))
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    time.acstime(time.localtime(time.time()))
AttributeError: module 'time' has no attribute 'acstime'. Did you mean: 'asctime'?
time.asctime(time.localtime(time.time()))
'Tue Jan  9 14:19:19 2024'
time.strftime('%x', time.localtime(time.time()))
'01/09/24'
time.strftime('%Y', time.localtime(time.time()))
'2024'
for i in range(10):
    print(i)
    time.sleep(1)

    
0
1
2
3
4
5
6
7
8
9
import math
math.gcd(60, 100, 80)
20
math.lcm(15,30)
30
math.lcm(15,25)
75
import random
random.random()
0.3654546941226149
random.randint(1,55)
52
def random_pop(data):
    number = random.randint(0, len(data) -1)
    return data.pop(number)

data = [1,2,3,4,5]
while data:
    print(random_pop(data))

    
1
3
2
4
5
data
[]
def random_pop(data):
    number = random.choice(data)
    data.remove(number)
    return number

data = [3,5,9,2,8]
while data:
    print(random_pop(data))

    
5
2
9
8
3
>>> data
[]
>>> student = ['강호동', '유재석', '신동엽']
>>> snack = ['사탕','초코렛']
>>> result = zip(student, snack)
>>> result
<zip object at 0x000001FFE24CB140>
>>> print(result)
<zip object at 0x000001FFE24CB140>
>>> print(list(result))
[('강호동', '사탕'), ('유재석', '초코렛')]
>>> import itertools
>>> student = ['강호동', '유재석', '신동엽']
>>> snack = ['사탕','초코렛']
result = itertools.zip_longest(student, snack, fillvalue = '새우깡')
print(list(result))
[('강호동', '사탕'), ('유재석', '초코렛'), ('신동엽', '새우깡')]
import itertools
list(itertools.permutations(['1','2','3'], 2))
[('1', '2'), ('1', '3'), ('2', '1'), ('2', '3'), ('3', '1'), ('3', '2')]
import shutil
shutil.copy('c:/my/a.txt', 'c:/test/a.txt.bak')
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    shutil.copy('c:/my/a.txt', 'c:/test/a.txt.bak')
  File "C:\Users\ds\AppData\Local\Programs\Python\Python312\Lib\shutil.py", line 423, in copy
    copyfile(src, dst, follow_symlinks=follow_symlinks)
  File "C:\Users\ds\AppData\Local\Programs\Python\Python312\Lib\shutil.py", line 260, in copyfile
    with open(src, 'rb') as fsrc:
FileNotFoundError: [Errno 2] No such file or directory: 'c:/my/a.txt'
import os

print(os.getcwd())
SyntaxError: multiple statements found while compiling a single statement
import os
print(os.getcwd())
C:\Users\ds\AppData\Local\Programs\Python\Python312
os.chdir('c:/')
print(os.getcwd())
c:\
shutil.copy('c:/my/a.txt', 'c:/test/a.txt.bak')
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    shutil.copy('c:/my/a.txt', 'c:/test/a.txt.bak')
  File "C:\Users\ds\AppData\Local\Programs\Python\Python312\Lib\shutil.py", line 423, in copy
    copyfile(src, dst, follow_symlinks=follow_symlinks)
  File "C:\Users\ds\AppData\Local\Programs\Python\Python312\Lib\shutil.py", line 260, in copyfile
    with open(src, 'rb') as fsrc:
FileNotFoundError: [Errno 2] No such file or directory: 'c:/my/a.txt'
shutil.copy('c:\my\a.txt', 'c:\test\a.txt.bak')
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    shutil.copy('c:\my\a.txt', 'c:\test\a.txt.bak')
  File "C:\Users\ds\AppData\Local\Programs\Python\Python312\Lib\shutil.py", line 423, in copy
    copyfile(src, dst, follow_symlinks=follow_symlinks)
  File "C:\Users\ds\AppData\Local\Programs\Python\Python312\Lib\shutil.py", line 260, in copyfile
    with open(src, 'rb') as fsrc:
OSError: [Errno 22] Invalid argument: 'c:\\my\x07.txt'
