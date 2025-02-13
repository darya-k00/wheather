import requests

def get_weather(city):
    params = {
        'MnTq': '',
        'lang': 'ru'
    }
    url = f'https://wttr.in/{city}'
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.text

def main():
    cities = ["аэропорт Шереметьево", "Лондон", "Череповец"]

    for city in cities:
        weather_info = get_weather(city)
        print(weather_info)

if __name__ == "__main__":
    main()

