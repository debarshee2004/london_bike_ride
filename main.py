# London Bike Sharing Dataset🚲

"""
# Installing Libraries
! pip install pandas
! pip install openpyxl
"""

# Importing the files
import pandas as pd

# Connecting the dataset
data = pd.read_csv("./data/london_merged.csv")

data

# explore the data
data.info()

data.shape

# count the unique values in the weather_code column
data.weather_code.value_counts()

# count the unique values in the season column
data.season.value_counts()

# specifying the column names that I want to use
new_cols_dict = {
    "timestamp": "time",
    "cnt": "count",
    "t1": "temp_real_C",
    "t2": "temp_feels_like_C",
    "hum": "humidity_percent",
    "wind_speed": "wind_speed_kph",
    "weather_code": "weather",
    "is_holiday": "is_holiday",
    "is_weekend": "is_weekend",
    "season": "season",
}

# Renaming the columns to the specified column names
data.rename(new_cols_dict, axis=1, inplace=True)

# changing the humidity values to percentage (i.e. a value between 0 and 1)
data.humidity_percent = data.humidity_percent / 100

# creating a season dictionary so that we can map the integers 0-3 to the actual written values
season_dict = {"0.0": "spring", "1.0": "summer", "2.0": "autumn", "3.0": "winter"}

# creating a weather dictionary so that we can map the integers to the actual written values
weather_dict = {
    "1.0": "Clear",
    "2.0": "Scattered clouds",
    "3.0": "Broken clouds",
    "4.0": "Cloudy",
    "7.0": "Rain",
    "10.0": "Rain with thunderstorm",
    "26.0": "Snowfall",
}

# changing the seasons column data type to string
data.season = data.season.astype("str")
# mapping the values 0-3 to the actual written seasons
data.season = data.season.map(season_dict)

# changing the weather column data type to string
data.weather = data.weather.astype("str")
# mapping the values to the actual written weathers
data.weather = data.weather.map(weather_dict)

# checking our dataframe to see if the mappings have worked
data.head()

# writing the final dataframe to an excel file that we will use in our Tableau visualizations. The file will be the 'london_bikes_final.xlsx' file and the sheet name is 'Data'
data.to_excel("london_bikes_final.xlsx", sheet_name="Data")
