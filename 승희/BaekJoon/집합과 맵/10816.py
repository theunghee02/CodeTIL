def binary_search(arr,target,start,end) :
    while start <= end :
        mid = (start + end) // 2
        if arr[mid] == target :
            return mid
        elif arr[mid] > target :
            end = mid - 1
        else :
            start = mid + 1
    return None

import sys
N = int(sys.stdin.readline().rstrip())
Nlist = list(map(int, sys.stdin.readline().rstrip().split()))
M = int(sys.stdin.readline().rstrip())
MList = list(map(int, sys.stdin.readline().rstrip().split()))
result = dict()
for k in MList :
    result[k] = 0
sortedMLi = sorted(MList)
for i in Nlist :
    re = binary_search(sortedMLi, i, 0, M-1)
    if re is not None :
        result[i] += 1
for j in MList :
    print(result[j], end=" ")