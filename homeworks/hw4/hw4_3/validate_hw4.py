"""
this is a validation program to make sure that the blog works correctly.
If you are reading this in clear text, you are probably violating the honor code
"""

import getopt
import pprint
import sys

import pymongo

# init the global cookie jar
# declare the variables to connect to db
connection = db = None
webhost = 'localhost:8082'
mongostr = 'mongodb://localhost:27017'
db_name = 'blog'


# this script will check that homework 4.3 is correct

def check_for_fast_posts_by_tag_page():
    posts = db.posts

    tag, res = "sphynx", False
    try:
        explain = posts.find({'tags': tag}).sort('date', direction=-1).limit(10).explain()
    except Exception as e:
        print(f'Can\'t query MongoDB..is it running? Error - {e}')
        return

    total_docs_examined = explain['executionStats']['totalDocsExamined']
    if total_docs_examined > 10:
        print('Sorry, executing the query to retrieve posts by tag is too slow.')
        print(f'We should be scanning no more than 10 documents. '
              f'You scanned - {total_docs_examined}')
        print('Here is the output from explain:')

        pp = pprint.PrettyPrinter(depth=6)
        pp.pprint(explain)
        return res
    else:
        res = True
        print('Blog retrieval by tag is super fast. Nice job.\n')
        return res


def get_the_middle_permalink():
    posts = db.posts
    try:
        c = posts.find().skip(500).limit(1)
        for doc in c:
            permalink = doc['permalink']
            return permalink
    except Exception as e:
        print(f'Can\'t query MongoDB..is it running? Error - {e}')
        return


def check_for_fast_blog_entry_page():
    posts = db.posts
    res = False
    permalink = get_the_middle_permalink()

    try:
        explain = posts.find({'permalink': permalink}).explain()
    except Exception as e:
        print(f'Can\'t query MongoDB..is it running? Error - {e}')
        return res

    total_docs_examined = explain['executionStats']['totalDocsExamined']
    if total_docs_examined > 1:
        print('Sorry, executing the query to retrieve a post by permalink is too slow')
        print(f'We should be scanning no more than 1 documents. '
              f'You scanned - {total_docs_examined}')
        print('Here is the output from explain:')

        pp = pprint.PrettyPrinter(depth=6)
        pp.pprint(explain)
        return res
    else:
        res = True
        print('Blog retrieval by permalink is super fast. Nice job.\n')
        return res


def check_for_fast_blog_home_page():
    posts = db.posts
    res = False
    try:
        explain = posts.find().sort('date', direction=-1).limit(10).explain()
    except Exception as e:
        print(f'Can\'t query MongoDB..is it running? Error - {e}')
        return res

    total_docs_examined = explain['executionStats']['totalDocsExamined']
    if total_docs_examined > 10:
        print('Sorry, executing the query to display the home page is too slow.')
        print(f'We should be scanning no more than 10 '
              f'documents. You scanned - {total_docs_examined}')
        print('Here is the output from explain:')

        pp = pprint.PrettyPrinter(depth=6)
        pp.pprint(explain)
        return res
    else:
        res = True
        print('Home page is super fast. Nice job.\n')
        return res


def check_for_data_integrity():
    """ Check to see if they loaded the data set """
    posts = db.posts
    res = False
    try:
        count = posts.count()
    except Exception as e:
        print(f'Can\'t query MongoDB..is it running? Error - {e}')
        return res

    if count != 1000:
        print(f'There are supposed to be 1000 documents. you have {count}')
        return res

    # find the most popular tags
    try:

        most_popular_tags = db.posts.aggregate([
            {'$project': {'tags': 1}},
            {'$unwind': '$tags'},
            {'$group': {'_id': '$tags', 'count': {'$sum': 1}}},
            {'$sort': {'count': -1}},
            {'$limit': 10}]
        )
    except Exception as e:
        print(f'Can\'t query MongoDB..is it running? Error - {e}')
        return res

    for item in most_popular_tags:
        if item['count'] == 13 and item['_id'] == "sphynx":
            res = True

    if not res:
        print('The dataset is not properly loaded. '
              'The distribution of post tags is wrong.')
        return res

    print('Data looks like it is properly loaded into the posts collection')

    return res


def arg_parsing(argv):
    """
    Command line arg parsing to make folks happy who want
      to run at mongolabs or mongohq this functions uses
      global vars to communicate. forgive me
    """
    global webhost
    global mongostr
    global db_name

    try:
        opts, args = getopt.getopt(argv, "-p:-m:-d:")
    except getopt.GetoptError:
        print("usage validate.py -p webhost -m mongoConnectString -d databaseName")
        print("\twebhost defaults to {0}".format(webhost))
        print("\tmongoConnectionString default to {0}".format(mongostr))
        print("\tdatabaseName defaults to {0}".format(db_name))
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("usage validate.py -p webhost -m mongoConnectString -d databaseName")
            sys.exit(2)
        elif opt in ("-p",):
            webhost = arg
            print(f'Overriding HTTP host to be {webhost}')
        elif opt in ("-m",):
            mongostr = arg
            print(f'Overriding MongoDB connection string to be {mongostr}')
        elif opt in ("-d",):
            db_name = arg
            print(f'Overriding MongoDB database to be {db_name}')


def main(argv):
    arg_parsing(argv)
    global connection
    global db

    print("Welcome to the HW 2.3 validation tester")

    # connect to the db (mongostr was set in arg_parsing)
    try:
        connection = pymongo.MongoClient(mongostr)
        db = connection[db_name]
    except Exception as e:
        print(f'can\'t connect to MongoDB using {mongostr} Is it running?')
        print(f'Exception was - {e}')
        sys.exit(1)

    if not check_for_data_integrity():
        print('Sorry, the data set is not loaded correctly in the posts collection')
        sys.exit(1)

    if not check_for_fast_blog_home_page():
        print('Sorry, the query to display the blog home page is too slow.')
        sys.exit(1)

    if not check_for_fast_blog_entry_page():
        print('Sorry, the query to retrieve a blog post by permalink is too slow.')
        sys.exit(1)

    if not check_for_fast_posts_by_tag_page():
        print('Sorry, the query to retrieve all posts with a certain tag is too slow')
        sys.exit(1)

    # if you are reading this in cleartext, you are violating the honor code.
    # You can still redeem yourself. Get it working and don't
    # submit the validation code until you do.
    # All a man has at the end of the day is his word.
    print('Tests Passed for HW 4.3. Your HW 4.3 validation code is 893jfns29f728fn29f20f2')


if __name__ == "__main__":
    main(sys.argv[1:])
