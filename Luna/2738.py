row, col = map(int, input().split())

list = [[ 0 for _ in range(col)] for _ in range(row)]
for i in range(row):
    line = input().split(" ")
    for j in range(col):
        list[i][j] = int(line[j])

list2 = [[0 for _ in range(col)] for _ in range(row)]
for i in range(row):
    line = input().split(" ")
    for j in range(col):
        list2[i][j] = int(line[j])

for i in range(row):
    for j in range(col):
        print(list[i][j] + list2[i][j], end=" ")
    print()