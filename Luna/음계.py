arr = list(map(int, input().split()))

for i in range(len(arr)-1):
    #오름차순
    if(arr[i]+1 == arr[i+1]): check = 0
    #내림차순
    elif(arr[i]-1 == arr[i+1]): check = 1
    #규칙이 지켜지지 않을때
    else :
        check = 2
        break


if check == 0: print("ascending")
elif check == 1: print("descending")
else : print("mixed")