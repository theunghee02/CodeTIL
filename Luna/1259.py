#sol1)
# while True:
#     numString = input()
#     if numString == "0": break

#     isPalindrome = True
#     j = len(numString) -1
#     for i in range(len(numString)//2):
#         if(numString[i] != numString[len(numString)-(i+1)]):
#             print("no")
#             isPalindrome = False
#             break
#     if (isPalindrome): 
#         print("yes")

while True:
    numString = input()
    if numString == "0": break

    isPalindrome = True
    j = len(numString) -1

    for i in range(len(numString)//2):
        if(numString[i] != numString[j]):
            print("no")
            isPalindrome = False
            break
        j-=1
        
    if (isPalindrome): 
        print("yes")
