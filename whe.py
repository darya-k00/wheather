import requests
from urllib.parse import urlencode

def get_weather(city):
    params = {
        'MnTq': '',
        'lang': 'ru'
    }
    query_string = urlencode(params)
    url = f'https://wttr.in/{city}?{query_string}'
    response = requests.get(url)
    response.raise_for_status()

    if response.status_code==200:
        return response.text
    else:
        print(f"{response.status_code}")

if __name__ == "__main__":
    cities = ["аэропорт Шереметьево", "Лондон", "Череповец"]

    for city in cities:
        weather_info = get_weather(city)
        print(weather_info)
