# this is the "app/robo_advisor.py" file

import requests
import json

#
# INFO INPUTS
#

request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo"

response = requests.get(request_url)
# print(type(response)) #> <class 'requests.models.Response'>
# print(response.status_code) #> 200
# print(response.text)

parsed_response = json.loads(response.text)

last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]

# breakpoint()

#
# INFO OUTPUTS
#

print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")

# Date and Time

import datetime
now = datetime.datetime.now()
print("REQUEST AT: " + str(now.strftime("%Y-%m-%d %I:%M %p")))

#

print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print("LATEST CLOSE: $100,000.00")
print("RECENT HIGH: $101,000.00")
print("RECENT LOW: $99,000.00")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")


 