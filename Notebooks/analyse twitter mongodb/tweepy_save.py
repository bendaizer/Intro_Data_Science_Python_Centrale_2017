import tweepy
from pymongo import MongoClient
import json

consumer_key = 	""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()

for data in tweepy.Cursor(api.search, q='#AI -filter:retweets', lang="en").items():
    client = MongoClient("192.168.99.100", 32768)
    db = client['twitter_db']
    collection = db['twitter_collection']
    collection.insert(data._json)