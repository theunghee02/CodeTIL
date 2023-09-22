N = int(input())
numbers = list(map(int, input().split()))
prime_num = 0
#약수 - 1과 자기자신
for num in numbers:
    # 2 부터 자기자신까지 
    for i in range(2, num+1):
        if num%i == 0:
            if num == i:
                prime_num +=1
            break

print(prime_num)