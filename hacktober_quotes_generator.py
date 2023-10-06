import requests

def fetch_random_quote():
    """
    Fetch quotes from quotable api
    https://github.com/lukePeavey/quotable
    """
    base_url = "https://api.quotable.io"
    # random quote endpoint
    endpoint = "/quotes/random"
    # full API URL
    api_url = f"{base_url}{endpoint}"
    try:
        # GET request to the API
        response = requests.get(api_url)
        if response.status_code == 200:
            # Parse the JSON
            data = response.json()
            quote = data[0].get("content")
            author = data[0].get("author")
            print("-------------------------------------------")
            print(f"Quote: '{quote}'\nAuthor: {author}")
            print()
            print('Happy Hacktoberfest!')
        else:
            print(f"Error: Unable to fetch a random quote (Status Code: {response.status_code})")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    print("Fetching a fresh quote, won't be a minute.")
    fetch_random_quote()
