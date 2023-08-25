N = int(input())
# ## 2차원 배열 생성
# files = [[0 for _ in range(1)] for _ in range(N)]
# ## 입력 받기
# for i in range(N):
#     file = input()
#     files[i][0] = file

# for i in range(len(files)):
#     print(files[i][0])
# for i in range(3):
#     for j in range(len(files[i][0])):
#         if(files[i][0][j])

#     print([i][0])

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
print(result)
print(''.join(result))
#print("\n".join(filenames))