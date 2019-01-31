import pinhook.plugin as p

help_text = ("This command sends a free-form message to town admins. "
             "It's relayed to their private admin channel. "
             "Use this when you don't have a specific action item for the admins but just want to "
             "leave them a note. Feel free to leave them a nice message.")

@p.register('!admins', help_text=help_text)
def admins(msg):
    output = '{} in {} says "{}"'.format(msg.nick, msg.channel, msg.arg)
    msg.privmsg('#admins-private', output)
    return p.message('{}: your message has been sent to the admins!'.format(msg.nick))
