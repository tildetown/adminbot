import pinhook.plugin as p

@p.command('!etiquette', help_text='show the etiquette link')
def etiquette(msg):
    output = '{}: the etiquette can be found here: https://tilde.town/wiki/etiquette.html'.format(msg.nick)
    return p.message(output)
