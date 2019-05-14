import pinhook.plugin as plugin

@plugin.register('!mods', help_text="same as !admins but sends a message to the IRC moderators")
def mods(msg):
    output = '{} in {} says "{}"'.format(msg.nick, msg.channel, msg.arg)
    msg.privmsg('#mods-private', output)
    return plugin.message('{}: your message has been sent to the moderators!'.format(msg.nick))
