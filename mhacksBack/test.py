import requests
from bs4 import BeautifulSoup

url = "https://www.forbes.com/sites/sergeiklebnikov/2019/10/11/top-cannabis-companies-have-lost-almost-10-billion-in-market-value-since-vaping-crisis-began/#3d433fac179a"

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

article = soup.find("div", class_="article-container")
sub = article.find("div", {"_ngcontent-c16": ""})
print(sub)

print(sub.get_text())


