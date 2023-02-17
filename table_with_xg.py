import requests
from bs4 import BeautifulSoup
import pprint
import pandas as pd

page_url = "https://fbref.com/en/comps/9/Premier-League-Stats"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}

page = requests.get(page_url, headers=headers)

html_doc = page.text

soup1 = BeautifulSoup(html_doc, 'html.parser')
soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')

title = soup2.title.get_text()
title = title.strip()

table = soup2.find("table", attrs={'id': "results2022-202391_overall"})
rows = table.find_all('tr')

table_data = []
premier_league_data = {}

for row in rows:
    cols = row.find_all('td')
    cols = [element.text.strip() for element in cols]
    table_data.append(cols)

table_data = table_data[1:]

for row in table_data:
    premier_league_data[row[0]] = {"Played": row[1],
                                    "Wins" : row[2],
                                    "Draws": row[3],
                                    "Loses": row[4],
                                    "Goals Scored": row[5],
                                    "Goals Against": row[6],
                                    "Goals Difference": row[7],
                                    "Points": row[8],
                                    "Expected Goals": row[10],
                                    "Expected goals against": row[11],
                                    "Expected goals difference": row[12],
                                    "Expected goals difference per 90 min": row[13]}

df = pd.DataFrame.from_dict(premier_league_data, orient='index')
df.to_csv('Premier_league_table', sep='\t')