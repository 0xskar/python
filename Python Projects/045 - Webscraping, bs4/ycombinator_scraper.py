import requests
from bs4 import BeautifulSoup
import re

r = requests.get("https://news.ycombinator.com/")
site = BeautifulSoup(r.text, "html.parser")
print(f"{site.title.string}\n")

# get title and links from class titleline
titles = site.find_all(class_="titleline")
article_links = [title.a.get("href") for title in titles]
article_titles = [title.a.getText() for title in titles]

# get score from class score
scores = site.find_all(class_="score")
article_scores = [score.getText() for score in scores]
article_scores = [int(re.search(r'\d+', score).group()) for score in article_scores]
num_articles = len(article_scores)

ordered_list_dict = []

# sort the lists highest to lowest
while num_articles > 0 and len(article_scores) > 0:
    for num in range(num_articles):
        # find highest article score then remove from list and add to ordered_list_dict
        max_num = max(article_scores)
        item_index = article_scores.index(max_num)
        title, link, score = article_titles[item_index], article_links[item_index], article_scores[item_index]
        dict_append = {
            "score": score,
            "title": title,
            "link": link
        }
        ordered_list_dict.append(dict_append)
        article_scores.pop(item_index), article_links.pop(item_index), article_titles.pop(item_index)

for article in ordered_list_dict:
    print(f"Score: {article['score']} - Article: {article['title']} - {article['link']}")

