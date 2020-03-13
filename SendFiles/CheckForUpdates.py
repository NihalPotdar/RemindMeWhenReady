# write algorithm which takes a list of names of some-kind and sends updates to an http endpoint at some interval
from pymongo import MongoClient
import credentials
import requests
import time
from flask import Flask, request
import send

client = MongoClient(credentials.mongo_db_client) 
list_db = {}
test_endpoint = "https://eng3ecop7bsoc.x.pipedream.net"
db_lengths = []
db_new_lengths = []

app = Flask(__name__)

@app.route('/', methods=['POST'])
def hello_world():
    return "Hello World!"

@app.route('/notify', methods=['GET'])
def notify():
    call_methods()
    return "Notification enabled! Please check your email"

def find_databases_and_collections():
    # find a list of databases and the corresponding collections
    for i in client.list_databases({}):
        name = i['name']
        if name != "admin" and name != 'local':
            list_db[i['name']] = client[i['name']].list_collection_names()

    print(list_db)

# compare list of databases and based on some requirement, send http request to specified endpoint

def find_documents_in_collection(original): # creates a snapshot of the inital number of documents in the database
    for db_name in list_db: # a dict of all the databases
        for collection_num in range(len(list_db[db_name])): # a list of all the collections
            if original == True:
                db_lengths.append( client[ db_name ][ list_db[db_name][collection_num] ].count_documents({}) )
            else:
                db_new_lengths.append( client[ db_name ][ list_db[db_name][collection_num] ].count_documents({}) )
    print(db_lengths) 
    print("new:",db_new_lengths)


def create_email():
    count = 0
    '''
    for db_name in list_db: # a dict of all the databases
        for collection in range(len(list_db[db_name])): # a list of all the collections
            count = count+1
            diff = db_new_lengths[count]-db_lengths[count]
            '''
    for i in client['Twitter_API']['Mentions'].find().sort('_id', -1).limit(1):
        print(i)

def call_methods():
    # before the process
    find_databases_and_collections() # finds the list of databases that we have to check

    # finding the number of old documents in the collections
    find_documents_in_collection(True) 

    #time.sleep(60) # test for this functionality

    # finding the number of new documents in the collection
    find_documents_in_collection(False)

    # compile the message
    create_email()

    #send the email
    #send_email()

    # after the process
    #check_for_change() # checks the database for any changes
    # find if something has changed in the database and alert user if required

def go_on_indefinitely():
    while(True): # comes back here every 7 days
        call_other_methods()
        time.sleep(24*7*60)

call_methods()
#print(db_lengths)
#print(client['Twitter_API'].list_collection_names())