def func(matrix, row, col, cache):
    if row == len(matrix) -1 and col == len(matrix) -1:
        return 1
    if row >= len(matrix) or row < 0 or col >= len(matrix) or col <0:
        return 0

    jump = matrix[row][col]
    if jump == 0:
        return 0
    total_paths = 0
    ## DP는 key 값에 따라 달라진다 -> row, col 의 2차원 배열로 구성
    # 이미 계산된 적이 있다면
    if cache[row][col] != -1:
        return cache[row][col]
    
    # 아래로 이동
    if row + jump < N:
        total_paths += func(matrix, row + jump, col, cache)

    # 오른쪽으로 이동
    if col + jump < N:
        total_paths += func(matrix, row, col + jump, cache)

    cache[row][col] = total_paths
    return total_paths

import sys
N = int(input())
read = sys.stdin.readline
matrix = [list(map(int, read().split())) for _ in range(N)]
cache = [[-1] * N for _ in range(N)]

print(func(matrix, 0,0, cache))
