#!/usr/bin/env python
from bson.son import SON

import pymongo

# connect to the db on standard port
connection = pymongo.MongoClient('mongodb://localhost')

db = connection.test  # attach to db
collection = db.grades  # specify the collection


def print_avg_students_score():
    try:
        pipeline = [
            {'$unwind': '$scores'},
            {'$match': {'scores.type': {'$ne': 'quiz'}}},
            {'$group': {'_id': {'class_id': '$class_id', 'student_id': '$student_id'},
                        'average': {'$avg': '$scores.score'}}},
            {'$group': {'_id': '$_id.class_id', 'average': {'$avg': '$average'}}},
            {'$sort': SON([('average', -1)])},
            {'$project': {'_id': 0, 'class_id': '$_id', 'average': 1}}
        ]
        cursor = collection.aggregate(pipeline)
        for doc in cursor:
            print(doc)

    except Exception as e:
        print(f'Error trying to read collection: {type(e)} - {e}')


def main():
    print_avg_students_score()


if __name__ == '__main__':
    main()

