## - 오기 전까지 쪼기
## 각각 계산
## 뺄셈
arr = input().split('-')
## 최종적으로 뺄셈을 하기 위한 저장할 곳
numbers = []
for i in arr:
    sum = 0
    ## 덧셈을 하기 위해 split -> 덧셈 계산
    tmp = i.split('+')
    for j in tmp:
        sum += int(j)
    numbers.append(sum)
#print(numbers)
sum2 = numbers[0]
for i in range (1,len(numbers)):
    sum2 -= numbers[i]
    ##sum2 = sum2 - numbers[1]
print(sum2)