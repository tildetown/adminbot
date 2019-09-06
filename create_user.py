#! /usr/bin/env python3
import getpass
import json
import os

from werkzeug.security import generate_password_hash

if 'users.json' in os.listdir():
    with open('users.json') as u:
        users = json.load(u)
else:
    with open('users.json', 'w') as u:
        json.dump({}, u)
    os.chmod('users.json', 0o600)
    users = {}

user = input('username> ')
password = getpass.getpass(prompt='password> ')

users[user] = generate_password_hash(password)

with open('users.json', 'w') as u:
    json.dump(users, u)