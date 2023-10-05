def palindrome(string):
    rev_string = string[::-1]
    return rev_string

while True:
    string = input("Enter a string or number to check palindrome:")
    rev = palindrome(string)
    if(string == rev):
        print("It is palindrome")
    else:
        print("It is not palindrome")
    check = input("Do you want to check again? yes/no:").lower();
    if(check != 'yes'):
        break
