from collections import deque

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

virus = []
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 2:
            virus.append((i, j))

def bfs(virus):
    visited = [[False for _ in range(M)] for _ in range(N)]
    queue = deque(virus)  # Start BFS from all virus cells

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if matrix[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

    bfs_cnt = sum(1 for i in range(N) for j in range(M) if matrix[i][j] == 0 and not visited[i][j])
    return bfs_cnt

def makeWall(cnt=0):
    global max_safe_area
    if cnt == 3:
        max_safe_area = max(max_safe_area, bfs(virus))
        return

    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 0:
                matrix[i][j] = 1
                makeWall(cnt + 1)
                matrix[i][j] = 0

max_safe_area = 0
makeWall()
print(max_safe_area)
