import yfinance as yf
import argparse


def get_stock_price(ticker):
    try:
        stock = yf.Ticker(ticker)

        todays_data = stock.history(period="1d")

        if todays_data.empty:
            print(f"Could not find data for {ticker}. Is the ticker correct?")
            return

        price = todays_data["Close"].iloc[-1]
        currency = stock.info.get("currency", "USD")

        print(f"--- {ticker.upper()} ---")
        print(f"Current Price: {price:.2f} {currency}")

        print(f"Day High: {todays_data['High'].iloc[-1]:.2f}")
        print(f"Day Low: {todays_data['Low'].iloc[-1]:.2f}")
    except Exception as e:
        print(f"Error: {e}")


def main():
    parser = argparse.ArgumentParser(description="Stock Price Checker")

    parser.add_argument("ticker", help="Stock ticker symbol")

    args = parser.parse_args()

    get_stock_price(args.ticker)



if __name__ == '__main__':
    main()

