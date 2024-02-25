import requests
from textblob import TextBlob
import json

URI = "https://api.nytimes.com/svc/archive/v1"

def getDataForMonth(year, month):
    url = URI + "/" + str(year) + "/" + str(month) + ".json"
    payload = {'api-key':'LfTwoHs39WAogFOzLDK9YhAJcnAHIhfn'}
    r = requests.get(url, params = payload)

    dict = {}
    for article in r.json()['response']['docs']:
        headlineAndAbstract = article['headline']['main'] + ". " + article['abstract']
        polarity = TextBlob(headlineAndAbstract).sentiment.polarity
        subjectivity = TextBlob(headlineAndAbstract).sentiment.subjectivity
        dict[article['headline']['main']] = {'x': polarity, 'y': subjectivity}

    return json.dumps(dict)

def getDataForYear(year):
    for i in range(1, 13):
        i + 1

if __name__ == "__main__":
    getDataForMonth(2024, 2)