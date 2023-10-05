import string

# remove all punctuation and spaces


def clean_sentence(sentence):
    symbols = string.punctuation
    for s in sentence:
        if s in symbols:
            sentence = sentence.replace(s, '')
    sentence = sentence.replace(' ', '').lower()

    return sentence


def check_palindrome(value):
    reverse = value[::-1]
    if reverse == value:
        print('Your sentence is palindrome.')
        return
    print("Sentence is not a palindrome.")


if __name__ == '__main__':
    sentence = input("Enter sentence to check if palindrome: ")
    cleaned_sentence = clean_sentence(sentence)
    check_palindrome(cleaned_sentence)
