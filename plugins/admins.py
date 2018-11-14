import pinhook.plugin as p

@p.register('!admins')
def admins(msg):
    output = '{} in {} says "{}"'.format(msg.nick, msg.channel, msg.text)
    msg.privmsg('#admins-private', output)
    return p.message('{}: your message has been sent to the admins!'.format(msg.nick))
