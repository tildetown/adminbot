import pinhook.plugin as plugin

@plugin.register('!modteam', help_text='This command lists out the current town IRC moderator roster. Responds in a PM.')
def adminteam(msg):
    msg.privmsg(msg.nick, 'In addition to !adminteam, the town IRC moderators are {}'.format(' '.join(msg.bot.modteam).strip()))
    return None
