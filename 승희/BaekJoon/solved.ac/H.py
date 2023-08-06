import sys
import numpy as np
N,M,Q = map(int, sys.stdin.readline().rstrip().split())
array = np.array([[0 for _ in range(M)] for _ in range(N)])
for i in range(Q) :
    num, rc, v = map(int, sys.stdin.readline().rstrip().split())
    if num == 1 :
        array[rc-1] += np.array([v] * M)
    elif num == 2 :
        for j in range(N) :
            array[j][rc-1] += np.array([[v if l == rc else 0 for l in range(M)] for k in range(N)])

for i in range(N) :
    print(*array[i])
# for k in range(N) :
#     for l in range(M) :
#         print(array[k][l], end=" ")
#     print()