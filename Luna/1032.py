N = int(input())
## 2차원 배열 생성
files = [[0 for _ in range(1)] for _ in range(N)]

for i in range(N):
    file = input()
    files[i][0] = file

for i in files:
    print([i][0])