import math
A, B, V = map(int, input().split())
day = 0
cnt = 0
# while 1:
#     cnt = cnt + A
#     if cnt >= V:
#         day+=1
#         print(day) 
#         break
#     cnt = cnt - B
#     day+=1

##sol2)
day= (V-B)/(A-B)
print(math.ceil(day))
