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


def test_last_hour_weekly_forecast_functionality():
    response = requests.get(f'{base_url}/last-hour-weekly-forecast',
                            params={'test': True}).json()
    correct = {'rome': [{'t_2m': 22.2, 'absolute_humidity_2m': 19.1, 'dew_point_2m': 21.8, 'date': '2022-09-15T23:00:00+00:00', 'since': '2022-09-15T23:00:00+00:00'}, {'t_2m': 22.8, 'absolute_humidity_2m': 16.2, 'dew_point_2m': 19.1, 'date': '2022-09-16T23:00:00+00:00', 'since': '2022-09-16T23:00:00+00:00'}]}
    assert response == correct
    print('Test Passed')


# test_latest_weekly_forecast()
# test_last_hour_weekly_forecast()
# test_average_of_last_3_forecasts()
# test_top_n_locations_of_each_metric(2)
test_last_hour_weekly_forecast_functionality()
