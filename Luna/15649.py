from itertools import permutations
n, m = map(int, input().split())
numbers = [i for i in range(1, n+1)]
perm = list(permutations(numbers, m))
# print(perm)
for i in perm:
    for j in i:
        print(j, end = ' ')
    print()