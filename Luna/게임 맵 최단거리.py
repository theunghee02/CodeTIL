# from collections import deque
# ## 노드를 방문 여부를 기록하는 배열
# visited = [False] * 6
# def bfs(maps, start, target):
#     n, m = len(maps), len(maps[0])

#     queue = deque()
#     queue.append(start)

#     while len(queue) !=0:
#         now = queue.popleft()
#         if visited[now] == 0:
#             visited[now] = 1
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

num_rows = grid       # Returns 3, as there are 3 rows in the grid.
num_columns = grid[0]
print(num_rows)
print(num_columns)