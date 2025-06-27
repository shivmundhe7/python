import requests

API_KEY = '98d883c1b5674448a7f0375b5a80c182'  
url = f'https://newsapi.org/v2/top-headlines?country=in&apiKey=98d883c1b5674448a7f0375b5a80c182'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    articles = data['articles']
    
    print("📰 Today's Top Headlines:\n")
    for i, article in enumerate(articles[:10], start=1):  # Show top 10 headlines
        print(f"{i}. {article['title']}")
        print(f"   {article['description']}")
        print(f"   Link: {article['url']}\n")
else:
    print("Failed to fetch news 😔")
