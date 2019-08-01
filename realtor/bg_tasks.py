# from django.shortcuts import HttpResponse
# from background_task import background
# from realtor.models import Agent, AgentsData, Background

# import requests
# from bs4 import BeautifulSoup

# import json

# @background(schedule=5)
# def hello(name):
#     print('hello')
#     try:
#         tweet = Background(tweet_id=1, tweet_text='hello world')
#         tweet.save()
#     except Exception as e:
#         print(e)


# @background(schedule=10)
# def scrape():
#     url = 'https://twitter.com/TheOnion'
#     data = requests.get(url)
#     html = BeautifulSoup(data.text, 'html.parser')
#     timeline = html.select('#timeline li.stream-item')
#     for tweet in timeline:
#         tweet_id = tweet['data-item-id']
#         tweet_text = tweet.select('p.tweet-text')[0].get_text()

#         tweet = Background(tweet_id=tweet_id, tweet_text=tweet_text)
#         tweet.save()

# This is a dev test








