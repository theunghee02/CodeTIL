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
    ##  청소기가 바라보는 방향 - 왼쪽으로
    for i in range(4):
        nd = (d+3)%4
        nr = r + dr[d]
        nc = c + dc[d]
        # 청소하지 않은 곳
        if 0<=nr<N and 0<=nc <M and matrix[nr][nc] == 0:
            if visited[nr][nc] == 0:
                visited[nr][nc] = 1
                r = nr
                c = nc
                cnt+=1
    ## 4방향 모두 청소가 되어있다면
        if 0 <= nr < N and 0 <= nc < M and matrix[nr][nc] == 1:
            # 후진 가능 - 후진 후 청소
            if matrix[r-dr[d]][c-dc[d]] == 0:
                r,c = r-dr[d], c-dc[d]
            # 후진 불가능 - stop
            if matrix[r-dr[d]][c-dc[d]] == 1:
                print(cnt)
                break