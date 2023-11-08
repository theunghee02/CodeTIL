def func(matrix, row, col):
    if row == len(matrix) -1 and col == len(matrix) -1:
        return 1
    if row >= len(matrix) or row < 0 or col >= len(matrix):
        return 0
    jump = matrix[row][col]
    total_paths = 0

    # 아래로 이동
    if row + jump < N:
        total_paths += func(matrix, row + jump, col)

    # 오른쪽으로 이동
    if col + jump < N:
        total_paths += func(matrix, row, col + jump)

    return total_paths


N = int(input())
matrix = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    line = input().split(" ")
    for j in range(N):
        matrix[i][j] = int(line[j])

print(func(matrix, 0,0))