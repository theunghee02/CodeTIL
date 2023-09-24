n = int(input())
list = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    line = input()
    for j in range(n):
        list[i][j] = int(line[j])

# global cnt # 집의 개수
dx = [-1,1,0,0]
dy = [0,0,-1,1]
cnt = 0
def dfs(x,y):
    if x <0 or y<0 or x>=n or y>=n:
        return False
    if list[x][y] == 1:
        global cnt
        cnt +=1
        list[x][y] = 0
        ## 상하좌우 재귀
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True # 집이 있을 경우 True
    return False # 없을 경우 False

home_cnt = []
for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            home_cnt.append(cnt)
            cnt = 0 # 한 단지내 집의 수를 초기화
home_cnt.sort()
print(len(home_cnt))
for i in home_cnt:
    print (i)
