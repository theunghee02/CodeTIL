N = int(input())
s = input()
r = 31
M = 1234567891
sum = 0
for i in range(N):
    
    hashnum = (ord(s[i])-96)
    sum +=hashnum * r **i

print(sum%M)