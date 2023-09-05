import sys
import math
a,b = map(int, sys.stdin.readline().rstrip().split())
A,B = map(int, sys.stdin.readline().rstrip().split())
reA = a * B + A * b
reB = b * B
divisor = math.gcd(reA, reB)
print(reA // divisor, reB // divisor)