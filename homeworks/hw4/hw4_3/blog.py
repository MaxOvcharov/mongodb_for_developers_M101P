# Copyright (c) 2008 - 2013 10gen, Inc. <http://10gen.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""
General Discussion on structure. This program implements a blog. This file is the best place to start to get
to know the code. In this file, which is the controller, we define a bunch of HTTP routes that are handled
by functions. The basic way that this magic occurs is through the decorator design pattern. Decorators
allow you to modify a function, adding code to be executed before and after the function. As a side effect
the bottle.py decorators also put each callback into a route table.

These are the routes that the blog must handle. They are decorated using bottle.py

This route is the main page of the blog
"""

__author__ = 'aje'

import os
import re
from html import escape

import pymongo
import bottle
import userDAO
import sessionDAO
import blogPostDAO

PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
USER_RE = re.compile(r'^[a-zA-Z0-9_-]{3,20}$')
PASS_RE = re.compile(r'^.{3,20}$')
EMAIL_RE = re.compile(r'^[\S]+@[\S]+\.[\S]+$')


@bottle.route('/')
def blog_index():

    cookie = bottle.request.get_cookie('session')

    username = sessions.get_username(cookie)

    # even if there is no logged in user, we can show the blog
    logged_user = posts.get_posts(10)

    return bottle.template(
        PROJECT_PATH + '/views/blog_template',
        dict(myposts=logged_user, username=username)
    )


@bottle.route('/tag/<tag>')
def posts_by_tag(tag="notfound"):
    """ The main page of the blog, filtered by tag """
    cookie = bottle.request.get_cookie("session")
    tag = escape(tag)

    username = sessions.get_username(cookie)

    # even if there is no logged in user, we can show the blog
    posts_by_tag = posts.get_posts_by_tag(tag, 10)

    return bottle.template(
        PROJECT_PATH + 'blog_template',
        dict(myposts=posts_by_tag, username=username)
    )


@bottle.get('/post/<permalink>')
def show_post(permalink='notfound'):
    """ Displays a particular blog post """

    cookie = bottle.request.get_cookie('session')

    username = sessions.get_username(cookie)
    permalink = escape(permalink)

    print(f'about to query on permalink = {permalink}')
    post = posts.get_post_by_permalink(permalink)

    if post is None:
        bottle.redirect('/post_not_found')

    # init comment form fields for additional comment
    comment = {'name': '', 'body': '', 'email': ''}

    return bottle.template(
        PROJECT_PATH + '/views/entry_template',
        dict(post=post, username=username, errors='', comment=comment)
    )


@bottle.post('/newcomment')
def post_new_comment():
    """ Used to process a comment on a blog post """
    name = bottle.request.forms.get('commentName')
    email = bottle.request.forms.get('commentEmail')
    body = bottle.request.forms.get('commentBody')
    permalink = bottle.request.forms.get('permalink')

    post = posts.get_post_by_permalink(permalink)
    cookie = bottle.request.get_cookie('session')

    username = sessions.get_username(cookie)

    # if post not found, redirect to post not found error
    if post is None:
        bottle.redirect('/post_not_found')
        return

    # if values not good, redirect to view with errors

    if name == '' or body == '':
        # user did not fill in enough information

        # init comment for web form
        comment = {'name': name, 'email': email, 'body': body}

        errors = 'Post must contain your name and an actual comment.'
        return bottle.template(
            PROJECT_PATH + '/views/entry_template',
            dict(post=post, username=username, errors=errors, comment=comment)
        )

    else:
        # it all looks good, insert the comment into the blog post
        # and redirect back to the post viewer
        posts.add_comment(permalink, name, email, body)
        bottle.redirect('/post/' + permalink)


@bottle.get('/post_not_found')
def post_not_found():
    return 'Sorry, post not found'


@bottle.get('/newpost')
def get_newpost():
    """
    Displays the form allowing a user to add a new post.
      Only works for logged in users
    """

    cookie = bottle.request.get_cookie('session')
    username = sessions.get_username(cookie)  # see if user is logged in
    if username is None:
        bottle.redirect('/login')

    return bottle.template(
        PROJECT_PATH + '/views/newpost_template',
        dict(subject='', body='', errors='', tags='', username=username)
    )


@bottle.post('/newpost')
def post_newpost():
    """
    Post handler for setting up a new post.
      Only works for logged in user.
    """
    title = bottle.request.forms.get('subject')
    post = bottle.request.forms.get('body')
    tags = bottle.request.forms.get('tags')

    cookie = bottle.request.get_cookie('session')
    username = sessions.get_username(cookie)  # see if user is logged in
    if username is None:
        bottle.redirect('/login')

    if title == '' or post == '':
        errors = 'Post must contain a title and blog entry'
        return bottle.template(
            PROJECT_PATH + '/views/newpost_template',
            dict(subject=escape(title, quote=True),
                 username=username, body=escape(post, quote=True),
                 tags=tags, errors=errors)
        )

    # extract tags
    tags = escape(tags)
    tags_array = extract_tags(tags)

    # looks like a good entry, insert it escaped
    escaped_post = escape(post, quote=True)

    # substitute some <p> for the paragraph breaks
    newline = re.compile('\r?\n')
    formatted_post = newline.sub('<p>', escaped_post)

    permalink = posts.insert_entry(title, formatted_post, tags_array, username)

    # now bottle.redirect to the blog permalink
    bottle.redirect('/post/' + permalink)


@bottle.get('/signup')
def present_signup():
    """ Displays the initial blog signup form """
    return bottle.template(PROJECT_PATH + '/views/signup',
                           dict(username='', password='',
                                password_error='',
                                email='', username_error='', email_error='',
                                verify_error=''))


@bottle.get('/login')
def present_login():
    """ Displays the initial blog login form """
    return bottle.template(PROJECT_PATH + '/views/login',
                           dict(username='', password='', login_error=''))


@bottle.post('/login')
def process_login():
    """ Handles a login request """

    username = bottle.request.forms.get('username')
    password = bottle.request.forms.get('password')

    print(f'user submitted: {username}, pass: {password}')

    user_record = users.validate_login(username, password)
    if user_record:
        # username is stored in the user collection in the _id key
        session_id = sessions.start_session(user_record['_id'])

        if session_id is None:
            bottle.redirect('/internal_error')

        cookie = session_id

        # Warning, if you are running into a problem whereby the
        # cookie being set here is not getting set on the redirect,
        # you are probably using the experimental version of bottle (.12).
        # revert to .11 to solve the problem.
        bottle.response.set_cookie('session', cookie)

        bottle.redirect('/welcome')

    else:
        return bottle.template(PROJECT_PATH + '/views/login',
                               dict(username=escape(username), password='',
                                    login_error='Invalid Login'))


@bottle.get('/internal_error')
@bottle.view('error_template')
def present_internal_error():
    return {'error': 'System has encountered a DB error'}


@bottle.get('/logout')
def process_logout():

    cookie = bottle.request.get_cookie('session')

    sessions.end_session(cookie)

    bottle.response.set_cookie('session', '')

    bottle.redirect('/signup')


@bottle.post('/signup')
def process_signup():

    email = bottle.request.forms.get('email')
    username = bottle.request.forms.get('username')
    password = bottle.request.forms.get('password')
    verify = bottle.request.forms.get('verify')

    # set these up in case we have an error case
    errors = {'username': escape(username), 'email': escape(email)}
    if validate_signup(username, password, verify, email, errors):

        if not users.add_user(username, password, email):
            # this was a duplicate
            errors['username_error'] = 'Username already in use. Please choose another'
            return bottle.template('signup', errors)

        session_id = sessions.start_session(username)
        print(session_id)
        bottle.response.set_cookie('session', session_id)
        bottle.redirect('/welcome')
    else:
        print('user did not validate')
        return bottle.template(PROJECT_PATH + '/views/signup', errors)


@bottle.get('/welcome')
def present_welcome():
    """ Check for a cookie, if present, then extract value """

    cookie = bottle.request.get_cookie('session')
    username = sessions.get_username(cookie)  # see if user is logged in
    if username is None:
        print('welcome: can\'t identify user...redirecting to signup')
        bottle.redirect('/signup')

    return bottle.template(PROJECT_PATH + '/views/welcome', {'username': username})


# Helper Functions

def extract_tags(tags):
    """
    Extracts the tag from the tags form element. an experience
      python programmer could do this in  fewer lines, no doubt
    """

    whitespace = re.compile('\s')

    nowhite = whitespace.sub('', tags)
    tags_array = nowhite.split(',')

    # let's clean it up
    cleaned = {tag for tag in tags_array if tag != ''}
    return tuple(cleaned)


def validate_signup(username, password, verify, email, errors):
    """
    Validates that the user information is valid for new signup,
      return True of False and fills in the error string if
      there is an issue
    """
    errors['username_error'] = ''
    errors['password_error'] = ''
    errors['verify_error'] = ''
    errors['email_error'] = ''

    if not USER_RE.match(username):
        errors['username_error'] = 'invalid username. try just letters and numbers'
        return False

    if not PASS_RE.match(password):
        errors['password_error'] = 'invalid password.'
        return False
    if password != verify:
        errors['verify_error'] = 'password must match'
        return False
    if email != '':
        if not EMAIL_RE.match(email):
            errors['email_error'] = 'invalid email address'
            return False
    return True


connection_string = 'mongodb://localhost'
connection = pymongo.MongoClient(connection_string)
database = connection.blog

posts = blogPostDAO.BlogPostDAO(database)
users = userDAO.UserDAO(database)
sessions = sessionDAO.SessionDAO(database)


bottle.debug(True)
bottle.run(host='localhost', port=8082)         # Start the webserver running and wait for requests

