n = 9
wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
## 인접 행렬 만들기
list = [[0 for _ in range(n+1)] for _ in range(n+1)]

# 그래프 생성
for v1, v2 in wires:
    list[v1][v2] = 1
    list[v2][v1] = 1

## 방문 여부 체크
visited = [False] * (n+1)
def dfs(start):
    visited[start] = True
    count = 1
    for i in range(len(list[start])):
        if list[start][i] == 1 and not visited[i]:
            count += dfs(i)
    return count

#송전탑의 개수차를 구하는 변수
answer = 999

## edge를 끊고 -> dfs 돌리기
for v1,v2 in wires:
    # 엣지 자르기
    list[v1][v2] = 0
    list[v2][v1] = 0
    count1 = dfs(v1)
    count2 = dfs(v2)
    diff = abs(count1 - count2)
    answer = min(answer, diff)
print(answer)
    # count1 = dfs(v1)
    # count2 = n - count1
    # diff = abs(count1 - count2)
    # answer = min(answer, diff)
    # 엣지를 하나 자르면 두개의 전력망이 나오는데,
    # 자른 엣지를 구성하는 두개의 노드에 대해 DFS를 돌린다
    # 두개의 전력망 속 송전탑의 개수를 센다.
    # 두개의 절댓값 차이를 계산한다.
    # answer = min(answer, diff)
