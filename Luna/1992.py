# N = int(input())
# list = [[0 for _ in range(N)]for _ in range(N)]
# for i in range(N):
#     line = input()
#     for j in range(N):
#         list[i][j] = line[j]
# ## 전체적으로 검사 -> 모두 같은 색이 아님 -> 4등분으로 쪼갬 -> 다시 검사
# print(list)
# def check(x,y,n):
#     #시작하는 인덱스를 now라고 정함
#     now = list[x][y]
#     for i in range(x, x+n):
#         for j in range(y+n):
#             # 첫번째 인덱스와 한번이라도 다르면 stop
#             if now != list[x][y]:
#                 break

N = int(input())
grid = [list(input()) for _ in range(N)]

def check(x, y, n):
    now = grid[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if grid[i][j] != now:
                return False
    return True

def divide(x, y, n):
    if check(x, y, n):
        return grid[x][y]
    else:
        new_size = n // 2
        result = "("
        result += divide(x, y, new_size)
        result += divide(x, y + new_size, new_size)
        result += divide(x + new_size, y, new_size)
        result += divide(x + new_size, y + new_size, new_size)
        result += ")"
        return result

result = divide(0, 0, N)
print(result)
