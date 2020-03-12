# write algorithm which takes a list of names of some-kind and sends updates to an http endpoint at some interval
from pymongo import MongoClient
import credentials
import requests

Warehouse = MongoClient(credentials.mongo_db_client) 
list_db = []
test_endpoint = "https://eng3ecop7bsoc.x.pipedream.net"

def checkforupdate():
    # find a list of databases
    for i in Warehouse.list_databases({}):
        name = i['name']
        if name != "admin" and name != 'local':
            list_db.append(i['name'])

    # compare list of databases and based on some requirement, send http request to specified endpoint

def send_post():
    print(requests.get(test_endpoint))

checkforupdate()
send_post()