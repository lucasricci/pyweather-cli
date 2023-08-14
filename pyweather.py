"""Make requests and remove non-ASCII characters"""
import requests
from unidecode import unidecode


def division_line(repetitions):
    """Function to print lines"""
    print("=" * repetitions)


cities = []
with open('list.txt', encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        cities.append(line.strip().replace("\n", ""))


while True:
    city = unidecode(input("City: ").title())
    if city in cities:
        break

API = ""
coord = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}"

geocoord = requests.get(coord, timeout=5)
coordData = geocoord.json()
u = input("Unit (Metric, Imperial, Standart [Kelvin]): ").lower()

lat = coordData['coord']['lat']
lon = coordData['coord']['lon']
url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units={u}&appid={API}"

response = requests.get(url, timeout=5)
data = response.json()

temperature = data['main']['temp']
feelsLike = data['main']['feels_like']
tempMax = data['main']['temp_max']
tempMin = data['main']['temp_min']
weather = data['weather'][0]['description']
humidity = data['main']['humidity']

if u == "metric":
    MEASUREMENT_UNIT = "ºC"
elif u == "imperial":
    MEASUREMENT_UNIT = "ºF"
else:
    MEASUREMENT_UNIT = "K"

division_line(40)
print(f'City: {city}')
print(f'Temperature: {round(temperature)}{MEASUREMENT_UNIT}')
print(f'Feels Like: {round(feelsLike)}{MEASUREMENT_UNIT}')
print(f'Weather: {weather.title()}')
print(f'Humidity: {humidity}%')
division_line(40)
