import sys
from string import ascii_uppercase
n,b = map(str, sys.stdin.readline().rstrip().split())
b = int(b)
apha = ascii_uppercase
leN = len(n)-1
res = 0

for i in n :
    if i.isdigit() :
        res += int(i) * b ** leN
    else :
        for j in range(len(apha)) :
            if i == apha[j] :
                res += (j+10) * b ** leN
    leN -= 1
print(res)