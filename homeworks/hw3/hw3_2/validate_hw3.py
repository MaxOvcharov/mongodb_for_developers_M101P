"""
this is a validation program to make sure that the blog works correctly.
If you are reading this in clear text, you are probably violating the honor code
"""
import pymongo
from urllib import parse
import requests
import random
import re
import string
import sys
import getopt

# init the global cookie jar
# declare the variables to connect to db
connection = db = None
webhost = 'localhost:8082'
mongostr = 'mongodb://localhost:27017'
db_name = 'blog'

# this script will check that homework 3.2 is correct


def make_salt(n):
    salt = ''
    for i in range(n):
        salt = salt + random.choice(string.ascii_letters)

    return salt


# this is a validation program to make sure that the blog works correctly.
def create_user(username, password):
    url = "http://{0}/signup".format(webhost)
    try:
        print(f'Trying to create a test user - {username}')
        data = parse.urlencode(
            [("email", ""), ("username", username), ("password", password), ("verify", password)]
        )
        response = requests.post(url=url, data=data)
        result = response.text
        users = db.users
        user = users.find_one({'_id': username})
        if user is None:
            print(f'Could not find the test user {username} in the users collection.')
            return False
        print(f'Found the test user {username} in the users collection')

        # check that the user has been built
        expr = re.compile("Welcome\s+" + username)
        if expr.search(result):
            return True

        print("When we tried to create a user, here is the output we got\n")
        print(result)

        return False
    except Exception as e:
        print(f'The request to {url} failed, so your blog may not be running - {e}')
        return False


def try_to_login(username, password):
    url = "http://{0}/login".format(webhost)
    try:
        print(f'Trying to login for test user: {username}')
        data = parse.urlencode([("username", username), ("password", password)])
        response = requests.post(url=url, data=data)
        cookie = response.request.headers.get('cookie').split('=')[1]
        result = response.text

        expr = re.compile("Welcome\s+" + username)
        if expr.search(result):
            return cookie

        print("When we tried to login, here is the output we got\n")
        print(result)
        return False
    except Exception as e:
        print(f'The request to {url} failed, so your blog may not be running - {e}')
        raise


def add_blog_post(title, post, tags, cookie):
    url = ''
    try:
        print("Trying to submit a post with title ", title)
        data = parse.urlencode([("body", post), ("subject", title), ("tags", tags)])
        url = "http://{0}/newpost".format(webhost)
        response = requests.post(url=url, data=data, cookies={'session': cookie})
        result = response.text
        expr = re.compile(title + ".+" + post, re.DOTALL)

        if expr.search(result):
            return True

        print("When we tried to post, here is the output we got\n")
        print(result)
        return False
    except:
        print("the request to ", url, " failed, so your blog may not be running.")
        raise


def add_blog_comment(title, post, cookie):
    url = ''
    try:
        print("Trying to submit a blog comment for post with title", title)
        url = "http://{0}/newcomment".format(webhost)
        
        doc = {}
        check_mongo_for_post(title, post, doc)

        permalink = doc['doc']['permalink']

        comment_name = make_salt(12)
        comment_body = make_salt(12)

        data = parse.urlencode(
            [("commentName", comment_name), ("commentBody", comment_body), ("permalink", permalink)]
        )
        response = requests.post(url=url, data=data, cookies={'session': cookie})
        result = response.text

        # check for successful addition of comment on page
        expr = re.compile(title + ".+" + post, re.DOTALL)

        if not expr.search(result):
            print("When we tried to find the comment we posted at the  ", url, " here is what we got")
            print(result)
            return False

        # check for successful addition of comment..retrieve the doc again
        if not check_mongo_for_post(title, post, doc):
            print("Could not find comment in database")
            return False
        
        found = False
        if 'comments' in doc['doc']:
            for comment in doc['doc']['comments']:
                if comment['body'] == comment_body and comment['author'] == comment_name:
                    found = True

        return found
    except:
        print("the request to ", url, " failed, so your blog may not be running.")
        raise


def check_blog_index(title1, title2, cookie):
    """
    grabs the blog index and checks that the posts appear in the right order
    """
    url = ''
    try:
        url = "http://{0}/".format(webhost)
        print("Trying to grab the blog home page at url ", url)
        response = requests.get(url=url, cookies={'session': cookie})
        result = response.text
        expr = re.compile(title2 + ".+" + title2, re.DOTALL)

        if expr.search(result):
            return True

        print("When we tried to read the blog index at ", url, " here is what we got")
        print(result)
        return False
    except:
        print("the request to ", url, " failed, so your blog may not be running.")
        raise


def check_mongo_for_post(title, body, document):
    """
    Check that a particular blog post is in the collection
    """
    
    posts = db.posts
    try:
        post = posts.find_one({'title': title, 'body': body})
        if post is None:
            print("Can't find post with title ", title, " in collection")
            return False
        document['doc'] = post
        return True
    except:
        print("can' query MongoDB..is it running?")
        raise


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
        elif opt in ("-p", ):
            webhost = arg
            print(f'Overriding HTTP host to be {webhost}')
        elif opt in ("-m", ):
            mongostr = arg
            print(f'Overriding MongoDB connection string to be {mongostr}')
        elif opt in ("-d", ):
            db_name = arg
            print(f'Overriding MongoDB database to be {db_name}')


def main(argv):
    arg_parsing(argv)
    global connection
    global db

    print("Welcome to the HW 2.3 validation tester")

    # connect to the db (mongostr was set in arg_parsing)
    connection = pymongo.MongoClient(mongostr)
    db = connection[db_name]

    username = make_salt(7)
    password = make_salt(8)

    # try to create user
    if create_user(username, password):
        print("User creation successful. ")
        # try to login
        cookie = try_to_login(username, password)
        if cookie:
            print("User login successful.")
            print("Validation Code is ", "jkfds5834j98fnm39njf0920f02")
        else:
            print("User login failed")
            print("Sorry, you have not solved it yet.")

    else:
        print("Sorry, you have not solved it yet.")
        sys.exit(1)

    # try to create a blog post
    post1 = make_salt(30)
    title1 = make_salt(30)
    tags1 = make_salt(5) + ", " + make_salt(5) + ", " + make_salt(5)

    if add_blog_post(title1, post1, tags1, cookie):
        print("Submission of single post successful")
    else:
        print("Unable to create a post")
        sys.exit(1)

    # try to create a second blog post
    post2 = make_salt(30)
    title2 = make_salt(30)
    tags2 = make_salt(5) + ", " + make_salt(5) + ", " + make_salt(5)

    if add_blog_post(title2, post2, tags2, cookie):
        print("Submission of second post successful")
    else:
        print("Unable to create second post")
        sys.exit(1)

    # now let's make sure that both posts appear on the home page
    # of the blog, in the correct order

    if check_blog_index(title1, title2, cookie):
        print("Block index looks good.")
    else:
        print("Blog index does not have the posts present, ordered correctly")
        sys.exit(1)

    # check for DB data integrity
    if not check_mongo_for_post(title1, post1, {}):
        print(f'Can\'t find blog post in blog db, posts collection with title {title}')
        sys.exit(1)
    else:
        print("Found blog post in posts collection")

    print("Tests Passed for HW 3.2. Your HW 3.2 validation code is 89jklfsjrlk209jfks2j2ek")

    # now check that you can post a comment
    if not add_blog_comment(title1, post1, cookie):
        print("Can't add blog comments (so HW 3.3 not yet complete)")
        sys.exit(1)
    else:
        print("Successfully added blog comments")

    print("Tests Passed for HW 3.3. Your HW 3.3 validation code is jk1310vn2lkv0j2kf0jkfs")


if __name__ == "__main__":
    main(sys.argv[1:])







