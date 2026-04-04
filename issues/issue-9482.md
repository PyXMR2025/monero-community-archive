---
title: monerod exit gets stuck/hangs at deinitializing p2p; network connection activity
  continues in background; command window will not close and cannot force process
  to close
source_url: https://github.com/monero-project/monero/issues/9482
author: mmortal03
assignees: []
labels:
- question
- discussion
- reproduction needed
- more info needed
created_at: '2024-09-14T22:03:55+00:00'
updated_at: '2026-02-18T21:51:05+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
This has been happening for years, but because it's difficult to debug the Windows version of monerod and because the issue itself is hard to reproduce every single time, I haven't gotten around to creating an issue report here.

What generally happens (and it just happened to me again today) is that I will run monerod for a while (maybe 12 hours) until it is fully synced, and then I will run the exit command. The exiting steps get to the point of deinitializing p2p, and there it remains stuck. At this point, I will wait maybe 20 minutes, then try clicking the X to close the command window, which will cause it to display the red text warning message (I forget what it says), but the window doesn't close. 

If I go into Task Manager and try to force close monerod.exe, I get a popup window saying, "Unable to terminate process", "The operation could not be completed.", "Access is denied."

And something new to add that I just noticed today is that when I go into Resource Monitor after it gets stuck, monerod.exe continues to show network activity and numerous TCP connections, so, clearly, the deinitializing of p2p doesn't fully complete wherever in the actual code that it gets stuck. 

Furthermore, I tried using a 3rd party tool such as CurrPorts to manually close out all of these network connections, but this didn't help in terms of closing the monerod.exe process. I think it might've lowered the remaining memory use of monerod.exe, but it still wouldn't close or be forced to close.
 
Ultimately, the only way I've found to get the process to actually close is to reboot the computer.

I'll run it again today and see if I can capture a log at level 0 to see if there's anything there that might help. (I usually don't run monerod with logging enabled.)

# Discussion History
## 0xFFFC0000 | 2024-09-15T16:29:18+00:00
I believe I have encountered this. Though I haven't debugged it to be 100% sure where and why this happens. 


I am suspicious of Miniupnpc, but that is just suspicion. 

## moneromooo-monero | 2024-11-27T12:02:14+00:00
Can you run a debugger when in that state, to see if one of the threads is somehow stuck somewhere ?

## mmortal03 | 2024-11-29T18:22:04+00:00
> Can you run a debugger when in that state, to see if one of the threads is somehow stuck somewhere ?

I recall trying to debug another issue some years ago on Windows, an issue that was more reproducible, but it ended up being something that wasn't able to be debugged on Windows.

In this case, since it happens infrequently, without clear steps to reproduce, I'd have to always run my node through a debugger, which doesn't seem practical. In the meantime, I've been running the node with logging each time I sync it (about once a week), but haven't caught it in the act yet. I've also had a screen recording tool going each time, just in case that might catch it, but so far, no luck. I hate these kind of intermittent issues. It could very well be some quirk with the dependencies and how they operate on the Windows side of things, like what was said above, possibly something to do with Miniupnpc. It's of a similar theme to the past issue that we could never figure out, involving zeromq, but at least that one was easier to reproduce.

# Action History
- Created by: mmortal03 | 2024-09-14T22:03:55+00:00
