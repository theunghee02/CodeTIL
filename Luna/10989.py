import sys
N = int(sys.stdin.readline())
arr = [0] * 10001
for _ in range(N):
    inputs = int(sys.stdin.readline())
    arr[inputs] +=1

## 인덱스 i가 arr[i]번 만큼 출력   
for i in range(10001):
    if(arr[i]!=0):
        for j in range(arr[i]):
            print(i)
