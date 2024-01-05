import yfinance as yf
import matplotlib.pyplot as plt

tick = input("\033[1;30;40m Enter a valid stock ticker \033[0m \n")
ticker = yf.Ticker(tick)

timeValue = input("\033[1;30;40m Enter the time period (5y, 10w, 6m, 14d, ytd) \033[0m \n")
hist = ticker.history(period=timeValue)

# Extract closing prices
closing_prices = hist["Close"]

# Plot the closing prices
plt.plot(closing_prices)
plt.title(f"{tick} Closing Prices")
plt.xlabel("Date")
plt.ylabel("Closing Price")

# Save the plot as a PNG image
plt.savefig("closing_prices.png")
plt.show()