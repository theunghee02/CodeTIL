# from itertools import permutations
# n, m = map(int, input().split())
# numbers = [i for i in range(1, n+1)]
# perm = list(permutations(numbers, m))
# # print(perm)
# for i in perm:
#     for j in i:
#         print(j, end = ' ')
#     print()
def func(numbers, visited, start):
    # Base Case : 모두가 선택된 상태
    if start == m:
        for i in numbers:
            if i!=0 : print(i, end=" ")
        print()
        return
    for i in range(len(numbers)):
        # 시도해보기
        if not visited[i]:
            visited[i] = True
            numbers[start] = i+1
            func(numbers, visited, start+1)
            # 백트래킹 (왔던길을 되돌아기도록, 원상복구)
            visited[i] = False

n, m = map(int, input().split())

numbers = [0] * n
visited = [False] * n
func(numbers, visited, 0)