N = int(input())
num1 = list(map(int, input().split()))
M = int(input())
num2 = list(map(int, input().split()))


for j in range(M):
    isExist = 0
    for i in range(N):
        if(num1[i] == num2[j]):
            isExist = 1
            break
    print(isExist)
