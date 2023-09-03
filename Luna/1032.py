N = int(input())
filenames = []

for i in range(N):
    file = input()
    filenames.append(file)

# filenames의 첫번째 값 저장
result = list(filenames[0])

for i in range(N):
    for j in range(len(result)):
        if result[j] == filenames[i][j]:
            continue
        else:
            result[j] = '?'

print(''.join(result))
