numbers = []
for i in range(5):
    numbers.append(int(input()))

index_counts = {}
## 개수세기
for index in numbers:
    if index in index_counts:
        index_counts[index] += 1
    else:
        index_counts[index] = 1

#print(index_counts)

for index, count in index_counts.items():
    if count % 2 == 1: print(index)

