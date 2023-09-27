def bfs(r) :
  global cnt

  q = deque([r])
  visited[r] = 1
  while q :
    r = q.popleft()
    graph[r].sort(reverse=True)
    for i in graph[r] :
      if visited[i] == 0 :
        cnt += 1
        visited[i] = cnt
        q.append(i)

import sys
from collections import deque
N, M, R = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
cnt = 1

for _ in range(M) :
  u, v = map(int, sys.stdin.readline().rstrip().split())
  graph[u].append(v)
  graph[v].append(u)

bfs(R)

for j in visited[1:] :
  print(j)