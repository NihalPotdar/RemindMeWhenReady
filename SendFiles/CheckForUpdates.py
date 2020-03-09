# write algorithm which takes a list of names of some-kind and sends updates to an http endpoint at some interval
from pymongo import MongoClient
import credentials

Warehouse = MongoClient(credentials.mongo_db_client) 

def checkforupdate():
    # get list of databases

    # find a list of databases
    for i in Warehouse.list_databases({}):
        name = i['name']
        if name != "admin" and name != 'local':
            print(name)

    # compare list of databases and based on some requirement, send http request to specified endpoint

checkforupdate()