def kanto(a,n) :
    if n == 1 :
        return
    for i in range(a+n//3, a+(n//3)*2) :
        string[i] = " "
    kanto(a,n//3)
    kanto(a+n//3*2, n//3)

import sys
sys.setrecursionlimit(10 ** 6)
while True :
    try :
        n = int(sys.stdin.readline().rstrip())
        string = ['-'] * (3**n)
        kanto(0, 3**n)
        print(''.join(string))
    except :
        break