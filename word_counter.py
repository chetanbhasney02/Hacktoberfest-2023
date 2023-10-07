def count_words(text):
    """
    This function takes a string as input and returns the number of words in it.
    """
    words = text.split()
    return len(words)

# Example usage:
text = "This is a sample text to count the number of words."
word_count = count_words(text)
print("Word count:", word_count)