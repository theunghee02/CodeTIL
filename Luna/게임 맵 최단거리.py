from collections import deque
## 노드를 방문 여부를 기록하는 배열
def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    return bfs(maps, 0,0,visited)

def bfs(maps, row, col, visited):
    queue = deque()
    queue.append((row, col, 1))
    moves = [(1,0),(-1,0), (0,1), (0,-1)]

    while len(queue) !=0:
        row, col, dist = queue.popleft()
        ## 목적지에 도착했을때 거리 반환
        if row == len(maps) - 1 and col == len(maps[0]) - 1:
            return dist 
        
        if visited[row][col] == 0:
            visited[row][col] = 1
            for dx, dy in moves:
                new_x, new_y = row + dx, col + dy

                if 0<= new_x < len(maps) and 0<= new_y <len(maps[0]) and maps[new_x][new_y] == 1:
                    queue.append((new_x, new_y, dist + 1))
    # 길이 더이상 갈 곳이 없으면
    return -1
