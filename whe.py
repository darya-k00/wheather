import requests

def get_weather(city):
    url = f'https://wttr.in/{city}?MnTq&lang=ru'
    response = requests.get(url)
    return response.text

if __name__ == "__main__":
    cities = ["аэропорт Шереметьево", "Лондон", "Череповец"]

    for city in cities:
        weather_info = get_weather(city)
        print(weather_info)
