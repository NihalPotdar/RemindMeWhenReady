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

# getting tweets on home_timeline
'''
# simple means for printing out whatever is on the home console
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet)
'''

# connect to mongo_db
client = MongoClient(credentials.mongo_db_client)

#finding where there is a mention of name
#print("\n'''''''''''RECENT MENTIONS''''''''''''''''''''''")

# recent mentions on twitter
recent_mentions = api.mentions_timeline()

# make a post to mongo_db, take mentions and add to db
mentions_collection = client.Twitter_API.Mentions 

# remove everything in the database
mentions_collection.delete_many({})

# add a document to the database
for mention in recent_mentions:
    
    '''
    mentions_collection.insert_one(
        mention._json
    )
    '''

try:
    print(mention.entities.entities)
except:
    print("There's an error!")
    '''
    print(mention.user.name)
    print(mention.user.screen_name)
    print(mention.text)
    print(mention.retweet_count)
    print(mention.favorite_count)
'''
#print("'''''''''''''''''''''''''''''''''''''''''''''''''")

# finding if a required friend has made a post
required_friends = ['YouthCentralYYC']


#print("\n''''''''''''''''FRIENDS'''''''''''''''''''''''''")
# user object for twitter
'''
user = api.get_user('NihalPotdar')
print(user.screen_name)
print(user.followers_count)
for friend in user.friends():
    print(friend.screen_name)
'''
#print("'''''''''''''''''''''''''''''''''''''''''''''''''")