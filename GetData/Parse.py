# the aim of this app is to act as a social media handler
'''
import requests
from bs4 import BeautifulSoup

# Social Media Page
URL = "https://nihalpotdar.github.io"
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find('')
# Printing out the content for testing
print(results.prettify())
'''
#http://docs.tweepy.org/en/latest/api.html#api-reference
import tweepy
import credentials
from pymongo import MongoClient
import json

# my credentials
auth = tweepy.OAuthHandler(credentials.consumer_key, credentials.consumer_secret_key)
auth.set_access_token(credentials.access_key, credentials.access_key_secret)
api = tweepy.API(auth)

'''

# connect to mongo_db
client = MongoClient(credentials.mongo_db_client)

#finding where there is a mention of name

# make a post to mongo_db, take mentions and add to db
mentions_collection = client.Twitter_API.Mentions 

# remove everything in the database
#mentions_collection.delete_many({})

# finding if a required friend has made a post
required_friends = ['YouthCentralYYC']


def friends():
    # user object for twitte
    user = api.get_user('NihalPotdar')
    print(user.screen_name)
    print(user.followers_count)
    for friend in user.friends():
        print(friend.screen_name)
'''

def upload(mention):
    upload = {}
    try:
        upload['url'] = mention._json['entities']['urls'][0]['expanded_url']     
        upload['name'] = mention.user.name
        upload['twitter_handle'] = mention.user.screen_name
        upload['tweet'] = mention.text
        upload['retweet_count'] = mention.retweet_count
        upload['liked count'] = mention.favorite_count
        print(upload)
    except:
        print("There's an error!")

'''
        mentions_collection.insert_one(
            mention._json
        )
'''

# recent mentions on twitter
recent_mentions = api.mentions_timeline()
# add a document to the database
for mention in recent_mentions:
    upload(mention)