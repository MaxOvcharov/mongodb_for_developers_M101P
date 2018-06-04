#!/usr/bin/env python
import pymongo

# connect to the db on standard port
connection = pymongo.MongoClient("mongodb://localhost")

db = connection.m101                 # attach to db
collection = db.funnynumbers         # specify the collection


magic = 0

try:
    cursor = collection.find()
    for item in cursor:
        if item['value'] % 3 == 0:
            magic = magic + item['value']
except Exception as e:
    print(f'Error trying to read collection: {type(e)} - {e}')


print(f'The answer to Homework One, Problem 2 is {magic}')
