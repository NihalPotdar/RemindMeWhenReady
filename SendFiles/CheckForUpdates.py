# write algorithm which takes a list of names of some-kind and sends updates to an http endpoint at some interval
from pymongo import MongoClient
import credentials
import requests
import time
from flask import Flask, request
import send
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import json

# mongo db
client = MongoClient(credentials.mongo_db_client) 
list_db = {}
test_endpoint = ""
db_lengths = []
db_new_lengths = []

# email
email = "\n "
to_send = False

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

def create_email(): # formulates the email to be sent out
    counter = 0
    for db_name in list_db: # a dict of all the databases
        for collection in list_db[db_name]: # find all collections
            global email
            num_queries = db_new_lengths[counter]-db_lengths[counter]
            
            if num_queries != 0: # new materials added
                global to_send
                to_send = True 

                email = email + db_name + " - " + collection + " <br> "
                for i in client[db_name][collection].find().sort('_id', -1).limit(num_queries): # going through all of the elements in the database
                    email = email+str(i)+" <br> "
                email = email +" <br> "

            counter = counter+1
    print("email: ", email)

def send_email():
    # creating the send grid service
    sendGrid = SendGridAPIClient(credentials.sendGridKey)

    message = Mail(
        from_email='nihalpot2002@gmail.com',
        to_emails='nihalpot2002@gmail.com',
        subject='Social Media Updates',
        html_content='<strong>'+email+'<strong>')
    try:
        response = sendGrid.send(message)
        return str(response.status_code)
    except Exception as e:
        return str(e)

def call_methods():
    # finds the list of databases that we have to check
    find_databases_and_collections() 

    # finding the number of old documents in the collections
    find_documents_in_collection(True) 

    # gets the data and wait for the response
    print("Waiting")
    time.sleep(30) 

    # finding the number of new documents in the collection
    find_documents_in_collection(False)

    # compile the message
    create_email()
    
    # send the email
    if to_send:
        print(send_email())

def go_on_indefinitely():
    while(True): # comes back here every 7 days
        call_methods()
        time.sleep(24*7*60)

def delete_all():
    for i in client.list_databases({}):
        print(i)
        name = i['name']
        
        if name != "admin" and name != 'local':
            for collection in client[i['name']].list_collection_names():
                client[name][collection].delete_many({})
            
delete_all()
#call_methods()
#print(db_lengths)
#print(client['Twitter_API'].list_collection_names())