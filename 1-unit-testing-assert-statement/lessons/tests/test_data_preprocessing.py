from data_utils import prepare_data
from pytest import approx

"""
(17379, 17)
['winter', 'spring', 'summer', 'fall']
 [2011, 2012]
 ['Saturday',
                                                 'Sunday',
                                                 'Monday',
                                                 'Tuesday',
                                                 'Wednesday',
                                                 'Thursday',
                                                 'Friday']
                                                 
['clear', 'cloudy', 'light_rain_snow', 'heavy_rain_snow']

    
"""
data = prepare_data()


def test_dim():
    assert data.shape == (17379, 17)


def test_season():
    assert data["season"].unique().tolist() == [
        'winter', 'spring', 'summer', 'fall']


def test_yr():
    assert data["yr"].unique().tolist() == [2011, 2012]


def test_weekday():
    assert data["weekday"].unique().tolist() == ['Saturday',
                                                 'Sunday',
                                                 'Monday',
                                                 'Tuesday',
                                                 'Wednesday',
                                                 'Thursday',
                                                 'Friday']


def test_weathersit():
    assert data["weathersit"].unique().tolist() == ['clear', 'cloudy',
                                                    'light_rain_snow', 'heavy_rain_snow']


def test_humdity():
    assert data["hum"].min() == 0.0
    assert data["hum"].max() == 100.0


def test_windspeed():
    assert data["windspeed"].min() == 0.0
    assert data["windspeed"].max() == approx(56.9, rel=0.1)
