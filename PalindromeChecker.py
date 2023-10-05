#Function to check string is palindrome or not in python!

# Here we will find reverse of the string and then Check if reverse and original are same or not.
# the predefined function ‘ ‘.join(reversed(string)) is used to reverse string.

def isPalindrome(s):

	rev = ''.join(reversed(s))

	# Checking if both string ar equal or not
	if (s == rev):
		return True
	return False

# main function

s = input("Enter your String: ")
ans = isPalindrome(s)

if (ans):
	print("Yes")
else:
	print("No")
