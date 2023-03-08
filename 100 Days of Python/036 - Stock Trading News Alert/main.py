import os
import requests
import re


def remove_html_tags(text):
    """Remove HTML Tags from String"""
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)


# API Documentation https://www.alphavantage.co/documentation/#daily
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# API Stuff/Get Enviroment variables
alpha_auth_api = os.environ['ALPHA_ADVANTAGE_API_KEY']
news_auth_api = os.environ['NEWS_API_KEY']
alpha_parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": alpha_auth_api
}
response = requests.get(STOCK_ENDPOINT, params=alpha_parameters)
response.raise_for_status()
stock_data = response.json()
stock_data = stock_data['Time Series (Daily)']
stock_data_list = [(date, data) for date, data in stock_data.items()]
y_close = float(stock_data_list[1][1]['4. close'])
before_y_close = float(stock_data_list[2][1]['4. close'])
before_y_close_date = stock_data_list[2]
# Find percentage difference between yesterday and day before
percentage_difference = abs((y_close - before_y_close) / ((y_close + before_y_close) / 2) * 100)
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
if abs(percentage_difference) < -5 or abs(percentage_difference) > 5:
    print("Get News")

# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
news_parameters = {
    "q": "tesla",
    "from": before_y_close_date,
    "sortBy": "publishedAt",
    "language": "en",
    "apiKey": news_auth_api
}
response = requests.get(NEWS_ENDPOINT, params=news_parameters)
response.raise_for_status()
news_data = response.json()
news_list = [story for story in news_data['articles'][:3]]## STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to your phone number.

for story in news_list:
    print(f"{STOCK_NAME} - {percentage_difference}%")
    print(story['title'])
    print(remove_html_tags((story['description'])))
    print(story['url'])
