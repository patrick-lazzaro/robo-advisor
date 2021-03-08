# this is the "app/robo_advisor.py" file

import csv
import json
import os

import dotenv
import requests

# to_usd function replicated from shopping cart project

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

# Define hasNumbers function

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

#
# INFO INPUTS
#

# Ask user for stock symbol
# Validate user input 

while True:
    symbol = input("WELCOME! PLEASE CHOOSE A STOCK TICKER (EX: IBM) ")

    if (hasNumbers(symbol) == True) or (len(symbol) < 1) or (len(symbol) > 5):
        print("Oh, expecting a properly-formed stock ticker like 'MSFT'. Please try again.")
    else:
        break

# API KEY

dotenv.load_dotenv()
api_key = os.getenv("ALPHAVANTAGE_API_KEY", default="demo") 

request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"

response = requests.get(request_url)

if "Error Message" in response.text:
    #print("Error")
    exit()

parsed_response = json.loads(response.text)

last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]

tsd = parsed_response["Time Series (Daily)"]

dates = list(tsd.keys()) # TODO: assumes first day is on top, sort to ensure latest day is first

latest_day = dates[0]
latest_close = tsd[latest_day]["4. close"]

# Recent High - Max of all high prices
# Recent Low - Min of all high prices

high_prices = []
low_prices = []

for date in dates:
    high_price = tsd[date]["2. high"]
    low_price = tsd[date]["3. low"]
    high_prices.append(float(high_price))
    low_prices.append(float(low_price))

recent_high = max(high_prices)
recent_low = min(low_prices)

#
# INFO OUTPUTS
#

csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv")

csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]

with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
    writer.writeheader() # uses fieldnames set above

    for date in dates:  
        daily_prices = tsd[date]
        writer.writerow({
            "timestamp": date,
            "open": daily_prices["1. open"],
            "high": daily_prices["2. high"],
            "low": daily_prices["3. low"],
            "close": daily_prices["4. close"],
            "volume": daily_prices["5. volume"],
        })

print("-------------------------")
print(f"SELECTED SYMBOL: {symbol}")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")

# Date and Time

import datetime
now = datetime.datetime.now()
print("REQUEST AT: " + str(now.strftime("%Y-%m-%d %I:%M %p")))

print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print(f"RECENT LOW: {to_usd(float(recent_low))}")
print("-------------------------")

# Recommendation and Reasoning Formula

if (float(latest_close) >= (recent_high * .90)): 
    recommendation = "STRONG BUY!"
    reason = "The stock is within 10% of its recent high, get it while it's still doing performing very strong"
elif (float(latest_close) >= (recent_high * .80)) & (float(latest_close) < (recent_high * .90)):
    recommendation = "BUY!"
    reason = "The stock is between 10%-20% of its recent high, it is doing well and is a good buy"
elif (float(latest_close) >= (recent_high * .65)) & (float(latest_close) < (recent_high * .80)):
    recommendation = "HOLD!"
    reason = "The stock is between 20%-35% of its recent high, I would hold any investment for now and look for movements in the price"
elif (float(latest_close) >= (recent_high * .50)) & (float(latest_close) < (recent_high * .65)):
    recommendation = "SELL!"
    reason = "The stock is between 35%-50% of its recent high, I would sell this declining stock at this point and watch to see if it increases soon"
else:
    recommendation = "STRONG SELL!"
    reason = "The stock is below 50% of its recent high, you do not want this plummeting stock in your portfolio right now"

print(f"RECOMMENDATION: {recommendation}")
print(f"RECOMMENDATION REASON: {reason}")
print("-------------------------")

# CSV Message

print(f"WRITING DATA TO CSV: {csv_file_path}...")
print("-------------------------")

# Exit Message

print("HAPPY INVESTING!")
print("-------------------------")


