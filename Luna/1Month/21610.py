from collections import deque
n, m = map(int, input().split()) # 배열의 갯수 N, 명령어 갯수 M
data = [list(map(int, input().split())) for _ in range(n)]
direction = [list(map(int, input().split())) for _ in range(m)]
cloud = [(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)]
cloud = deque(cloud)
# 순서대로 1,2,3,4,5,6,7,8
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
def move_rain(dir, distance):
    for _ in range(len(cloud)):
        x, y = cloud.popleft()
        nx = (x + dx[dir] * distance) % n
        ny = (y + dy[dir] * distance) % n
        if nx < 0 : nx += n
        if ny < 0 : ny += n
        cloud.append((nx, ny))
        visited[nx][ny] = True # 구름 사라짐
        data[nx][ny] +=1
# 물복사 버그 마법은 대각선 방향인 애들한테 물이있는 바구니의 수 만큼 (r,c)가 증가
def water_copy():
    while cloud:
        x, y = cloud.popleft()
        # 대각선 검사
        for i in range(1, 8, 2):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx < n and 0<=ny < n and data[nx][ny] >0:
                data[x][y] +=1

for dir, distance in direction:
    visited = [[False] * n for _ in range(n)]
    move_rain(dir-1, distance) # 비내리기
    water_copy() # 물복사 버그 마법
    #구름 생성
    for i in range(n):
        for j in range(n):
            if data[i][j] >=2 and not visited[i][j]:
                cloud.append((i, j))
                data[i][j] -=2
sum = 0
for i in range(n):
    for j in range(n):
        sum += data[i][j]

print(sum)