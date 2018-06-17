#!/usr/bin/env python
import pymongo

# connect to the db on standard port
connection = pymongo.MongoClient('mongodb://localhost')

db = connection.school  # attach to db
collection = db.students  # specify the collection


def _process_student_scores(student_data):
    priv_score, homework_counter = 0, 0
    for score in student_data['scores']:
        if score['type'] == 'homework' and homework_counter == 0:
            homework_counter += 1
            priv_score = score['score']
        elif score['type'] == 'homework' and homework_counter != 0:
            homework_counter += 1
            if priv_score > score['score']:
                priv_score = score['score']

        if score['type'] == 'homework' and homework_counter > 1:
            student_id = student_data['_id']
            find_query = {'_id': student_id}
            update_query = {'$pull': {'scores': {'type': 'homework', 'score': priv_score}}}
            collection.update_one(find_query, update_query)
            print(f'DELETE ITEM FROM ARRAY: {student_id}')
            break


def delete_lowest_students_scores():
    try:
        projection = {'scores': 1}
        cursor = collection.find({}, projection)

        for student_data in cursor:
            _process_student_scores(student_data)

    except Exception as e:
        print(f'Error trying to read collection: {type(e)} - {e}')


def check_result():
    assert collection.count() == 200
    res1 = collection.find_one({'_id': 137})
    correct_res = {
        '_id': 137,
        'name': 'Tamika Schildgen',
        'scores': [
            {
                'type': 'exam',
                'score': 4.433956226109692
            },
            {
                'type': 'quiz',
                'score': 65.50313785402548
            },
            {
                'type': 'homework',
                'score': 89.5950384993947
            }
        ]
    }
    assert res1 == correct_res


def main():
    delete_lowest_students_scores()
    check_result()


if __name__ == '__main__':
    main()
