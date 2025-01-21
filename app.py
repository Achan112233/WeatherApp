import requests
from dotenv import load_dotenv

import os

load_dotenv()

api_key = os.getenv("API_KEY")

user_input = input("Enter City: ")

weather_data = requests.get(f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{user_input}?key={api_key}")

if weather_data.status_code == 400: 
    print("City not found")
else:
    weather_description = weather_data.json()['days'][0]['description']

    day = weather_data.json()['days'][0]['datetime']

    print(f"weather for {day} is {weather_description}")


