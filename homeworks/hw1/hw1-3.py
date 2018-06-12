#!/usr/bin/env python

import pymongo
import bottle

@bottle.get("/hw1/<n>")
def get_hw1(n):

    # connect to the db on standard port
    connection = pymongo.MongoClient("mongodb://localhost")

    n = int(n)

    db = connection.m101                 # attach to db
    collection = db.funnynumbers         # specify the collection


    try:
        cursor = collection.find({}, limit=1, skip=n).sort('value', direction=1)
        for item in cursor:
            return str(int(item['value'])) + "\n"
    except Exception as e:
        print(f'Error trying to read collection: {type(e)} - {e}')


bottle.debug(True)
bottle.run(host='localhost', port=8080)
