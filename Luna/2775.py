# 0층부터 14층까지의 아파트 만들기
apt = [[0] * 15 for _ in range(15)]

# 0 층 구하기
for i in range(15):
    apt[0][i] = i
for i in range(15):
    for j in range(15):
        for k in range(j+1):
            apt[i][j] += apt[i-1][k]

test_case = int(input())
for i in range(test_case):
    row = int(input()) ##층
    col = int(input()) ##호
    print(apt[row][col])