"""
treeHit = 0
while treeHit < 10:
    treeHit += 1
    print("나무를 %d번 찍었다!!" % treeHit)
    if treeHit == 10:
        print("나무가 넘어갑니다.")
---------------------------------------------------------------
number = 0
while number != 4:
    prompt = input("명령어 입력 : ")
    print(prompt)
    number = int(input("숫자입력 : "))
-------------------------------------------------------------
coffee = 10
money = 300
while money:
    print("돈이 있군요. 커피 받아요")
    #coffee -= 1
    coffee = coffee - 1
    print("남은 커피는 %d잔 입니다. " % coffee)
    if coffee == 0:
        print("커피가 없습니다. ")
        break
----------------------------------------------------------------
coffee = 10
while True:
    money = int(input("돈을 넣으세요 : "))
    if money ==  300:
        coffee = coffee - 1
        print("커피 받아요 남은커피는 %d잔 입니다. " % coffee)
    elif money > 300:
        print("커피 받고 거스름돈 %d원 받으세요" % (money-300))
        coffee = coffee - 1
        print("남은커피는 %d잔 입니다. " % coffee)
    elif money < 300:
        print("돈이 부족합니다.")
    if coffee == 0:
        break
--------------------------------------------------------
i = 1
sum = 0
while  i <= 100:
    sum += i
    i += 1
print("1부터 100까지 합계는 %d " % sum)
-------------------------------------------------------------

num1 = int(input("시작 수 입력 : "))
num2 = int(input("끝 수 입력 : "))
sum = 0
print("%d부터 %d까지 합계는 " % (num1, num2), end="")엔터를 치지않겠다는 의미
while  num1 <= num2:
    sum += num1
    num1 += 1
print(" %d " % sum)





**끝내고 싶으면
num1 = int(input("시작 수 입력 : "))
num2 = int(input("끝 수 입력 : "))
if num1 == 0:
break
sum = 0
print("%d부터 %d까지 합계는 " % (num1, num2), end="")엔터를 치지않겠다는 의미
while  num1 <= num2:
    sum += num1
    num1 += 1
print(" %d " % sum)





a = 0
while a < 10:
    a = a+1
    if a % 2 == 0:
        continue // 는 이값이 맞으면 다시 처음으로 돌아간다
                        밑에잇는 프린트 작업을 하지않는다 
    print(a)
    

test_list = ['one', 'two', 'three']
// test_list.reverse() 거꾸로 출력 

for i in test_list:
    print(i)




test_list = ['one', 'two', 'three']
test_list.reverse()
for i in test_list.count('two'):
    print(i)
    


a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)



for i in range(0,10):
    print(i)    
marks = [90,25,67,45,80]
number = 0
for m in marks:
    number = number+1
    if m >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)

add = 0
for i in range(1,11,2):
    print("%d + " % add, end="")
    add += i
    print(" %d = %d" % (i, add))



marks = [90,25,67,45,80]
for i in range(len(marks)):
    if marks[i] < 60:
        continue
    print("%d번 학생 축하합니다. " % (i+1))



**역순으로 입력값 만큼 역재생 
n = input("숫자입력 : ")
for i in range(len(n)-1, -1, -1):
    print(n[i])





n = int(input())

for i in range(n+1):
    print("*" * i)




**역순으로 뽑아 내는 거 
n = int(input())

for i in range(n, 0, -1):
    print("*" * i)


"""







