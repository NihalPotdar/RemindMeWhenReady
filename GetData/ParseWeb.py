# parses the web for the top 10 results and will add to db if there are any updates

import requests
from bs4 import BeautifulSoup
import UserDetails
import credentials
from pymongo import MongoClient

# the base url to check
BaseURL = "https://www.google.com/search?q="

# the user to check
user = UserDetails.user

# the first quotation mark in the parsed url
first_mark_url = 0

# initializing mongodb
Top10Collections = MongoClient(credentials.mongo_db_client).Web_Parser.Top10Mentions

def get_url(): # finding the url to be searched
    if " " in user:
        space = user.find(" ")
        first_name = user[0:(user.find(" "))]
        last_name = user[(user.find(" ")+1):len(user)]
        return BaseURL+first_name+"+"+last_name
    else:
        return BaseURL+user

def is_required_url(url):
    # checks if the contained href tag is actually an url
    url = str(url)
    return True if "/url" in url else False

def upload_and_check(hyperlink):
    # the message to put on mongodb
    try:
        message = {}

        # finding where the url ends
        last_mark_url = hyperlink.find("\"", first_mark_url)
        title_start = hyperlink.find("Wnd")+5

        # finding the message parameters
        title = hyperlink[ title_start : hyperlink.find("<", title_start)]

        if Top10Collections.count_documents({"title":title}) > 0: # doesn't exist on mongodb 
            print("Already Exists!")
            return

        # compiling the message
        message['url'] = hyperlink[first_mark_url:last_mark_url]
        message['title'] = title

        print("New Item")
        print(message)

        # putting the message body onto the database
        Top10Collections.insert_one(message)

    except Exception as e:
        print(e)

if __name__ == "__main__":
    #Top10Collections.delete_many({}) # clearing the mongo database
    
    # using beasutiful soup to fix the html formatting
    page = requests.get(get_url())
    soup = BeautifulSoup(page.content, 'html.parser')

    # finding the required aspects of the returned results
    for i in soup.find_all(href=is_required_url):
        i = str(i) 

        # avoiding images in the hyperlinks
        if i.find("BNeawe vvjwJb AP7Wnd") == -1:
            continue

        # will always be the same for all the specified url's
        if first_mark_url == 0:
            first_mark_url = i.find("q=")+2

        upload_and_check(i)