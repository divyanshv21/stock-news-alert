STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY_STOCK = "your api-key"
API_KEY_NEWS = "your api-key"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

import requests
import datetime
from twilio.rest import Client

parameters = {
    'function': 'TIME_SERIES_DAILY_ADJUSTED',
    'symbol': STOCK,
    'apikey': API_KEY_STOCK
}

response = requests.get(STOCK_ENDPOINT, params=parameters)

daily_prices = response.json()['Time Series (Daily)']
yesterday = datetime.date.today() - datetime.timedelta(days=1)
yesterday_str = yesterday.strftime('%Y-%m-%d')
day_before_yesterday = datetime.date.today() - datetime.timedelta(days=4)
day_before_yesterday_str = day_before_yesterday.strftime('%Y-%m-%d')

if yesterday_str in daily_prices:
        closing_price_yesterday = float(daily_prices[yesterday_str]['4. close'])
else:
    print('No data available for yesterday')

if day_before_yesterday_str in daily_prices:
        closing_price_day_before_yesterday = float(daily_prices[day_before_yesterday_str]['4. close'])
else:
    print('No data available for yesterday')

difference = round( abs(closing_price_yesterday - closing_price_day_before_yesterday), 2)
percentage_change = (difference/closing_price_yesterday)*100

print(percentage_change)
if percentage_change >= 2:
    query_parameters = {
        "q": COMPANY_NAME,
        "pageSize": 3,
        "apiKey": API_KEY_NEWS
    }

    response = requests.get(NEWS_ENDPOINT, params=query_parameters)

    if response.status_code == 200:
        articles = response.json()["articles"]
        for article in articles:
            print(article["title"])
    else:
        print("An error occurred while fetching the news:", response.text)

    response = requests.get(NEWS_ENDPOINT, params={
        'country': 'us',
        'apiKey': 'your api-key'
    })

    # set up Twilio client
    account_sid = 'your account sid'
    auth_token = 'your auth token'
    client = Client(account_sid, auth_token)

    # send a separate message for each article
    for article in articles:
        title = article['title']
        description = article['description']
        message = f"TSLA: 🔺2%\n\nHeadline: {title}\n\nBrief: {description}"
        client.messages.create(
            to='number on which message is to be sent',
            from_='your twilio number',
            body=message
        )
