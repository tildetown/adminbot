import pinhook.plugin as plugin

@plugin.command('!adminteam', help_text='This command lists out the current town admin roster. Responds in a PM.')
def adminteam(msg):
    msg.privmsg(msg.nick, 'The town admins are {}'.format(', '.join(msg.ops).strip()))
    return None
