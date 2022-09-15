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
    correct = {'athens': [], 'rome': [
        {'t_2m': 22.2, 'absolute_humidity_2m': 19.1, 'dew_point_2m': 21.8, 'date': '2099-09-15T23:00:00+00:00',
         'since': '2099-09-15T14:01:53.301000+00:00'},
        {'t_2m': 22.8, 'absolute_humidity_2m': 16.2, 'dew_point_2m': 19.1, 'date': '2099-09-16T23:00:00+00:00',
         'since': '2099-09-15T14:01:53.301000+00:00'}]}
    assert response == correct
    print('Test Passed')


def test_average_of_last_3_forecasts_functionality():
    response = requests.get(f'{base_url}/average-of-last-3-forecasts',
                            params={'test': True}).json()
    correct = {'athens': [],
               'rome': [{'t_2m': 22.1, 'absolute_humidity_2m': 13.7, 'dew_point_2m': 16.5,
                         'date': '2099-09-15T03:00:00+00:00'},
                        {'t_2m': 22.7, 'absolute_humidity_2m': 12.9, 'dew_point_2m': 15.5,
                         'date': '2099-09-15T04:00:00+00:00'},
                        {'t_2m': 22.8, 'absolute_humidity_2m': 12.7, 'dew_point_2m': 15.3,
                         'date': '2099-09-15T05:00:00+00:00'},
                        {'t_2m': 20.9, 'absolute_humidity_2m': 15.1, 'dew_point_2m': 17.9,
                         'date': '2099-09-15T06:00:00+00:00'},
                        {'t_2m': 20.3, 'absolute_humidity_2m': 15.0, 'dew_point_2m': 17.8,
                         'date': '2099-09-15T07:00:00+00:00'},
                        {'t_2m': 20.0, 'absolute_humidity_2m': 15.0, 'dew_point_2m': 17.7,
                         'date': '2099-09-15T08:00:00+00:00'},
                        {'t_2m': 20.9, 'absolute_humidity_2m': 14.7, 'dew_point_2m': 17.5,
                         'date': '2099-09-15T09:00:00+00:00'},
                        {'t_2m': 22.2, 'absolute_humidity_2m': 15.3, 'dew_point_2m': 18.2,
                         'date': '2099-09-15T10:00:00+00:00'},
                        {'t_2m': 24.5, 'absolute_humidity_2m': 16.1, 'dew_point_2m': 19.1,
                         'date': '2099-09-15T11:00:00+00:00'},
                        {'t_2m': 25.8, 'absolute_humidity_2m': 16.9, 'dew_point_2m': 19.9,
                         'date': '2099-09-15T12:00:00+00:00'},
                        {'t_2m': 25.6, 'absolute_humidity_2m': 16.7, 'dew_point_2m': 19.8,
                         'date': '2099-09-15T13:00:00+00:00'},
                        {'t_2m': 27.5, 'absolute_humidity_2m': 17.9, 'dew_point_2m': 21.0,
                         'date': '2099-09-15T14:00:00+00:00'},
                        {'t_2m': 27.7, 'absolute_humidity_2m': 18.0, 'dew_point_2m': 21.1,
                         'date': '2099-09-15T15:00:00+00:00'},
                        {'t_2m': 27.9, 'absolute_humidity_2m': 18.2, 'dew_point_2m': 21.3,
                         'date': '2099-09-15T16:00:00+00:00'},
                        {'t_2m': 27.6, 'absolute_humidity_2m': 18.2, 'dew_point_2m': 21.2,
                         'date': '2099-09-15T17:00:00+00:00'},
                        {'t_2m': 26.7, 'absolute_humidity_2m': 18.7, 'dew_point_2m': 21.7,
                         'date': '2099-09-15T18:00:00+00:00'},
                        {'t_2m': 26.3, 'absolute_humidity_2m': 19.5, 'dew_point_2m': 22.3,
                         'date': '2099-09-15T19:00:00+00:00'},
                        {'t_2m': 25.1, 'absolute_humidity_2m': 19.4, 'dew_point_2m': 22.1,
                         'date': '2099-09-15T20:00:00+00:00'},
                        {'t_2m': 23.0, 'absolute_humidity_2m': 19.1, 'dew_point_2m': 21.8,
                         'date': '2099-09-15T21:00:00+00:00'},
                        {'t_2m': 23.0, 'absolute_humidity_2m': 19.4, 'dew_point_2m': 22.1,
                         'date': '2099-09-15T22:00:00+00:00'},
                        {'t_2m': 22.2, 'absolute_humidity_2m': 19.1, 'dew_point_2m': 21.8,
                         'date': '2099-09-15T23:00:00+00:00'},
                        {'t_2m': 21.4, 'absolute_humidity_2m': 18.2, 'dew_point_2m': 20.9,
                         'date': '2099-09-16T00:00:00+00:00'},
                        {'t_2m': 19.6, 'absolute_humidity_2m': 16.4, 'dew_point_2m': 19.1,
                         'date': '2099-09-16T01:00:00+00:00'},
                        {'t_2m': 19.1, 'absolute_humidity_2m': 16.2, 'dew_point_2m': 18.9,
                         'date': '2099-09-16T02:00:00+00:00'},
                        {'t_2m': 20.8, 'absolute_humidity_2m': 15.8, 'dew_point_2m': 18.6,
                         'date': '2099-09-16T03:00:00+00:00'},
                        {'t_2m': 20.7, 'absolute_humidity_2m': 15.4, 'dew_point_2m': 18.2,
                         'date': '2099-09-16T04:00:00+00:00'},
                        {'t_2m': 20.0, 'absolute_humidity_2m': 15.8, 'dew_point_2m': 18.6,
                         'date': '2099-09-16T05:00:00+00:00'},
                        {'t_2m': 19.6, 'absolute_humidity_2m': 15.8, 'dew_point_2m': 18.6,
                         'date': '2099-09-16T06:00:00+00:00'},
                        {'t_2m': 19.5, 'absolute_humidity_2m': 15.7, 'dew_point_2m': 18.4,
                         'date': '2099-09-16T07:00:00+00:00'},
                        {'t_2m': 20.0, 'absolute_humidity_2m': 15.3, 'dew_point_2m': 18.0,
                         'date': '2099-09-16T08:00:00+00:00'},
                        {'t_2m': 21.4, 'absolute_humidity_2m': 15.7, 'dew_point_2m': 18.5,
                         'date': '2099-09-16T09:00:00+00:00'},
                        {'t_2m': 23.6, 'absolute_humidity_2m': 16.1, 'dew_point_2m': 19.1,
                         'date': '2099-09-16T10:00:00+00:00'},
                        {'t_2m': 25.1, 'absolute_humidity_2m': 16.3, 'dew_point_2m': 19.3,
                         'date': '2099-09-16T11:00:00+00:00'},
                        {'t_2m': 26.1, 'absolute_humidity_2m': 17.0, 'dew_point_2m': 20.0,
                         'date': '2099-09-16T12:00:00+00:00'},
                        {'t_2m': 27.2, 'absolute_humidity_2m': 16.4, 'dew_point_2m': 19.6,
                         'date': '2099-09-16T13:00:00+00:00'},
                        {'t_2m': 28.1, 'absolute_humidity_2m': 15.6, 'dew_point_2m': 18.8,
                         'date': '2099-09-16T14:00:00+00:00'},
                        {'t_2m': 27.9, 'absolute_humidity_2m': 15.5, 'dew_point_2m': 18.7,
                         'date': '2099-09-16T15:00:00+00:00'},
                        {'t_2m': 27.5, 'absolute_humidity_2m': 15.9, 'dew_point_2m': 19.1,
                         'date': '2099-09-16T16:00:00+00:00'},
                        {'t_2m': 27.1, 'absolute_humidity_2m': 15.5, 'dew_point_2m': 18.6,
                         'date': '2099-09-16T17:00:00+00:00'},
                        {'t_2m': 26.6, 'absolute_humidity_2m': 15.9, 'dew_point_2m': 19.0,
                         'date': '2099-09-16T18:00:00+00:00'},
                        {'t_2m': 25.7, 'absolute_humidity_2m': 16.2, 'dew_point_2m': 19.3,
                         'date': '2099-09-16T19:00:00+00:00'},
                        {'t_2m': 24.3, 'absolute_humidity_2m': 16.3, 'dew_point_2m': 19.3,
                         'date': '2099-09-16T20:00:00+00:00'},
                        {'t_2m': 22.9, 'absolute_humidity_2m': 16.4, 'dew_point_2m': 19.3,
                         'date': '2099-09-16T21:00:00+00:00'},
                        {'t_2m': 22.8, 'absolute_humidity_2m': 16.2, 'dew_point_2m': 19.1,
                         'date': '2099-09-16T22:00:00+00:00'},
                        {'t_2m': 22.8, 'absolute_humidity_2m': 16.2, 'dew_point_2m': 19.1,
                         'date': '2099-09-16T23:00:00+00:00'}]}
    assert response == correct
    print('Test Passed')


def test_top_n_locations_of_each_metric_functionality():
    response = requests.get(f'{base_url}/top-n-locations-of-each-metric',
                            params={'n': 1, 'test': True}).json()
    correct = {'t_2m': [{'name': 'rome', 'maximum': 28.1}], 'absolute_humidity_2m': [{'name': 'rome', 'maximum': 19.5}],
               'dew_point_2m': [{'name': 'rome', 'maximum': 22.3}]}
    assert response == correct
    print('Test Passed')


test_latest_weekly_forecast()
test_last_hour_weekly_forecast()
test_average_of_last_3_forecasts()
test_top_n_locations_of_each_metric(2)
test_last_hour_weekly_forecast_functionality()
test_average_of_last_3_forecasts_functionality()
test_top_n_locations_of_each_metric_functionality()
