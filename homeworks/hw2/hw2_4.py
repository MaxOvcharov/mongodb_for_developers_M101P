#!/usr/bin/env python
import pymongo

# connect to the db on standard port
connection = pymongo.MongoClient("mongodb://localhost")

db = connection.video                 # attach to db
collection = db.movieDetails                   # specify the collection


def delete_lowest_students_scores():
    try:
        projection = {'title': 1, '_id': 0}
        query = {'year': 2013, 'rated': 'PG-13', 'awards.wins': {'$eq': 0}}
        res = collection.find_one(query, projection)
        print(f'Movie name: \'{res["title"]}\'')
    except Exception as e:
        print(f'Error trying to read collection: {type(e)} - {e}')


def main():
    delete_lowest_students_scores()


if __name__ == '__main__':
    main()
