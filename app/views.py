#-*- coding: utf-8 -*-
from django.shortcuts import render
import oauth2 as oauth
import json


def home(request):
	tweet_list = _get_tweet_list()
	return render(request,"home.html", {"tweet_list":tweet_list})

def _get_tweet_list():
	CONSUMER_KEY = "YOUR_CONSUMER_KEY"
	CONSUMER_SECRET = "YOUR_CONSUMER_SECRET"
	ACCESS_KEY = "YOUR_ACCESS_KEY"
	ACCESS_SECRET = "YOUR_ACCESS_SECRET"
	consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
	access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
	client = oauth.Client(consumer, access_token)
	timeline_endpoint = "https://api.twitter.com/1.1/statuses/home_timeline.json"
	response, data = client.request(timeline_endpoint)
	tweets = json.loads(data)
	tweet_list=[]
	for tweet in tweets:
		tweet1 = tweet["text"]
		tweet = tweet1.split("https")
		tweet_list.append({"tweet":tweet[0]})
	return tweet_list
