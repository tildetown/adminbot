import pinhook.plugin as p

@p.register('!psa', help_text='Usable only by the town admins, this causes adminbot to anonymously relay a message to #tildetown.')
def psa(msg):
    if msg.nick in msg.ops:
        msg.privmsg('#tildetown', '***** PSA: {}'.format(msg.arg))

