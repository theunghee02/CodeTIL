vertax_cnt = int(input())
edge_cnt = int(input())
## 인접 행렬 만들기
matrix = [[0 for _ in range(vertax_cnt+1)] for _ in range(vertax_cnt+1)]

for i in range(edge_cnt):
    v1, v2 = map(int, input().split())
    matrix[v1][v2] = 1
    matrix[v2][v1] = 1

# 방문 기록
visited = [False] * (vertax_cnt +1)
def dfs(start):
    visited[start] = True
    cnt = 1 #현재 노드를 감염된 것으로 카운트
    for i in range(len(matrix[start])):
        if matrix[start][i] == 1 and not visited[i]:
            cnt += dfs(i)
    return cnt

# 1번 컴퓨터에서 시작해서 바이러스 전파 확인
infected_count = dfs(1)

# 1번 컴퓨터는 이미 감염된 상태이므로 1을 빼고 출력
print(infected_count - 1)