import json
import re
import threading
import os

from flask import Flask, request
from flask_httpauth import HTTPBasicAuth
import pinhook.bot
from werkzeug.security import check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()
with open('users.json') as u:
    USERS = json.load(u)

class AdminBot(pinhook.bot.Bot):
    townie_re = re.compile('townie-[a-f0-9]{16}')
    modteam = [
        'aliasless',
        'diodelasses',
        'spacecadet',
    ]

    def _add_known_nick(self, nick):
        nicks = self.known_nicks
        nicks.append(nick)
        nicks.sort()
        with open('known_nicks.json', 'w') as k:
            json.dump(nicks, k, indent=2)

    def _check_for_nick_file(self):
        if 'known_nicks.json' not in os.listdir():
            with open('known_nicks.json', 'w') as k:
                json.dump([], k)

    @property
    def known_nicks(self):
        self._check_for_nick_file()
        with open('known_nicks.json') as k:
            nicks = json.load(k)
        return nicks

    def on_join(self, c, e):
        nick = e.source.nick
        if nick not in self.known_nicks and e.target == '#tildetown' and not self.townie_re.match(nick):
            welcome = "Welcome, {}! I hope you're well. If you haven't seen it yet, please read over our wiki page about this chat: https://tilde.town/wiki/socializing/irc".format(nick)
            c.privmsg(nick, welcome)
            self._add_known_nick(nick)

    def on_invite(self, c, e):
        if e.arguments[0] in self.chanlist:
            c.join(e.arguments[0])
            self.logger.info('Joining {} at request of {}'.format(e.arguments[0], e.source))

    def call_help(self, op):
        # this is going to be handled by a listener plugin
        pass

@auth.verify_password
def verify_password(username, password):
    if username in USERS:
        return check_password_hash(USERS.get(username), password)
    return False

with open('pw.secret') as p:
    pw = p.read().strip()
with open('channels.json') as c:
    channels = json.load(c)
ops = [
    'vilmibm',
    'archangelic',
    'equa',
    'l0010o0001l'
]
bot = AdminBot(channels, 'adminbot', 'localhost', ops=ops, ns_pass=pw)

@app.route('/notify', methods=['POST'])
@auth.login_required
def notify_admins():
    channel = request.json['channel']
    message = request.json['message']
    bot.connection.privmsg(channel, message)

if __name__ == '__main__':
    bot_thread = threading.Thread(target=bot.start)
    bot_thread.start()
    flask_thread = threading.Thread(target=app.run)
    flask_thread.start()
