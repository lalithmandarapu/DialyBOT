import pywhatkit
import requests
import datetime
import schedule
import time

API_KEY = "Your OpenWeatherMap API key"


PHONE_NUMBER = "Target phone number"

def get_weather_report(city="Hyderabad"):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            return f"❌ Error fetching weather: {data['message']}"

        temperature = data["main"]["temp"]
        condition = data["weather"][0]["description"].title()
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        weather_report = (
            f" Weather Update for {city}\n"
            f" Temperature: {temperature}°C\n"
            f" Condition: {condition}\n"
            f" Humidity: {humidity}%\n"
            f" Wind Speed: {wind_speed} m/s"
        )
        return weather_report
    except Exception as e:
        return f"❌ Could not fetch weather: {str(e)}"

def send_weather_update():
    weather = get_weather_report("Hyderabad")


    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute + 2  

    if minute >= 60:
        minute -= 60
        hour += 1
        if hour >= 24:
            hour = 0

    print(f"[Scheduling] Sending weather at {hour:02d}:{minute:02d}")
    try:
        pywhatkit.sendwhatmsg(PHONE_NUMBER, message, hour, minute, wait_time=10, tab_close=True)
        print("✅ Weather report scheduled!")
    except Exception as e:
        print(f"❌ Failed to schedule message: {str(e)}")

# Run once immediately
send_weather_update()

schedule.every().hour.at(":00").do(send_weather_update)

print("📡 Running hourly weather updates...")
while True:
    schedule.run_pending()
    time.sleep(60)
