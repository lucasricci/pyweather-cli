# Many thanks to https://simplemaps.com/data/world-cities

import requests
from unidecode import unidecode


def divisionLine(n):
    print("=" * n)


cities = []
with open('list.txt') as f:
    lines = f.readlines()
    for line in lines:
        cities.append(line.strip().replace("\n",""))


while True:
    city = unidecode(input("City: ").title())
    if city in cities:
        break
    else:
        continue

api_key = "b0c459ecb088b162b63f90fabf2f6574"
coord = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

geocoord = requests.get(coord)
coordData = geocoord.json()
unit = input("Unit (Metric, Imperial, Standart [Kelvin]): ").lower()

url = f"https://api.openweathermap.org/data/2.5/weather?lat={coordData['coord']['lat']}&lon={coordData['coord']['lon']}&units={unit}&appid={api_key}"

response = requests.get(url)
data = response.json()

temperature = data['main']['temp']
feelsLike = data['main']['feels_like']
tempMax = data['main']['temp_max']
tempMin = data['main']['temp_min']
weather = data['weather'][0]['description']
humidity = data['main']['humidity']

if unit == "metric":
    measurementUnit = "ºC"
elif unit == "imperial":
    measurementUnit = "ºF"
else:
    measurementUnit = "K"

divisionLine(40)
print(f'City: {city}')
print(f'Temperature: {round(temperature)}{measurementUnit}')
print(f'Feels Like: {round(feelsLike)}{measurementUnit}')
print(f'Weather: {weather.title()}')
print(f'Humidity: {humidity}%')
divisionLine(40)

# print(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units={unit}&appid={api_key}")