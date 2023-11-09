# 화폐 종류, 거슬러줄 돈
n, k = map(int, input().split())
coin_list = []

# 입력 받기
for i in range(n):
    coin_list.append(int(input()))
## 그리디
coin_list.sort(reverse=True)

cnt = 0
for i in range(n):
    cnt += k//coin_list[i]
    k = k%coin_list[i]

print(cnt)