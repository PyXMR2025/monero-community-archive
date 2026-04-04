---
title: CTRL+C stops the CLI wallet
source_url: https://github.com/monero-project/monero/issues/4681
author: tmoravec
assignees: []
labels:
- invalid
created_at: '2018-10-21T08:49:05+00:00'
updated_at: '2018-11-17T17:58:11+00:00'
type: issue
status: closed
closed_at: '2018-11-16T23:25:01+00:00'
---

# Original Description
When users press CTRL+C in Bash, it clears whatever is written on the command line and gives a new prompt instead. Similarly in Python and Jupyter, and many other interactive CLI utilities.

In monero-wallet-cli, CTRL+C exits the program instead, which is somewhat unintuitive (muscle memory etc.) . If you think this is worth fixing, I offer to try to change that.

# Discussion History
## moneromooo-monero | 2018-10-21T08:56:15+00:00
This is on purpose.

## moneromooo-monero | 2018-10-21T09:01:04+00:00
Though if consensus is to stop this, I'm OK with the change (which is trivial, just SIG_IGN it).
It's canonical for ^C to stop the program though (with the difference that simplewallet saves when this happens, whereas you might expect a kill without saving, but I thought the potential for data loss was too high).

## fluffypony | 2018-10-21T09:02:54+00:00
I would definitely push back on this. Monero isn’t a shell, it’s a userland application and should be terminated by ctrl-c.

## tmoravec | 2018-10-21T09:22:51+00:00
So what's the “easy” way to clear what's written on in the command line? For example when users realize they pasted a wrong address, holding Backspace for half a minute is the only way?

BTW shell is a userland application too. So is Python REPL. Or Midnight Commander. Or bc. Or virtually any readline application. You are right about the SIGINT meaning, but I believe this is a usability tradeoff.

## fluffypony | 2018-10-21T09:26:06+00:00
@tmoravec the correct way of clearing the line in bash is ctrl-u, not ctrl-c. If that doesn’t work on Monero then that’s something that should be investigated.

## moneromooo-monero | 2018-10-21T09:45:16+00:00
bc ends with ^C fwiw :P

I usually ctrl arrow and ^W to fix part of a command line. Down arrow to clear. I guess it's down to what you're used to though.

I suppose there could be a setting to control this (though there are no settings for monerod).


## heavenly | 2018-10-21T15:05:31+00:00
CTRL C normally closes a program

## hyc | 2018-10-21T15:56:44+00:00
@tmoravec Please learn how to use your terminal. Read the stty(1) manpage. As fluffypony already said, Ctrl-U is the default keycode for deleting an entire input line, but you can set it to anything you want.

## thomasvaughan | 2018-10-22T12:11:15+00:00
@tmoravec To supplement suggestion from @hyc , ~/.inputrc is also honoured (tested by using vi key-bindings inside inside monero-wallet-cli).

## tmoravec | 2018-10-22T13:27:53+00:00
The point was not anybody's particular muscle memory, but consistency with other command-line based applications, including the contested bc (see below :) ) . In either case, if the general consensus is to keep the current behavior, feel free to close this issue. At least it's documented now.



```
 $ bc
bc 1.07.1
Copyright 1991-1994, 1997, 1998, 2000, 2004, 2006, 2008, 2012-2017 Free Software Foundation, Inc.
This is free software with ABSOLUTELY NO WARRANTY.
For details type `warranty'.
^C
(interrupt) use quit to exit.
quit
$
```

## moneromooo-monero | 2018-11-07T14:19:43+00:00
lol, I use 1.07.1 too. How weird. I suspect either Fedora or your distro changed something about this then.


## screab-idh | 2018-11-10T23:30:54+00:00
I use Ctrl-C to abnormally terminate many programs for at least 10 years. Ctrl-C sends a SIGINT signal to the process. Applications that didn't override the [default behavior](
http://pubs.opengroup.org/onlinepubs/9699919799/basedefs/signal.h.html) will interpret SIGINT as a terminating signal, thus terminating the process. 


@tmoravec What operating system are you using ? I want to use this as the A+ question for my students at the end of this semester.


Also, may I point to the fact that I've read the entire conversation and this looks like sarcasm.
> The point was not anybody's particular muscle memory

Please, refrain from sarcasm :) 

## anonimal | 2018-11-13T16:56:13+00:00
>Please, refrain from sarcasm :)

Ancient astronaut theorists have shown that, when translated correctly, Monero is the Esperanto word for "the great sarcasm". True story.

## moneromooo-monero | 2018-11-16T23:16:08+00:00
Most seem to prefer it that way, closing.

+invalid

## trasherdk | 2018-11-17T17:58:11+00:00
On Slackware 14.2
```bash
# bc
bc 1.06.95
Copyright 1991-1994, 1997, 1998, 2000, 2004, 2006 Free Software Foundation, Inc.
This is free software with ABSOLUTELY NO WARRANTY.
For details type `warranty'. 
^C
(interrupt) Exiting bc.
#
```
And that's how it's always been :)


# Action History
- Created by: tmoravec | 2018-10-21T08:49:05+00:00
- Closed at: 2018-11-16T23:25:01+00:00
