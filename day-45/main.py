from bs4 import BeautifulSoup
import requests
import pprint


# with open('website.html', encoding='utf-8') as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, 'html.parser')
#
# all_anchors_tags = soup.find_all(name="a")
#
# class_is_heading = soup.find_all(class_="heading")
# print(class_is_heading)
#
# h3_heading = soup.find_all("h3", class_="heading")
# print(h3_heading)
#
# company_url = soup.select_one(selector="p a")
# print(company_url)

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')
title_list= soup.select(selector=".titleline a")
for title in title_list:
    print(title.text)

