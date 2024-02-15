import requests

api_url = "https://newsapi.org/v2/top-headlines"

query_params = {
    "sources": "bbc news",
    "apikey": "9ad18454dd954e5eb213933507c94823"
}

response = requests.get(api_url, params=query_params)

articles = response.json()["articles"]

for article in articles:
    print(article["title"])
    print(article["description"])
    print("-" * 100)

