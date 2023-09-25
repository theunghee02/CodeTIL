import sys
n = int(sys.stdin.readline().rstrip())
dic = {}
cnt = 0
for j in range(n) :
    string = sys.stdin.readline().rstrip()
    if string == "ENTER" :
        for key,value in dic.items() :
            if value == 1 :
                cnt += 1
        dic = {}
    else :
        if string not in dic :
            dic[string] = 1
for key,value in dic.items() :
    if value == 1 :
        cnt += 1
print(cnt)