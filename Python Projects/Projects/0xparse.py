from urllib.request import urlopen
from bs4 import BeautifulSoup

url = input("Enter URL to parse (ex: https://0xskar.github.io): ")
extract_tag = input("Enter the tag to extract (ex: p for <p>): ")

page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")

# create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(html, 'html.parser')

# find all the tags
tag_outputs = soup.find_all(extract_tag)

# loop through the list of tags and print the text
for tag_output in tag_outputs:
    print(tag_output.get_text())