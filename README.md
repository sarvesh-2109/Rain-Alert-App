# Rain Alert App

## Overview

This Rain Alert App is a simple Python application designed to check the weather forecast for your location and send an email alert if rain is expected. It utilizes the OpenWeatherMap API to get weather data and SMTP protocol for sending email notifications.

## Output


https://github.com/sarvesh-2109/Rain-Alert-App/assets/113255836/33eff785-1a14-4954-b96f-2b2f255e2127



## Features

- Fetches weather data from OpenWeatherMap API.
- Checks for rain in the forecast.
- Sends an email alert if rain is expected.

## Prerequisites

- Python 3
- A free OpenWeatherMap API key.
- An email account with SMTP access.

## Installation and Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/rain-alert-app.git
   ```
2. Install required Python packages:
   ```bash
   pip install requests
   ```
3. Obtain an API key from [OpenWeatherMap](https://openweathermap.org/api).
4. Set up an email account that will be used to send the alerts. If you're using Gmail, you'll need to generate an App Password.

## Configuration

1. Open the Python script (`main.py`).
2. Replace the `API_KEY` variable with your OpenWeatherMap API key.
3. Set the `MY_EMAIL` variable to your email address.
4. Set the `PASSWORD` variable to your email password or App Password (for Gmail).
5. Adjust the `weather_params` dictionary for your location by setting the correct latitude (`lat`) and longitude (`lon`).

## Usage

Run the script:

```bash
python main.py
```

If rain is forecasted in your location within the next few hours, you'll receive an email alert.

## Security Note

This application uses SMTP to send emails and requires your email credentials. Ensure you understand the risks and never share your credentials or API keys publicly. It's recommended to use environment variables or other secure methods for handling sensitive information.

## Contribution

Feel free to fork the project, make improvements, or suggest changes. Contributions are welcome!

## Disclaimer

This project is for educational purposes. Please use responsibly.


