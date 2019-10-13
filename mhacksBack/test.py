import requests
from bs4 import BeautifulSoup

url = "https://www.cnn.com/2019/10/12/us/four-dead-in-brooklyn-shooting/index.html"

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

article = soup.find("div", itemprop="articleBody")
'''
[s.extract() for s in article.findAll('div', class_="story-asset")]
[s.extract() for s in article.findAll('span', class_="exclude-from-newsgate")]
[s.extract() for s in article.findAll('cta-atoms-container-inline')]
[s.extract() for s in article.findAll('script')]
[s.extract() for s in article.findAll('div', class_="article-print-url")]
'''
print(article.get_text())

