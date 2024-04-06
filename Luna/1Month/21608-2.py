N = int(input())
students = [list(map(int, input().split())) for _ in range(N*N)]

matrix = [[0] * N for _ in range(N)]
dx = [-1,1, 0, 0]
dy = [0, 0, 1, -1]
## 1. 좋아하는 학생이 가장 많이 인접한 곳으로
## 2. 여러개 라면, 인접한 칸 중 비어있는 칸이 가장 많은 자리
# 즉 좋아하는 학생의 수가 같다면 좋아하는 학생의 위치를 저장해서 인접한 곳의 수를 세어 빈칸이 몇개인지 확인
## 3. 비어있는 칸의 수가 같다면, 행의 번호 작은게 우선 > 열의 번호
for student in students:
    num = student[0] #현재 학생 번호
    #print(num)
    max_like, max_empty = -1,-1
    seat = []
    # 교실의 자리 탐색 - 한자리에 대한 좋아하는 친구, 빈자리 탐색
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 0: # 빈자리 일 경우
                like = 0
                empty = 0
                for k in range(4): # 상하좌우 탐색
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0<= nx<N and 0<=ny<N:
                        # 좋아하는 친구가 있다면
                        if matrix[nx][ny] in student[1:]:
                            like += 1
                        elif matrix[nx][ny] == 0:
                            empty +=1
                # maxPrefer 보다 큰 prefer 라면 seat를 초기화, 이 위치를 넣어라
                if like>max_like or (like == max_like and empty > max_empty):
                    max_like = like
                    max_empty = empty
                    seat = [(i,j)]
                # maxPrefer 가 여러개 일 경우, 해당하는 seat의 자리를 다 넣어라
                elif like == max_like and empty == max_empty:
                    seat.append((i,j))
    # 학생을 최적의 자리에 배치합니다.
    if seat:
        best_seat = min(seat)
        matrix[best_seat[0]][best_seat[1]] = num

students.sort()
happy = 0
for i in range(N):
    for j in range(N):
        like = 0
        now = matrix[i][j]
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if matrix[nx][ny] in students[now-1][1:]:
                    like += 1
        if like != 0:
            happy += 10 ** (like - 1)

print(happy)