---
title: 'Segmentation fault for monerod v0.11.0.0 on Ubuntu 16.04, '
source_url: https://github.com/monero-project/monero/issues/2588
author: jklaise
assignees: []
labels: []
created_at: '2017-10-06T09:08:57+00:00'
updated_at: '2017-10-15T17:54:20+00:00'
type: issue
status: closed
closed_at: '2017-10-15T17:54:20+00:00'
---

# Original Description
Same issue as #2490, here's the gdb output:

```
GNU gdb (Ubuntu 7.11.1-0ubuntu1~16.5) 7.11.1
Copyright (C) 2016 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
<http://www.gnu.org/software/gdb/documentation/>.
For help, type "help".
Type "apropos word" to search for commands related to "word".
(gdb) ./monerod
Undefined command: "".  Try "help".
(gdb) run
Starting program:  
No executable file specified.
Use the "file" or "exec-file" command.
(gdb) file
No executable file now.
No symbol file now.
(gdb) file monerod
Reading symbols from monerod...done.
(gdb) run
Starting program: /home/janis/source/monero-v0.11.0.0/monerod 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
2017-10-06 08:48:37.539     7ffff7fe4740        INFO    global  src/daemon/main.cpp:279 Monero 'Helium Hydra' (v0.11.0.0-release)
2017-10-06 08:48:37.539     7ffff7fe4740        INFO    global  src/daemon/protocol.h:55        Initializing cryptonote protocol...
2017-10-06 08:48:37.539     7ffff7fe4740        INFO    global  src/daemon/protocol.h:60        Cryptonote protocol initialized OK
[New Thread 0x7ffff72e2700 (LWP 17298)]
[New Thread 0x7ffff6de1700 (LWP 17299)]
[New Thread 0x7ffff68e0700 (LWP 17300)]
2017-10-06 08:48:37.541     7ffff7fe4740        INFO    global  src/daemon/p2p.h:63     Initializing p2p server...
[New Thread 0x7ffff63df700 (LWP 17301)]
[New Thread 0x7ffff5bde700 (LWP 17302)]
[1507279717] libunbound[17294:0] info: warning: unsupported algorithm for trust anchor . DS IN
[1507279717] libunbound[17294:0] warning: trust anchor . has no supported algorithms, the anchor is ignored (check if you need to upgrade unbound and openssl)
[New Thread 0x7ffff53dd700 (LWP 17303)]
[New Thread 0x7ffff4bdc700 (LWP 17304)]
[Thread 0x7ffff63df700 (LWP 17301) exited]
[Thread 0x7ffff4bdc700 (LWP 17304) exited]
[Thread 0x7ffff53dd700 (LWP 17303) exited]
[Thread 0x7ffff5bde700 (LWP 17302) exited]
2017-10-06 08:48:41.585     7ffff7fe4740        INFO    global  src/daemon/p2p.h:68     P2p server initialized OK
2017-10-06 08:48:41.585     7ffff7fe4740        INFO    global  src/daemon/rpc.h:58     Initializing core rpc server...
2017-10-06 08:48:41.585     7ffff7fe4740        INFO    global  contrib/epee/include/net/http_server_impl_base.h:70     Binding on 127.0.0.1:18081
2017-10-06 08:48:41.585     7ffff7fe4740        INFO    global  src/daemon/rpc.h:63     Core rpc server initialized OK on port: 18081
2017-10-06 08:48:41.585     7ffff7fe4740        INFO    global  src/daemon/core.h:73    Initializing core...
2017-10-06 08:48:41.586     7ffff7fe4740        INFO    global  src/cryptonote_core/cryptonote_core.cpp:323     Loading blockchain from folder /home/janis/.bitmonero/lmdb
 ...
[New Thread 0x7ffff4bdc700 (LWP 17305)]
2017-10-06 08:48:41.932     7ffff7fe4740        INFO    global  src/cryptonote_core/cryptonote_core.cpp:421     Loading checkpoints
2017-10-06 08:48:42.089     7ffff7fe4740        WARN    net.dns src/common/dns_utils.cpp:487    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-10-06 08:48:42.089     7ffff7fe4740        INFO    global  src/blockchain_db/lmdb/db_lmdb.cpp:578  [batch] DB resize needed
2017-10-06 08:48:42.091     7ffff7fe4740        INFO    global  src/blockchain_db/lmdb/db_lmdb.cpp:494  LMDB Mapsize increased.  Old: 20052MiB, New: 21076MiB
2017-10-06 08:48:42.092     7ffff7fe4740        INFO    global  src/daemon/core.h:78    Core initialized OK
2017-10-06 08:48:42.092     7ffff7fe4740        INFO    global  src/daemon/rpc.h:68     Starting core rpc server...
[New Thread 0x7ffff53dd700 (LWP 17306)]
[New Thread 0x7ffff5bde700 (LWP 17307)]
2017-10-06 08:48:42.093 [SRV_MAIN]      INFO    global  src/daemon/rpc.h:73     Core rpc server started ok
[New Thread 0x7ffff63df700 (LWP 17308)]
[New Thread 0x7fffe7fff700 (LWP 17309)]
2017-10-06 08:48:42.094 [SRV_MAIN]      INFO    global  src/daemon/p2p.h:78     Starting p2p net loop...
[New Thread 0x7fffe77fe700 (LWP 17310)]
[New Thread 0x7fffe6ffd700 (LWP 17311)]
[New Thread 0x7fffe6afc700 (LWP 17312)]
[New Thread 0x7fffe65fb700 (LWP 17313)]
[New Thread 0x7fffe60fa700 (LWP 17314)]
[New Thread 0x7fffe5bf9700 (LWP 17315)]
[New Thread 0x7fffe56f8700 (LWP 17316)]
[New Thread 0x7fffe51f7700 (LWP 17317)]
[New Thread 0x7fffe4cf6700 (LWP 17318)]
[New Thread 0x7fffe47f5700 (LWP 17319)]
[New Thread 0x7fffcbfff700 (LWP 17320)]
2017-10-06 08:48:43.094 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1247
**********************************************************************
The daemon will start synchronizing with the network. This may take a long time to complete.

You can set the level of process detailization* through "set_log <level|categories>" command*,
where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING)

Use the "help" command to see the list of available commands.
**********************************************************************

2017-10-06 08:48:43.232 [P2P1]  WARN    net.dns src/common/dns_utils.cpp:487    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-10-06 08:48:43.737 [P2P7]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1543
**********************************************************************
You are now synchronized with the network. You may now start monero-wallet-cli.

Use the "help" command to see the list of available commands.
**********************************************************************
2017-10-06 08:48:44.787 [P2P1]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:305     [116.93.119.79:18080 OUT] Sync data returned a new top blo
ck candidate: 1288623 -> 1414604 [Your node is 125981 blocks (174 days) behind] 
SYNCHRONIZATION started

Thread 24 "monerod" received signal SIGSEGV, Segmentation fault.
[Switching to Thread 0x7fffcbfff700 (LWP 17320)]
__memcmp_sse4_1 () at ../sysdeps/x86_64/multiarch/memcmp-sse4.S:1525
1525    ../sysdeps/x86_64/multiarch/memcmp-sse4.S: No such file or directory.
```


# Discussion History
## moneromooo-monero | 2017-10-06T09:38:33+00:00
Fixed by https://github.com/monero-project/monero/pull/2492

## KelvinJones | 2017-10-09T17:15:47+00:00
Same problem here. Downloaded everything fresh, upgraded to Ubuntu 16 and still have this:

2017-10-09 17:11:43.772 [P2P4]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:305     [37.59.49.7:18080 OUT] Sync data returned a new top block candidate: 1288623 -> 1417025 [Your node is 128402 blocks (178 days) behind]
SYNCHRONIZATION started
Segmentation fault (core dumped)

I'm happy to re-do if needed. 

@moneromooo-monero please point me in the right direction if possible.  Thanks in advance.


## moneromooo-monero | 2017-10-09T17:35:33+00:00
Are you running with #2492 ? It's now in master.

## KelvinJones | 2017-10-09T18:23:30+00:00
This is what I downloaded:

https://downloads.getmonero.org/cli/linux64

It looks like cloning requires compiling?  I'm not a coder, sorry for my ignorance.

The Windows version also stalled at the same place but I'll try again.


## moneromooo-monero | 2017-10-09T18:43:56+00:00
That version does not contain the fix. You'll have to build master to get the fix.

## KelvinJones | 2017-10-09T20:43:28+00:00
Thanks. Did that, built from the master. It doesn't crash but it doesn't seem to make any progress either.  I'll let it run for the night and see what happens.  This is all I get for now, it doesn't get past block 1288623:

2017-10-09 20:27:46.602 [P2P9]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:305     [62.4.21.85:18080 OUT] Sync data returned a new top block candidate: 1288623 -> 1417116 [Your node is 128493 blocks (178 days) behind]
SYNCHRONIZATION started
2017-10-09 20:33:23.046 [P2P4]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:305     [163.172.14.142:18081 OUT] Sync data returned a new top block candidate: 1288623 -> 1417118 [Your node is 128495 blocks (178 days) behind]
SYNCHRONIZATION started
2017-10-09 20:36:15.644 [P2P5]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:305     [172.104.139.177:18080 OUT] Sync data returned a new top block candidate: 1288623 -> 1417119 [Your node is 128496 blocks (178 days) behind]
SYNCHRONIZATION started
2017-10-09 20:37:33.920 [P2P7]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:305     [176.9.89.132:18080 OUT] Sync data returned a new top block candidate: 1288623 -> 1417120 [Your node is 128497 blocks (178 days) behind]
SYNCHRONIZATION started
2017-10-09 20:39:08.316 [P2P6]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:305     [84.113.41.54:18080 OUT] Sync data returned a new top block candidate: 1288623 -> 1417121 [Your node is 128498 blocks (178 days) behind]
SYNCHRONIZATION started


## moneromooo-monero | 2017-10-09T20:57:56+00:00
Please:
- exit monerod
- run it again with --log-level 2
- exit after 30 seconds
- post the resulting log to fpaste.org or pastebin.mozilla.org (not pastebin.com)


## KelvinJones | 2017-10-09T21:25:04+00:00
Done.

DOWNLOAD:
https://paste.fedoraproject.org/paste/HQ2yq10GMKoiUh-krqYFfQ#

VIEW RAW:
https://paste.fedoraproject.org/paste/HQ2yq10GMKoiUh-krqYFfQ/raw


## moneromooo-monero | 2017-10-09T21:47:57+00:00
Thanks. This looks like this is fixed by https://github.com/monero-project/monero/pull/2552

## KelvinJones | 2017-10-10T04:43:13+00:00
Thanks again.  This is what I pulled (sorry, downloaded) and got the above result:
https://github.com/monero-project/monero.git
Latest commit was 3 days ago. Isn't #2552 included?  If not, how do I pull just 2552?

## moneromooo-monero | 2017-10-10T09:01:44+00:00
That should do it:

git fetch origin pull/2552/head:2552
git checkout -b 2552-rebased
git cherry-pick 2552

Once you're done:
git checkout master

## KelvinJones | 2017-10-10T18:36:27+00:00
Looks like that's done it!
Thank you. Sync is continuing. Hope to have the pool up in the next day.


## forresthopkinsa | 2017-10-12T16:52:03+00:00
I just encountered this problem on a fresh Xenial installation. 2552 fixed it. Thanks!

(note that there's a typo in that first command, that extra `1`)

## moneromooo-monero | 2017-10-12T17:31:58+00:00
Thanks, fixed.

## forresthopkinsa | 2017-10-12T20:10:35+00:00
Unfortunately, I spoke too soon. 2552 does make it work, which is great, but only for a short period of time -- after several minutes of syncing, it reverts to endless "x days behind, synchronization started" messages, at which point I have to restart the daemon to make it start actually syncing again.

## moneromooo-monero | 2017-10-12T20:11:59+00:00
Restart with --log-level 1, paste logs to fpaste.org

## forresthopkinsa | 2017-10-12T20:53:22+00:00
[Here you go](https://paste.fedoraproject.org/paste/oMAOt0DCgrDaV1h4Th0-~Q), although I'm not sure if this is the same error I normally get -- it doesn't look like it. But that might be the different log level, I guess?

Also, I find it extremely suspicious that it shows the commit ID of the second-to-newest commit; it's not taking into account the 2552 commit. I know that I re-made the program... I'll investigate it more.

EDIT: I just re-made it and now it's showing the right commit ID when starting monerod. I have no idea what happened before, or why it semi-fixed the problem when I (presumably) failed a `make` command... I'll report back with results on this one.

## forresthopkinsa | 2017-10-12T21:15:00+00:00
Okay, after successfully updating it to include 2552, it  still fails. [Log output](https://paste.fedoraproject.org/paste/Ro9LEq63wU5q~TSk66t9hQ).

## moneromooo-monero | 2017-10-12T23:03:48+00:00
Yes, it's a different bug, and one for which I have no fix yet.

## moneromooo-monero | 2017-10-12T23:06:33+00:00
Though, do you have https://github.com/monero-project/monero/pull/2492 ? It's in master currently, but you might have an older one ?

## moneromooo-monero | 2017-10-12T23:08:14+00:00
Also cherry-pick anohter fix: https://github.com/monero-project/monero/pull/2604

## forresthopkinsa | 2017-10-12T23:08:39+00:00
So I'm back to the `SYNCHRONIZATION STARTED` problem now, the `unknown parent` problem seems to have gone away (??). [Here](https://paste.fedoraproject.org/paste/gWRou8300z4z0rk2aCSiXQ) is the output, it's a much more manageable log than before. Running with 2552, of course.

And yeah, my two latest commits are 3cfcd57 (from #2552 , cherry-picking 69ce33f ) and then 86e9de5, which is as of now the latest master.

I'll try #2604 momentarily.

## moneromooo-monero | 2017-10-12T23:20:22+00:00
<s>In fact, this log looks a lot like what 2492 fixed, so you might not have that patch in. If it still breaks with the two patches above (2492 and 2604), please upload a new log.</s> I hadn't seen your latest comment yet, nevermind. Guess there's still some bugginess that's unfixed still.

## forresthopkinsa | 2017-10-12T23:38:27+00:00
I don't know, I've definitely got e457aa5 (2492) merged in already. I'm running with 0a87279 (2604) right now, and it's looking roughly the same as before. I'll give it a while to run and then I'll upload a log.

## forresthopkinsa | 2017-10-12T23:57:10+00:00
Okay, it's been running about 20 minutes. This build includes 2552, 2604, and the latest master, 2548 (which also includes 2492).

[Log](https://paste.fedoraproject.org/paste/-JKshj7m1BhPmY86Jf4UcQ).

## moneromooo-monero | 2017-10-13T07:36:36+00:00
That log looks like it's working.

## forresthopkinsa | 2017-10-13T16:20:33+00:00
Is that how it's supposed to look? It's only syncing about _20 blocks every 100 seconds or so_, and it gets to the point where it shows `SYNCHRONIZATION started` between each actual sync... I don't feel like this is the correct behavior? Especially on a dedicated 16-thread 24GB-RAM server with 180Mb down, right?

## radfish | 2017-10-13T16:45:11+00:00
On Fri, Oct 13, 2017 at 09:20:44AM -0700, Forrest Hopkins wrote:
> Is that how it's supposed to look? It's only syncing about _20 blocks every 100 seconds or so_, and it gets to the point where it shows `SYNCHRONIZATION started` between each actual sync... I don't feel like this is the correct behavior? Especially on a dedicated 16-thread 24GB-RAM server with 180Mb down, right?

FWIW, I'm getting similar log, but much slower than 20blocks per 100sec,
on a tiny ARM board. You can run 'sync_info' command to see the rate at
which it is downloading block spans. Also check how much of your CPUs
monerod is utilizing (via top/htop).


## forresthopkinsa | 2017-10-13T17:17:06+00:00
Alright then, if this is the speed that the last few thousand blocks are expected to sync at, then I guess I'm good! I'll report back if any other issues arise. Thanks!

## moneromooo-monero | 2017-10-13T17:44:45+00:00
It is certainly not in scope for a segmentation fault bug anyway.

The sync started message is not really expected so much, unless there is a new peer, or a peer was not syncing anymore, then starts syncing again.

## moneromooo-monero | 2017-10-15T17:46:31+00:00
+resolved

# Action History
- Created by: jklaise | 2017-10-06T09:08:57+00:00
- Closed at: 2017-10-15T17:54:20+00:00
