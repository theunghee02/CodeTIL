
N, M = map(int, input().split())
list = [[0 for _ in range(N)] for _ in range(M)]
for i in range(N):
    line = input()
    for j in range(M):
        list[i][j] = line[j]

answer1 = ["BWBWBWBW", "WBWBWBWB","BWBWBWBW", "WBWBWBWB","BWBWBWBW", "WBWBWBWB","BWBWBWBW", "WBWBWBWB"]
answer2 = ["WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW","WBWBWBWB", "BWBWBWBW","WBWBWBWB", "BWBWBWBW"]
## 8 * 8로 자르기 위해
for row in range(N-7):
    for col in range(M-7):
        white_idx = 0
        black_idx = 0
        # 흰, 검 체크
        for a in range(8):
            for b in range(8):
                if list[row + a][col + b] != answer1[a][b]: 
                    white_idx += 1

        for a in range(8):
            for b in range(8):
                if list[row + a][col + b] != answer2[a][b]: 
                    black_idx += 1
        # 최소값 저장해두기
        min_idx = min(white_idx, black_idx)
# 최소값 중 최소값 출력                        
print(min_idx)












