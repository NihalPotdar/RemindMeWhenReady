#http://docs.tweepy.org/en/latest/api.html#api-reference
import tweepy
import credentials
from pymongo import MongoClient
import json
import UserDetails

# my credentials
auth = tweepy.OAuthHandler(credentials.consumer_key, credentials.consumer_secret_key)
auth.set_access_token(credentials.access_key, credentials.access_key_secret)
api = tweepy.API(auth)

# connect to mongo_db
client = MongoClient(credentials.mongo_db_client)
mentions_collection = client.Twitter_API.Mentions 
# remove everything in the database
#mentions_collection.delete_many({})

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

def document_value(mention, url): # returns an object that is added to mongo db
    upload = {}
    try:
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

def upload(mention, url): # get the tweet and upload to mongodb
    doc = document_value(mention, url) # get the document to be uploaded
    formulate_message(doc, doc['created_at']) # add it to the sendgrid message
    mentions_collection.insert_one(
       doc
    )

def tweet_logic(mention):
    try:
        if(len(mention._json['entities']['urls']) != 0): # direct mention in tweet
            url = mention._json['entities']['urls'][0]['expanded_url']
        else: # tweet reply
            url = mention._json['user']['url']

        if(validate_doc(url)): # if the specified tweet doesn't exist
            upload(mention, url)  
        else:
            print("already exists")          
    except Exception as e: # won't add the tweet if there is a problem
        print(e)

if(__name__ == '__main__'):
    # name of the user
    user = UserDetails.user
    
    # recent mentions on twitter
    recent_mentions = api.mentions_timeline()
        
    for mention in recent_mentions: # going through each of the mentions
        tweet_logic(mention)