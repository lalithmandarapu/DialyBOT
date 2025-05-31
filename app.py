
from flask import Flask
from twilio.rest import Client
import schedule, time, threading
from weather_service import get_location_from_number, get_weather
from config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_WHATSAPP_NUMBER

app = Flask(__name__)
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

numbers = ["whatsapp:+91987654321"]  # YOUR verified number

daily_log = {number: [] for number in numbers}

# 🕒 Daily Routine
daily_schedule = [
    ("06:00", "🚶 Time to go for a morning walk!"),
    ("09:00", "🍳 Time for breakfast!"),
    ("13:00", "🍱 It's lunch time!"),
    ("17:00", "☕ Enjoy your evening snacks!"),
    ("18:00", "🚶 Time for evening walk!"),
    ("20:00", "🍽️ Dinner time!"),
    ("22:00", "😴 Time to sleep. Good night!"),
]

def send_whatsapp_message(number, body):
    message = client.messages.create(
        from_=TWILIO_WHATSAPP_NUMBER,
        to=number,
        body=body
    )
    print(f"✅ Message sent to {number}: {message.sid}")

def scheduled_task(time_label, activity_msg):
    for number in numbers:
        city = get_location_from_number(number)
        weather = get_weather(city)
        summary = weather["summary"]
        description = weather["description"]

        full_message = f"{activity_msg}\n{summary}"
        send_whatsapp_message(number, full_message)

        # 📝 Log for summary
        daily_log[number].append((time_label, activity_msg, description))

def send_summary():
    for number in numbers:
        log = daily_log[number]
        travel_safe_count = sum(
            1 for _, msg, desc in log
            if "walk" in msg.lower() and all(x not in desc for x in ["rain", "storm", "snow"])
        )
        total_walks = sum(1 for _, msg, _ in log if "walk" in msg.lower())

        travel_note = f"🚶 Walks planned: {total_walks} | Safe: {travel_safe_count}"
        summary = "\n📊 *Daily Summary:*\n" + "\n".join(
            f"{time} - {msg.split('!')[0]} ({desc})" for time, msg, desc in log
        ) + f"\n\n{travel_note}"
        
        send_whatsapp_message(number, summary)
        daily_log[number] = []

def run_scheduler():
    for time_label, activity in daily_schedule:
        schedule.every().day.at(time_label).do(scheduled_task, time_label, activity)
    schedule.every().day.at("22:30").do(send_summary)

    while True:
        schedule.run_pending()
        time.sleep(1)

@app.route("/")
def home():
    return "✅ WhatsApp Weather & Routine Bot is running."

if __name__ == "__main__":
    t = threading.Thread(target=run_scheduler)
    t.start()
    app.run(port=5000)

