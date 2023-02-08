import requests
from bs4 import BeautifulSoup
import pprint

class Parser:

    def __init__(self):

        self.page_url_london = 'https://www.google.com/search?q=londyn+wysoko%C5%9B%C4%87+nad+poziomem+morza&sxsrf=AJOqlzV3SwcSBhoyn2kDGs9Cu5qB8_93jA%3A1673795620259&ei=JBjEY7-xD4j2qwHWwYSACg&oq=londyn+wyso&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAxgBMgUIABCABDIFCAAQgAQyBggAEBYQHjIGCAAQFhAeOgoIABBHENYEELADOgcIABCwAxBDOg0IABDkAhDWBBCwAxgBOgwILhDIAxCwAxBDGAI6DwguENQCEMgDELADEEMYAjoOCC4QgAQQsQMQxwEQrwE6CwguEIAEEMcBEK8BOggIABCABBCxAzoECAAQQ0oECEEYAEoECEYYAVB1WPESYLIkaAFwAXgAgAGhAYgBrQWSAQMwLjWYAQCgAQHIARPAAQHaAQYIARABGAnaAQYIAhABGAg&sclient=gws-wiz-serp'
        self.page_url_liverpool = 'https://www.google.com/search?q=liverpool+wysoko%C5%9B%C4%87+nad+poziomem+morza&sxsrf=AJOqlzUEhYtLxc9p39YUnUKeGGxJLjrOQw%3A1673808752621&ei=cEvEY4_BJc2Exc8PlaCmMA&oq=liverpool+wysoko%C5%9B%C4%87+nad&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAxgAMgUIIRCgATIFCCEQoAEyBQghEKABMgUIIRCgAToKCAAQRxDWBBCwA0oECEEYAEoECEYYAFDBBVj2B2DAHGgBcAF4AYAB-AKIAdgGkgEHMC4xLjAuMpgBAKABAcgBCMABAQ&sclient=gws-wiz-serp'
        self.page_url_manchester = 'https://www.google.com/search?q=manchester+wysoko%C5%9B%C4%87+nad+poziomem+morza&oq=manchester+wysoko&aqs=chrome.3.69i57j33i160l4.7170j1j7&sourceid=chrome&ie=UTF-8'
        self.page_url_newcastle = 'https://www.google.com/search?q=newcastle+upon+tyne+wysoko%C5%9B%C4%87&oq=newcastle+upon+tyne+wysok&aqs=chrome.1.69i57j33i160l2.10289j1j9&sourceid=chrome&ie=UTF-8'
        self.page_url_leeds = 'https://www.google.com/search?q=leeds+height+above+sea+level&sxsrf=AJOqlzUUi5yJ8lr1WsRBjqpjxmv3qMeIGA%3A1673984994943&ei=4vvGY8qTOcr-7_UP0aewwAI&oq=leeds+hei&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAxgAMggIABCABBDLATIICAAQgAQQywEyBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeOgoIABBHENYEELADOgUIABCABDoLCC4QgAQQxwEQ0QM6DgguEIAEEMcBEK8BEMsBOggILhCABBDLAUoECEEYAEoECEYYAFCCBljOB2DuFmgBcAF4AIABqQGIAdwDkgEDMC4zmAEAoAEByAEIwAEB&sclient=gws-wiz-serp'
        self.page_url_nottingham = 'https://www.google.com/search?q=nottingham+height+above+sea+level&sxsrf=AJOqlzXSCY-NGUf9np9vdE4X0tz7gmafrw%3A1673985128934&ei=aPzGY5PJOOfn7_UPgbCL-AU&oq=nott+height+above+sea+level&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAxgAMgYIABAHEB46CAgAEAcQHhAPSgQIQRgASgQIRhgAUABYlgRgtg1oAHAAeACAAbwBiAH0BJIBAzAuNJgBAKABAcABAQ&sclient=gws-wiz-serp'
        self.pager_url_leicester = 'https://www.google.com/search?q=leicester+height+above+sea+level&sxsrf=AJOqlzVzIb3aHN0OW07tVdGlqUcCI5mE4A%3A1673985853333&ei=Pf_GY82BFJXxkgXyxoHYAw&oq=leicester+heig&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAxgBMggIABCABBDLATIICAAQgAQQywEyCAgAEIAEEMsBMggIABCABBDLATIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjoNCC4QxwEQ0QMQ6gIQJzoHCCMQ6gIQJzoHCC4Q6gIQJzoGCCMQJxATOgQIIxAnOgsILhCABBDHARDRAzoFCAAQgAQ6BQguEIAEOgQIABBDOgQILhBDOggILhCABBDUAjoICC4QgAQQywE6CwguEIAEENQCEMsBOg4ILhCABBDHARCvARDLAToOCC4QgAQQxwEQ0QMQywFKBAhBGABKBAhGGABQiQdY4zxg90ZoAHAAeACAAd0EiAHxD5IBCTAuNy4yLjUtMZgBAKABAbABCsABAQ&sclient=gws-wiz-serp'
        self.page_url_birmingham = 'https://www.google.com/search?q=birmingham+uk+height+above+sea+level&sxsrf=AJOqlzXi47kWb9uu3FTnXOniC0WqXQAyQA%3A1674291175316&ei=56fLY8jtEo-XsAeE4o-IBg&oq=bir+height+above+sea+level&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAxgAMgYIABAHEB4yCAgAEAcQHhAPMgYIABAHEB46CAgAEAcQHhAKSgQIQRgASgQIRhgAUABYtgJgsRhoAHAAeACAAcgBiAGnA5IBBTAuMi4xmAEAoAEBwAEB&sclient=gws-wiz-serp'
        self.page_url_wolverhampton = 'https://www.google.com/search?q=wolverhampton+uk+height+above+sea+level&sxsrf=AJOqlzXNPIi8kPxnHKCWn1lvt7er3MnRlg%3A1674291973338&ei=BavLY-6mFIyBi-gP7_6Z6AQ&ved=0ahUKEwiuvcjSp9j8AhWMwAIHHW9_Bk0Q4dUDCA8&uact=5&oq=wolverhampton+uk+height+above+sea+level&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzoKCAAQRxDWBBCwAzoFCAAQogRKBAhBGABKBAhGGABQnwRY8h1grx9oAXABeACAAagCiAHOEpIBBTAuOC41mAEAoAEByAEGwAEB&sclient=gws-wiz-serp'
        self.page_url_brighton = 'https://www.google.com/search?q=brighton+uk+height+above+sea+level&sxsrf=AJOqlzWkpwm-6fhwXFwwnC9xBfRmTOITrw%3A1674292584038&ei=aK3LY8uAAovmsAel2rCAAQ&oq=bri+uk+height+above+sea+level&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQARgAMggIIRCgARDDBDoGCAAQBxAeSgQIQRgASgQIRhgAUABY_wdg4RRoAHABeACAAbwDiAHACpIBBzItMi4xLjGYAQCgAQHAAQE&sclient=gws-wiz-serp'
        self.page_url_southampton = 'https://www.google.com/search?q=southampton+uk+height+above+sea+level&sxsrf=AJOqlzVQNnqk_bTwlXdMlSo2H3oLti6Fnw%3A1674293201994&ei=0a_LY8alPJPBlAat54WgBw&oq=south+uk+height+above+sea+level&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAxgAMggIIRCgARDDBEoECEEYAUoECEYYAFDNBFilCmDaEWgBcAB4AIABswGIAa0FkgEDMC41mAEAoAEBwAEB&sclient=gws-wiz-serp'


    def get_web_status(self, url_webstie):
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
        web_status = requests.get(url_webstie, headers=headers)
    
        return web_status

    def website_content(self, status_web):
        soup1 = BeautifulSoup(status_web.content, 'html.parser')
        soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')

        return soup2

    def scrapper_city_name(self, content_of_webside, class_name):
    
        city_name = content_of_webside.find(class_=class_name).get_text()
        city_name = city_name.strip()

        return city_name

    def scrapper_city_height(self, content_of_webside, class_name):
    
        height = content_of_webside.find(class_=class_name).get_text()
        height = height.strip()

        return height

    def get_data(self):
        
        london = self.scrapper_city_name(self.website_content(self.get_web_status(self.page_url_london)), "SPZz6b")
        london = london[0:6]

        liverpool = self.scrapper_city_name(self.website_content(self.get_web_status(self.page_url_liverpool)), "VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc lEBKkf")
        liverpool = liverpool[234:243]

        manchester = self.scrapper_city_name(self.website_content(self.get_web_status(self.page_url_manchester)), "GzssTd")

        newcastle = self.scrapper_city_name(self.website_content(self.get_web_status(self.page_url_newcastle)), "VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc lEBKkf")
        newcastle = newcastle.replace('\n', '')
        newcastle = newcastle.strip()
        newcastle = newcastle[144:163]

        leeds = self.scrapper_city_name(self.website_content(self.get_web_status(self.page_url_leeds)), "VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc lEBKkf")
        leeds = leeds.strip()
        leeds = leeds.replace('\n', '')
        leeds = leeds[92:97]

        nottingham = self.scrapper_city_name(self.website_content(self.get_web_status(self.page_url_nottingham)), "GzssTd")

        leicester = self.scrapper_city_name(self.website_content(self.get_web_status(self.pager_url_leicester)), "GzssTd")

        birmingham = self.scrapper_city_name(self.website_content(self.get_web_status(self.page_url_birmingham)), "GzssTd")

        wolverhampton = self.scrapper_city_name(self.website_content(self.get_web_status(self.page_url_wolverhampton)), "GzssTd")

        brighton = self.scrapper_city_name(self.website_content(self.get_web_status(self.page_url_brighton)), "VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc lEBKkf")
        brighton = brighton.strip()
        brighton = brighton.replace('\n', '')
        brighton = brighton[:8]

        southampton = self.scrapper_city_name(self.website_content(self.get_web_status(self.page_url_southampton)), "VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc lEBKkf")
        southampton = southampton[40:51]

        london_height = self.scrapper_city_height(self.website_content(self.get_web_status(self.page_url_london)),"wHYlTd z8gr9e")
        london_height = london_height[0:2]
        #london_height = int(london_height)

        liverpool_height = self.scrapper_city_height(self.website_content(self.get_web_status(self.page_url_liverpool)), "VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc lEBKkf")
        liverpool_height = liverpool_height.replace('\n', '')
        liverpool_height = liverpool_height[150:153]
        #liverpool_height = int(liverpool_height)

        manchester_height = self.scrapper_city_height(self.website_content(self.get_web_status(self.page_url_manchester)), "VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc lEBKkf")
        manchester_height = manchester_height[150:152]
        #manchester_height = int(manchester_height)

        leeds_height = self.scrapper_city_height(self.website_content(self.get_web_status(self.page_url_leeds)), "hgKElc")
        leeds_height = leeds_height[137:139]
        #leeds_height = int(leeds_height)

        nottingham_height = self.scrapper_city_height(self.website_content(self.get_web_status(self.page_url_nottingham)), "VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc lEBKkf")
        nottingham_height = nottingham_height.replace('\n', '')
        nottingham_height = nottingham_height.strip()
        nottingham_height = nottingham_height[125:127]
        #nottingham_height = int(nottingham_height)

        leicester_height = self.scrapper_city_height(self.website_content(self.get_web_status(self.pager_url_leicester)), "Z0LcW t2b5Cf CfV8xf")
        leicester_height = leicester_height.replace("′", "")
        leicester_height = leicester_height[:2]
        #leicester_height = int(leicester_height)

        birmingham_height = self.scrapper_city_height(self.website_content(self.get_web_status(self.page_url_birmingham)), "Z0LcW t2b5Cf CfV8xf")
        birmingham_height = birmingham_height.replace("′", "")
        birmingham_height = birmingham_height[:3]
        #birmingham_height = int(birmingham_height)

        wolverhampton_height = self.scrapper_city_height(self.website_content(self.get_web_status(self.page_url_wolverhampton)), "Z0LcW t2b5Cf CfV8xf")
        wolverhampton_height = wolverhampton_height.replace("′", "")
        wolverhampton_height = wolverhampton_height[:3]
        #wolverhampton_height = int(wolverhampton_height)

        dictionary_with_info = {}

        dictionary_with_info[london] = london_height
        dictionary_with_info[liverpool] = liverpool_height
        dictionary_with_info[manchester] = manchester_height
        dictionary_with_info[newcastle] = 30
        dictionary_with_info[leeds] = leeds_height
        dictionary_with_info[nottingham] = nottingham_height
        dictionary_with_info[leicester] = leicester_height
        dictionary_with_info[birmingham] = birmingham_height
        dictionary_with_info[wolverhampton] = wolverhampton_height
        dictionary_with_info[brighton] = 10
        dictionary_with_info[southampton] = 21

        return dictionary_with_info

object_dict = Parser()
print(object_dict.get_data())