#!/usr/bin/env python
from bson.son import SON

import pymongo

# connect to the db on standard port
connection = pymongo.MongoClient('mongodb://localhost')

db = connection.enron  # attach to db
collection = db.messages  # specify the collection


def print_count_msgs():
    try:
        res = collection.count({'headers.From': 'andrew.fastow@enron.com', 'headers.To': 'jeff.skilling@enron.com'})
        print(f'Number of messages(andrew.fastow@enron.com -> jeff.skilling@enron.com): {res}')
    except Exception as e:
        print(f'Error trying to read collection: {type(e)} - {e}')


def main():
    print_count_msgs()


if __name__ == '__main__':
    main()

