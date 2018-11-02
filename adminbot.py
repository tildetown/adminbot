import json
import os

import pinhook.bot

class AdminBot(pinhook.bot.Bot):
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
        if nick not in self.known_nicks and e.target == '#tildetown':
            welcome = "Welcome, {}! I hope you're well. If you haven't seen it yet, please read over our wiki page about this chat: https://tilde.town/wiki/socializing/irc".format(nick)
            c.privmsg(nick, welcome)
            self._add_known_nick(nick)

    def call_help(self):
        # this is going to be handled by a listener plugin
        pass


if __name__ == '__main__':
    channels = [
        '#tildetown',
        '#admins',
        '#admins-private'
    ]
    ops = [
        'vilmibm',
        'archangelic'
    ]
    bot = AdminBot(channels, 'adminbot', 'localhost', ops=ops)
    bot.start()
