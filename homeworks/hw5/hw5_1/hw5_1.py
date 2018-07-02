#!/usr/bin/env python
from bson.son import SON

import pymongo

# connect to the db on standard port
connection = pymongo.MongoClient('mongodb://localhost')

db = connection.blog  # attach to db
collection = db.posts  # specify the collection


def print_first_and_last_comment_authors():
    try:
        pipeline = [
            {'$unwind': '$comments'},
            {'$group': {'_id': {'author': '$comments.author'}, 'count': {'$sum': 1}}},
            {'$sort': SON([('count', -1)])},
            {'$project': {'_id': 0, 'author': '$_id.author', 'count': 1}}
        ]
        doc = {}
        cursor = collection.aggregate(pipeline)
        for doc in cursor:
            print(doc)

        assert doc.get('author') == 'Mariela Sherer'
        assert doc.get('count') == 387
    except Exception as e:
        print(f'Error trying to read collection: {type(e)} - {e}')


def main():
    print_first_and_last_comment_authors()


if __name__ == '__main__':
    main()

