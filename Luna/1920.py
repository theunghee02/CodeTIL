N = int(input())
num1 = set(map(int, input().split()))
M = int(input())
num2 = list(map(int, input().split()))

for j in range(M):
    isExist = 0
    if num2[j] in num1:
        isExist = 1
        print(isExist)
    else : print(isExist)