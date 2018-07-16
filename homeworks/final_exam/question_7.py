#!/usr/bin/env python
from bson.son import SON

import pymongo

# connect to the db on standard port
connection = pymongo.MongoClient('mongodb://localhost')

db = connection.music  # attach to db - music
albums = db.albums  # specify the collection - albums
images = db.images  # specify the collection - images


def print_first_and_last_comment_authors():
    try:
        albums.create_index([('images', pymongo.ASCENDING)], name='images')

        pipeline1 = [
            {'$unwind': '$tags'},
            {'$group': {'_id': {'tag': '$tags'}, 'count': {'$sum': 1}}},
            {'$project': {'_id': 0, 'tag': '$_id.tag', 'count': 1}},
            {'$match': {'tag': 'kittens'}}
        ]
        cursor = images.aggregate(pipeline1)
        totall_kittens_num = 0
        for doc in cursor:
            totall_kittens_num = doc.get('count')

        print(f'IMAGES NUM BEFORE: {totall_kittens_num}')

        pipeline2 = [
            {'$unwind': '$tags'},
            {'$match': {'tags': 'kittens'}},
            {'$project': {'_id': 0, 'img_id': '$_id', 'tag': '$tags'}},
        ]
        cursor = images.aggregate(pipeline2)
        for doc in cursor:
            is_exists = albums.count({'images': doc.get('img_id')})
            if not is_exists:
                totall_kittens_num -= 1

        print(f'IMAGES NUM AFTER: {totall_kittens_num}')

    except Exception as e:
        print(f'Error trying to read collection: {type(e)} - {e}')


def main():
    print_first_and_last_comment_authors()


if __name__ == '__main__':
    main()

