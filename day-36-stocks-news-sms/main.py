import os
from newsapi import NewsApiClient
from twilio.rest import Client

import requests
from datetime import datetime, timedelta

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

NEWS_API_KEY = 'b0469e723bbb4cbe940deef5a089bc16'
ALPHA_API_KEY = '9OICO6IKK8QO9NH4'

account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

alpha_params = {
    'function': 'TIME_SERIES_DAILY_ADJUSTED',
    'symbol': STOCK,
    'apikey': ALPHA_API_KEY
}

alpha_response = requests.get('https://www.alphavantage.co/query', params=alpha_params)
alpha_response.raise_for_status()
stock_data = alpha_response.json()['Time Series (Daily)']


def get_percentage_change():
    yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
    before_yesterday = (datetime.now() - timedelta(days=2)).strftime('%Y-%m-%d')
    closing_price_yesterday = float(stock_data[yesterday]['4. close'])
    closing_price_before_yesterday = float(stock_data[before_yesterday]['4. close'])
    percentage = (closing_price_yesterday - closing_price_before_yesterday) / closing_price_yesterday * 100
    # return float(percentage, 2)
    return -5.3


def get_news():
    newsapi = NewsApiClient(api_key=NEWS_API_KEY)
    top_headlines = newsapi.get_top_headlines(q=COMPANY_NAME,
                                              sources='bloomberg',
                                              language='en')
    return top_headlines


def send_message(percentage_sign: str):
    # Send a seperate message with the percentage change and each article's title and description to your phone number.
    for num in range(3):
        news_data = get_news()['articles'][num]
        headline = news_data['title']
        brief = news_data['description']
        message_body = f"{STOCK}: {percentage_sign}{get_percentage_change()}% \n" \
                       f" Headline: {headline} ({STOCK}) \n" \
                       f" Brief: {brief}"
        message = client.messages \
            .create(
            body=message_body,
            from_='+13204411296',
            to='+15513198155')
    print(message.status)


# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday).
if get_percentage_change() > 5.0:
    up = '🔺'
    send_message(up)
elif get_percentage_change() < -5.0:
    down = '🔻'
    send_message(down)

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
