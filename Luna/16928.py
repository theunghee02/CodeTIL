from collections import deque
ladder_num, snake_num = map(int, input().split())
matrix = [0] * 101
visited = [False] * 101
ladder = dict()
snake = dict()

for _ in range(ladder_num):
    x, y = map(int, input().split())
    ladder[x] = y

for _ in range(snake_num):
    u,v = map(int, input().split())
    snake[u] = v

queue = deque()
queue.append(1) #1번칸부터 시작
while len(queue)!=0:
    queue.append()