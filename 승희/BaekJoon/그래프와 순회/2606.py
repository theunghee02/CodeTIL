def bfs(v) :
    global cnt

    q = deque([v])
    visited[v] = 1
    while q :
        v = q.popleft()
        for i in graph[v] :
             if visited[i] == 0 :
                q.append(i)
                cnt += 1
                visited[i] = 1

import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

m = int(sys.stdin.readline().rstrip())
for i in range(m) :
    u,v = map(int, sys.stdin.readline().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 0
bfs(1)

print(cnt)