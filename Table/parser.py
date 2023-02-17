import requests
from bs4 import BeautifulSoup
import pprint
import pandas as pd
import os
import datetime

class Parser:

    def __init__(self):

        self.page_url = "https://fbref.com/en/comps/9/Premier-League-Stats"

    def get_data(self):

        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}

        page = requests.get(self.page_url, headers=headers)

        html_doc = page.text

        soup1 = BeautifulSoup(html_doc, 'html.parser')
        soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')

        title = soup2.title.get_text()
        title = title.strip()

        table = soup2.find("table", attrs={'id': "results2022-202391_overall"})
        rows = table.find_all('tr')

        table_data = []
        

        for row in rows:
            cols = row.find_all('td')
            cols = [element.text.strip() for element in cols]
            table_data.append(cols)

        table_data = table_data[1:]

        list_of_dict = []

        for row in table_data:
            premier_league_data = {}
            premier_league_data['Club'] = row[0]
            premier_league_data['Played'] = row[1]
            premier_league_data['Wins'] = row[2]
            premier_league_data['Draws'] = row[3]
            premier_league_data['Loses'] = row[4]
            premier_league_data['Goals Scored'] = row[5]
            premier_league_data['Goals Against'] = row[6]
            premier_league_data['Goals Difference'] = row[7]
            premier_league_data['Points'] = row[8]
            premier_league_data['Expected Goals'] = row[10]
            premier_league_data['Expected Goals Against'] = row[11]
            premier_league_data['Expected Goals Difference'] = row[12]
            premier_league_data['Expected goals difference per 90 min'] = row[13]
            premier_league_data['Time'] = datetime.datetime.now()

            list_of_dict.append(premier_league_data)

        return list_of_dict

    def convert_to_df(self):
        data = self.get_data()
        dataframe = pd.DataFrame(data)

        return dataframe

    def convert_to_csv(self):
        
        data_df = self.convert_to_df()
        if not os.path.isfile('Pl_table.csv'):
            load_to_csv_file = data_df.to_csv('Pl_table.csv')
        else:
            load_to_csv_file = data_df.to_csv('Pl_table.csv', mode='a', header=False)

        return load_to_csv_file
