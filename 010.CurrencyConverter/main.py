def currency_converter():
    rates = {
        "USD": 1.0,
        "EUR": 0.92,
        "GBP": 0.79,
        "JPY": 151,
        "CAD": 1.35,
        "AUD": 1.52,
    }

    print("---- Python Currency Converter ----")
    print(f"Supported currencies: {', '.join(rates.keys())}")

    try:
        amount = float(input("\nEnter the amount: "))
        from_curr = input("From currency: ").upper().strip()
        to_curr = input("To currency: ").upper().strip()

        if from_curr not in rates or to_curr not in rates:
            print("Error: One or both currencies are not supported!")
            return

        amount_in_usd = amount / rates[from_curr]
        converted_amount = amount_in_usd * rates[to_curr]

        print("-" * 30)
        print(f"{amount:.2f} {from_curr} = {converted_amount:.2f} {to_curr}")
        print("-" * 30)
    except ValueError:
        print("Invalid input. Please enter a numeric value!")


if __name__ == "__main__":
    currency_converter()
