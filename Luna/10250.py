N = int(input())
# while(N) :
#     h, w, n = map(int, input().split())
#     floor = n%h
#     line = (n//h) + 1
    
#     if(floor == 0) :
#         floor = h
#         line -= 1
#     # if(line == 1) :
#     #     line += 2
#     print(floor * 100 + line)
#     N-=1
for _ in range(N):
    h, w, n = map(int, input(). split())
    row = (n-1)//h
    col = (n-1)%h

    print((col+1)* 100 + (row+1) )