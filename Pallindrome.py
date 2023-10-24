#pallindromechecker

j = -1
flag = 0
def pallindrome_checker(string):
    for i in string:
        if i != string[j]:
            flag = 1
            break
        j = j - 1
   if flag == 1:
       print("NO")
   else :
       print("Yes")




