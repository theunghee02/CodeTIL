inputs = []
remainder = [0 for _ in range(1000)]
## 입력받기
for i in range(10):
    inputs.append(int(input()))
## 나머지 갯수 확인
for i in inputs:
    remainder[i%42]+=1
cnt = 0
for i in remainder:
    if i !=0 :cnt+=1

print(cnt)

