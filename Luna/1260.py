##DFS -> 스택
##BFS -> 큐
from collections import deque
## 리스트로 입력 받음
inputs = list(map(int, input().split()))

N = inputs[0] ## 정점의 갯수
M = inputs[1] ## 간선의 갯수
start = inputs[2]

## 인접 행렬 만들기
matrix = [[0 for _ in range(N+1)] for _ in range(N+1)]

## 서로 연결된 노드 1로 표시
for i in range(M):  
    v1, v2 = map(int, input().split())
    matrix[v1][v2] = 1
    matrix[v2][v1] = 1

## 방문기록
visited1 = [False] * (N+1) #dfs
visited2 = [False] * (N+1) #bfs

def dfs(start):
    print(start, end = " ")
    visited1[start] = True
    for i in range(len(matrix[start])):
        if matrix[start][i] == 1 and not visited1[i]:
            dfs(i)

def bfs(start):
    queue = deque()
    queue.append(start)

    while len(queue) != 0:
        now = queue.popleft()
        if visited2[now] == 0:
            visited2[now] = 1
        print(now, end=" ")

        ## now와 연결이 된 애들
        for i in range(len(matrix[start])):
            if matrix[now][i] == 1 and not visited2[i]:
                queue.append(i)
                visited2[i] = 1

dfs(start)
print()
bfs(start)