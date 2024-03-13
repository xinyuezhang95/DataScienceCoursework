# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 20:44:08 2024

@author: zxy23
"""
import os
import requests
from twilio.rest import Client

api_key = os.environ.get("OWM_API_KEY")
api_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
account_sid = os.environ.get("OWM_ACCT_ID")
auth_token = os.environ.get("OWM_AUTH_TOKEN")
twilio_from = os.environ.get("TWILIO_FROM")
twilio_to = os.environ.get("TWILIO_TO")

weather_params = {
    "lat": 36.197899,
    "lon": -86.623161,
    "appid": api_key,
    "cnt": 4,
    }

response = requests.get(api_endpoint, params = weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for weather in weather_data["list"]:
    weather_details = weather["weather"]
    for det in weather_details:
        if int(det["id"]) < 700:
            will_rain = True
            
if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
      from_=twilio_from,
      body="It is going to rain today. Remember to bring an unbrella.",
      to=twilio_to
    )
    print(message.status)
