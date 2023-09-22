import sys
N = int(sys.stdin.readline().rstrip())
current = list(map(int, sys.stdin.readline().rstrip().split()))
start = 1
oneLine = []
for i in current :
    oneLine.append(i)
    while oneLine and oneLine[-1] == start :
        oneLine.pop()
        start += 1
    if len(oneLine) > 1 and oneLine[-1] > oneLine[-2] :
        print("Sad")
        sys.exit()
if oneLine :
    print('Sad')
else :
    print('Nice')