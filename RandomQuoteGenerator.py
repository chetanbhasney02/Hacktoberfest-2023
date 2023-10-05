import random

# List of quotes
quotes = [
    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
    "The only way to achieve the impossible is to believe it is possible. - Charles Kingsleigh",
    "The best way to predict the future is to invent it. - Alan Kay",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt"
]

def display_random_quote():
    random_quote = random.choice(quotes)
    print("Random Quote:")
    print(random_quote)

if __name__ == "__main__":
    display_random_quote()
