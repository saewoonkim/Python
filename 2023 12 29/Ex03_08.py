"""

import time

def long_task():
    for i in range(5):
        time.sleep(1)
        print("working : %s" % i)
        
print("Start")

for i in range(5):
    long_task()

print("End")


import time
import threading

def long_task():
    for i in range(5):
        time.sleep(1)
        print("working : %s" % i)
        
print("Start")

threads = []

for i in range(5):
    t = threading.Thread(target=long_task)
    threads.append(t)

for t in threads:
    t.start()

print("End")
//지 마음대로 배열 순서 다틀리게 나옴
처음에 스타트 엔드 나오고 배열틀리게나옴





import time
import threading

def long_task():
    for i in range(5):
        time.sleep(1)
        print("working : %s" % i)
        
print("Start")

threads = []

for i in range(5):
    t = threading.Thread(target=long_task)
    threads.append(t)

for t in threads:
    t.start()
    
for t in threads:
    t.join()

print("End")

//조인이 들어가면서 스타트 하고 일처리하고 엔드가 나오지만
일처리 부분이 엉망임 병행 수행 스레드



def a():
    return 1 / 0
def b():
    a()

def main():
    try:
        b()
    except:
        print("오류 발생")

import traceback

def a():
    return 1 / 0
def b():
    a()

def main():
    try:
        b()
    except:
        print("오류 발생")
        print(traceback.format_exc())



import json
with open('myinfo.json') as f :
    data = json.load(f)

type(data)
data

import json
data = {'name' : '홍길동', 'birth' : '0528', 'age' : 30}
with open('myinfo1.json', 'w') as f:
    json.dump(data, f)

import json
data = {'name' : '홍길동', 'birth' : '0528', 'age' : 30}
with open('myinfo2.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False)


"""


