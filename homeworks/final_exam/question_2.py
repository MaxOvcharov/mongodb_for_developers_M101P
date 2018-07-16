#!/usr/bin/env python
from bson.son import SON

import pymongo

# connect to the db on standard port
connection = pymongo.MongoClient('mongodb://localhost')

db = connection.enron  # attach to db
collection = db.messages  # specify the collection


def print_first_and_last_comment_authors():
    try:
        pipeline = [
            {'$unwind': '$headers.To'},
            {'$group': {'_id': {'_id': '$_id', 'sender': '$headers.From'}, 'recipients': {'$addToSet': '$headers.To'}}},
            {'$unwind': '$recipients'},
            {'$group': {'_id': {'sender': '$_id.sender', 'recipient': '$recipients'}, 'count': {'$sum': 1}}},
            {'$sort': SON([('count', 1)])},
            {'$project': {'_id': 0, 'sender': '$_id.sender', 'recipient': '$_id.recipient', 'count': 1}},
        ]
        cursor = collection.aggregate(pipeline)
        for doc in cursor:
            print(doc)

    except Exception as e:
        print(f'Error trying to read collection: {type(e)} - {e}')


def main():
    print_first_and_last_comment_authors()


if __name__ == '__main__':
    main()

