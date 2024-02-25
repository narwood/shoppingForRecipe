import requests
import json

r = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/dog")

# with open('APIpractice/dictionaryResponse.txt', 'w', encoding='utf-8') as f:
#     f.write(str(r.json()))

print(r.json()[0]["word"])

