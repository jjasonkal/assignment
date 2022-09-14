import requests
from requests.auth import HTTPBasicAuth
from geopy.geocoders import Nominatim
from decouple import config

from fill_table import fill_table_with_content


def forecasts(latitude, longitude):
    # complete url address
    complete_url = f'{base_url}/{seven_days_forecasts}/{parameters}/{latitude},{longitude}/{output_format}'

    # get method of requests module
    response = requests.get(complete_url, auth=HTTPBasicAuth(username, password))

    # json method of response object
    try:
        x = response.json()
        if x['status'] == 'OK':
            return x['data']
        else:
            print(" City Not Found ")
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)


if __name__ == '__main__':
    # get local variables from .env
    username = config('API_USERNAME')
    password = config('API_PASSWORD')

    # base_url variable to store url
    base_url = "https://api.meteomatics.com"

    # seven days time points
    seven_days_forecasts = 'todayT00:00:00ZPT167H:PT1H'

    # describes the temperature 2 meters above ground (Celsius)
    temperature = 't_2m:C'
    # describes the absolute humidity 2 meters above ground (gm3)
    humidity = 'absolute_humidity_2m:gm3'
    # describes the instantaneous value of the dew point temperature 2 meters above ground (Celsius)
    dew_point = 'dew_point_2m:C'
    parameters = f'{temperature},{humidity},{dew_point}'

    # api output
    output_format = 'json'

    for iteration in range(3):
        invalid_city = True
        while invalid_city:
            # user input
            city_name = input(f'Enter city name number {iteration+1} : ')

            # find the latitude and longitude of the cities
            geolocator = Nominatim(user_agent="user")

            # try valid city name
            try:
                location = geolocator.geocode(city_name)
                lat = str(location.latitude)
                lon = str(location.longitude)
                fill_table_with_content(city_name.lower(), forecasts(lat, lon))
                print(f'New forecasts stored for {city_name.lower()}')
                invalid_city = False
            except AttributeError as e:
                print('\nEnter a valid city name!')



