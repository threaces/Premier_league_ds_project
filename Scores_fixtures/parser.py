import requests
from bs4 import BeautifulSoup
import pprint
import os
import pandas as pd
import datetime

class Parser:

    def __init__(self):

        self.arsenal_fixture = 'https://fbref.com/en/squads/18bb7c10/2022-2023/matchlogs/all_comps/schedule/Arsenal-Scores-and-Fixtures-All-Competitions'
        self.city_fixture = 'https://fbref.com/en/squads/b8fd03ef/2022-2023/matchlogs/all_comps/schedule/Manchester-City-Scores-and-Fixtures-All-Competitions'
        self.man_united_fixture = 'https://fbref.com/en/squads/19538871/2022-2023/matchlogs/all_comps/schedule/Manchester-United-Scores-and-Fixtures-All-Competitions'
        self.newcastle_fixture = 'https://fbref.com/en/squads/b2b47a98/2022-2023/matchlogs/all_comps/schedule/Newcastle-United-Scores-and-Fixtures-All-Competitions'
        self.tottenham_fixture = 'https://fbref.com/en/squads/361ca564/2022-2023/matchlogs/all_comps/schedule/Tottenham-Hotspur-Scores-and-Fixtures-All-Competitions'
        self.brighton_fixture = 'https://fbref.com/en/squads/d07537b9/2022-2023/matchlogs/all_comps/schedule/Brighton-and-Hove-Albion-Scores-and-Fixtures-All-Competitions'
        self.brentford_fixture = 'https://fbref.com/en/squads/cd051869/2022-2023/matchlogs/all_comps/schedule/Brentford-Scores-and-Fixtures-All-Competitions'
        self.fulham_fixture = 'https://fbref.com/en/squads/fd962109/2022-2023/matchlogs/all_comps/schedule/Fulham-Scores-and-Fixtures-All-Competitions'
        self.chelsea_fixture = 'https://fbref.com/en/squads/cff3d9bb/2022-2023/matchlogs/all_comps/schedule/Chelsea-Scores-and-Fixtures-All-Competitions'
        self.liverpool_fixture = 'https://fbref.com/en/squads/822bd0ba/2022-2023/matchlogs/all_comps/schedule/Liverpool-Scores-and-Fixtures-All-Competitions'
        self.aston_villa_fixture = 'https://fbref.com/en/squads/8602292d/2022-2023/matchlogs/all_comps/schedule/Aston-Villa-Scores-and-Fixtures-All-Competitions'
        self.crystal_fixture = 'https://fbref.com/en/squads/47c64c55/2022-2023/matchlogs/all_comps/schedule/Crystal-Palace-Scores-and-Fixtures-All-Competitions'
        self.leicester_fixture = 'https://fbref.com/en/squads/a2d435b3/2022-2023/matchlogs/all_comps/schedule/Leicester-City-Scores-and-Fixtures-All-Competitions'
        self.nottingham_fixture = 'https://fbref.com/en/squads/e4a775cb/2022-2023/matchlogs/all_comps/schedule/Nottingham-Forest-Scores-and-Fixtures-All-Competitions'
        self.wolverhampton_fixture = 'https://fbref.com/en/squads/8cec06e1/2022-2023/matchlogs/all_comps/schedule/Wolverhampton-Wanderers-Scores-and-Fixtures-All-Competitions'
        self.westham_fixture = 'https://fbref.com/en/squads/7c21e445/2022-2023/matchlogs/all_comps/schedule/West-Ham-United-Scores-and-Fixtures-All-Competitions'
        self.leeds_fixture = 'https://fbref.com/en/squads/5bfb9659/2022-2023/matchlogs/all_comps/schedule/Leeds-United-Scores-and-Fixtures-All-Competitions'
        self.everton_fixture = 'https://fbref.com/en/squads/d3fd31cc/2022-2023/matchlogs/all_comps/schedule/Everton-Scores-and-Fixtures-All-Competitions'
        self.bournemouth_fixture = 'https://fbref.com/en/squads/4ba7cbea/2022-2023/matchlogs/all_comps/schedule/Bournemouth-Scores-and-Fixtures-All-Competitions'
        self.southampton_fixture = 'https://fbref.com/en/squads/33c895d4/2022-2023/matchlogs/all_comps/schedule/Southampton-Scores-and-Fixtures-All-Competitions'

        self.dict_clubs = {'Arsenal': self.arsenal_fixture,
                            'Manchester City': self.city_fixture,
                            'Manchester United': self.man_united_fixture,
                            'Newcastle United': self.newcastle_fixture,
                            'Tottenham Hotspur': self.tottenham_fixture,
                            'Brighton and Hove Albion': self.brighton_fixture,
                            'Brentford': self.brentford_fixture,
                            'Fulham': self.fulham_fixture,
                            'Chelsea': self.chelsea_fixture,
                            'Liverpool': self.liverpool_fixture,
                            'Aston Villa': self.aston_villa_fixture,
                            'Crystal Palace': self.crystal_fixture,
                            'Leicester City': self.leicester_fixture,
                            'Nottingham Forest': self.nottingham_fixture,
                            'Wolverhampton Wanderers': self.wolverhampton_fixture,
                            'West Ham United': self.westham_fixture,
                            'Leeds United': self.leeds_fixture,
                            'Everton': self.everton_fixture,
                            'Bournemouth': self.bournemouth_fixture,
                            'Southampton': self.southampton_fixture}

    def get_web_status(self, url_webstie):
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
        web_status = requests.get(url_webstie, headers=headers)
        html_doc = web_status.text
    
        return html_doc

        
    def get_data_club(self, club_name, website):

        page_content = self.get_web_status(website)

        soup1 = BeautifulSoup(page_content, 'html.parser')
        soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')

        table = soup2.find("table", attrs={'id': "matchlogs_for"})
        rows = table.find_all('tr')
        dates = table.find_all('th')

        table_data = []
        dates_list = []

        for row in rows:
            cols = row.find_all('td')
            cols = [element.text.strip() for element in cols]
            table_data.append(cols)

        for row in dates:
            date = row.find_all('a')
            date = [element.text.strip() for element in date]
            dates_list.append(date)

        dates_list = dates_list[19:]

        table_data = table_data[1:]

        full_list = list(zip(dates_list, table_data))

        list_of_games = []

        for index in range(len(full_list)):

            club_fixture = {}

            if len(full_list[index][0]) != 0:
                date = full_list[index][0][0]
                club_fixture[date] = {'Time' : full_list[index][1][0], 
                                        'Competition': full_list[index][1][1],
                                        'Round': full_list[index][1][2],
                                        'Venue': full_list[index][1][4],
                                        "Result": full_list[index][1][5],
                                        'Goals scored': full_list[index][1][6],
                                        'Goals against': full_list[index][1][7],
                                        'Opponent': full_list[index][1][8],
                                        'Expected goals': full_list[index][1][9],
                                        'Expected goals against': full_list[index][1][10],
                                        'Ball possesion': full_list[index][1][11]}
                club_fixture['Club fixture'] = club_name
                club_fixture['Date'] = date
                club_fixture['Time'] = full_list[index][1][0]
                club_fixture['Round'] = full_list[index][1][2]
                club_fixture['Venue'] = full_list[index][1][4]
                club_fixture['Result'] = full_list[index][1][5]
                club_fixture['Goals Scored'] = full_list[index][1][6]
                club_fixture['Goals Against'] = full_list[index][1][7]
                club_fixture['Opponent'] = full_list[index][1][8]
                club_fixture['Expected Goals'] = full_list[index][1][9]
                club_fixture['Expected Goals Against'] = full_list[index][1][10]
                club_fixture['Ball Possesion'] = full_list[index][1][11]
                club_fixture['Download Time'] = datetime.datetime.now()

                list_of_games.append(club_fixture)
            else:
                continue
                    
                
        return list_of_games

    def get_data(self):
        
        list_club_fixture = []

        for item in self.dict_clubs.keys():
            list_club_fixture.append(self.get_data_club(item, self.dict_clubs[item]))

        return list_club_fixture

    def convert_to_df(self):
        list_of_df = []

        for item in self.dict_clubs.keys():
            data = self.get_data_club(item, self.dict_clubs[item])
            dataframe = pd.DataFrame(data)
            list_of_df.append(dataframe)

        final_df = pd.concat(list_of_df, ignore_index=True)

        return final_df

    def convert_to_csv(self):
        
        data_df = self.convert_to_df()
        if not os.path.isfile('Fixtures.csv'):
            load_to_csv_file = data_df.to_csv('Fixtures.csv')
        else:
            load_to_csv_file = data_df.to_csv('Fixtures.csv', mode='a', header=False)

        return load_to_csv_file
