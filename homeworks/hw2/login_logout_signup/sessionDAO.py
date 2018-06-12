
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
"""
The session Data Access Object handles interactions with the sessions collection
"""

__author__ = 'aje'

import sys
import random
import string


class SessionDAO:

    def __init__(self, database):
        self.db = database
        self.sessions = database.sessions

    def start_session(self, username):
        """
        will start a new session id by adding a new document to
          the sessions collection returns the sessionID or None
        """

        session_id = self.get_random_str(32)
        session = {'username': username, '_id': session_id}

        try:
            self.sessions.insert_one(session)
        except Exception:
            print(f'Unexpected error on start_session: {sys.exc_info()[0]}')
            return None

        return str(session['_id'])

    def end_session(self, session_id):
        """ Will send a new user session by deleting from sessions table """

        if session_id:
            self.sessions.delete_one({'_id': session_id})

    def get_session(self, session_id):
        """ if there is a valid session, it is returned """
        if session_id:
            session = self.sessions.find_one({'_id': session_id})
            return session

    def get_username(self, session_id):
        """
        Get the username of the current session, or
          None if the session is not valid
        """
        session = self.get_session(session_id)
        if session:
            return session['username']

    def get_random_str(self, num_chars):
        random_string = ""
        for i in range(num_chars):
            random_string = random_string + random.choice(string.ascii_letters)

        return random_string
