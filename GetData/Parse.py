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

# connect to mongo_db
client = MongoClient(credentials.mongo_db_client)
mentions_collection = client.Twitter_API.Mentions 
# remove everything in the database
mentions_collection.delete_many({})

# send grid message
message = {}

def friends():
    # finding if a required friend has made a post
    required_friends = ['YouthCentralYYC']
    user = api.get_user('NihalPotdar')
    print(user.screen_name)
    print(user.followers_count)
    for friend in user.friends():
        print(friend.screen_name)

def validate_doc(url): # returns true if the tweet exists and false otherwise
    return False if mentions_collection.count_documents({'url':url}) > 0 else True

def formulate_message(doc, created_at):
    message[created_at] = doc
    print(message)

def document_value(mention): # returns an object that is added to mongo db
    upload = {}
    try:
        url = mention._json['entities']['urls'][0]['expanded_url']
        upload['url'] = url
        upload['created_at'] = mention._json['created_at']
        upload['name'] = mention.user.name
        upload['twitter_handle'] = mention.user.screen_name
        upload['tweet'] = mention.text
        upload['retweet_count'] = mention.retweet_count
        upload['liked count'] = mention.favorite_count
        return upload
    except:
        return { 'problem':"There's an error!" }

def upload(mention): # get the tweet and upload to mongodb
    doc = document_value(mention) # get the document to be uploaded
    formulate_message(doc, doc['created_at']) # add it to the sendgrid message
    mentions_collection.insert_one(
       doc
    )

if(__name__ == '__main__'):
    # recent mentions on twitter
    recent_mentions = api.mentions_timeline()
    # add a document to the database      
    for mention in recent_mentions:
        try:
            url = mention._json['entities']['urls'][0]['expanded_url']
            if(validate_doc(url)): # if the specified tweet doesn't exist
                upload(mention)  
            else:
                print("already exists")          
        except: # won't add the tweet if there is a problem
            continue

# get all mentions and add to mongo_db
# compare existing mentions if they don't exist