# a층 b호 = (a-1)층 1호~b호
T = int(input())

for i in range(T):
    k = int(input()) #층
    n = int(input()) #호
    ##0층
    # 0층부터 14층까지의 각 호수에 대한 값을 미리 계산하여 저장
    apartment = [[0] * n for _ in range(k+1)]

    # 0층 초기화
    for i in range(n):
        apartment[0][i] = i + 1

    # 1층부터 k층까지 각 층의 호수를 계산
    for i in range(1, k+1):
        for j in range(n):
            for l in range(j+1):
                apartment[i][j] += apartment[i-1][l]

    # 결과 출력
    print(apartment[k][n-1])
    # floor = [i for i in range(1, n+1)]

# for x in range(k):
#     for y in range(1, n):
#         floor[y] += floor[y-1]
#     print(floor[-1])
# for x in range(14):
#     for y in range(14):
#         floor