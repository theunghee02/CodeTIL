list = [[0 for _ in range(9)] for _ in range(9)]
## 입력시킴
for i in range(9):
    line = input().split(" ")
    for j in range(9):
        list[i][j] = int(line[j])

max = list[0][0]
## 최댓값
for i in range(9):
    for j in range(9):
        if(max <= list[i][j]):
            max = list[i][j]
            x,y = i, j
print(max)
print(x + 1, y + 1, end=" ")