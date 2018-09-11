import json
import requests
from requests import RequestException


def get_current_forecast(location):
    """Get current forecast data.

    Given a latitude and longitude, fetches the current weather forecast from Weather.gov API
    Args:
        location (str): a latitude and longitude point seperated by a comma (e.g. 42.02,-93.65)
    Returns:
        A description of the current weather forecast or "Error" if error occurs
    """
    # Download the JSON data for the Point from Weather.gov API
    url = 'https://api.weather.gov/points/%s' % location
    try:
        response = requests.get(url)
    except RequestException:
        return "Error"

    # Load Point JSON data
    weather_data = json.loads(response.text)

    # Extract the URL for the Forecast from the point JSON and download
    url = weather_data['properties']['forecast']
    try:
        response = requests.get(url)
    except RequestException:
        return "Error"

    # Load Forecast JSON data
    weather_data = json.loads(response.text)

    # Get the current forecast (today, rest of today, tonight)
    current = weather_data['properties']['periods'][0]['detailedForecast']

    return current
