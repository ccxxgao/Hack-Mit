# import feedparser
# import urllib.parse
import requests

NEWS_API_KEY = '5215f4914c064233bfe6cfe63e161137'

def get_news(*keywords):
    search_str = '%20'.join(keywords)
    u = 'https://newsapi.org/v2/everything?q={}&sortBy=popularity&apiKey={}'.format(search_str, NEWS_API_KEY)
    r = requests.get(u)
    return r.json()['articles']
