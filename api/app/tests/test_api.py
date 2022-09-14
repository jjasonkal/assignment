import requests

base_url = 'http://localhost/weather'


def test_latest_weekly_forecast():
    response = requests.get(f'{base_url}/latest-weekly-forecast').json()
    print(response)


def test_last_hour_weekly_forecast():
    response = requests.get(f'{base_url}/last-hour-weekly-forecast').json()
    print(response)


def test_average_of_last_3_forecasts():
    response = requests.get(f'{base_url}/average-of-last-3-forecasts').json()
    print(response)


def test_top_n_locations_of_each_metric(n):
    response = requests.get(f'{base_url}/top-n-locations-of-each-metric',
                            params={'n': n}).json()
    print(response)


test_latest_weekly_forecast()
test_last_hour_weekly_forecast()
test_average_of_last_3_forecasts()
test_top_n_locations_of_each_metric(2)
