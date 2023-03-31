# Stock Price Checker and News Alert

This Python script fetches the daily adjusted closing prices of a particular stock and calculates the percentage change between yesterday's closing price and the closing price of four days ago. If the percentage change is greater than or equal to 2, it fetches the latest news articles related to the stock using the News API and sends an SMS alert containing the stock's symbol, the percentage change, and the headline and brief of each news article.

## Requirements

1. Python 3
2. requests library
3. datetime module
4. twilio library
5. A Twilio account (for sending SMS alerts)
6. An Alpha Vantage API key (for fetching stock prices)
7. A News API key (for fetching news articles)

## Setup

1. Clone the repository and navigate to the directory containing the script.
2. Install the required libraries: ```pip install requests twilio```
3. Update the script with your API keys for Alpha Vantage and News API, as well as your Twilio account SID and auth token.
4. Replace your twilio number with your Twilio phone number and number on which message is to be sent with the phone number that will receive the SMS alerts.
5. Replace STOCK and COMPANY_NAME with the symbol and name of the stock you want to track.

## Usage

To run the script, execute the following command in your terminal:

```
python stock_alert.py
```

The script will output the percentage change in the stock's price and the headline and brief of each news article related to the stock. It will also send an SMS alert containing the same information if the percentage change is greater than or equal to 2.
