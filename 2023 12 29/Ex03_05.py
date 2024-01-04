"""
f = open("new.txt", 'w')
f.close()


f = open("new.txt", 'w')
for i in range(1,11):
    data = "%d번째 입니다 \n" % i
    f.write(data)
f.close()

f = open("new.txt", 'r')
line = f.readline()
print(line)
f.close()



f = open("new.txt", 'r')
while True:
    line = f.readline()
    if not line :
        break
    print(line)
f.close()



f = open("new.txt", 'r')
lines = f.readlines()
lines1 = []
for i in lines:
    lines1.append(i.strip())
    print(i)
f.close()

print(lines1)
f = open('new.txt', 'r')
data = f.read()
print(data)
f.close()



f = open('new.txt', 'r')
for i in f:
    print(i)
f.close()

f = open('new.txt', 'a')
f.write("마지막 줄 추가")
f.close()

with open('new.txt', 'w') as f:
    f.write("Life is too short")


import sys

args = sys.argv[1:]
for i in args:
    print(i)



//파일 지우는법 
import os
os.remove("new.txt")


//되새김 문제 185

def is_odd(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(is_odd(4))




def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result / len(args)

print(avg_numbers(1,2,3,4,))





input1 = int(input("숫자입력 : "))
input2 = int(input("숫자입력 : "))

total = input1 + input2
print("두 수의 합은 %d 입니다" % total)








f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close()

f2 = open("test.txt", 'r')
print(f2.read())
f2.close()





user_input = input("input : ")
f = open('test.txt', 'a')
f.write(user_input)
f.write('\n')
f.close()





f = open('test.txt', 'r')
body = f.read()
f.close()

body = body.replace('java', 'python')

f = open('test.txt', 'w')
f.write(body)
f.close


import sys
args = sys.argv[1:]
sum = 0
for i in args:
    sum += int(i)
print(sum)







//TTT ANSER





def is_odd(number):
    if number % 2 == 0:
        return False
    else :
        return True

is_odd(5)



def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result / len(args)

print(avg_numbers(1,2,3,4,5))

input1 = input("첫 수:")
input2 = input("둘 수:")

total = int(input1) + int(input2)
print("합 : %d" % total)


f1 = open("test_1.txt", 'w')
f1.write("Life")
f1.close()

f2 = open("test_1.txt", 'r')
print(f2.read())
f2.close()



user_input = input("내용 :")
f4 = open('test_1.txt', 'a')
f4.write(user_input)
f4.write('\n')
f4.close()

f5 = open('test_1.txt', 'r')
body = f5.read()
f5.close()

body = body.replace('good', 'so so good')

f6 = open('test_1.txt', 'w')
f6.write(body)
f6.close()


import sys
args = sys.argv[1:]
i = 0
for i in args:
    i += i
print(i)


import sys
args = sys.argv[1:]
sum = 0
for i in args:
    sum += int(i)
print(sum)

"""
