import requests
from textblob import TextBlob
import json

URI = "https://api.nytimes.com/svc/archive/v1"

def main(year, month):
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

if __name__ == "__main__":
    main(2024, 1)