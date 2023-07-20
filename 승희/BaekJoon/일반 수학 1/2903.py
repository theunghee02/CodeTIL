import sys
import math
n = int(sys.stdin.readline().rstrip())
spot = 4
for i in range(n) :
    spot = (math.sqrt(spot)*2-1) ** 2
print(int(spot))