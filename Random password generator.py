#creating a strong password using python's random module

import random

a1=['a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z']

password=[]

a2=str(input("Do you want to include alphabets y or n "))
if a2=='y':
    a5=int(input('How many alphabets do you want'))
    for i in range(0,a5):
        random_alpha = random.choice(a1)
        password.append(random_alpha)
else:
    pass


a3=str(input("Do you want to include number y or n "))
n=int(input("specify the final number till which you want to include in the password "))
if a3=='y':
    a6=int(input('How many numbers do you want '))
    for i in range(0,a6):
        r=random.randint(0,n)
        password.append(r)
else:
    pass


s=['!','@','#','$','%',"^",'&','*']
a4=str(input("Do you want to include speial characters? y or n "))
if a4=='y':
    a7=int(input('How many special characters do you want '))
    for i in range(0,a7):
        random_char = random.choice(s)
        password.append(random_char)
else:
    pass


p=(' '.join(map(str, password)))
print(p.replace(" ", ""))