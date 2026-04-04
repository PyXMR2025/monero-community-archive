---
title: Segmentation fault on freshly compiled v0.16
source_url: https://github.com/monero-project/monero/issues/6602
author: kalibox
assignees: []
labels: []
created_at: '2020-05-31T02:15:01+00:00'
updated_at: '2020-10-22T14:31:26+00:00'
type: issue
status: closed
closed_at: '2020-10-22T14:31:26+00:00'
---

# Original Description
Hi, I've just built the new daemon via pulling the git down and it completed successfully without any errors. Upon running it, it launches OK but crashes out. Error message is:

Segmentation fault 

I have the following switches on and run a local shell script to launch the daemon:

--data-dir 
--rpc-bind-ip
--rpc-bind-port
--confirm-external-bind
--log-level  
--max-log-files 5

Thoughts please?

Thanks


# Discussion History
## kalibox | 2020-05-31T02:19:35+00:00
Edit: looking at logs I see this:

2020-05-31 02:18:37.243 E Setting timer on a shut down object

Thanks.

## kalibox | 2020-05-31T02:28:12+00:00
And these:

2020-05-31 02:26:21.783 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:133  Exception: std::runtime_error
2020-05-31 02:26:21.783 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:134  Unwound call stack:
2020-05-31 02:26:21.786 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:172      [1]  0x113) [0x5582a544fd50]:__cxa_throw+0x113) [0x5582a544fd50]


## vtnerd | 2020-05-31T05:54:51+00:00
This is very little information. Is it possible to post anything more from the log?

## kalibox | 2020-05-31T07:39:33+00:00
Hi, thanks for the reply. Yes, sure. Let me know what you need and I'll get it for you.

Thanks.

## moneromooo-monero | 2020-05-31T10:50:50+00:00
gdb /path/to/monerod core

Use the path to monerod, and the name of the core file. Might have numbers after it (ig, core.4832).
If your OS does not generate core files:
ulimit -c unlimited
echo core | sudo tee /proc/sys/kernel/core_pattern

Then try again.

Once in gdb after it crashed:

bt

Then post the multi page output.


## moneromooo-monero | 2020-05-31T10:51:25+00:00
And the last ~100 lines of the log.

## kalibox | 2020-06-01T15:25:33+00:00
Thanks. I've not done this before so not sure if I would end up doxxing myself. Does this produce any identifiable information?

Edit: also, just to add the DB is from v0.15. Do I need to resync the chain?

Edit#2: just to compare, I've rebuilt v0.15.0.5 and it still runs flawlessly. Not sure but my amateur guess is that some in the new code needs reviewing? Thank you anyway, very appreciative of the community.

## moneromooo-monero | 2020-06-01T17:51:32+00:00
There'll be the path to wherever you put monero. This likely includes your home directory. Feel free to replace it with a placeholder. That should be all.

You do not need to resync the chain (unless it's corrupted somehow, but that's orthogonal to the version).


## moneromooo-monero | 2020-10-15T22:43:45+00:00
ping ?

## kalibox | 2020-10-15T23:11:47+00:00
Hey @moneromooo-monero, we can defo close this issue as v0.17.x has fixed my issues I had with v0.16. All good now. Many thanks.

## moneromooo-monero | 2020-10-22T14:31:26+00:00
Alright, good to know.

# Action History
- Created by: kalibox | 2020-05-31T02:15:01+00:00
- Closed at: 2020-10-22T14:31:26+00:00
