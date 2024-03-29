a, cnt = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [0, 2, 4, 6]
f = open('homework4.txt', 'w')
for i in cnt:
    f.write(f"{a[i] ** 2}\n") #문자열로 변환