import requests

url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 9.03,
    "longitude": 38.74,
    "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
    "temperature_unit": "celsius",
    "timezone": "Africa/Addis_Ababa"
}

response = requests.get(url, params=params, timeout=10)

print("Status:", response.status_code)

data = response.json()

# Access the nested dictionary
current = data["current"]

# Extract weather information
temperature = current["temperature_2m"]
humidity = current["relative_humidity_2m"]
wind_speed = current["wind_speed_10m"]

# Display the results
print("\n========== WEATHER ==========")
print(f"Temperature: {temperature}°C")
print(f"Humidity: {humidity}%")
print(f"Wind Speed: {wind_speed} km/h")
print("=============================")