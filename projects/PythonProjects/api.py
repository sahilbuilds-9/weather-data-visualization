import json
from urllib.request import urlopen

# We need coordinates to get weather data
latitude = 48.85   # Paris latitude
longitude = 2.35   # Paris longitude

# Build the API URL with our parameters
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

# Make the request
with urlopen(url) as response:
    data = json.load(response)

print(data)
#////////////////////

import json
from urllib.request import urlopen

def get_weather(latitude, longitude):
    url = (
        "https://api.open-meteo.com/v1/forecast?"
        f"latitude={latitude}&longitude={longitude}"
        "&current=temperature_2m,wind_speed_10m"
    )
    with urlopen(url) as response:
        data = json.load(response)
    return data['current']['temperature_2m']

# Get temperature for different cities
rampur_temp = get_weather(28.789305,79.024956)
moradabad_temp = get_weather(28.838648, 78.773331)
bazpur_temp = get_weather(29.158001, 79.147598)

print(f"Rampur: {rampur_temp}°C")
print(f"Moradabad: {moradabad_temp}°C")
print(f"Bazpur: {bazpur_temp}°C")
