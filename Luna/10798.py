my_list = []

for i in range(5):
    line = input()
    my_list.append(line)

## 가장 긴 행
max_row = max(my_list, key = len)

for j in range(len(max_row)):
    for i in range(5):
        if j < len(my_list[i]):
            print(my_list[i][j], end="")
        else: continue


