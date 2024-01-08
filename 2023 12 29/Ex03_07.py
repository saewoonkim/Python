"""
a = int(input("숫자입력 : "))
if a < 0:
    print(a * (-1))
else :
    print(a)

a = int(input("숫자입력 : "))
print(abs(a))


n = int(input("리스트 길이 입력 : "))
arr = []
arr = input("숫자 입력 : ").split()

for i in range(n):
    arr[i] = int(arr[i])
    
print(max(arr)- min(arr))

n = list(map(int, input("숫자 입력 : ").split()))
print(max(n) - min(n))


n = int(input("리스트 길이 입력 : "))
arr = []
arr = input().split()

for i in range(n):
    arr[i] = int(arr[i])

print(max(arr) - min(arr))


n = int(input("리스트 길이 입력"))
arr = []
arr = input().split()

for i in range(n):
    arr[i] = int(arr[i])

for i in range(0, n, 2):
    print(arr[i], end=" ") 
// 0 에서 2 까지 2씩 상승 범위를 만들수 있음

print()

for i in range(1, n, 2):
    print(arr[i], end=" ")
//1에서 2 까지 범위



n = int(input("리스트 길이 입력 : "))
arr = []
arr = input("숫자들 입력 : ").split()
num5 = []
for i in range(n):
    arr[i] = int(arr[i])
 
for i in range(n):
    if arr[i] % 2 == 0 and arr[i] % 5 == 0:
        print(arr[i], end=" ")


//짝수이면서 5의배수인수

print("")


for i in range(n):
    if arr[i] % 5 == 0:
        num5.append(arr[i])
        
print(max(num5), min(num5))


//짝수이면서 5의배수이고
//최대값과 최소값

"""























