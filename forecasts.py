import requests
from requests.auth import HTTPBasicAuth
from geopy.geocoders import Nominatim
from decouple import config


def forecasts(latitude, longitude):
    # complete url address
    complete_url = f'{base_url}/{seven_days_forecasts}/{parameter}/{latitude},{longitude}/{output_format}'

    # get method of requests module
    response = requests.get(complete_url, auth=HTTPBasicAuth(username, 'ZeE4e6h75P'))

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
    seven_days_forecasts = 'now+24H--now+168H:P1D'

    # describes the temperature 2 meters above ground (Celsius)
    parameter = 't_2m:C'

    # api output
    output_format = 'json'

    for iteration in range(3):
        invalid_city = True
        while invalid_city:
            # user input
            city_name = input(f'Enter city name number {iteration+1} : ')

            # find the latitude and longitude of the cities
            geolocator = Nominatim(user_agent="user_agent")

            # try valid city name
            try:
                location = geolocator.geocode(city_name)
                lat = str(location.latitude)
                lon = str(location.longitude)
                print(forecasts(lat, lon))
                invalid_city = False
            except AttributeError as e:
                print('\nEnter a valid city name!')



