N = int(input())
numbers = []
for i in range(N):
    x, y = map(int, input().split())
    numbers.append((x,y))

for i in numbers:
    rank = 1
    for j in numbers:
        if (i[0] < j[0] and i[1] < j[1]):
            rank +=1
    print(rank, end = " ")