import sys
n,b = map(int, sys.stdin.readline().rstrip().split())
s = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
res = ''
while n :
    res += s[n%b]
    n //= b
print(res[::-1])

# N, B = map(int, input().split())
# s = ''
# arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#
# while N:
#     s += str(arr[N%B])
#     N //= B
#
# print(s[::-1])
