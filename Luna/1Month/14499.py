## 주사위
dice = [0,0,0,0,0,0]
## 명령어
N, M, x, y, r = map(int, input().split())
## 지도
arr_map = [list(map(int, input().split()))for i in range(N)]
## 명령어배열
command = list(map(int, input().split()))
# 동 - 1, 서 - 2, 북 - 3, 남 -4
dx = [0,1, -1, 0, 0]
dy = [0, 0, 0, -1, 1]

for c in command: # 명령어에 따라 주사위 위치 변경
    nx = x + dx[c]
    ny = y + dy[c]
    if not 0 <= nx < N or not 0 <= ny < M:  ## 범위 밖에 있는 좌표면 continue
        continue ## 이게 가장 문제 일것 같은데 이해가 안됨
    # 명령어에 따라 주사위의 좌표를 업뎃해줘야 함
    up, back, right, left, front, down = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if c == 1: # 동
        # 방향은 위, 뒤, 오, 왼, 앞, 아래
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = left, back, up, down, front, right
    elif c == 2: #서
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = right, back, down, up, front, left
    elif c ==3: #북 #5, 1, 3, 4, 6, 2
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = front, up, right, left, down,back
    else: #남 #2, 6, 3, 4,1, 5
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = back, down, right, left, up, front

    if arr_map[nx][ny] == 0: # 지도에 숫자가 0일때
        arr_map[nx][ny] = dice[5]
    else : # 지도에 숫자가 0이 아닐때
        dice[5] = arr_map[nx][ny]
        arr_map[nx][ny] = 0
    x, y = nx, ny
    print(dice[0])