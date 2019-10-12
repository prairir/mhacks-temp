from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import urllib2
from bs4 import BeautifulSoup
import re



def retMag():
    #search db stuff
    #
    #

    if !valIn:
        checkurl(url)
    return nlp(text)


def checkurl(url):
    if re.match("www\.cbc\.ca\/news\/(.*)", url).group() in url:
        return getText(url, 'c')
    elif re.match("www\.forbes\.com\/sites\/\w+\/(\d+\/){3}\S+",url).group() in url:
        return getText(url, 'f')
    elif re.match("(cnn.com\/S+", url).group() in url:
        return getText(url, 'n')
    elif re.match("www\.foxnews\.com\/\w+\/(.*)",url).group() in url:
        return getText(url, 'x')
    elif re.match("(www\.usatoday\.com\/story\/w+\/\S+)", url).group() in url:
        return getText(url, 'u')
    elif re.match("(www\.nbcnews\.com\/\S+)", url).group() in url:
        return getText(url, 'b')
    else:
        return None

def getText(url, flag):
    if flag == 'f':
        article = soup.find("div", class_="article-container")
        sub = article.find("div", {"_ngcontent-c16": ""})
        return nlp(sub.get_text())

    
    
def nlp(text):
    client = language.LanguageServiceClient()

    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    sentiment = client.analyze_sentiment(document=document).document_sentiment

    print('Text: {}'.format(text))
    print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))
    
    return [sentiment.score, sentiment.magnitude]


'''
www\.cbc\.ca\/news\/(.*)
www\.foxnews\.com\/\w+\/(.*)
cnn\.com/\S+
www\.usatoday\.com\/story\/\w+\/\S+
www\.nbcnews.com\/\S+
www\.forbes\.com\/sites\/\w+\/(\d+\/){3}\S+
'''

