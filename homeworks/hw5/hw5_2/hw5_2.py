#!/usr/bin/env python
from bson.son import SON

import pymongo

# connect to the db on standard port
connection = pymongo.MongoClient('mongodb://localhost')

db = connection.test  # attach to db
collection = db.zips  # specify the collection


def print_avg_city_pop(states):
    try:
        pipeline = [
            {'$match': {'state': {'$in': states}, 'pop': {'$gt': 25000}}},
            {'$group': {'_id': {'state': '$state', 'city': '$city'}, 'avr_count': {'$sum': '$pop'}}},
            {'$sort': SON([('_id.state', -1)])},
            # {'$project': {'_id': 0, 'state': '$_id.state', 'avr_count': 1}}
        ]
        cursor = collection.aggregate(pipeline)
        res = count = 0
        for doc in cursor:
            count += 1
            res += doc.get('avr_count')
            print(doc)
        print(f'\nRESULT: {int(res / count)}')

    except Exception as e:
        print(f'Error trying to read collection: {type(e)} - {e}')


def main():
    print_avg_city_pop(['CT', 'NJ'])
    print_avg_city_pop(['CA', 'NY'])


if __name__ == '__main__':
    main()

