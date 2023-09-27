from itertools import combinations
n, m = map(int, input().split())
numbers = [i for i in range(1, n+1)]
perm = list(combinations(numbers, m))
# print(perm)
for i in perm:
    for j in i:
        print(j, end = ' ')
    print()