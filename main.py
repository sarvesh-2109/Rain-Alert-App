import requests
import smtplib

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = # Your Open Weather Map API key

MY_EMAIL = # Your Email Address
PASSWORD = # Your Email App Password

weather_params = {
    "lat": 19.17, # Your latitude
    "lon": 84.24, # Your longitude
    "appid": API_KEY,
    "cnt": 4,
}

response = requests.get(url=OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject: Weather Alert!\n\nIt is going to rain today. Don't forget to carry an umbrella."
        )
