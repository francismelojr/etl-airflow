import json
import os
from datetime import datetime

import requests
from dotenv import load_dotenv

from contracts.schema import WeatherSchema

load_dotenv()

key = os.getenv('WEATHER_API_KEY')


def get_current_weather(city: str):

    url = (
        f'http://api.weatherapi.com/v1/current.json?key={key}&q=Paris&aqi=yes'
    )

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        with open(
            f"src/output/{data['location']['name'].lower()}-{datetime.now().strftime('%d-%m-%Y-%H:%M:%S')}.json",
            'w',
        ) as f:
            json.dump(data, f)

        return data
    else:
        print(f'Error: {response.status_code}')
        return None
