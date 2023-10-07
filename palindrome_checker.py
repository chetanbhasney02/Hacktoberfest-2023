def is_palindrome(s):
    s = ''.join(e for e in s if e.isalnum()).lower()  # Remove non-alphanumeric characters and convert to lowercase
    return s == s[::-1]

def main():
    user_input = input("Enter a word or phrase: ")
    
    if is_palindrome(user_input):
        print("Yes, it's a palindrome!")
    else:
        print("No, it's not a palindrome.")

if __name__ == "__main__":
    main()
