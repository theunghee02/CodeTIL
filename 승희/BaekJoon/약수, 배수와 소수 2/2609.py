def LCM(a,b) :
    return a * b // math.gcd(a,b)
import sys
import math
a,b = map(int, sys.stdin.readline().rstrip().split())
print(math.gcd(a,b))
print(LCM(a,b))