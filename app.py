import requests
from dotenv import load_dotenv

import os

load_dotenv()

api_key = os.getenv("API_KEY")

user_input = input("Enter City: ")

weather_data = requests.get(f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{user_input}?key={api_key}")




