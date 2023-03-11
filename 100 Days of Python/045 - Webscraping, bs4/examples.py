from bs4 import BeautifulSoup
import lxml

with open("website.html", encoding="utf8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "lxml")
# print(soup.title.string)
print(soup.title.name)
print(soup.prettify())
all_anchors = soup.find_all(name="a")
print(all_anchors)
all_paragraphs = soup.find_all(name="p")
print(all_paragraphs)

for tag in all_anchors:
    print(tag.getText())

for p in all_paragraphs:
    print(p.getText())

for tag in all_anchors:
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)
