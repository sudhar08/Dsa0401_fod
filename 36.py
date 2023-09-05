import pandas as pd

def calculate_stock_variability(stock_data):
    # Calculate the standard deviation and range of stock prices
    std_deviation = stock_data['Close'].std()
    price_range = stock_data['Close'].max() - stock_data['Close'].min()
    
    return std_deviation, price_range

def main():
    # Read the stock data from the CSV file
    file_path = "C:/Users/mailm/Downloads/stock_data.csv"
    stock_data = pd.read_csv(file_path)

    # Calculate the variability of stock prices
    std_deviation, price_range = calculate_stock_variability(stock_data)

    # Print the results
    print("Stock Price Variability:")
    print("Standard Deviation:", std_deviation)
    print("Price Range:", price_range)

    # Provide insights based on the calculated values
    if std_deviation < 10:
        print("The stock price is relatively stable.")
    elif std_deviation >= 10 and std_deviation < 50:
        print("The stock price has moderate variability.")
    else:
        print("The stock price is highly volatile.")

    if price_range < 50:
        print("The stock price range is relatively narrow.")
    elif price_range >= 50 and price_range < 100:
        print("The stock price range is moderate.")
    else:
        print("The stock price range is wide.")

if __name__ == "__main__":
    main()
