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

import tweepy
import credentials

auth = tweepy.OAuthHandler(credentials.consumer_key, credentials.consumer_secret_key)
auth.set_access_token(credentials.access_key, credentials.access_key_secret)
api = tweepy.API(auth)

'''
# simple means for printing out whatever is on the home console
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet)
'''

# user object for twitter
user = api.get_user('NihalPotdar')
print(user.screen_name)
print(user.followers_count)