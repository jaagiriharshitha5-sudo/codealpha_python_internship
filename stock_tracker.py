stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 180,
    "MSFT": 420
}

portfolio = {}
total_investment = 0

print("===== STOCK PORTFOLIO TRACKER =====")

while True:

    stock = input("\nEnter stock name (or type 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available.")
        print("Available stocks:", ", ".join(stock_prices.keys()))
        continue

    quantity = int(input("Enter quantity: "))

    portfolio[stock] = quantity

    investment = stock_prices[stock] * quantity

    total_investment += investment

    print("Investment for", stock, "=", investment)

print("\n===== PORTFOLIO SUMMARY =====")

for stock, quantity in portfolio.items():

    value = stock_prices[stock] * quantity

    print(stock, ":", quantity, "shares =", value)

print("\nTotal Investment =", total_investment)