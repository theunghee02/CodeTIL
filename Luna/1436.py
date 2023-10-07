N = int(input())
### 6이 적어도 3개이66상
start = 666
cnt = 0
while True:
    if '666' in str(start):
        cnt +=1
    if cnt == N:
        print(start)
        break
    start+=1