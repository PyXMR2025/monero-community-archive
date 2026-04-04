---
title: '[BUG] monerod halts on x64 4.11.9-1-ARCH at seemingly random times'
source_url: https://github.com/monero-project/monero/issues/2180
author: JollyMort
assignees: []
labels:
- bug
created_at: '2017-07-17T21:35:34+00:00'
updated_at: '2017-09-07T16:17:17+00:00'
type: issue
status: closed
closed_at: '2017-09-07T16:17:17+00:00'
---

# Original Description
Happened 2 times, first time on release build (moneromooo's sync-hit branch, but it happened before on tagged ver.), second time on debug build. Monerod just stops responding at seemingly random time and cpu drops to 0. 

```
$ top -H -p 12876

top - 23:34:23 up 3 days,  2:49,  1 user,  load average: 0.40, 0.50, 0.47
Threads:  25 total,   0 running,   0 sleeping,   0 stopped,   0 zombie
```

Log1: https://paste.fedoraproject.org/paste/Du9z1KQfcTTwIjjLNG4mgw/raw
Log2: https://paste.fedoraproject.org/paste/2ZopyB3vj9dwHYiITlo1fw/raw

# Discussion History
## dEBRUYNE-1 | 2017-08-25T15:54:17+00:00
+bug

## knaccc | 2017-09-03T16:21:36+00:00
I'm experiencing the same issue on a fresh install of Fedora 26. I did not build it myself, I installed the binary linked here: https://build.getmonero.org/downloads/monero-core-e217203-linux-amd64.tar.gz

gdb output: http://termbin.com/eh7h

glibc version: 2.25-9.fc26

## JollyMort | 2017-09-03T16:39:17+00:00
I'm running 335681896a8ea6142a4331aa203ce728d507265c, seems like it's more stable for me. Honestly, didn't pay attention but I don't recall it stopped like before and it's been running for days.

## hyc | 2017-09-07T15:33:54+00:00
Based on #2323 and @knaccc confirming that glibc 2.25 is being used, this is clearly a bug in glibc. We should be able to close this or #2323 now, yes?

# Action History
- Created by: JollyMort | 2017-07-17T21:35:34+00:00
- Closed at: 2017-09-07T16:17:17+00:00
