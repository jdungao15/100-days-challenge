import requests
import os
from twilio.rest import Client

API_KEY = '69f04e4613056b159c2761a9d9e664d2'
OWM_ENDPOINT = 'https://api.openweathermap.org/data/2.5/onecall'
account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token  = os.environ.get('TWILIO_AUTH_TOKEN')

weather_params = {
    'lat': 40.934340,
    'lon': -74.016870,
    'appid': API_KEY,
    "exclude": "current,minutely,daily",
}

response = requests.get(OWM_ENDPOINT, weather_params)
response.raise_for_status()
weather_data = response.json()['hourly']
first_twelve_hour = [data for data in weather_data[:12]]

will_rain = False
for hour in first_twelve_hour:
    condition_code = hour['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It's going to rain today. Remember bring an ☔",
            from_='+13204411296',
            to='+15512410650'
    )
    print(message.status)
