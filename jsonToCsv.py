import requests
from textblob import TextBlob
import json

URI = "https://api.nytimes.com/svc/archive/v1"
file = "./database.json"

def getDataForMonth(year, month):
    url = URI + "/" + str(year) + "/" + str(month) + ".json"
    payload = {'api-key':'LfTwoHs39WAogFOzLDK9YhAJcnAHIhfn'}
    r = requests.get(url, params = payload)

    with open(file, 'w', encoding='utf-8') as f:
        dict = {}
        for article in r.json()['response']['docs']: 
            headlineAndAbstract = article['headline']['main'] + ". " + article['abstract']
            polarity = round(TextBlob(headlineAndAbstract).sentiment.polarity, 2)
            subjectivity = round(TextBlob(headlineAndAbstract).sentiment.subjectivity, 2)
            headline = str(article['headline']['main'])
            dict[headline] = {'x': polarity, 'y': subjectivity}
        json.dump(dict, f)

searchFile = 'searchDatabase.csv'

def searchByParams(payload): 
    url = "https://api.nytimes.com/svc/search/v2/articlesearch.json"
    r = requests.get(url, params = payload)

    with open(searchFile, 'w', encoding='utf-8') as f:
        f.write(str(r.json()))

if __name__ == "__main__":
    getDataForMonth(2019, 1)