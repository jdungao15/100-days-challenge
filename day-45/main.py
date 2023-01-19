from bs4 import BeautifulSoup
import pprint

with open('website.html', encoding='utf-8') as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')

all_anchors_tags = soup.find_all(name="a")
pprint.pprint(all_anchors_tags)