import requests

api_key = '946f969ffc9b74d9c87a84a69ccb66e7'

def get_weather(city_name):
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'q': city_name, 'appid': api_key}

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        main_data = data['main']
        temperature = main_data['temp']
        description = data['weather'][0]['description']

        celsius_temperature = kelvin_to_celsius(temperature)

        print(f"Sää paikkakunnalla {city_name}:")
        print(f"Säätila: {description}")
        print(f"Lämpötila: {celsius_temperature:.2f} °C")
    else:
        print("Säätilan hakeminen epäonnistui. Tarkista paikkakunnan nimi ja API-avain.")

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15


if __name__ == '__main__':
    city_name = input("Anna paikkakunnan nimi: ")
    get_weather(city_name)
