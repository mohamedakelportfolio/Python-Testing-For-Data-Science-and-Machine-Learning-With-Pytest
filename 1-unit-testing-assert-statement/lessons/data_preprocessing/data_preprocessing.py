# imports
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# data path
data_file = "../../data/hour.csv"

# load hourly data
hourly_data = pd.read_csv(data_file)

# preview dataset
print(hourly_data.head())
# Check data format, number of missing values in the data and general statistics
# print some generic statistics about the data
print(f"Shape of data: {hourly_data.shape}")
print(
    f"Number of missing values in the data: {hourly_data.isnull().sum().sum()}")

# get statistics on the numerical columns
print(hourly_data.describe().T)

# Preprocessing temporal and weather features
# create a copy of the original data
preprocessed_data = hourly_data.copy()

# tranform seasons
seasons_mapping = {1: 'winter', 2: 'spring', 3: 'summer', 4: 'fall'}
preprocessed_data['season'] = preprocessed_data['season'].apply(
    lambda x: seasons_mapping[x])

# transform yr
yr_mapping = {0: 2011, 1: 2012}
preprocessed_data['yr'] = preprocessed_data['yr'].apply(
    lambda x: yr_mapping[x])

# transform weekday
weekday_mapping = {
    0: 'Sunday',
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thursday',
    5: 'Friday',
    6: 'Saturday'
}
preprocessed_data['weekday'] = preprocessed_data['weekday'].apply(
    lambda x: weekday_mapping[x])

# transform weathersit
weather_mapping = {1: 'clear', 2: 'cloudy',
                   3: 'light_rain_snow', 4: 'heavy_rain_snow'}
preprocessed_data['weathersit'] = preprocessed_data['weathersit'].apply(
    lambda x: weather_mapping[x])

# transorm hum and windspeed
preprocessed_data['hum'] = preprocessed_data['hum']*100
preprocessed_data['windspeed'] = preprocessed_data['windspeed']*67

# visualize preprocessed columns
cols = ['season', 'yr', 'weekday', 'weathersit', 'hum', 'windspeed']
preprocessed_data[cols].sample(10, random_state=123)
