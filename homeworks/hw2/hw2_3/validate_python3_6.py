"""
This is a validation program to make sure that the blog works correctly.
If you are reading this in clear text, you are probably violating the honor code
"""

import pymongo
from urllib import request, parse
from http.cookiejar import CookieJar
import random
import re
import string
import sys
import getopt


# declare the variables to connect to db
connection = None
db = None

webhost = "localhost:8082"
mongostr = "mongodb://localhost:27017"
db_name = "blog"


# makes a little salt
def make_salt(n):
    salt = ""
    for i in range(n):
        salt = salt + random.choice(string.ascii_letters)
    return salt


def create_user(username, password):
    url = "http://{0}/signup".format(webhost)
    try:
        print(f'Trying to create a test user - {username}')
        cj = CookieJar()
        data = parse.urlencode(
            [("email", ""), ("username", username), ("password", password), ("verify", password)]
        )
        req = request.Request(url, data=data.encode())
        opener = request.build_opener(request.HTTPCookieProcessor(cj))
        f = opener.open(req)

        users = db.users
        user = users.find_one({'_id': username})
        if user is None:
            print(f'Could not find the test user {username} in the users collection.')
            return False
        print(f'Found the test user {username} in the users collection')

        # check that the user has been built
        result = f.read()
        expr = re.compile("Welcome\s+" + username)
        if expr.search(result.decode()):
            return True
        
        print("When we tried to create a user, here is the output we got\n")
        print(result)
        
        return False
    except Exception as e:
        print(f'The request to {url} failed, so your blog may not be running.')
        return False


def try_to_login(username, password):
    url = "http://{0}/login".format(webhost)
    try:
        print(f'Trying to login for test user: {username}')
        cj = CookieJar()
        data = parse.urlencode([("username", username), ("password", password)])
        req = request.Request(url=url, data=data.encode())
        opener = request.build_opener(request.HTTPCookieProcessor(cj))
        f = opener.open(req)

        # check for successful login
        result = f.read()
        expr = re.compile("Welcome\s+" + username)
        if expr.search(result.decode()):
            return True

        print("When we tried to login, here is the output we got\n")
        print(result)
        return False
    except:
        print(f'The request to {url} failed, so your blog may not be running.')
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
        if try_to_login(username, password):
            print("User login successful.")
            print("Validation Code is ", "jkfds5834j98fnm39njf0920f02")
        else:
            print("User login failed")
            print("Sorry, you have not solved it yet.")

    else:
        print("Sorry, you have not solved it yet.")
        sys.exit(1)


if __name__ == "__main__":
    main(sys.argv[1:])







