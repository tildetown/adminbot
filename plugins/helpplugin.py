import pinhook.plugin as plugin

@plugin.listener('help')
def help_plugin(msg):
    if msg.text.startswith('{}: !help'.format(msg.botnick)):
        cmds = sorted([c for c in plugin.cmds])
        for cmd in cmds:
            msg.privmsg(msg.nick, '{} {}'.format(cmd, plugin.cmds[cmd]['help']))
    return None # no need to inform the channel where the command was initiated
