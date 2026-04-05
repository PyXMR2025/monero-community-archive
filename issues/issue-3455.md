---
title: Personal log doesn't work with --background
source_url: https://github.com/xmrig/xmrig/issues/3455
author: maravento
assignees: []
labels:
- bug
- libuv
created_at: '2024-04-02T14:10:50+00:00'
updated_at: '2025-06-16T19:44:32+00:00'
type: issue
status: closed
closed_at: '2025-06-16T19:44:32+00:00'
---

# Original Description
**Describe the bug**
Personal log doesn't work with --background

**To Reproduce**
```
sudo ./xmrig --algo=rx/0 --url=rx.unmineable.com:3333 --user=$coin:$address.$worker --keepalive --threads=2 --background --log-file=/home/user/my_log.log
```
No logs in "my_log.log
If I delete "--background" the records appear in the terminal and in the "my_log.log"

```
user@mst:~$ ls -l my_log.log
-rwxrwxrwx 1 user user 0 abr  3 09:17 my_log.log
```

**Expected behavior**
That the logs be saved in the custom log `my_log.log` and can use the `--background` option, so that nothing appears in the console

**Required data**
 - XMRig version 6.21.2
 - OS: Ubuntu 22.04
 - CPU Intel Xeon

**Workaround**

replace personal log with `--syslog`

```
sudo ./xmrig --algo=rx/0 --url=rx.unmineable.com:3333 --user=$coin:$address.$worker --keepalive --threads=2 --background --syslog
```

# Discussion History
## SnAFKe | 2024-06-03T17:58:43+00:00
https://github.com/MoneroOcean/xmrig/issues/145

## Spudz76 | 2024-06-03T18:18:02+00:00
Also of note from my tracing, the file gets created, everything makes it through all the way to the last `uv_fs_write` but then gets lost.  File stays zero length.  So I suspect something weird with libuv and `fork()` although I can't find any reason why, it seems like it should work.  All the setup including Log backend and file and event loop creation occurs after the `fork()` and appears to work fine.  My testing was done with the versions built by the build_deps script, and not the OS ones.

Possibly related notes in libuv code: https://github.com/libuv/libuv/blob/v1.x/src/unix/async.c#L293

Perhaps instead of regular `fork()` the libuv fork must be used?

## Spudz76 | 2024-06-03T18:56:18+00:00
Found it, this patch works but I have less than zero clue if it's the ideal way to fix it.  Seems like creating a new loop and not using the default one is more proper but that seems like a ton more work considering the at least 20 various calls to `uv_default_loop()` all over the place.

## SnAFKe | 2024-06-04T02:13:41+00:00
I can confirm PR works.

## Spudz76 | 2024-06-04T02:27:31+00:00
Still lightly buggy in that when you send a kill to the backgrounded process it doesn't seem to execute the normal exit path, instead it simply dies.  But it could be it just misses writing the last couple of lines to the log somehow (although it works fine and logs everything in foreground).  Also that might not matter enough to hold up merging the PR.

## SnAFKe | 2024-06-04T02:37:10+00:00
Wierd, i force kill -9 or pkill and logs seems exit normal not strange symbols or incomplete logs.

Maybe i miss something but if you say still buggy then must be.

## Spudz76 | 2024-06-04T04:23:47+00:00
When in foreground and you kill either with default signal or with `-INT` the log gets the message that it caught the signal and then the cpu backend stopping message.  When in background those messages are not there.

## Spudz76 | 2024-06-04T04:32:50+00:00
A different patch that still fixes this, does not fix the signal behavior either, however it is cleaner and simpler.

## Spudz76 | 2024-06-04T21:36:54+00:00
The actual problem was simply the construction of Signals before the fork, none of my ideas were really doing anything.

## Spudz76 | 2024-06-04T21:38:21+00:00
And I think the logging is not related to Signals not being caught, but actually libuv not flushing the pending async write events before exiting (so it exits cleanly but doesn't flush the last couple lines to the logfile).

# Action History
- Created by: maravento | 2024-04-02T14:10:50+00:00
- Closed at: 2025-06-16T19:44:32+00:00
