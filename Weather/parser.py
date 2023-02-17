import requests
import json
import pprint
import sqlite3
import pandas as pd
import datetime
import os

class Parser:

    def __init__(self):

        self.api_key = 'e34df5c0b3e62f3832c2d9d4bf1797d4'

        self.list_of_cities = ['London', 'Manchester', 'Liverpool', 'Leeds', 'Leicester', 'Newcastle upon Tyne', 'Birmingham', 
                    'Wolverhampton', 'Nottingham', 'Leicester', 'Brighton', 'Southampton', 'Bournemouth']

    def get_coordinates(self, key_for_api, city_name):
        city_name = city_name.title()

        url = f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=5&appid={key_for_api}'

        response = requests.get(url)

        x = response.json()
  
        return (x[0]['lat'], x[0]['lon'])

    def get_dict_coordinates(self):

        dict_of_coordinates = {}

        for item in self.list_of_cities:
            city = self.get_coordinates(self.api_key, item)

            dict_of_coordinates[item] = {'lat': city[0], 'lon': city[1]}

        return dict_of_coordinates

    def weather_description(self, key_for_api, lat, lon):
        url_weather = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key_for_api}'

        response_weather = requests.get(url_weather)

        weather_json = response_weather.json()
        list_of_weather_param = [weather_json['main']['temp'], weather_json['main']['pressure'], weather_json['main']['humidity'], weather_json['wind']['speed'], weather_json['wind']['deg']]

        return list_of_weather_param

    def get_data(self):
        list_of_dicts = []
        

        for item in self.list_of_cities:
            lat = self.get_dict_coordinates()[item]['lat']
            lon = self.get_dict_coordinates()[item]['lon']

            weather_info = self.weather_description(self.api_key, lat, lon)

            dict_of_weather_info = {}
            #dict_of_weather_info[item] = {'Temperature': weather_info[0], 'Pressure': weather_info[1], 'Humidity': weather_info[2], 'Wind speed': weather_info[3], 'Wind deg': weather_info[4], 'Time': }
            dict_of_weather_info['City'] = item
            dict_of_weather_info['Temperature'] = weather_info[0]
            dict_of_weather_info['Pressure'] = weather_info[1]
            dict_of_weather_info['Humidity'] = weather_info[2]
            dict_of_weather_info['Wind speed'] = weather_info[3]
            dict_of_weather_info['Wind deg'] = weather_info[4]
            dict_of_weather_info['Time'] = datetime.datetime.now()

            list_of_dicts.append(dict_of_weather_info)

        return list_of_dicts


    def convert_to_df(self):
        data = self.get_data()
        dataframe = pd.DataFrame(data)

        return dataframe

    def convert_to_csv(self):
        
        data_df = self.convert_to_df()
        if not os.path.isfile('weather_data.csv'):
            load_to_csv_file = data_df.to_csv('weather_data.csv')
        else:
            load_to_csv_file = data_df.to_csv('weather_data.csv', mode='a', header=False)

        return load_to_csv_file
