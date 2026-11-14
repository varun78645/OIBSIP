
import requests

print("================================")
print("        BASIC WEATHER APP")
print("================================")

# Get city name
city = input("Enter city name: ")

try:
    # Find city coordinates
    geo_url = "https://geocoding-api.open-meteo.com/v1/search"

    geo_params = {
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json"
    }

    geo_response = requests.get(geo_url, params=geo_params, timeout=10)
    geo_response.raise_for_status()
    geo_data = geo_response.json()

    if "results" not in geo_data:
        print("Error: City not found. Please enter a valid city.")

    else:
        location = geo_data["results"][0]

        latitude = location["latitude"]
        longitude = location["longitude"]
        city_name = location["name"]
        country = location.get("country", "Unknown")

        # Get weather information
        weather_url = "https://api.open-meteo.com/v1/forecast"

        weather_params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": [
                "temperature_2m",
                "relative_humidity_2m",
                "apparent_temperature",
                "weather_code",
                "wind_speed_10m"
            ]
        }

        weather_response = requests.get(
            weather_url, params=weather_params, timeout=10
        )
        weather_response.raise_for_status()
        weather_data = weather_response.json()

        current = weather_data["current"]
        code = current["weather_code"]

        # Weather condition descriptions
        conditions = {
            0: "Clear Sky",
            1: "Mainly Clear",
            2: "Partly Cloudy",
            3: "Overcast",
            45: "Foggy",
            48: "Rime Fog",
            51: "Light Drizzle",
            53: "Moderate Drizzle",
            55: "Heavy Drizzle",
            61: "Light Rain",
            63: "Moderate Rain",
            65: "Heavy Rain",
            71: "Light Snow",
            73: "Moderate Snow",
            75: "Heavy Snow",
            80: "Rain Showers",
            81: "Moderate Rain Showers",
            82: "Heavy Rain Showers",
            95: "Thunderstorm"
        }

        condition = conditions.get(code, "Unknown Condition")

        # Display weather report
        print("\n========== WEATHER REPORT ==========")
        print("City:", city_name)
        print("Country:", country)
        print("Temperature:", current["temperature_2m"], "°C")
        print("Feels Like:", current["apparent_temperature"], "°C")
        print("Condition:", condition)
        print("Humidity:", current["relative_humidity_2m"], "%")
        print("Wind Speed:", current["wind_speed_10m"], "km/h")
        print("====================================")

except requests.exceptions.RequestException:
    print("Error: Unable to connect to the weather service.")

except (KeyError, IndexError, ValueError):
    print("Error: Unable to process weather information.")

