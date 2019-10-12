from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types


def parse(text):
    
    return nlp(text)


def nlp(text):
    client = language.LanguageServiceClient()

    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    sentiment = client.analyze_sentiment(document=document).document_sentiment

    print('Text: {}'.format(text))
    print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))
    
    return [sentiment.score, sentiment.magnitude]


