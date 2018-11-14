import pinhook.plugin as p

ADMINS = [
    'vilmibm',
    'archangelic'
]

@p.register('!psa')
def psa(msg):
    if msg.nick in ADMINS:
        msg.privmsg('#tildetown', '***** PSA: {}'.format(msg.text))

