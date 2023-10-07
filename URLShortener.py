import random
import string

class URLShortener:
    def __init__(self):
        self.url_mapping = {}
    def generate_code(self, length=6):
        """Generate a random code for the URL."""
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(length))
    def shorten_url(self, original_url):
        """Shorten the given URL and return the shortened URL."""
        if original_url in self.url_mapping:
            return self.url_mapping[original_url]
        else:
            short_code = self.generate_code()
            short_url = f"http://short.url/{short_code}"
            self.url_mapping[original_url] = short_url
            return short_url

def main():
    url_shortener = URLShortener()

    while True:
        original_url = input("Enter the URL to shorten (or 'exit' to quit): ")
        if original_url.lower() == 'exit':
            break

        shortened_url = url_shortener.shorten_url(original_url)
        print(f"Shortened URL: {shortened_url}")

if __name__ == "__main__":
    main()
