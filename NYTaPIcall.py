import requests

URI = "https://api.nytimes.com/svc/archive/v1"

payload = {'api-key':'LfTwoHs39WAogFOzLDK9YhAJcnAHIhfn'}
r = requests.get("https://api.nytimes.com/svc/archive/v1/2019/1.json?api-key=LfTwoHs39WAogFOzLDK9YhAJcnAHIhfn", params = payload)

# with open('NYTdata.txt', 'w', encoding='utf-8') as f:
#     f.write(str(r.json()))

for article in r.json()['response']['docs']:
    