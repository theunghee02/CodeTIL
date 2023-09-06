spell = ["z", "d", "x"]
dic = ["def", "dww", "dzx", "loveaw"]
result = ''
isValid = 0 

for word in dic:
    # 해당 단어가 유효한지 판단
    isWordValid = 1
    for ch in spell:
        if ch not in word:
            isWordValid = 0
            break
    if isWordValid == 1:
        isValid = 1

if isValid == 1:
    print(1)
else:
    print(2)

## sol2)
# for word in dic:
#     # 해당 단어가 유효한지 판단
#     isValid = 1
#     for ch in spell:
#         if ch not in word:
#             isValid = 0
#             break
#     if isValid == 1:break

# if isValid == 1:
#     print(1)
# else:
#     print(2)
