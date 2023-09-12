def isPrime(num) :
    if num == 0 or num == 1 :
        return False
    else :
        for i in range(2,int(num**0.5)+1) :
            if num % i == 0 :
                return False
    return True

import sys
M,N = map(int, sys.stdin.readline().rstrip().split())
for j in range(M,N+1) :
    if isPrime(j) :
        print(j)