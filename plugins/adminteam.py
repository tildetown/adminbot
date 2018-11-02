import pinhook.plugin as plugin

@plugin.register('!adminteam', 'This command lists out the current town admin roster. Responds in a PM.')
def adminteam(msg):
    admins = [
        'vilmibim',
        'archangelic',
        'l0010o0001l',
        'karlen',
        'equa'
    ]
    msg.privmsg(msg.nick, 'The town admins are {}'.format(' '.join(adminteam).strip()))
    return None
