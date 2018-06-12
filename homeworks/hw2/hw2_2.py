#!/usr/bin/env python
import pymongo

# connect to the db on standard port
connection = pymongo.MongoClient("mongodb://localhost")

db = connection.students                 # attach to db
collection = db.grades                   # specify the collection


def delete_lowest_students_scores():
    try:
        # projection = {'student_id: 1, score: 1'}
        sort_query = [('student_id', pymongo.ASCENDING), ('score', pymongo.ASCENDING)]
        cursor = collection.find({'type': 'homework'}).sort(sort_query)
        student_id, score, homework_counter = 0, 0, 0
        for student_data in cursor:
            if student_id == student_data['student_id'] and homework_counter == 0:
                homework_counter += 1
                score = student_data['score']
            elif student_id != student_data['student_id'] and homework_counter == 0:
                homework_counter += 1
                score = student_data['score']
                student_id = student_data['student_id']
            else:
                homework_counter += 1

            if student_data['student_id'] == student_id and homework_counter > 1:
                delete_query = \
                    {'student_id': student_data['student_id'], 'score': score}
                res = collection.delete_one(delete_query)
                homework_counter = 0
                print(f'DELETE RES: {res.deleted_count} - {student_id}')
    except Exception as e:
        print(f'Error trying to read collection: {type(e)} - {e}')


def check_result():
    assert db.grades.count() == 600
    projection = {'student_id': 1, 'type': 1, 'score': 1, '_id': 0}
    res1 = collection.find_one({}, projection, sort=[('score', -1), ], skip=100, limit=1)
    assert res1 == {'student_id': 100, 'type': 'homework', 'score': 88.50425479139126}
    sort_query2 = [('student_id', 1), ('score', 1)]
    res2 = db.grades.find({}, projection).sort(sort_query2).limit(5)
    output_res2 = (
        {"student_id": 0, "type": "quiz", "score": 31.95004496742112},
        {"student_id": 0, "type": "exam", "score": 54.6535436362647},
        {"student_id": 0, "type": "homework", "score": 63.98402553675503},
        {"student_id": 1, "type": "homework", "score": 44.31667452616328},
        {"student_id": 1, "type": "exam", "score": 74.20010837299897}
    )

    for res_data in res2:
        assert res_data in output_res2


def main():
    delete_lowest_students_scores()
    check_result()


if __name__ == '__main__':
    main()
