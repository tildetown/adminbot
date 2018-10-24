# adminbot spec

This file documents both what adminbot does ambiently and what commands it responds to.

## Behaviors

### Welcome message

adminbot knows what users it has seen and which ones it hasn't. When an unrecognized user joins
`#tildetown`, adminbot welcomes them and gives some helpful hints.

```
--> | wren has joined
<adminbot> Welcome, wren! I hope you're well. If you haven't seen it yet, please read over our wiki
           page about this chat: https://tilde.town/wiki/socializing/irc
```

## Commands

### !rollcall

Reports its purpose and presence.

```
<wren> !rollcall
<adminbot> I act as a helper for the town's admins! For more info see https://github.com/tildetown/adminbot .
```

### !help

Returns a listing of this bot's commands. Responds in a private message, and only if directed to
adminbot itself.

In `#tildetown`:

```
<wren> i forget what adminbot does
<wren> but i'll ask it privately so as not to spam
<wren> adminbot: !help
```

In private message buffer:

```
<adminbot> !command0 helptext
<adminbot> !command1 helptext
<adminbot> !command2 helptext
```

### !adminteam

This command lists out the current town admin roster. Responds in a PM.

In `#tildetown`:

```
<wren> just to bug the admins i'm going to highlight them, watch
<wren> !adminteam
```

In private message buffer:

```
<adminbot> The town admins are vilmibm archangelic l0010o0001l equa
```

### !admins

This command sends a free-form message to town admins. It's relayed to their private admin channel.
Use this when you don't have a specific action item for the admins but just want to leave them a note.
Feel free to leave them a nice message.

In `#tildetown`:

```
<wren> !admins y'all are cute have a nice day :3
<adminbot> I've sent your message to the admins.
```

In `#admins-private`

```
<adminbot> wren in #tildetown says "y'all are cure have a nice day :3"
* vilmibm blushes
```

### !page

This command sends a push notification to an admin. **USE THIS SPARINGLY**. This command interrupts
an admin's day to day life and should only be used for server emergencies.

```
<wren> oh jeez the CPU is locked up i can barely type
<wren> !page there is a runaway process killing the CPU
<adminbot> Admin alerted!
```

### !ticket

This command opens up a help ticket. Use this command if you want an admin to take some specific
action.

```
<jillbob> i really love brainfuck but it's not installed
<wren> jillbob: you can open a ticket and ask for it to be installed with !ticket :)
<jillbob> oh joy!
<jillbob> !ticket install brainfuck package please
<adminbot> Ticket #123 created!
```

### !psa

Usable only by the town admins, this causes adminbot to anonymously relay a message to `#tildetown`.

In `#admins-private`:

```
<vilmibm> !psa hi everyone yr cute
```

In `#tildetown`:

```
<adminbot> ***** PSA: hi everyone yr cute
* wren blushes
```
