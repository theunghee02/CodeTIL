from collections import deque
def bfs(start, target):
    MAX = 100001
    visited = [False] * MAX
    queue = deque()
    queue.append([start, 0])

    while len(queue) != 0:
        now, time = queue.popleft()
        if now == target: return time
        next_position = [now -1, now + 1, now *2]

        for i in next_position:
            if 0<=i <MAX and visited[i] == False:
                visited[i] = True
                queue.append([i, time + 1])

start, target = map(int, input().split())
result = bfs(start, target)
print(result)