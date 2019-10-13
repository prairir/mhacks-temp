from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import requests
from bs4 import BeautifulSoup
import re



def retMag():
    #search db stuff
    #
    #
    '''
    if !valIn:
        checkurl(url)
    return nlp(text)
    '''


def checkurl(url):
    print(url)
    if re.search("www\.cbc\.ca\/news\/(.*)", url) != None:
        return getText(url, 'c')
    elif re.search("www\.forbes\.com\/sites\/\w+\/(\d+\/){3}\S+",url) != None:
        return getText(url, 'f')
    elif re.search("(cnn.com\/\S+)", url) != None:
        return getText(url, 'n')
    elif re.search("www\.foxnews\.com\/\w+\/(.*)",url) != None:
        return getText(url, 'x')
    elif re.search("(www\.usatoday\.com\/story\/\w+\/\S+)", url) != None:
        return getText(url, 'u')
    elif re.search("(www\.nbcnews\.com\/\S+)", url) != None:
        return getText(url, 'b')
    else:
        return (0.0, 0.0) 

def getText(url, flag):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    
    if flag == 'f':
        article = soup.find("div", class_="article-container")
        sub = article.find("div", {"_ngcontent-c16": ""})
        return nlp(sub.get_text())
    elif flag == 'x':
        article = soup.find("div", class_="article-body")
        try: 
            [s.extract() for s in article('strong')]
            [s.extract() for s in article.findAll('div', class_="caption")]
        except:
            pass
        return nlp(article.get_text())
    elif flag == 'b':
        article = soup.find("div", class_="bodyContent___1eruQ")
        try: 
            [s.extract() for s in article.findAll('section', class_="inlineVideo___3ZAlE")]
        except:
            pass
        return nlp(article.get_text())
    elif flag == 'c':
        article = soup.find("div", class_="story")
        try:
            [s.extract() for s in article.findAll('a')]
        except:
            pass
        return nlp(article.get_text())
    
    elif flag == 'n':
        article = soup.find("div", itemprop="articleBody")
        try: 
            [s.extract() for s in article.findAll('div', class_="el__embedded el__embedded--standard")]
            [s.extract() for s in article.findAll('cite', class_="el-editorial-source")]
        except:
            pass
        return nlp(article.get_text())
    elif flag == 'u':
        article = soup.find("div", class_="asset-double-wide double-wide p402_premium")
        try:
            [s.extract() for s in article.findAll('div', class_="story-asset")]
            [s.extract() for s in article.findAll('span', class_="exclude-from-newsgate")]
            [s.extract() for s in article.findAll('cta-atoms-container-inline')]
            [s.extract() for s in article.findAll('script')]
            [s.extract() for s in article.findAll('div', class_="article-print-url")]
        except:
            pass
        return nlp(article.get_text())

    
def nlp(text):
    client = language.LanguageServiceClient()

    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    sentiment = client.analyze_sentiment(document=document).document_sentiment

    print('Text: {}'.format(text))
    print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))
    
    return (float(sentiment.score), float(sentiment.magnitude))


'''
www\.cbc\.ca\/news\/(.*)
www\.foxnews\.com\/\w+\/(.*)
cnn\.com/\S+
www\.usatoday\.com\/story\/\w+\/\S+
www\.nbcnews.com\/\S+
www\.forbes\.com\/sites\/\w+\/(\d+\/){3}\S+
'''

