"""
result = 0
i = 1
while i <= 1000:
    if i % 3 == 0:
        result += i
    i += 1
print(result)





i = 0
while True:
    i += 1
    if i > 5:
        break
    print("*" * i)

for i in range(1,101):
    print(i)





A = [70,60,55,75,95,90,80,85,100]
total = 0
for score in A:
    total += score
average = total / 10 //total +=total/len(A)
print("총점: %d 평균: %1f %(total,average))






//레인지 활용
for i in range(0, len(A)):
    if A[i] % 2 == 0:
        print(A[i], end="")



//그냥 2배수 
for i in A:
    if i % 2 == 0:
    print(i)




for i in range(0, len(A),2)://2는 투칸씩 띄운다 2배씩 간다 
    print(A[i], end = "")
print()





def say():
    return 'Hello'




def add1(a, b):
    print(a+b)




def add(a, b):
    return a+b




def add_many(*args):
    result = ' '
    for i in args:
        result += i
    return result




def add_mul(choice, *params):
    if choice == 'add':
        result = 0
        for i in params:
            result += i

    elif choice == 'mul':
        result = 1
        for i in params:
            result *= i
    return result



    
def add_mul(a,b):
    return a+b, a*b



def say_nick(nick):
    if nick == '바보':
        return
    print("내 별명은 %s입니다" % nick)

def say_myself(name, age, man=True):
    print(name)
    print(age)
    if man:
        print("남")
    else:
        print("여")
        

def say_myself(name, age, man=True):
    print(name)
    print(age)
    if man:
        print("남")
    else:
        print("여")
        

a = 1
def vartest(a):
    a = a + 1
    return a

print(vartest(a))
print(a)




def vartest(a):
    a = a + 1
    return a

print(vartest(a))




a = 1
def vartest():
    global a
    a = a+1

vartest()
print(a)




a = input("아무 문자 입력 :")
print(a)

for i in range(1, 11):
    print(i, end=" ")





def my(first, last):
    for i in range(first, last+1):
        return print(i, end=" ")




///리스트형태의 데이터 출력  
def my(first, last):
    mylist = []
    for i in range(first, last+1):
        mylist.append(i)//리스트 만드는 추가 함수 
    return mylist   






//////////////////////////////////////
def my(first, last):
    mylist = []
    for i in range(first, last+1):
        mylist.append(i)
    return mylist

def my_list():
    num1 = int(input("리스트 시작 수 : "))
    num2 = int(input("리스트 끝 수 : "))
    result = my(num1, num2)
    return result
    //리스트값을 받아서 리스트화로 만들어서 나타냄 
/////////////////////////////////////////



f = open ("새파일.txt",'w')
f.close()


f = open("new.txt", 'w')
f.close()


f = open("c:/ptest/new.txt", 'w')
f.close()


f = open("new.txt", 'w')
for i in range(0, 10):
    f.write("%d : 안녕하시요 \n" % i)
f.close()

"""


















