def lcm(a,b) :
    return a * b // math.gcd(a,b)

import sys
import math
for _ in range(int(sys.stdin.readline().rstrip())) :
    A,B = map(int, sys.stdin.readline().rstrip().split())
    print(lcm(A,B))