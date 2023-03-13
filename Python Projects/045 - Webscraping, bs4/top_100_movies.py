import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

r = requests.get(URL)
site = BeautifulSoup(r.text, "html.parser")
print(f"{site.title.string}")

movies = site.find_all("h3", class_="title")
original_titles = [title.getText() for title in movies]
title_list = []
for item in original_titles:
    parts = item.split(") ")

    # check if : exists in parts
    for i, part in enumerate(parts):
        if ":" in part and i != 1:
            new_part = part.split(": ")
            parts[i] = new_part[0]
            parts.insert(i+1, new_part[1])

    title = parts
    title_list.append(title)

reversed_titles = title_list[::-1]

with open("movies.txt", "w", encoding="utf-8") as file:
    file.write("TOP 100 MOVIE LIST\n=================\n")
    for title in reversed_titles:
        file.write(f"{title[0]}) {title[1]}\n")
    file.close()

