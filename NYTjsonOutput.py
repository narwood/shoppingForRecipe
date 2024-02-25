import requests
from textblob import TextBlob
import json
import base64

URI = "https://api.nytimes.com/svc/archive/v1"
file = "./database.csv"

def getDataForMonth(year, month):
    url = URI + "/" + str(year) + "/" + str(month) + ".json"
    payload = {'api-key':'LfTwoHs39WAogFOzLDK9YhAJcnAHIhfn'}
    r = requests.get(url, params = payload)

    with open(file, 'w', encoding='utf-8') as f:
        f.write("Headline,Polarity,Subjectivity\n")
        for article in r.json()['response']['docs']: #somebody's got a problem with 'response' key
            headlineAndAbstract = article['headline']['main'] + ". " + article['abstract']
            polarity = round(TextBlob(headlineAndAbstract).sentiment.polarity, 2)
            subjectivity = round(TextBlob(headlineAndAbstract).sentiment.subjectivity, 2)
            headline = str(article['headline']['main'])
            f.write(headline + "," + str(polarity) + "," + str(subjectivity) + "\n")

        

if __name__ == "__main__":
    getDataForMonth(2019, 1)