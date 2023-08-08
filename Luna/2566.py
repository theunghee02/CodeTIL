array = 3 * [[0] * 3]
for i in range(len(array)):
    for j in range(len(array[0])):
        array.append(list(map(int, input().split())))
