import requests
from config import OPENWEATHER_API_KEY

def get_location_from_number(phone_number):
    phone_location_map = {
        "whatsapp:+91987654321": "Hyderabad"  
    }
    return phone_location_map.get(phone_number, "Chennai")

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
    res = requests.get(url).json()

    if res.get("cod") != 200:
        return {"summary": "❌ Weather unavailable.", "description": "unknown"}

    main = res["main"]
    weather = res["weather"][0]["description"]
    return {
        "summary": f"🌤️ {city}: {main['temp']}°C, {weather}",
        "description": weather.lower()
    }
