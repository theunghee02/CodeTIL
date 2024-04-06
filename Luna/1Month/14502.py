#  0은 빈 칸, 1은 벽, 2는 바이러스
# 새로 세울 수 있는 벽의 개수는 3개
# 안정 영역의 최대값
N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]
from collections import deque
# for 문 반복을 줄이기 위해 바이러스 위치는 밖에서 구하기
virus = []
emptyCell = 0
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 2:
            virus.append((i, j))
        elif matrix[i][j] == 0:
            emptyCell +=1
def bfs(virus, emptyCell):
    visited = [[False for _ in range(M)]for _ in range(N)]
    queue = deque()
    for v in virus: # 출발점 넣기
        queue.append(v)
    bfs_cnt = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0<=ny<M:
                if matrix[nx][ny] == 0 and visited[nx][ny] == False: # 빈칸이라면
                    visited[nx][ny] = True # 감염
                    bfs_cnt +=1 # 감염된 수
                    queue.append((nx, ny))
    return emptyCell - bfs_cnt -3

max_safe_area = 0

for i in range(N):
    for j in range(M):
        if matrix[i][j] == 0:
            matrix[i][j] = 1 # 빈공간이라면 벽을 세우기
            for k in range(i, N):
                for l in range(M):
                    if matrix[k][l] == 0:
                        matrix[k][l] = 1  # 빈공간이라면 벽을 세우기
                        for m in range(k,N):
                            for n in range(M):
                                if matrix[m][n] == 0:
                                    matrix[m][n] = 1  # 빈공간이라면 벽을 세우기
                                    max_safe_area = max(max_safe_area, bfs(virus, emptyCell))
                                    matrix[m][n] = 0
                        matrix[k][l] = 0
            matrix[i][j] = 0
print(max_safe_area)