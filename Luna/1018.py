
N, M = map(int, input().split())
list = [[0 for _ in range(N)] for _ in range(M)]
for i in range(N):
    line = input()
    for j in range(M):
        list[i][j] = line[j]
print(list)
## 8 * 8로 자르기 위해
for row in range(N-7):
    for col in range(M-7):
        white_idx = 0
        black_idx = 0
        # 흰, 검 체크
        for i in range(row, row+8):
            for j in range(col, col+8):
                
                        