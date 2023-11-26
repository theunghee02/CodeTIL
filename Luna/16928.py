from collections import deque

def bfs(start, target):
    queue = deque()
    queue.append([start, 0])  # 1번칸부터 시작
    
    while len(queue) != 0:
        now, cnt = queue.popleft()
        if now == target:
            return cnt
        if visited[now] == 0:
            visited[now] = 1
            for i in range(1, 7):
                # 현재 위치에서 주사위의 값 더함
                check = i + now
                if check in ladder.keys():
                    check = ladder[check]
                if check in snake.keys():
                    check = snake[check]
                if check <= 100 and visited[check] == 0:
                    queue.append([check, cnt + 1])

ladder_num, snake_num = map(int, input().split())
visited = [0] * 101  # 입력으로 받는 숫자 중 가장 큰 값에 따라 크기 동적으로 조정
ladder = dict()
snake = dict()
cnt = 0

for _ in range(ladder_num):
    x, y = map(int, input().split())
    ladder[x] = y

for _ in range(snake_num):
    u, v = map(int, input().split())
    snake[u] = v

print(bfs(1, 100))
