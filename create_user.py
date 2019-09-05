#! /usr/bin/env python3

import getpass
import json

from werkzeug.security import generate_password_hash

with open('users.json') as u:
    users = json.load(u)

user = input('username> ')
password = getpass.getpass(prompt='password> ')

users[user] = generate_password_hash(password)

with open('users.json', 'w') as u:
    json.dump(users, u)