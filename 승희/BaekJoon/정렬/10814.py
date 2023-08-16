import sys
N = int(sys.stdin.readline().rstrip())
array = []
for _ in range(N) :
    a,b = map(str, sys.stdin.readline().rstrip().split())
    array.append(tuple([int(a),b]))
sortedDict = sorted(array, key = lambda x : x[0])
for i in sortedDict :
    print(i[0], i[1])