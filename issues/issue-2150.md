---
title: 'readline: some commands are ignored'
source_url: https://github.com/monero-project/monero/issues/2150
author: moneromooo-monero
assignees: []
labels: []
created_at: '2017-07-05T14:22:07+00:00'
updated_at: '2017-07-06T13:19:06+00:00'
type: issue
status: closed
closed_at: '2017-07-06T13:12:14+00:00'
---

# Original Description
Sometimes, commands are ignored. Press enter after a command, and nothing happens. A subsequent command will be executed, so it's not like it's timing out waiting on a lock (this can happen, and is something unrelated entirely - when needing the blockchain lock while syncing, for instance). Might be related to #2117. This is rare-ish, but happens a few times daily.

# Discussion History
## jtgrassie | 2017-07-05T17:56:54+00:00
Was the command added to the history though? That might help isolate whats going on.

## moneromooo-monero | 2017-07-05T20:14:56+00:00
I don't know. If it happens again, I'll check and report.

## moneromooo-monero | 2017-07-05T20:18:17+00:00
It does. I just tried it, running commands a, b, c, d... q was not run (ie, I did not get an error for q), but it got added to the history.

## jtgrassie | 2017-07-06T00:51:42+00:00
Right, so if it's adding to history, is readline verified as the problem? Reason I say is this... to get added to history, the condition var would notify and get_line would return the command to calling code.

## jtgrassie | 2017-07-06T01:23:12+00:00
`q` for some odd reason appears to be translated to quit/exit for me.


## jtgrassie | 2017-07-06T01:26:55+00:00
Unknown commands are certainly showing funky results though. Sometimes the cursor is midway inside the prompt. That maybe a red herring but I'll take a look at fixing that anyway.

## jtgrassie | 2017-07-06T01:30:43+00:00
OK so q is a valid command for exit:
```
else if(0 == command.compare("exit") || 0 == command.compare("q"))
```

## moneromooo-monero | 2017-07-06T10:54:14+00:00
Ah, I'd forgot about that :) Still, it should have quit, and it didn't.

## moneromooo-monero | 2017-07-06T10:56:29+00:00
q is actually a dud command, it never quits here. I guess something else compares with "exit" elsewhere. I'll try to repro again.

## moneromooo-monero | 2017-07-06T11:05:33+00:00
I can get it to happen while I'm syncing, so while the blockchain lock has high contention (and the commands wait for that lock). if I send two commands in quick succession, like "status" and "print_cn" just after a "Synced" message. I'll only get the status output. I'd need to revert all the readline stuff again to double check it does work then though, since while I don't remember that being the case in the past, I don't think I particularly tried to do this.

There's also some weird extra characters sometimes popping up on messages. I'd never seen that before, and I'm in a mind to blame the readline patches, but I do not have clear evidence they're related:

T�Height: 4401/947885 (0.5%) on testnet, not mining, net hash 340 H/s, v1, up to date, 2(out)+0(in) connections, uptime 0d 0h 2m 16s�

Usually, I only see the one extra char at the end. I'd never seen them at start of line before. Maybe it's the readline prompt getting printed at the same time as the actual output ?


## jtgrassie | 2017-07-06T11:30:08+00:00
>  I'd need to revert all the readline stuff again to double check

Its fairly easy to just switch readline off as theres a CMake option `USE_READLINE` which you can switch to OFF when running cmake. That way we can at least confirm when an issue is readline related or not.

The extra characters _could_ be readline related (and I would also be in a mind to blame it!) as it does have to hijack the input and output streams and at the same time allow the logging to continuing working without a huge refactor. I've not seen this character issue ever though.

> Still, it should have quit, and it didn't.

Yes I have seen exit delays occasionally too. Even with are recent work trying to solve that. I'm not convinced this is readline though as I have seen delays exiting without readline switched on.



## moneromooo-monero | 2017-07-06T12:20:35+00:00
Delays exiting are fine, as long as you see a "Stop signal sent" message.

## jtgrassie | 2017-07-06T12:31:34+00:00
When exiting wallet or daemon? I only ever see that output when stopping the daemon. The wallet doesn't output the message when exiting.

## moneromooo-monero | 2017-07-06T12:44:11+00:00
Actually, I was too cynical. After rebuilding without readline, the problem still happens, so it's inherited.
I don't get any extra characters though, so those two things are unrelated.
I can either change the bug subject, or close and reopen.

## moneromooo-monero | 2017-07-06T12:44:30+00:00
I was exiting the daemon.

## jtgrassie | 2017-07-06T13:09:03+00:00
> I can either change the bug subject, or close and reopen.

It would be helpful for me if the character issue can be it's own issue, so recommend closing this. I'm struggling to keep track of the specific issues!

Thanks

## moneromooo-monero | 2017-07-06T13:15:43+00:00
Done, I've created two separate bugs for those, and added my testing without readline for the ignored command one.

## jtgrassie | 2017-07-06T13:19:06+00:00
Many thanks

# Action History
- Created by: moneromooo-monero | 2017-07-05T14:22:07+00:00
- Closed at: 2017-07-06T13:12:14+00:00
