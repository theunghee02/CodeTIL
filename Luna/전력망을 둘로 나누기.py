n = int(input())
## 인접 행렬 만들기
list = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(n-1):
    v1, v2 = int(input().split())
    list[v1][v2] = 1
    list[v2][v1] = 1

## 방문 여부 체크
visited = [False] * (n+1)
def dfs(start):


##끊고 -> dfs 돌리기
