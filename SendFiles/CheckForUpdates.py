# write algorithm which takes a list of names of some-kind and sends updates to an http endpoint at some interval
from pymongo import MongoClient
import credentials
import requests
import time

client = MongoClient(credentials.mongo_db_client) 
list_db = {}
test_endpoint = "https://eng3ecop7bsoc.x.pipedream.net"
db_lengths = []

def find_databases_and_collections():
    # find a list of databases
    for i in client.list_databases({}):
        name = i['name']
        if name != "admin" and name != 'local':
            list_db[i['name']] = client[i['name']].list_collection_names()

            for count, q in enumerate(client[i['name']].list_collection_names()):
                print(count)
                list_db[i['name']][count].append(client[i['name']][q].count_documents({}))
                
                #list_db[ [i['name']][count] ]
    print_db()

def print_db(): 
    # print out the list of databases
    print(list_db)

# compare list of databases and based on some requirement, send http request to specified endpoint

def maintain_original(): # creates a snapshot of the inital number of documents in the database
    for db_name in list_db: # a dict of all the databases
        for collection_num in range(len(list_db[db_name])): # a list of all the collections
            db_lengths.append( client[ db_name ][ list_db[db_name][collection_num] ].count_documents({}) )

def send_post_to_parseAPI():
    print(requests.get(test_endpoint))

def call_other_methods():
    # before the process
    find_databases() # finds the list of databases that we have to check
    maintain_original() # gets a snapshot of the original state of the database

    # the process
    send_post_to_parseAPI() # send request to parse API and wait for this call to complete

    # after the process
    check_for_change() # checks the database for any changes
    # find if something has changed in the database and alert user if required

def go_on_indefinitely():
    while(True): # comes back here every 7 days
        call_other_methods()
        time.sleep(24*7*60)

find_databases_and_collections()
#maintain_original()
#print(db_lengths)
#print(client['Twitter_API'].list_collection_names())