import sys
arr = list(map(int, sys.stdin.readline().rstrip().split()))
while arr[0] != 0 and arr[1] != 0 and arr[2] != 0 :
    num = 0
    max = arr[0]
    nArr = [0,1,2]
    for i in range(1,len(arr)) :
        if max < arr[i] :
            max = arr[i]
            num = i
    nArr.pop(num)
    if arr[num] ** 2 == arr[nArr[0]] ** 2 + arr[nArr[1]] ** 2 :
        print('right')
    else :
        print('wrong')
    arr = list(map(int, sys.stdin.readline().rstrip().split()))