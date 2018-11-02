import pinhook.plugin as plugin

@plugin.register('!rollcall', help_text='Gives a short message about what this bot does')
def rollcall(msg):
    return plugin.message("I act as a helper for the town's admins! For more info see https://github.com/tildetown/adminbot .")

