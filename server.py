import yaml
import requests

with open('.secrets.yml', 'r') as f:
    secrets = yaml.safe_load(f.read())

api_key = secrets['bing-api-key']
news_url = secrets['news-url']

headers = {
    "Ocp-Apim-Subscription-Key": api_key
}

response = requests.get(news_url, headers=headers)
response.raise_for_status()
data = response.json()['value']

for article in data:
    print(article['name'].strip())
    print(article['url'].strip())
    print(article['description'].strip())
    for provider in article['provider']:
        print(provider['name'])
