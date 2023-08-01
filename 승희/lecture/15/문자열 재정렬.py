s = input()
charList = []
sum = 0
for i in s :
    if int(ord(i)) > 64 :
        charList.append(i)
    else :
        sum += int(i)
charList.sort()
for i in charList :
    print(i, end="")
print(sum)