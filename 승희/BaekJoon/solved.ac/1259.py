import sys
inp = sys.stdin.readline().rstrip()
while inp != '0' :
    no = 0
    for i in range(len(inp)//2) :
        if inp[i] != inp[len(inp)-i-1] :
            no = 1
            break
    if no :
        print('no')
    else :
        print('yes')
    inp = sys.stdin.readline().rstrip()