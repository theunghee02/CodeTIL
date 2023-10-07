
N = int(input())
grid = [[0 for _ in range(N)] for _ in range(N)]

## 2차원 배열 입력 받기
for i in range(N):
    line = input()
    for j in range(N):
        grid[i][j] = line[j]

def check(x, y, n):
    now = grid[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if grid[i][j] != now:
                return False
    return True

def divide(x, y, n):
    ## 모든 요소가 모두 동일할때
    if check(x, y, n):
        return grid[x][y]
    
    ## 모든 요소가 동일하지 않을때
    else:
        new_size = n // 2
        result = "("
        result += divide(x, y, new_size) # 1사분면
        result += divide(x, y + new_size, new_size) # 2사분면
        result += divide(x + new_size, y, new_size) # 3사분면
        result += divide(x + new_size, y + new_size, new_size) # 4사분면
        result += ")"
        return result

result = divide(0, 0, N)
print(result)
