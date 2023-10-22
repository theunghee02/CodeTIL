def solution(wires, n):
    ## 인접 행렬 만들기
    matrix = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    # 그래프 생성
    for v1, v2 in wires:
        matrix[v1][v2] = 1
        matrix[v2][v1] = 1

    def dfs(start,visited):
        ## 방문 여부 체크
        visited[start] = True
        count = 1
        for i in range(1, n+1):
            if matrix[start][i] == 1 and not visited[i]:
                count += dfs(i, visited)
        return count

    #송전탑의 개수차를 구하는 변수
    answer = 999

    ## edge를 끊고 -> dfs 돌리기
    for v1,v2 in wires:
        # 엣지 자르기
        matrix[v1][v2] = 0
        matrix[v2][v1] = 0
        visited = [False] * (n + 1)

        count1 = dfs(v1, visited)
        count2 = dfs(v2, visited)

        diff = abs(count1 - count2)
        answer = min(answer, diff)
        # 전력망 복구
        matrix[v1][v2] = 1
        matrix[v2][v1] = 1
    return answer

result = solution([[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]],9)
print(result)