from WeatherApp import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")

user_input = input("Enter City: ")

weather_data = requests.get()

