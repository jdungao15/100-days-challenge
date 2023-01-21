from bs4 import BeautifulSoup
import requests
import pprint as pp


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

# response = requests.get("https://news.ycombinator.com/news")
# yc_web_page = response.text
#
#
# soup = BeautifulSoup(yc_web_page, 'html.parser')
# article= soup.select(selector=".titleline>a")
# # article_vote = soup.select(selector=".score")
#
# article_texts= []
# article_links = []
#
# for article_tag in article:
#     text = article_tag.text
#     link = article_tag['href']
#     article_texts.append(text)
#     article_links.append(link)
#
# article_upvotes = [int(score.text.split()[0]) for score in soup.select(selector='.score')]
#
#
# highest_upvote = max(article_upvotes)
# highest_upvote_index= article_upvotes.index(highest_upvote)
# highest_upvote_link = article_links[highest_upvote_index]
# highest_upvote_text = article_texts[highest_upvote_index]
#
# print(highest_upvote_text)
# print(highest_upvote_link)
# print(highest_upvote)

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
contents = response.text
soup = BeautifulSoup(contents, 'html.parser')
movies_tags = soup.select(selector="h3.title")
movies_list = []

for movie in movies_tags:
    movies_list.append(movie.text)
sorted_movies = movies_list[::-1]

with open('movies.txt', 'w', encoding="utf-8") as f:
    for movie in sorted_movies:
        f.write(movie + "\n")