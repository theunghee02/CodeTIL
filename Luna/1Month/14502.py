#  0은 빈 칸, 1은 벽, 2는 바이러스
# 새로 세울 수 있는 벽의 개수는 3개
# 안정 영역의 최대값
N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]
from collections import deque
def bfs():
    queue = deque()
    bfs_cnt = 0
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 2:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0<=ny<M:
                if matrix[nx][ny] == 0: # 빈칸이라면
                    matrix[ny][nx] = 2 # 감염
                    bfs_cnt +=1
                    queue.append((nx, ny))
def makeWall(cnt):
    if cnt == 3:
        bfs()
        return

    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 0:
                matrix[i][j] = 1 # 빈공간이라면 벽을 세우기
                makeWall(cnt+1) # 다시 벽 만들러가

  makeWall(1)