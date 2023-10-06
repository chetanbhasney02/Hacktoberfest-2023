def is_palindrome(s):
    # Remove spaces and convert the string to lowercase
    s = s.replace(" ", "").lower()
    
    # Compare the original string with its reverse
    return s == s[::-1]

# Input string to check for palindrome
input_string = input("Enter a string: ")

if is_palindrome(input_string):
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")
    
