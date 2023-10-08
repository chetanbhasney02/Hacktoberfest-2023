from forex_python.converter import CurrencyRates

# Create an instance of the CurrencyRates class
c = CurrencyRates()

def exchange_rates():
    # Get a list of available currencies and their codes
    currencies = c.get_rates('')
    print("Available currencies:")
    for code, rate in currencies.items():
        print(f"{code}: {rate}")

def exchange_currency():
    # Input the source currency, amount, and target currency
    source_currency = input("Enter source currency code: ").upper()
    target_currency = input("Enter target currency code: ").upper()
    amount = float(input("Enter the amount: "))

    # Calculate the exchange rate
    exchange_rate = c.convert(source_currency, target_currency, amount)
    print(f"{amount} {source_currency} is equal to {exchange_rate} {target_currency}")

if __name__ == "__main__":
    print("Welcome to Currency Exchange Rate Calculator")
    
    while True:
        print("\nOptions:")
        print("1. Get exchange rates")
        print("2. Convert currency")
        print("3. Quit")
        
        choice = input("Select an option (1/2/3): ")
        
        if choice == '1':
            exchange_rates()
        elif choice == '2':
            exchange_currency()
        elif choice == '3':
            print("Thank you for using Currency Exchange Rate Calculator. Goodbye!")
            break
        else:
            print("Invalid option. Please select a valid option (1/2/3).")
