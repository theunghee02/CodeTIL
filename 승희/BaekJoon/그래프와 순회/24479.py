def DFS(graph, v, visited) :
    global n
    visited[v] = n
    graph[v].sort()
    for i in graph[v] :
        if not visited[i] :
            n += 1
            DFS(graph, i, visited)

import sys
sys.setrecursionlimit(150000)
n = 1
N,M,R = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for i in range(M) :
    a,b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

DFS(graph, R, visited)
for i in range(1, N+1):
    print(visited[i])