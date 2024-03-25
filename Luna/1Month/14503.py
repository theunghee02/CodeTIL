N, M = map(int,input().split())
# 로봇 청소기의 위치, 바라보는 방향
r, c, d = map(int, input().split())
matrix = [list(map(int, input().split())) for i in range(N)]
# 북 동 남 서
dr = [-1,0,1,0]
dc = [0,1,0,-1]
visited = [[0]*M for _ in range(N)]
visited[r][c] = 1
cnt = 1 # 청소 횟수

while True:
    flag = False # 청소하지 않음
    ##  청소기가 바라보는 방향 - 왼쪽으로
    for i in range(4):
        d = (d+3)%4 # 반시계 방향으로 회전
        nr = r + dr[d]
        nc = c + dc[d]
        # 청소하지 않은 곳
        if 0<=nr<N and 0<=nc <M and matrix[nr][nc] == 0:
            if visited[nr][nc] == 0:
                visited[nr][nc] = 1
                r = nr
                c = nc
                cnt+=1
                flag = True # 청소 했음
                break

    ## 4방향 모두 청소가 되어있다면
    if flag == False:
        # 후진 가능한지 확인
        if matrix[r-dr[d]][c-dc[d]] == 0: # 후진할 수 있다면
            r, c = r-dr[d], c-dc[d]
        else: # 후진 할 수 없다면
            break
print(cnt)