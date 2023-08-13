import sys
count = [0] * 10001
for _ in range(int(sys.stdin.readline().rstrip())) :
    count[int(sys.stdin.readline().rstrip())] += 1

for i in range(1,10001) :
    for _ in range(count[i]) :
        print(i)