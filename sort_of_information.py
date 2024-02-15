from newsapi import NewsApiClient

# Initialize NewsApiClient with your API key
api_key = '9ad18454dd954e5eb213933507c94823'
newsapi = NewsApiClient(api_key=api_key)

# Define your search parameters
query = 'india'  # Specify your search query
language = 'en'             # Specify the language of the articles (e.g., 'en' for English)
sources = 'Aaj Tak'        # Specify the news sources (e.g., 'bbc-news')
category = 'business'            # Specify a category if you want to narrow down (e.g., 'business')

# Make the API request
articles = newsapi.get_everything(q=query,  )

# Process the results
print(len(articles))
if articles['status'] == 'ok':
    for article in articles['articles']:
        print(article)
        # print(article['url'])
else:
    print("Error fetching articles:", articles['message'])
