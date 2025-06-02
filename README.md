#  Weather WhatsApp Notification Bot

This Python script automatically sends hourly weather updates for Hyderabad via WhatsApp using the **pywhatkit** module and OpenWeatherMap API.

---

##  Features

-  Real-time weather updates for Hyderabad
- Sends WhatsApp messages **every hour**
- Customizable message text
-  Automatically handles scheduling and formatting

---

##  Requirements

- Python 3.8 to 3.11 (64-bit)
- WhatsApp Web login (must be logged in on your default browser)
- Internet connection

---

## Python Dependencies

Install the required Python packages using:

```bash
pip install pywhatkit requests schedule
```

# Setup

Get OpenWeatherMap API Key
Sign up at https://openweathermap.org/ and get your free API key.

Update the script with your information:

Replace API_KEY with your OpenWeatherMap API key.

Replace PHONE_NUMBER with your WhatsApp number (e.g., +919XXXXXXXXX).

Change city from "Hyderabad" if desired.
