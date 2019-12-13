from django.shortcuts import render
import requests
# import random



# Create your views here.
def newslist(request):
    news_url = 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=74c3bda5e80940128f54741ba6816686'

    r = requests.get(news_url)

    # total_news = r.json()['totalResults']
    Nlist = r.json()['articles']

    # news_number = random.randrange(0,total_news)

    # title = r.json()['articles'][news_number]['title']
    # author = r.json()['articles'][news_number]['author']
    # content = r.json()['articles'][news_number]['content']
    # image = r.json()['articles'][news_number]['urlToImage']
    # published = r.json()['articles'][news_number]['publishedAt']

    context = {
        'newslist' : Nlist[:5]
    }

    return render(request, 'news.html', context)