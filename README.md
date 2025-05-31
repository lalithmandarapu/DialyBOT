# 🌤️ WhatsApp Weather & Daily Routine Bot

This project is a Flask-based WhatsApp bot that sends weather updates and scheduled daily routine messages directly to your WhatsApp using the **Twilio API** and **OpenWeatherMap**.

---

## 📌 Features

- Sends daily routine messages (e.g., wake up, lunch, evening walk)
- Adds real-time weather updates for your city with each message
- Sends a summary of the day every night, showing which walks were safe based on weather
- Fully customizable schedule
- Built with Flask, Twilio, OpenWeather API, and Python schedule

---

## 📁 Project Structure

whatsapp-weather-bot/
├── app.py # Main application and scheduler
├── weather_service.py # Fetches city and weather info
├── config.py # API credentials
└── README.md # Project guide


---

## ⚙️ Prerequisites

- Python 3.x
- A Twilio account with WhatsApp sandbox setup
- OpenWeatherMap API key
- Flask, Requests, Twilio, and Schedule Python modules

---

## 🔧 Installation

1. **Clone the repository**
```bash
git clone https://github.com/your-username/whatsapp-weather-bot.git
cd whatsapp-weather-bot

Install dependencies
pip install flask twilio schedule requests

Verify your WhatsApp number with Twilio

Send the join code from the Twilio Console to +14155238886 from your WhatsApp

Update your number and city in the code

In app.py, set your verified WhatsApp number:
numbers = ["whatsapp:+91YOURNUMBER"]

In weather_service.py, map your number to a city:
phone_location_map = {
    "whatsapp:+91YOURNUMBER": "YourCity"
}

Running the App
python app.py

The app will start a background scheduler

Weather and routine messages will be sent automatically at specified times

Visit http://localhost:5000 to see the bot status

