import pinhook.plugin as p

ADMINS = [
    'vilmibm',
    'archangelic'
]

@p.register('!psa', help_text='Usable only by the town admins, this causes adminbot to anonymously relay a message to #tildetown.')
def psa(msg):
    if msg.nick in ADMINS:
        msg.privmsg('#tildetown', '***** PSA: {}'.format(msg.text))

