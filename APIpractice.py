import requests

URI = "https://api.nytimes.com/svc/archive/v1"

payload = {'api-key':'LfTwoHs39WAogFOzLDK9YhAJcnAHIhfn'}
r = requests.get("https://api.nytimes.com/svc/archive/v1/2019/1.json?api-key=LfTwoHs39WAogFOzLDK9YhAJcnAHIhfn", params = payload)
print(r.json())
