s = input()
alpa = [0,'a','b','c','d','e','f','g','h']
dx = [2,-2,1,-1]
dy = [1,-1,2,-2]
x,y = 1,1
for i in range(len(s)) :
    if s[i] in alpa :
        x = int(alpa.index(s[i]))
    else :
        y = int(s[i])

count = 0
for i in range(2) :
    if x+dx[i] < 0 or x+dx[i] > 9 or y+dy[i] < 0 or y+dy[i] > 9 :
        continue
    count += 1

for i in range(2,4) :
    if x+dx[i] < 0 or x+dx[i] > 9 or y+dy[i] < 0 or y+dy[i] > 9 :
        continue
    count += 1
print(count)