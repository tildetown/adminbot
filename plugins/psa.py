import pinhook.plugin as p

@p.command('!psa', help_text='Usable only by the town admins, this causes adminbot to anonymously relay a message to #tildetown.')
def psa(msg):
    if msg.nick in msg.ops or msg.nick in msg.bot.modteam:
        msg.privmsg('#tildetown', '***** PSA: {}'.format(msg.arg))
        msg.privmsg('#announcements', '***** PSA: {}'.format(msg.arg))

