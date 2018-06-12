#!/usr/bin/env python
import pymongo

# connect to the db on standard port
connection = pymongo.MongoClient("mongodb://localhost")

db = connection.video                 # attach to db
collection = db.movieDetails                   # specify the collection


def delete_lowest_students_scores():
    try:
        query = {'countries.1': 'Sweden'}
        res = collection.count(query)
        print(f'Movies list "Sweden" second in the the list of countries: {res}')
    except Exception as e:
        print(f'Error trying to read collection: {type(e)} - {e}')


def main():
    delete_lowest_students_scores()


if __name__ == '__main__':
    main()
