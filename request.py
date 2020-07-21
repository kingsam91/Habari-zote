from app import create_app
from newsapi import NewsApiClient
from config import config_options

newsapi = NewsApiClient(api_key='96573ce4e2984891a9f56fd982912bc8')

def get_news():
    '''
    Function that gets the json responce to our url request
    '''
    topheadlines = newsapi.get_top_headlines(
        sources='al-jazeera-english,bbc-news,the-verge')
    articles = topheadlines['articles']

    url = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        url.append(myarticles['url'])
        img.append(myarticles['urlToImage'])

    news_results = zip(news, url, img)

    return news_results


def get_news_by_custom_source(source):
'''
    Function that gets the json responce to our url request
    '''
    topheadlines = newsapi.get_top_headlines(
        sources=source)

    articles = topheadlines['articles']

    url = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        url.append(myarticles['url'])
        img.append(myarticles['urlToImage'])

    news_results = zip(news, url, img)


    return news_results


def get_sources():

    return sources_results