---
title: monerod --help screen window opens and then closes automatically
source_url: https://github.com/monero-project/monero/issues/2653
author: shmacoshmuesday
assignees: []
labels:
- invalid
created_at: '2017-10-14T13:34:26+00:00'
updated_at: '2017-11-24T17:56:23+00:00'
type: issue
status: closed
closed_at: '2017-11-24T17:56:23+00:00'
---

# Original Description
Windows 8 x64
Monero 11.0.0 

When I run monerod --help (or monerod.exe --help) it opens a second window with the help text, but it just flashes up briefly, runs through the help file and closes immediately. 

I've also tried adding |more to it, which does work for other windows commands, but apparently |more can't be appended to the --help argument in windows.

# Discussion History
## moneromooo-monero | 2017-10-14T13:42:09+00:00
Where you are running monerod --help ? From a terminal ?

## shmacoshmuesday | 2017-10-14T14:04:40+00:00
Correct, wanted to add some arguments at startup and so did --help in the console from within the 11.0.0 directory and ran into this.


## moneromooo-monero | 2017-10-14T14:20:57+00:00
That does sound like another windows weirdness tbh. monerod doesn't run terminals, so it's the OS choosing to do so.

## shmacoshmuesday | 2017-10-14T14:46:18+00:00
That makes sense because when I run just monerod.exe it does pop up another window but in that case the new terminal window stays up. 

If I just double-click on monerod.exe it pops up a terminal window reporting the current status (even reports smart mining cpu usage which is an excellent feature) and allows commands such as status and exit. Sorry if I'm stating the obvious but just giving my experience with the monerod terminal in windows. (Wishing there was a way to minimize that to the tray)

## moneromooo-monero | 2017-10-14T15:36:26+00:00
When you say "reporting the current status", you mean it does that when you run the status command, right ? Not unprompted ?

## shmacoshmuesday | 2017-10-14T20:03:37+00:00
Sorry right, when I say current status I just mean it does the same as the linux monerod terminal in that it gives you info on what's happening, not the same info as when you type status. But typing the status command works and give you the correct status info. So it's just like the linux monerod terminal but  pops up in its own window.

## moneromooo-monero | 2017-10-14T20:06:26+00:00
I wonder if that's actually monerod or not. It's unclear from your description. If it's another program, then it might indeed spawn terminals.

## shmacoshmuesday | 2017-10-14T20:34:30+00:00
Sorry if my description is unclear but it's definitely monerod. Here's a step by step. If I open a command prompt and then run monerod (being in the right directory or specifying the right directory) then another terminal or command window will pop up with details for monerod, saying things such as that it's starting to sync, whether it finds valid checkpoints (I think that's the verbiage) etc. In the original window the monerod command looks like it's completed and you're at another command line. In the new terminal window you can see how the monerod command is doing and you can type in commands such as status or exit and it monerod will respond with the expected output. 

## shmacoshmuesday | 2017-10-14T20:38:09+00:00
The problem that I'm reporting though is that on the command line, if I run it as monerod --help, then that second window will pop up, scroll through the help, and then close right away. I've found that adding /k to a command (guessing I'd have to run this in the 'run' window) will keep the terminal from closing immediately. I'm going to try that later when I have a little more time

## MaxXor | 2017-10-15T08:02:35+00:00
I can't reproduce this on Windows 8 32bit. When I type `monerod --help` in the terminal it outputs the help text in the same window. Also when I run `monerod` it runs in the same terminal and doesn't open a new window.

## shmacoshmuesday | 2017-10-15T12:19:22+00:00
interesting, I'm on 8.1 64 bit. Thought maybe there was an O/S setting or something about open commands in new terminal window or something but haven't found anything yet, aside from adding /k

## moneromooo-monero | 2017-11-24T17:40:09+00:00
/k is certainly not a monerod option. This behaviour seems to be something unrelated to monero.

+invalid


# Action History
- Created by: shmacoshmuesday | 2017-10-14T13:34:26+00:00
- Closed at: 2017-11-24T17:56:23+00:00
