import sys
n,b = map(int, sys.stdin.readline().rstrip().split())
s = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
res = ''
while n :
    res += s[n%b]
    n //= b
print(res[::-1])
