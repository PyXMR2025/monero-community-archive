---
title: Monerod Syncing problem
source_url: https://github.com/monero-project/monero/issues/9141
author: tczee36
assignees: []
labels:
- reproduction needed
- not reproducible
- more info needed
created_at: '2024-01-29T20:05:32+00:00'
updated_at: '2024-02-18T14:02:58+00:00'
type: issue
status: closed
closed_at: '2024-02-08T10:40:49+00:00'
---

# Original Description
Hi,

trying to sync a pruned node, getting some weird log output.

2024-01-29 20:01:36.247 I [207.244.240.82:18080 OUT] Sync data returned a new top block candidate: 3067647 -> 3072795 [Your node is 5148 blocks (7.2 days) behind] 
2024-01-29 20:01:36.248 I SYNCHRONIZATION started
2024-01-29 20:01:37.555 I [110.40.229.103:18080 OUT] Sync data returned a new top block candidate: 3067647 -> 3344842 [Your node is 277195 blocks (1.1 years) behind] 

There seems to be another chain, and its ahead for 1.1 years? (3344842 blocks)

I know this cannot be right, because the current chain is only 30676XX blocks

Feels like an attacker trying to disrupt network stability. 

Also getting _Segment Fault_ after auto switching to this longer chain.

Is the DNS-blacklist not working properly?

# Discussion History
## selsta | 2024-01-29T20:09:57+00:00
Please see https://github.com/monero-project/monero/issues/9139

> Also getting Segment Fault after auto switching to this longer chain.

How do you know the segfault is related to this longer chain? Can you share a backtrace?

## tczee36 | 2024-01-29T20:12:38+00:00
> Please see #9139
> 
> > Also getting Segment Fault after auto switching to this longer chain.
> 
> How do you know the segfault is related to this longer chain? Can you share a backtrace?

No segfault issues during sync until it switched to the longer chain. Had to run while loop to keep Monerod from stopping.

Tell me what to do to get the backtrace

## selsta | 2024-01-29T20:17:01+00:00
It didn't switch to this longer chain, it just logged that a node has sent a new top block condidate. So far I haven't seen another person report that this crashed their node so I'm not sure if it's related to your issue.

> Tell me what to do to get the backtrace

Which OS are you using?

## tczee36 | 2024-01-29T20:22:45+00:00
> It didn't switch to this longer chain, it just logged that a node has sent a new top block condidate. So far I haven't seen another person report that this crashed their node so I'm not sure if it's related to your issue.
> 
> > Tell me what to do to get the backtrace
> 
> Which OS are you using?

This is on Alpine linux, i'm new on this distro

## selsta | 2024-01-29T20:24:19+00:00
What kind of hardware do you use?

## tczee36 | 2024-01-29T20:41:35+00:00
> What kind of hardware do you use?

3900x / 16gb ram/ 2.5inch ssd/asrock b550

## selsta | 2024-01-29T20:43:46+00:00
For a backtrace you need gdb installed, and then execute gdb with the monerod binary

```
gdb /path/tomonerod
```

then wait for it to load and enter

```
start
```

then monerod should start to sync, wait for it to segfault and enter

```
thread apply all bt
```

and share the output.

## tczee36 | 2024-01-30T01:03:44+00:00
> For a backtrace you need gdb installed, and then execute gdb with the monerod binary
> 
> ```
> gdb /path/tomonerod
> ```
> 
> then wait for it to load and enter
> 
> ```
> start
> ```
> 
> then monerod should start to sync, wait for it to segfault and enter
> 
> ```
> thread apply all bt
> ```
> 
> and share the output.

i blocked the IP with longer chain, problem went away. Unable to reproduce the problem now.
everything is synced and working

thanks for the replies

*edit: nevermind, seeing segment fault again, will try to reproduce the problem again.

## tczee36 | 2024-01-30T16:47:49+00:00
alpine:~/monero-x86_64-linux-gnu-v0.18.3.1$ gdb monerod
GNU gdb (GDB) 14.1
Copyright (C) 2023 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-alpine-linux-musl".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<https://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from monerod...
(gdb)
Temporary breakpoint 1 at 0xed784
Starting program: /home/xmr/monero-x86_64-linux-gnu-v0.18.3.1/monerod
warning: Unable to find dynamic linker breakpoint function.
GDB will be unable to debug shared library initializers
and track explicitly loaded dynamic code.
process 26557 is executing new program: /lib/ld-musl-x86_64.so.1
Error in re-setting breakpoint 1: Function "main" not defined.
2024-01-30 08:06:15.327 I Monero 'Fluorine Fermi' (v0.18.3.1-release)
2024-01-30 08:06:15.327 I Initializing cryptonote protocol...
2024-01-30 08:06:15.327 I Cryptonote protocol initialized OK
2024-01-30 08:06:15.327 I Initializing core...
2024-01-30 08:06:15.328 I Loading blockchain from folder /home/xmr/.bitmonero/lmdb ...
[New LWP 26560]
[New LWP 26561]
[New LWP 26562]
[New LWP 26563]
[New LWP 26564]
[New LWP 26565]
[New LWP 26566]
[New LWP 26567]
[New LWP 26568]
[New LWP 26569]
[New LWP 26570]
[New LWP 26571]
[New LWP 26572]
[New LWP 26573]
[New LWP 26574]
[New LWP 26575]
[New LWP 26576]
[New LWP 26577]
[New LWP 26578]
[New LWP 26579]
[New LWP 26580]
[New LWP 26581]
[New LWP 26582]
[New LWP 26583]
[New LWP 26584]
2024-01-30 08:06:15.866 I Loading checkpoints
2024-01-30 08:06:15.866 I Core initialized OK
2024-01-30 08:06:15.866 I Initializing p2p server...
2024-01-30 08:06:15.874 I p2p server initialized OK
2024-01-30 08:06:15.874 I Initializing core RPC server...
2024-01-30 08:06:15.874 I Binding on 127.0.0.1 (IPv4):18081
[LWP 26561 exited]
2024-01-30 08:06:16.121 I core RPC server initialized OK on port: 18081
[New LWP 26585]
[New LWP 26586]
[New LWP 26587]
2024-01-30 08:06:16.122 I Starting core RPC server...
[New LWP 26588]
[New LWP 26589]
2024-01-30 08:06:16.123 I core RPC server started ok
[New LWP 26590]
[New LWP 26591]
[New LWP 26592]
2024-01-30 08:06:16.124 I Starting p2p net loop...
[New LWP 26593]
[New LWP 26594]
[New LWP 26595]
[New LWP 26596]
[New LWP 26597]
[New LWP 26598]
[New LWP 26599]
[New LWP 26600]
[New LWP 26601]
[New LWP 26602]
[New LWP 26603]
2024-01-30 08:06:17.125 I
2024-01-30 08:06:17.125 I **********************************************************************
2024-01-30 08:06:17.125 I The daemon will start synchronizing with the network. This may take a long time to complete.
2024-01-30 08:06:17.125 I
2024-01-30 08:06:17.125 I You can set the level of process detailization through "set_log <level|categories>" command,
2024-01-30 08:06:17.125 I where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg,
*:WARNING).
2024-01-30 08:06:17.125 I
2024-01-30 08:06:17.125 I Use the "help" command to see the list of available commands.
2024-01-30 08:06:17.125 I Use "help <command>" to see a command's documentation.
2024-01-30 08:06:17.125 I **********************************************************************
[New LWP 26604]
[New LWP 26605]
[New LWP 26606]
[New LWP 26607]
[New LWP 26608]
[New LWP 26609]
[New LWP 26610]
2024-01-30 08:06:17.686 I
2024-01-30 08:06:17.686 I **********************************************************************
2024-01-30 08:06:17.686 I You are now synchronized with the network. You may now start monero-wallet-cli.
2024-01-30 08:06:17.686 I
2024-01-30 08:06:17.686 I Use the "help" command to see the list of available commands.
2024-01-30 08:06:17.686 I **********************************************************************
Height: 3073123/3073123 (100.0%) on mainnet, not mining, net hash 2.28 GH/s, v16, 2(out)+0(in) connections, uptime 0d 0h 0m 6
s
[New LWP 26611]
[New LWP 26612]
[New LWP 26613]
[New LWP 26614]
[LWP 26613 exited]
[LWP 26611 exited]
[LWP 26614 exited]
[LWP 26612 exited]
Height: 3073125/3073125 (100.0%) on mainnet, not mining, net hash 2.27 GH/s, v16, 12(out)+0(in) connections, uptime 0d 0h 1m
56s
unknown command: stsatus
Use "help" to list all commands and their usage
unknown command: statuis
Use "help" to list all commands and their usage
Height: 3073167/3073167 (100.0%) on mainnet, not mining, net hash 2.28 GH/s, v16, 12(out)+0(in) connections, uptime 0d 1h 18m
 53s
2024-01-30 10:06:18.023 W No incoming connections - check firewalls/routers allow port 18080
2024-01-30 11:06:18.808 W No incoming connections - check firewalls/routers allow port 18080
2024-01-30 12:06:18.958 W No incoming connections - check firewalls/routers allow port 18080
2024-01-30 13:06:19.896 W No incoming connections - check firewalls/routers allow port 18080
2024-01-30 14:06:20.298 W No incoming connections - check firewalls/routers allow port 18080
2024-01-30 15:06:20.596 W No incoming connections - check firewalls/routers allow port 18080

Thread 39 "ld-musl-x86_64." received signal SIGSEGV, Segmentation fault.
[Switching to LWP 26597]
0x00007ffff7226e65 in ?? ()

(gdb)

Thread 52 (LWP 26610 "ld-musl-x86_64."):
#0  __cp_end () at src/thread/x86_64/syscall_cp.s:29
#1  0x00007ffff7fb74fc in __syscall_cp_c (nr=202, u=<optimized out>, v=<optimized out>, w=<optimized out>, x=<optimized out>,
 y=<optimized out>, z=0) at src/thread/pthread_cancel.c:33
#2  0x00007ffff7fb6a2e in __futex4_cp (to=<optimized out>, val=2, op=128, addr=0x7fed8e7a7654) at src/thread/__timedwait.c:24
#3  __timedwait_cp (addr=addr@entry=0x7fed8e7a7654, val=val@entry=2, clk=clk@entry=0, at=at@entry=0x0, priv=128, priv@entry=1
) at src/thread/__timedwait.c:52
#4  0x00007ffff7fb7894 in __pthread_cond_timedwait (c=0x7ffff7ce61b8, m=0x7ffff7ce6190, ts=0x0) at src/thread/pthread_cond_ti
medwait.c:100
#5  0x00007ffff6f2d5ad in ?? ()
#6  0x0000000000000000 in ?? ()

Thread 51 (LWP 26609 "ld-musl-x86_64."):
#0  __cp_end () at src/thread/x86_64/syscall_cp.s:29
#1  0x00007ffff7fb74fc in __syscall_cp_c (nr=202, u=<optimized out>, v=<optimized out>, w=<optimized out>, x=<optimized out>,
 y=<optimized out>, z=0) at src/thread/pthread_cancel.c:33
#2  0x00007ffff7fb6a2e in __futex4_cp (to=<optimized out>, val=2, op=128, addr=0x7fed8ecaa654) at src/thread/__timedwait.c:24
#3  __timedwait_cp (addr=addr@entry=0x7fed8ecaa654, val=val@entry=2, clk=clk@entry=0, at=at@entry=0x0, priv=128, priv@entry=1
) at src/thread/__timedwait.c:52
--Type <RET> for more, q to quit, c to continue without paging--
#4  0x00007ffff7fb7894 in __pthread_cond_timedwait (c=0x7ffff7ce61b8, m=0x7ffff7ce6190, ts=0x0) at src/thread/pthread_cond_ti
medwait.c:100
#5  0x00007ffff6f2d5ad in ?? ()
#6  0x0000000000000000 in ?? ()

Thread 50 (LWP 26608 "ld-musl-x86_64."):
#0  __cp_end () at src/thread/x86_64/syscall_cp.s:29
#1  0x00007ffff7fb74fc in __syscall_cp_c (nr=202, u=<optimized out>, v=<optimized out>, w=<optimized out>, x=<optimized out>,
 y=<optimized out>, z=0) at src/thread/pthread_cancel.c:33
#2  0x00007ffff7fb6a2e in __futex4_cp (to=<optimized out>, val=2, op=128, addr=0x7fed8f1ad654) at src/thread/__timedwait.c:24
#3  __timedwait_cp (addr=addr@entry=0x7fed8f1ad654, val=val@entry=2, clk=clk@entry=0, at=at@entry=0x0, priv=128, priv@entry=1
) at src/thread/__timedwait.c:52
#4  0x00007ffff7fb7894 in __pthread_cond_timedwait (c=0x7ffff7ce61b8, m=0x7ffff7ce6190, ts=0x0) at src/thread/pthread_cond_ti
medwait.c:100
#5  0x00007ffff6f2d5ad in ?? ()
#6  0x0000000000000000 in ?? ()

Thread 49 (LWP 26607 "ld-musl-x86_64."):
#0  __cp_end () at src/thread/x86_64/syscall_cp.s:29
#1  0x00007ffff7fb74fc in __syscall_cp_c (nr=202, u=<optimized out>, v=<optimized out>, w=<optimized out>, x=<optimized out>,
 y=<optimized out>, z=0) at src/thread/pthread_cancel.c:33
#2  0x00007ffff7fb6a2e in __futex4_cp (to=<optimized out>, val=2, op=128, addr=0x7fed8f6b0654) at src/thread/__timedwait.c:24
#3  __timedwait_cp (addr=addr@entry=0x7fed8f6b0654, val=val@entry=2, clk=clk@entry=0, at=at@entry=0x0, priv=128, priv@entry=1
) at src/thread/__timedwait.c:52
#4  0x00007ffff7fb7894 in __pthread_cond_timedwait (c=0x7ffff7ce61b8, m=0x7ffff7ce6190, ts=0x0) at src/thread/pthread_cond_ti
medwait.c:100
#5  0x00007ffff6f2d5ad in ?? ()
#6  0x0000000000000000 in ?? ()

Thread 48 (LWP 26606 "ld-musl-x86_64."):
#0  __cp_end () at src/thread/x86_64/syscall_cp.s:29
#1  0x00007ffff7fb74fc in __syscall_cp_c (nr=202, u=<optimized out>, v=<optimized out>, w=<optimized out>, x=<optimized out>,
 y=<optimized out>, z=0) at src/thread/pthread_cancel.c:33
#2  0x00007ffff7fb6a2e in __futex4_cp (to=<optimized out>, val=2, op=128, addr=0x7fed8fbb3654) at src/thread/__timedwait.c:24
#3  __timedwait_cp (addr=addr@entry=0x7fed8fbb3654, val=val@entry=2, clk=clk@entry=0, at=at@entry=0x0, priv=128, priv@entry=1
) at src/thread/__timedwait.c:52
#4  0x00007ffff7fb7894 in __pthread_cond_timedwait (c=0x7ffff7ce61b8, m=0x7ffff7ce6190, ts=0x0) at src/thread/pthread_cond_ti
medwait.c:100
#5  0x00007ffff6f2d5ad in ?? ()
#6  0x0000000000000000 in ?? ()

Thread 47 (LWP 26605 "ld-musl-x86_64."):
#0  __cp_end () at src/thread/x86_64/syscall_cp.s:29
--Type <RET> for more, q to quit, c to continue without paging--
#1  0x00007ffff7fb74fc in __syscall_cp_c (nr=202, u=<optimized out>, v=<optimized out>, w=<optimized out>, x=<optimized out>,
 y=<optimized out>, z=0) at src/thread/pthread_cancel.c:33
#2  0x00007ffff7fb6a2e in __futex4_cp (to=<optimized out>, val=2, op=128, addr=0x7fed900b8654) at src/thread/__timedwait.c:24
#3  __timedwait_cp (addr=addr@entry=0x7fed900b8654, val=val@entry=2, clk=clk@entry=0, at=at@entry=0x0, priv=128, priv@entry=1
) at src/thread/__timedwait.c:52
#4  0x00007ffff7fb7894 in __pthread_cond_timedwait (c=0x7ffff7ce61b8, m=0x7ffff7ce6190, ts=0x0) at src/thread/pthread_cond_ti
medwait.c:100
#5  0x00007ffff6f2d5ad in ?? ()
#6  0x0000000000000000 in ?? ()

Thread 46 (LWP 26604 "ld-musl-x86_64."):
#0  __cp_end () at src/thread/x86_64/syscall_cp.s:29
#1  0x00007ffff7fb74fc in __syscall_cp_c (nr=202, u=<optimized out>, v=<optimized out>, w=<optimized out>, x=<optimized out>,
 y=<optimized out>, z=0) at src/thread/pthread_cancel.c:33
#2  0x00007ffff7fb6a2e in __futex4_cp (to=<optimized out>, val=2, op=128, addr=0x7fed905bb654) at src/thread/__timedwait.c:24
#3  __timedwait_cp (addr=addr@entry=0x7fed905bb654, val=val@entry=2, clk=clk@entry=0, at=at@entry=0x0, priv=128, priv@entry=1
) at src/thread/__timedwait.c:52
#4  0x00007ffff7fb7894 in __pthread_cond_timedwait (c=0x7ffff7ce61b8, m=0x7ffff7ce6190, ts=0x0) at src/thread/pthread_cond_ti
medwait.c:100
#5  0x00007ffff6f2d5ad in ?? ()
#6  0x0000000000000000 in ?? ()

Thread 45 (LWP 26603 "ld-musl-x86_64."):
#0  __cp_end () at src/thread/x86_64/syscall_cp.s:29
#1  0x00007ffff7fb74fc in __syscall_cp_c (nr=202, u=<optimized out>, v=<optimized out>, w=<optimized out>, x=<optimized out>,
 y=<optimized out>, z=0) at src/thread/pthread_cancel.c:33
#2  0x00007ffff7fb6a2e in __futex4_cp (to=<optimized out>, val=2, op=128, addr=0x7fed90aee664) at src/thread/__timedwait.c:24
#3  __timedwait_cp (addr=addr@entry=0x7fed90aee664, val=val@entry=2, clk=clk@entry=0, at=at@entry=0x0, priv=128, priv@entry=1
) at src/thread/__timedwait.c:52
#4  0x00007ffff7fb7894 in __pthread_cond_timedwait (c=0x7ffff7ec5f08, m=0x7ffff7ec5ee0, ts=0x0) at src/thread/pthread_cond_ti
medwait.c:100
#5  0x00007ffff6b30d77 in ?? ()
#6  0x00007ffff7ec5eb0 in ?? ()
#7  0x00007fed90aee740 in ?? ()
#8  0x00007ffff7ec5eb0 in ?? ()
#9  0x00007fed90aee740 in ?? ()
#10 0x00007fed90aee770 in ?? ()
#11 0xadea727fa4f0003a in ?? ()
#12 0x00007ffff800b338 in ?? ()
#13 0x00007ffff7ec5eb0 in ?? ()
#14 0x00007ffff7e74ac0 in ?? ()
#15 0x00007fed90aee810 in ?? ()
#16 0x00007fed90aee770 in ?? ()
#17 0x00007fed90aee730 in ?? ()
#18 0x00007fed90aee740 in ?? ()
#19 0x00007ffff6dcc049 in ?? ()
#20 0x00007fed90aee778 in ?? ()
#21 0x0000000000000000 in ?? ()

Thread 44 (LWP 26602 "ld-musl-x86_64."):
#0  __cp_end () at src/thread/x86_64/syscall_cp.s:29
#1  0x00007ffff7fb74fc in __syscall_cp_c (nr=281, u=<optimized out>, v=<optimized out>, w=<optimized out>, x=<optimized out>,
 y=<optimized out>, z=8) at src/thread/pthread_cancel.c:33
#2  0x00007ffff7f7c286 in epoll_pwait (fd=8, ev=0x7fed90ff1070, cnt=128, to=-1, sigs=0x0) at src/linux/epoll.c:28
#3  0x00007ffff6b2fc7d in ?? ()
#4  0x0000000000000000 in ?? ()

Thread 43 (LWP 26601 "ld-musl-x86_64."):
#0  __cp_end () at src/thread/x86_64/syscall_cp.s:29
#1  0x00007ffff7fb74fc in __syscall_cp_c (nr=202, u=<optimized out>, v=<optimized out>, w=<optimized out>, x=<optimized out>,
 y=<optimized out>, z=0) at src/thread/pthread_cancel.c:33
#2  0x00007ffff7fb6a2e in __futex4_cp (to=<optimized out>, val=2, op=128, addr=0x7fed914f4664) at src/thread/__timedwait.c:24
#3  __timedwait_cp (addr=addr@entry=0x7fed914f4664, val=val@entry=2, clk=clk@entry=0, at=at@entry=0x0, priv=128, priv@entry=1
) at src/thread/__timedwait.c:52
#4  0x00007ffff7fb7894 in __pthread_cond_timedwait (c=0x7ffff7ec5f08, m=0x7ffff7ec5ee0, ts=0x0) at src/thread/pthread_cond_ti
medwait.c:100
#5  0x00007ffff6b30d77 in ?? ()
#6  0x00007ffff7ec5eb0 in ?? ()
#7  0x00007fed914f4740 in ?? ()
#8  0x00007ffff7ec5eb0 in ?? ()
#9  0x00007fed914f4740 in ?? ()
#10 0x00007fed914f4770 in ?? ()
#11 0xadea727fa4f0003a in ?? ()
#12 0x00007ffff800b338 in ?? ()
#13 0x00007ffff7ec5eb0 in ?? ()
#14 0x00007ffff7e74ac0 in ?? ()
#15 0x00007fed914f4810 in ?? ()
#16 0x00007fed914f4770 in ?? ()
#17 0x00007fed914f4730 in ?? ()
#18 0x00007fed914f4740 in ?? ()
#19 0x00007ffff6dcc049 in ?? ()
#20 0x00007fed914f4778 in ?? ()
#21 0x0000000000000000 in ?? ()

Thread 42 (LWP 26600 "ld-musl-x86_64."):
#0  __cp_end () at src/thread/x86_64/syscall_cp.s:29
#1  0x00007ffff7fb74fc in __syscall_cp_c (nr=202, u=<optimized out>, v=<optimized out>, w=<optimized out>, x=<optimized out>,
 y=<optimized out>, z=0) at src/thread/pthread_cancel.c:33
#2  0x00007ffff7fb6a2e in __futex4_cp (to=<optimized out>, val=2, op=128, addr=0x7fed919f7664) at src/thread/__timedwait.c:24
#3  __timedwait_cp (addr=addr@entry=0x7fed919f7664, val=val@entry=2, clk=clk@entry=0, at=at@entry=0x0, priv=128, priv@entry=1
) at src/thread/__timedwait.c:52
#4  0x00007ffff7fb7894 in __pthread_cond_timedwait (c=0x7ffff7ec5f08, m=0x7ffff7ec5ee0, ts=0x0) at src/thread/pthread_cond_ti
medwait.c:100
#5  0x00007ffff6b30d77 in ?? ()
#6  0x00007ffff7ec5eb0 in ?? ()
#7  0x00007fed919f7740 in ?? ()
#8  0x00007ffff7ec5eb0 in ?? ()
#9  0x00007fed919f7740 in ?? ()
#10 0x00007fed919f7770 in ?? ()
#11 0xadea727fa4f0003a in ?? ()
#12 0x00007fed919f78c0 in ?? ()
#13 0x00007ffff7ec5eb0 in ?? ()
#14 0x00007ffff7e74ac0 in ?? ()
#15 0x00007fed919f7810 in ?? ()
#16 0x00007fed919f7770 in ?? ()
#17 0x00007fed919f7730 in ?? ()
#18 0x00007fed919f7740 in ?? ()
#19 0x00007ffff6dcc049 in ?? ()
#20 0x00007fed919f7778 in ?? ()
#21 0x0000000000000000 in ?? ()

Thread 41 (LWP 26599 "ld-musl-x86_64."):
#0  __cp_end () at src/thread/x86_64/syscall_cp.s:29
#1  0x00007ffff7fb74fc in __syscall_cp_c (nr=202, u=<optimized out>, v=<optimized out>, w=<optimized out>, x=<optimized out>,
 y=<optimized out>, z=0) at src/thread/pthread_cancel.c:33
#2  0x00007ffff7fb6a2e in __futex4_cp (to=<optimized out>, val=2, op=128, addr=0x7fed91efa664) at src/thread/__timedwait.c:24
#3  __timedwait_cp (addr=addr@entry=0x7fed91efa664, val=val@entry=2, clk=clk@entry=0, at=at@entry=0x0, priv=128, priv@entry=1
) at src/thread/__timedwait.c:52
#4  0x00007ffff7fb7894 in __pthread_cond_timedwait (c=0x7ffff7ec5f08, m=0x7ffff7ec5ee0, ts=0x0) at src/thread/pthread_cond_ti
medwait.c:100
#5  0x00007ffff6b30d77 in ?? ()
#6  0x00007ffff7ec5eb0 in ?? ()
#7  0x00007fed91efa740 in ?? ()
#8  0x00007ffff7ec5eb0 in ?? ()
#9  0x00007fed91efa740 in ?? ()
#10 0x00007fed91efa770 in ?? ()
#11 0xadea727fa4f0003a in ?? ()
#12 0x00007fed91efa8c0 in ?? ()
#13 0x00007ffff7ec5eb0 in ?? ()
#14 0x00007ffff7e74ac0 in ?? ()
#15 0x00007fed91efa810 in ?? ()
#16 0x00007fed91efa770 in ?? ()
#17 0x00007fed91efa730 in ?? ()
#18 0x00007fed91efa740 in ?? ()
#19 0x00007ffff6dcc049 in ?? ()
#20 0x00007fed91efa778 in ?? ()
#21 0x0000000000000000 in ?? ()

Thread 40 (LWP 26598 "ld-musl-x86_64."):
#0  __cp_end () at src/thread/x86_64/syscall_cp.s:29
#1  0x00007ffff7fb74fc in __syscall_cp_c (nr=202, u=<optimized out>, v=<optimized out>, w=<optimized out>, x=<optimized out>,
 y=<optimized out>, z=0) at src/thread/pthread_cancel.c:33
#2  0x00007ffff7fb6a2e in __futex4_cp (to=<optimized out>, val=2, op=128, addr=0x7fed923fd664) at src/thread/__timedwait.c:24
#3  __timedwait_cp (addr=addr@entry=0x7fed923fd664, val=val@entry=2, clk=clk@entry=0, at=at@entry=0x0, priv=128, priv@entry=1
) at src/thread/__timedwait.c:52
#4  0x00007ffff7fb7894 in __pthread_cond_timedwait (c=0x7ffff7ec5f08, m=0x7ffff7ec5ee0, ts=0x0) at src/thread/pthread_cond_ti
medwait.c:100
#5  0x00007ffff6b30d77 in ?? ()
#6  0x00007ffff7ec5eb0 in ?? ()
#7  0x00007fed923fd740 in ?? ()
#8  0x00007ffff7ec5eb0 in ?? ()
#9  0x00007fed923fd740 in ?? ()
#10 0x00007fed923fd770 in ?? ()
#11 0xadea727fa4f0003a in ?? ()
#12 0x00007fed923fd8c0 in ?? ()
#13 0x00007ffff7ec5eb0 in ?? ()
#14 0x00007ffff7e74ac0 in ?? ()
#15 0x00007fed923fd810 in ?? ()
#16 0x00007fed923fd770 in ?? ()
#17 0x00007fed923fd730 in ?? ()
#18 0x00007fed923fd740 in ?? ()
#19 0x00007ffff6dcc049 in ?? ()
#20 0x00007fed923fd778 in ?? ()
#21 0x0000000000000000 in ?? ()

Thread 39 (LWP 26597 "ld-musl-x86_64."):
#0  0x00007ffff7226e65 in ?? ()
#1  0x00007ffff6e04f37 in ?? ()
#2  0x0000000000000043 in ?? ()
#3  0xadea727fa4f0003a in ?? ()
#4  0x00007fed929002a0 in ?? ()
#5  0x00007fed92900150 in ?? ()
#6  0x00007fed929002b0 in ?? ()
#7  0x00007ffff75acc22 in ?? ()
#8  0x00007fed92900160 in ?? ()
#9  0x0000000000000000 in ?? ()

Thread 38 (LWP 26596 "ld-musl-x86_64."):
#0  __cp_end () at src/thread/x86_64/syscall_cp.s:29
#1  0x00007ffff7fb74fc in __syscall_cp_c (nr=202, u=<optimized out>, v=<optimized out>, w=<optimized out>, x=<optimized out>,
 y=<optimized out>, z=0) at src/thread/pthread_cancel.c:33
#2  0x00007ffff7fb6a2e in __futex4_cp (to=<optimized out>, val=2, op=128, addr=0x7fed92e03664) at src/thread/__timedwait.c:24
#3  __timedwait_cp (addr=addr@entry=0x7fed92e03664, val=val@entry=2, clk=clk@entry=0, at=at@entry=0x0, priv=128, priv@entry=1
) at src/thread/__timedwait.c:52
#4  0x00007ffff7fb7894 in __pthread_cond_timedwait (c=0x7ffff7ec5f08, m=0x7ffff7ec5ee0, ts=0x0) at src/thread/pthread_cond_ti
medwait.c:100
#5  0x00007ffff6b30d77 in ?? ()
#6  0x00007ffff7ec5eb0 in ?? ()
#7  0x00007fed92e03740 in ?? ()
#8  0x00007ffff7ec5eb0 in ?? ()
#9  0x00007fed92e03740 in ?? ()
#10 0x00007fed92e03770 in ?? ()
#11 0xadea727fa4f0003a in ?? ()
#12 0x00007fed92e038c0 in ?? ()
#13 0x00007ffff7ec5eb0 in ?? ()
#14 0x00007ffff7e74ac0 in ?? ()
#15 0x00007fed92e03810 in ?? ()
#16 0x00007fed92e03770 in ?? ()
#17 0x00007fed92e03730 in ?? ()
#18 0x00007fed92e03740 in ?? ()
#19 0x00007ffff6dcc049 in ?? ()
#20 0x00007fed92e03778 in ?? ()
#21 0x0000000000000000 in ?? ()

Thread 37 (LWP 26595 "ld-musl-x86_64."):
#0  __wake (priv=128, cnt=1, addr=0x7fed92900664) at ./arch/x86_64/syscall_arch.h:31
#1  unlock (l=0x7fed92900664) at src/thread/pthread_cond_timedwait.c:45
#2  unlock (l=0x7fed92900664) at src/thread/pthread_cond_timedwait.c:42
#3  __private_cond_signal (c=0x7ffff7ec5f08, n=0) at src/thread/pthread_cond_timedwait.c:208
#4  0x00007ffff6b30381 in ?? ()
#5  0x0000000000000000 in ?? ()

Thread 36 (LWP 26594 "ld-musl-x86_64."):
#0  __cp_end () at src/thread/x86_64/syscall_cp.s:29
#1  0x00007ffff7fb74fc in __syscall_cp_c (nr=202, u=<optimized out>, v=<optimized out>, w=<optimized out>, x=<optimized out>,
 y=<optimized out>, z=0) at src/thread/pthread_cancel.c:33
#2  0x00007ffff7fb6a2e in __futex4_cp (to=<optimized out>, val=2, op=128, addr=0x7fed93809664) at src/thread/__timedwait.c:24
#3  __timedwait_cp (addr=addr@entry=0x7fed93809664, val=val@entry=2, clk=clk@entry=0, at=at@entry=0x0, priv=128, priv@entry=1
) at src/thread/__timedwait.c:52
#4  0x00007ffff7fb7894 in __pthread_cond_timedwait (c=0x7ffff7ec5f08, m=0x7ffff7ec5ee0, ts=0x0) at src/thread/pthread_cond_ti
medwait.c:100
#5  0x00007ffff6b30d77 in ?? ()
#6  0x00007ffff7ec5eb0 in ?? ()
#7  0x00007fed93809740 in ?? ()
#8  0x00007ffff7ec5eb0 in ?? ()
#9  0x00007fed93809740 in ?? ()
#10 0x00007fed93809770 in ?? ()
#11 0xadea727fa4f0003a in ?? ()
#12 0x00007fed938098c0 in ?? ()
#13 0x00007ffff7ec5eb0 in ?? ()
#14 0x00007ffff7e74ac0 in ?? ()
#15 0x00007fed93809810 in ?? ()
#16 0x00007fed93809770 in ?? ()
#17 0x00007fed93809730 in ?? ()
#18 0x00007fed93809740 in ?? ()
#19 0x00007ffff6dcc049 in ?? ()
#20 0x00007fed93809778 in ?? ()
#21 0x0000000000000000 in ?? ()

Thread 35 (LWP 26593 "ld-musl-x86_64."):
#0  __cp_end () at src/thread/x86_64/syscall_cp.s:29
#1  0x00007ffff7fb74fc in __syscall_cp_c (nr=202, u=<optimized out>, v=<optimized out>, w=<optimized out>, x=<optimized out>,
 y=<optimized out>, z=0) at src/thread/pthread_cancel.c:33
#2  0x00007ffff7fb6a2e in __futex4_cp (to=<optimized out>, val=2, op=128, addr=0x7fed9382c7e4) at src/thread/__timedwait.c:24
#3  __timedwait_cp (addr=addr@entry=0x7fed9382c7e4, val=val@entry=2, clk=clk@entry=0, at=at@entry=0x7fed9382c8f0, priv=128, p
riv@entry=1) at src/thread/__timedwait.c:52
#4  0x00007ffff7fb7894 in __pthread_cond_timedwait (c=0x7fed93850320, m=0x7fed938502f8, ts=0x7fed9382c8f0) at src/thread/pthr
ead_cond_timedwait.c:100
#5  0x00007ffff756e599 in ?? ()
#6  0x00007ffff7ffbac0 in ?? ()
#7  0x00007fed938502f8 in ?? ()
#8  0x00007fed93850220 in ?? ()
#9  0x00007fed938502f8 in ?? ()
#10 0x0000000000000001 in ?? ()
#11 0x0000000000000060 in ?? ()
#12 0x0000000000000000 in ?? ()

Thread 34 (LWP 26592 "ld-musl-x86_64."):
#0  __cp_end () at src/thread/x86_64/syscall_cp.s:29
#1  0x00007ffff7fb74fc in __syscall_cp_c (nr=7, u=<optimized out>, v=<optimized out>, w=<optimized out>, x=<optimized out>, y
=<optimized out>, z=0) at src/thread/pthread_cancel.c:33
#2  0x00007ffff7fa93db in poll (fds=<optimized out>, n=<optimized out>, timeout=<optimized out>) at src/select/poll.c:9
#3  0x00007ffff7014210 in ?? ()
#4  0xffffffff9384f4f0 in ?? ()
#5  0x00007ffff7e6faf8 in ?? ()
#6  0x000000009384f500 in ?? ()
#7  0x00007fed9384f770 in ?? ()
#8  0x0000000100000014 in ?? ()
#9  0xadea727fa4f0003a in ?? ()
#10 0x00007fed9384f580 in ?? ()
#11 0x00007fed9384f770 in ?? ()
#12 0x00007fed9384f530 in ?? ()
#13 0x00007ffff70010d3 in ?? ()
#14 0x00007fed9384f510 in ?? ()
#15 0xffffffff9384f770 in ?? ()
#16 0x00007fed9384f580 in ?? ()
#17 0x00007ffff7e6fa90 in ?? ()
#18 0x00007fed9384f530 in ?? ()
#19 0x00007fed9384f770 in ?? ()
#20 0x00007fed9384f580 in ?? ()
#21 0x00007fed9384f770 in ?? ()
#22 0x00007fed9384f630 in ?? ()
#23 0x00007ffff701a4df in ?? ()
#24 0x0000000000000000 in ?? ()

Thread 33 (LWP 26591 "ld-musl-x86_64."):
#0  __cp_end () at src/thread/x86_64/syscall_cp.s:29
#1  0x00007ffff7fb74fc in __syscall_cp_c (nr=202, u=<optimized out>, v=<optimized out>, w=<optimized out>, x=<optimized out>,
 y=<optimized out>, z=0) at src/thread/pthread_cancel.c:33
#2  0x00007ffff7fb6a2e in __futex4_cp (to=<optimized out>, val=2, op=128, addr=0x7fed93874584) at src/thread/__timedwait.c:24
#3  __timedwait_cp (addr=addr@entry=0x7fed93874584, val=val@entry=2, clk=clk@entry=0, at=at@entry=0x0, priv=128, priv@entry=1
) at src/thread/__timedwait.c:52
#4  0x00007ffff7fb7894 in __pthread_cond_timedwait (c=0x7fed9396b9c8, m=0x7fed9396b9a0, ts=0x0) at src/thread/pthread_cond_ti
medwait.c:100
#5  0x00007ffff6b16716 in ?? ()
#6  0x00007ffff7d92aa0 in ?? ()
#7  0x00007fed9396b9a0 in ?? ()
#8  0x00007ffff7df4d90 in ?? ()
#9  0x00007fed9396b9a0 in ?? ()
#10 0x00007fed93a83b01 in ?? ()
#11 0x00007ffff7070f77 in ?? ()
#12 0x0000000000000020 in ?? ()
#13 0x00007fed8dfab9c0 in ?? ()
#14 0x0000000000000001 in ?? ()
#15 0x00007ffff7ce7300 in ?? ()
#16 0x0000000000000020 in ?? ()
#17 0x00007fed9396b858 in ?? ()
#18 0x0000000000000001 in ?? ()
#19 0x00007fed9396b9f8 in ?? ()
#20 0x0000000000000020 in ?? ()
#21 0x00007ffff6b164e8 in ?? ()
#22 0x0000000000000001 in ?? ()
#23 0x00007ffff7606d7b in ?? ()
#24 0x0000000000000020 in ?? ()
#25 0x00007ffff7d92aa0 in ?? ()
#26 0x0000000000000001 in ?? ()
#27 0x00007fff00000000 in ?? ()
#28 0x0000000000000000 in ?? ()

Thread 32 (LWP 26590 "ld-musl-x86_64."):
#0  __cp_end () at src/thread/x86_64/syscall_cp.s:29
#1  0x00007ffff7fb74fc in __syscall_cp_c (nr=23, u=<optimized out>, v=<optimized out>, w=<optimized out>, x=<optimized out>,
y=<optimized out>, z=0) at src/thread/pthread_cancel.c:33
#2  0x00007ffff7fa94c2 in select (n=<optimized out>, rfds=<optimized out>, wfds=<optimized out>, efds=<optimized out>, tv=<op
timized out>) at src/select/select.c:39
#3  0x00007ffff6b16b21 in ?? ()
#4  0x00007fed93897920 in ?? ()
#5  0x00007fed9396b8f8 in ?? ()
#6  0x0000000000000000 in ?? ()

Thread 31 (LWP 26589 "ld-musl-x86_64."):
#0  __cp_end () at src/thread/x86_64/syscall_cp.s:29
#1  0x00007ffff7fb74fc in __syscall_cp_c (nr=281, u=<optimized out>, v=<optimized out>, w=<optimized out>, x=<optimized out>,
 y=<optimized out>, z=8) at src/thread/pthread_cancel.c:33
#2  0x00007ffff7f7c286 in epoll_pwait (fd=12, ev=0x7fed938da070, cnt=128, to=-1, sigs=0x0) at src/linux/epoll.c:28
#3  0x00007ffff6b2fc7d in ?? ()
#4  0x0000000000000000 in ?? ()

Thread 30 (LWP 26588 "ld-musl-x86_64."):
#0  __cp_end () at src/thread/x86_64/syscall_cp.s:29
#1  0x00007ffff7fb74fc in __syscall_cp_c (nr=202, u=<optimized out>, v=<optimized out>, w=<optimized out>, x=<optimized out>,
 y=<optimized out>, z=0) at src/thread/pthread_cancel.c:33
#2  0x00007ffff7fb6a2e in __futex4_cp (to=<optimized out>, val=2, op=128, addr=0x7fed938fd664) at src/thread/__timedwait.c:24
#3  __timedwait_cp (addr=addr@entry=0x7fed938fd664, val=val@entry=2, clk=clk@entry=0, at=at@entry=0x0, priv=128, priv@entry=1
) at src/thread/__timedwait.c:52
#4  0x00007ffff7fb7894 in __pthread_cond_timedwait (c=0x7ffff7ec5c28, m=0x7ffff7ec5c00, ts=0x0) at src/thread/pthread_cond_ti
medwait.c:100
#5  0x00007ffff6b30d77 in ?? ()
#6  0x00007ffff7ec5bd0 in ?? ()
#7  0x00007fed938fd740 in ?? ()
#8  0x00007ffff7d91540 in ?? ()
#9  0x00007ffff7d914d0 in ?? ()
#10 0x00007ffff7d914e0 in ?? ()
#11 0xadea727fa4f0003a in ?? ()
#12 0x00007fed938fd8c0 in ?? ()
#13 0x00007ffff7ec5bd0 in ?? ()
#14 0x00007ffff7e6d618 in ?? ()
#15 0x00007fed938fd810 in ?? ()
#16 0x00007fed938fd770 in ?? ()
#17 0x00007fed938fd730 in ?? ()
#18 0x00007fed938fd740 in ?? ()
#19 0x00007ffff6b3d179 in ?? ()
#20 0x00007fed938fd778 in ?? ()
#21 0x0000000000000000 in ?? ()

Thread 29 (LWP 26587 "ld-musl-x86_64."):
#0  __cp_end () at src/thread/x86_64/syscall_cp.s:29
#1  0x00007ffff7fb74fc in __syscall_cp_c (nr=202, u=<optimized out>, v=<optimized out>, w=<optimized out>, x=<optimized out>,
 y=<optimized out>, z=0) at src/thread/pthread_cancel.c:33
#2  0x00007ffff7fb6a2e in __futex4_cp (to=<optimized out>, val=2, op=128, addr=0x7fed939207e4) at src/thread/__timedwait.c:24
#3  __timedwait_cp (addr=addr@entry=0x7fed939207e4, val=val@entry=2, clk=clk@entry=0, at=at@entry=0x7fed93920950, priv=128, p
riv@entry=1) at src/thread/__timedwait.c:52
#4  0x00007ffff7fb7894 in __pthread_cond_timedwait (c=0x7ffff7df6c40, m=0x7ffff7df6c18, ts=0x7fed93920950) at src/thread/pthr
ead_cond_timedwait.c:100
#5  0x00007ffff756e599 in ?? ()
#6  0x0000000000000000 in ?? ()

Thread 28 (LWP 26586 "ZMQbg/IO/0"):
#0  __cp_end () at src/thread/x86_64/syscall_cp.s:29
#1  0x00007ffff7fb74fc in __syscall_cp_c (nr=281, u=<optimized out>, v=<optimized out>, w=<optimized out>, x=<optimized out>,
 y=<optimized out>, z=8) at src/thread/pthread_cancel.c:33
#2  0x00007ffff7f7c286 in epoll_pwait (fd=19, ev=0x7fed93942d40, cnt=256, to=-1, sigs=0x0) at src/linux/epoll.c:28
#3  0x00007ffff6ffe1d6 in ?? ()
#4  0x0000000000000000 in ?? ()

Thread 27 (LWP 26585 "ZMQbg/Reaper"):
#0  __cp_end () at src/thread/x86_64/syscall_cp.s:29
#1  0x00007ffff7fb74fc in __syscall_cp_c (nr=281, u=<optimized out>, v=<optimized out>, w=<optimized out>, x=<optimized out>,
 y=<optimized out>, z=8) at src/thread/pthread_cancel.c:33
#2  0x00007ffff7f7c286 in epoll_pwait (fd=17, ev=0x7fed93965d40, cnt=256, to=-1, sigs=0x0) at src/linux/epoll.c:28
#3  0x00007ffff6ffe1d6 in ?? ()
#4  0x0000000000000000 in ?? ()

Thread 26 (LWP 26584 "ld-musl-x86_64."):
#0  __cp_end () at src/thread/x86_64/syscall_cp.s:29
#1  0x00007ffff7fb74fc in __syscall_cp_c (nr=202, u=<optimized out>, v=<optimized out>, w=<optimized out>, x=<optimized out>,
 y=<optimized out>, z=0) at src/thread/pthread_cancel.c:33
#2  0x00007ffff7fb6a2e in __futex4_cp (to=<optimized out>, val=2, op=128, addr=0x7fed93fbc654) at src/thread/__timedwait.c:24
#3  __timedwait_cp (addr=addr@entry=0x7fed93fbc654, val=val@entry=2, clk=clk@entry=0, at=at@entry=0x0, priv=128, priv@entry=1
) at src/thread/__timedwait.c:52
#4  0x00007ffff7fb7894 in __pthread_cond_timedwait (c=0x7ffff7ce5a18, m=0x7ffff7ce59f0, ts=0x0) at src/thread/pthread_cond_ti
medwait.c:100
#5  0x00007ffff6f2d5ad in ?? ()
#6  0x0000000000000000 in ?? ()

Thread 25 (LWP 26583 "ld-musl-x86_64."):
#0  __cp_end () at src/thread/x86_64/syscall_cp.s:29
#1  0x00007ffff7fb74fc in __syscall_cp_c (nr=202, u=<optimized out>, v=<optimized out>, w=<optimized out>, x=<optimized out>,
 y=<optimized out>, z=0) at src/thread/pthread_cancel.c:33
#2  0x00007ffff7fb6a2e in __futex4_cp (to=<optimized out>, val=2, op=128, addr=0x7fed944bf654) at src/thread/__timedwait.c:24
#3  __timedwait_cp (addr=addr@entry=0x7fed944bf654, val=val@entry=2, clk=clk@entry=0, at=at@entry=0x0, priv=128, priv@entry=1
) at src/thread/__timedwait.c:52
#4  0x00007ffff7fb7894 in __pthread_cond_timedwait (c=0x7ffff7ce5a18, m=0x7ffff7ce59f0, ts=0x0) at src/thread/pthread_cond_ti
medwait.c:100
#5  0x00007ffff6f2d5ad in ?? ()
#6  0x0000000000000000 in ?? ()

Thread 24 (LWP 26582 "ld-musl-x86_64."):
#0  __cp_end () at src/thread/x86_64/syscall_cp.s:29
#1  0x00007ffff7fb74fc in __syscall_cp_c (nr=202, u=<optimized out>, v=<optimized out>, w=<optimized out>, x=<optimized out>,
 y=<optimized out>, z=0) at src/thread/pthread_cancel.c:33
#2  0x00007ffff7fb6a2e in __futex4_cp (to=<optimized out>, val=2, op=128, addr=0x7fed949c2654) at src/thread/__timedwait.c:24
#3  __timedwait_cp (addr=addr@entry=0x7fed949c2654, val=val@entry=2, clk=clk@entry=0, at=at@entry=0x0, priv=128, priv@entry=1
) at src/thread/__timedwait.c:52
#4  0x00007ffff7fb7894 in __pthread_cond_timedwait (c=0x7ffff7ce5a18, m=0x7ffff7ce59f0, ts=0x0) at src/thread/pthread_cond_ti
medwait.c:100
#5  0x00007ffff6f2d5ad in ?? ()
#6  0x0000000000000000 in ?? ()

Thread 23 (LWP 26581 "ld-musl-x86_64."):
#0  __cp_end () at src/thread/x86_64/syscall_cp.s:29
#1  0x00007ffff7fb74fc in __syscall_cp_c (nr=202, u=<optimized out>, v=<optimized out>, w=<optimized out>, x=<optimized out>,
 y=<optimized out>, z=0) at src/thread/pthread_cancel.c:33
#2  0x00007ffff7fb6a2e in __futex4_cp (to=<optimized out>, val=2, op=128, addr=0x7fed94ec5654) at src/thread/__timedwait.c:24
#3  __timedwait_cp (addr=addr@entry=0x7fed94ec5654, val=val@entry=2, clk=clk@entry=0, at=at@entry=0x0, priv=128, priv@entry=1
) at src/thread/__timedwait.c:52
#4  0x00007ffff7fb7894 in __pthread_cond_timedwait (c=0x7ffff7ce5a18, m=0x7ffff7ce59f0, ts=0x0) at src/thread/pthread_cond_ti
medwait.c:100
#5  0x00007ffff6f2d5ad in ?? ()
#6  0x0000000000000000 in ?? ()

Thread 22 (LWP 26580 "ld-musl-x86_64."):
#0  __cp_end () at src/thread/x86_64/syscall_cp.s:29
#1  0x00007ffff7fb74fc in __syscall_cp_c (nr=202, u=<optimized out>, v=<optimized out>, w=<optimized out>, x=<optimized out>,
 y=<optimized out>, z=0) at src/thread/pthread_cancel.c:33
#2  0x00007ffff7fb6a2e in __futex4_cp (to=<optimized out>, val=2, op=128, addr=0x7fed953c8654) at src/thread/__timedwait.c:24
#3  __timedwait_cp (addr=addr@entry=0x7fed953c8654, val=val@entry=2, clk=clk@entry=0, at=at@entry=0x0, priv=128, priv@entry=1
) at src/thread/__timedwait.c:52
#4  0x00007ffff7fb7894 in __pthread_cond_timedwait (c=0x7ffff7ce5a18, m=0x7ffff7ce59f0, ts=0x0) at src/thread/pthread_cond_ti
medwait.c:100
#5  0x00007ffff6f2d5ad in ?? ()
#6  0x0000000000000000 in ?? ()

Thread 21 (LWP 26579 "ld-musl-x86_64."):
#0  __cp_end () at src/thread/x86_64/syscall_cp.s:29
#1  0x00007ffff7fb74fc in __syscall_cp_c (nr=202, u=<optimized out>, v=<optimized out>, w=<optimized out>, x=<optimized out>,
 y=<optimized out>, z=0) at src/thread/pthread_cancel.c:33
#2  0x00007ffff7fb6a2e in __futex4_cp (to=<optimized out>, val=2, op=128, addr=0x7fed958cb654) at src/thread/__timedwait.c:24
#3  __timedwait_cp (addr=addr@entry=0x7fed958cb654, val=val@entry=2, clk=clk@entry=0, at=at@entry=0x0, priv=128, priv@entry=1
) at src/thread/__timedwait.c:52
#4  0x00007ffff7fb7894 in __pthread_cond_timedwait (c=0x7ffff7ce5a18, m=0x7ffff7ce59f0, ts=0x0) at src/thread/pthread_cond_ti
medwait.c:100
#5  0x00007ffff6f2d5ad in ?? ()
#6  0x0000000000000000 in ?? ()

Thread 20 (LWP 26578 "ld-musl-x86_64."):
#0  __cp_end () at src/thread/x86_64/syscall_cp.s:29
#1  0x00007ffff7fb74fc in __syscall_cp_c (nr=202, u=<optimized out>, v=<optimized out>, w=<optimized out>, x=<optimized out>,
 y=<optimized out>, z=0) at src/thread/pthread_cancel.c:33
#2  0x00007ffff7fb6a2e in __futex4_cp (to=<optimized out>, val=2, op=128, addr=0x7fed95dce654) at src/thread/__timedwait.c:24
#3  __timedwait_cp (addr=addr@entry=0x7fed95dce654, val=val@entry=2, clk=clk@entry=0, at=at@entry=0x0, priv=128, priv@entry=1
) at src/thread/__timedwait.c:52
#4  0x00007ffff7fb7894 in __pthread_cond_timedwait (c=0x7ffff7ce5a18, m=0x7ffff7ce59f0, ts=0x0) at src/thread/pthread_cond_ti
medwait.c:100
#5  0x00007ffff6f2d5ad in ?? ()
#6  0x0000000000000000 in ?? ()

Thread 19 (LWP 26577 "ld-musl-x86_64."):
#0  __cp_end () at src/thread/x86_64/syscall_cp.s:29
#1  0x00007ffff7fb74fc in __syscall_cp_c (nr=202, u=<optimized out>, v=<optimized out>, w=<optimized out>, x=<optimized out>,
 y=<optimized out>, z=0) at src/thread/pthread_cancel.c:33
#2  0x00007ffff7fb6a2e in __futex4_cp (to=<optimized out>, val=2, op=128, addr=0x7fed962d1654) at src/thread/__timedwait.c:24
#3  __timedwait_cp (addr=addr@entry=0x7fed962d1654, val=val@entry=2, clk=clk@entry=0, at=at@entry=0x0, priv=128, priv@entry=1
) at src/thread/__timedwait.c:52
#4  0x00007ffff7fb7894 in __pthread_cond_timedwait (c=0x7ffff7ce5a18, m=0x7ffff7ce59f0, ts=0x0) at src/thread/pthread_cond_ti
medwait.c:100
#5  0x00007ffff6f2d5ad in ?? ()
#6  0x0000000000000000 in ?? ()

Thread 18 (LWP 26576 "ld-musl-x86_64."):
#0  __cp_end () at src/thread/x86_64/syscall_cp.s:29
#1  0x00007ffff7fb74fc in __syscall_cp_c (nr=202, u=<optimized out>, v=<optimized out>, w=<optimized out>, x=<optimized out>,
 y=<optimized out>, z=0) at src/thread/pthread_cancel.c:33
#2  0x00007ffff7fb6a2e in __futex4_cp (to=<optimized out>, val=2, op=128, addr=0x7fed967d4654) at src/thread/__timedwait.c:24
#3  __timedwait_cp (addr=addr@entry=0x7fed967d4654, val=val@entry=2, clk=clk@entry=0, at=at@entry=0x0, priv=128, priv@entry=1
) at src/thread/__timedwait.c:52
#4  0x00007ffff7fb7894 in __pthread_cond_timedwait (c=0x7ffff7ce5a18, m=0x7ffff7ce59f0, ts=0x0) at src/thread/pthread_cond_ti
medwait.c:100
#5  0x00007ffff6f2d5ad in ?? ()
#6  0x0000000000000000 in ?? ()

Thread 17 (LWP 26575 "ld-musl-x86_64."):
#0  __cp_end () at src/thread/x86_64/syscall_cp.s:29
#1  0x00007ffff7fb74fc in __syscall_cp_c (nr=202, u=<optimized out>, v=<optimized out>, w=<optimized out>, x=<optimized out>,
 y=<optimized out>, z=0) at src/thread/pthread_cancel.c:33
#2  0x00007ffff7fb6a2e in __futex4_cp (to=<optimized out>, val=2, op=128, addr=0x7fed96cd7654) at src/thread/__timedwait.c:24
#3  __timedwait_cp (addr=addr@entry=0x7fed96cd7654, val=val@entry=2, clk=clk@entry=0, at=at@entry=0x0, priv=128, priv@entry=1
) at src/thread/__timedwait.c:52
#4  0x00007ffff7fb7894 in __pthread_cond_timedwait (c=0x7ffff7ce5a18, m=0x7ffff7ce59f0, ts=0x0) at src/thread/pthread_cond_ti
medwait.c:100
#5  0x00007ffff6f2d5ad in ?? ()
#6  0x0000000000000000 in ?? ()

Thread 16 (LWP 26574 "ld-musl-x86_64."):
#0  __cp_end () at src/thread/x86_64/syscall_cp.s:29
#1  0x00007ffff7fb74fc in __syscall_cp_c (nr=202, u=<optimized out>, v=<optimized out>, w=<optimized out>, x=<optimized out>,
 y=<optimized out>, z=0) at src/thread/pthread_cancel.c:33
#2  0x00007ffff7fb6a2e in __futex4_cp (to=<optimized out>, val=2, op=128, addr=0x7fed971da654) at src/thread/__timedwait.c:24
#3  __timedwait_cp (addr=addr@entry=0x7fed971da654, val=val@entry=2, clk=clk@entry=0, at=at@entry=0x0, priv=128, priv@entry=1
) at src/thread/__timedwait.c:52
#4  0x00007ffff7fb7894 in __pthread_cond_timedwait (c=0x7ffff7ce5a18, m=0x7ffff7ce59f0, ts=0x0) at src/thread/pthread_cond_ti
medwait.c:100
#5  0x00007ffff6f2d5ad in ?? ()
#6  0x0000000000000000 in ?? ()

Thread 15 (LWP 26573 "ld-musl-x86_64."):
#0  __cp_end () at src/thread/x86_64/syscall_cp.s:29
#1  0x00007ffff7fb74fc in __syscall_cp_c (nr=202, u=<optimized out>, v=<optimized out>, w=<optimized out>, x=<optimized out>,
 y=<optimized out>, z=0) at src/thread/pthread_cancel.c:33
#2  0x00007ffff7fb6a2e in __futex4_cp (to=<optimized out>, val=2, op=128, addr=0x7fed976dd654) at src/thread/__timedwait.c:24
#3  __timedwait_cp (addr=addr@entry=0x7fed976dd654, val=val@entry=2, clk=clk@entry=0, at=at@entry=0x0, priv=128, priv@entry=1
) at src/thread/__timedwait.c:52
#4  0x00007ffff7fb7894 in __pthread_cond_timedwait (c=0x7ffff7ce5a18, m=0x7ffff7ce59f0, ts=0x0) at src/thread/pthread_cond_ti
medwait.c:100
#5  0x00007ffff6f2d5ad in ?? ()
#6  0x0000000000000000 in ?? ()

Thread 14 (LWP 26572 "ld-musl-x86_64."):
#0  __cp_end () at src/thread/x86_64/syscall_cp.s:29
#1  0x00007ffff7fb74fc in __syscall_cp_c (nr=202, u=<optimized out>, v=<optimized out>, w=<optimized out>, x=<optimized out>,
 y=<optimized out>, z=0) at src/thread/pthread_cancel.c:33
#2  0x00007ffff7fb6a2e in __futex4_cp (to=<optimized out>, val=2, op=128, addr=0x7fed97be0654) at src/thread/__timedwait.c:24
#3  __timedwait_cp (addr=addr@entry=0x7fed97be0654, val=val@entry=2, clk=clk@entry=0, at=at@entry=0x0, priv=128, priv@entry=1
) at src/thread/__timedwait.c:52
#4  0x00007ffff7fb7894 in __pthread_cond_timedwait (c=0x7ffff7ce5a18, m=0x7ffff7ce59f0, ts=0x0) at src/thread/pthread_cond_ti
medwait.c:100
#5  0x00007ffff6f2d5ad in ?? ()
#6  0x0000000000000000 in ?? ()

Thread 13 (LWP 26571 "ld-musl-x86_64."):
#0  __cp_end () at src/thread/x86_64/syscall_cp.s:29
#1  0x00007ffff7fb74fc in __syscall_cp_c (nr=202, u=<optimized out>, v=<optimized out>, w=<optimized out>, x=<optimized out>,
 y=<optimized out>, z=0) at src/thread/pthread_cancel.c:33
#2  0x00007ffff7fb6a2e in __futex4_cp (to=<optimized out>, val=2, op=128, addr=0x7fed980e3654) at src/thread/__timedwait.c:24
#3  __timedwait_cp (addr=addr@entry=0x7fed980e3654, val=val@entry=2, clk=clk@entry=0, at=at@entry=0x0, priv=128, priv@entry=1
) at src/thread/__timedwait.c:52
#4  0x00007ffff7fb7894 in __pthread_cond_timedwait (c=0x7ffff7ce5a18, m=0x7ffff7ce59f0, ts=0x0) at src/thread/pthread_cond_ti
medwait.c:100
#5  0x00007ffff6f2d5ad in ?? ()
#6  0x0000000000000000 in ?? ()

Thread 12 (LWP 26570 "ld-musl-x86_64."):
#0  __cp_end () at src/thread/x86_64/syscall_cp.s:29
#1  0x00007ffff7fb74fc in __syscall_cp_c (nr=202, u=<optimized out>, v=<optimized out>, w=<optimized out>, x=<optimized out>,
 y=<optimized out>, z=0) at src/thread/pthread_cancel.c:33
#2  0x00007ffff7fb6a2e in __futex4_cp (to=<optimized out>, val=2, op=128, addr=0x7fed985e6654) at src/thread/__timedwait.c:24
#3  __timedwait_cp (addr=addr@entry=0x7fed985e6654, val=val@entry=2, clk=clk@entry=0, at=at@entry=0x0, priv=128, priv@entry=1
) at src/thread/__timedwait.c:52
#4  0x00007ffff7fb7894 in __pthread_cond_timedwait (c=0x7ffff7ce5a18, m=0x7ffff7ce59f0, ts=0x0) at src/thread/pthread_cond_ti
medwait.c:100
#5  0x00007ffff6f2d5ad in ?? ()
#6  0x0000000000000000 in ?? ()

Thread 11 (LWP 26569 "ld-musl-x86_64."):
#0  __cp_end () at src/thread/x86_64/syscall_cp.s:29
#1  0x00007ffff7fb74fc in __syscall_cp_c (nr=202, u=<optimized out>, v=<optimized out>, w=<optimized out>, x=<optimized out>,
 y=<optimized out>, z=0) at src/thread/pthread_cancel.c:33
#2  0x00007ffff7fb6a2e in __futex4_cp (to=<optimized out>, val=2, op=128, addr=0x7fed98ae9654) at src/thread/__timedwait.c:24
#3  __timedwait_cp (addr=addr@entry=0x7fed98ae9654, val=val@entry=2, clk=clk@entry=0, at=at@entry=0x0, priv=128, priv@entry=1
) at src/thread/__timedwait.c:52
#4  0x00007ffff7fb7894 in __pthread_cond_timedwait (c=0x7ffff7ce5a18, m=0x7ffff7ce59f0, ts=0x0) at src/thread/pthread_cond_ti
medwait.c:100
#5  0x00007ffff6f2d5ad in ?? ()
#6  0x0000000000000000 in ?? ()

Thread 10 (LWP 26568 "ld-musl-x86_64."):
#0  __cp_end () at src/thread/x86_64/syscall_cp.s:29
#1  0x00007ffff7fb74fc in __syscall_cp_c (nr=202, u=<optimized out>, v=<optimized out>, w=<optimized out>, x=<optimized out>,
 y=<optimized out>, z=0) at src/thread/pthread_cancel.c:33
#2  0x00007ffff7fb6a2e in __futex4_cp (to=<optimized out>, val=2, op=128, addr=0x7fed98fec654) at src/thread/__timedwait.c:24
#3  __timedwait_cp (addr=addr@entry=0x7fed98fec654, val=val@entry=2, clk=clk@entry=0, at=at@entry=0x0, priv=128, priv@entry=1
) at src/thread/__timedwait.c:52
#4  0x00007ffff7fb7894 in __pthread_cond_timedwait (c=0x7ffff7ce5a18, m=0x7ffff7ce59f0, ts=0x0) at src/thread/pthread_cond_ti
medwait.c:100
#5  0x00007ffff6f2d5ad in ?? ()
#6  0x0000000000000000 in ?? ()

Thread 9 (LWP 26567 "ld-musl-x86_64."):
#0  __cp_end () at src/thread/x86_64/syscall_cp.s:29
#1  0x00007ffff7fb74fc in __syscall_cp_c (nr=202, u=<optimized out>, v=<optimized out>, w=<optimized out>, x=<optimized out>,
 y=<optimized out>, z=0) at src/thread/pthread_cancel.c:33
#2  0x00007ffff7fb6a2e in __futex4_cp (to=<optimized out>, val=2, op=128, addr=0x7fed994ef654) at src/thread/__timedwait.c:24
#3  __timedwait_cp (addr=addr@entry=0x7fed994ef654, val=val@entry=2, clk=clk@entry=0, at=at@entry=0x0, priv=128, priv@entry=1
) at src/thread/__timedwait.c:52
#4  0x00007ffff7fb7894 in __pthread_cond_timedwait (c=0x7ffff7ce5a18, m=0x7ffff7ce59f0, ts=0x0) at src/thread/pthread_cond_ti
medwait.c:100
#5  0x00007ffff6f2d5ad in ?? ()
#6  0x0000000000000000 in ?? ()

Thread 8 (LWP 26566 "ld-musl-x86_64."):
#0  __cp_end () at src/thread/x86_64/syscall_cp.s:29
#1  0x00007ffff7fb74fc in __syscall_cp_c (nr=202, u=<optimized out>, v=<optimized out>, w=<optimized out>, x=<optimized out>,
 y=<optimized out>, z=0) at src/thread/pthread_cancel.c:33
#2  0x00007ffff7fb6a2e in __futex4_cp (to=<optimized out>, val=2, op=128, addr=0x7fed999f2654) at src/thread/__timedwait.c:24
#3  __timedwait_cp (addr=addr@entry=0x7fed999f2654, val=val@entry=2, clk=clk@entry=0, at=at@entry=0x0, priv=128, priv@entry=1
) at src/thread/__timedwait.c:52
#4  0x00007ffff7fb7894 in __pthread_cond_timedwait (c=0x7ffff7ce5a18, m=0x7ffff7ce59f0, ts=0x0) at src/thread/pthread_cond_ti
medwait.c:100
#5  0x00007ffff6f2d5ad in ?? ()
#6  0x0000000000000000 in ?? ()

Thread 7 (LWP 26565 "ld-musl-x86_64."):
#0  __cp_end () at src/thread/x86_64/syscall_cp.s:29
#1  0x00007ffff7fb74fc in __syscall_cp_c (nr=202, u=<optimized out>, v=<optimized out>, w=<optimized out>, x=<optimized out>,
 y=<optimized out>, z=0) at src/thread/pthread_cancel.c:33
#2  0x00007ffff7fb6a2e in __futex4_cp (to=<optimized out>, val=2, op=128, addr=0x7fed99ef5654) at src/thread/__timedwait.c:24
#3  __timedwait_cp (addr=addr@entry=0x7fed99ef5654, val=val@entry=2, clk=clk@entry=0, at=at@entry=0x0, priv=128, priv@entry=1
) at src/thread/__timedwait.c:52
#4  0x00007ffff7fb7894 in __pthread_cond_timedwait (c=0x7ffff7ce5a18, m=0x7ffff7ce59f0, ts=0x0) at src/thread/pthread_cond_ti
medwait.c:100
#5  0x00007ffff6f2d5ad in ?? ()
#6  0x0000000000000000 in ?? ()

Thread 6 (LWP 26564 "ld-musl-x86_64."):
#0  __cp_end () at src/thread/x86_64/syscall_cp.s:29
#1  0x00007ffff7fb74fc in __syscall_cp_c (nr=202, u=<optimized out>, v=<optimized out>, w=<optimized out>, x=<optimized out>,
 y=<optimized out>, z=0) at src/thread/pthread_cancel.c:33
#2  0x00007ffff7fb6a2e in __futex4_cp (to=<optimized out>, val=2, op=128, addr=0x7fed9a3f8654) at src/thread/__timedwait.c:24
#3  __timedwait_cp (addr=addr@entry=0x7fed9a3f8654, val=val@entry=2, clk=clk@entry=0, at=at@entry=0x0, priv=128, priv@entry=1
) at src/thread/__timedwait.c:52
#4  0x00007ffff7fb7894 in __pthread_cond_timedwait (c=0x7ffff7ce5a18, m=0x7ffff7ce59f0, ts=0x0) at src/thread/pthread_cond_ti
medwait.c:100
#5  0x00007ffff6f2d5ad in ?? ()
#6  0x0000000000000000 in ?? ()

Thread 5 (LWP 26563 "ld-musl-x86_64."):
#0  __cp_end () at src/thread/x86_64/syscall_cp.s:29
#1  0x00007ffff7fb74fc in __syscall_cp_c (nr=202, u=<optimized out>, v=<optimized out>, w=<optimized out>, x=<optimized out>,
 y=<optimized out>, z=0) at src/thread/pthread_cancel.c:33
#2  0x00007ffff7fb6a2e in __futex4_cp (to=<optimized out>, val=2, op=128, addr=0x7fed9a8fb654) at src/thread/__timedwait.c:24
#3  __timedwait_cp (addr=addr@entry=0x7fed9a8fb654, val=val@entry=2, clk=clk@entry=0, at=at@entry=0x0, priv=128, priv@entry=1
) at src/thread/__timedwait.c:52
#4  0x00007ffff7fb7894 in __pthread_cond_timedwait (c=0x7ffff7ce5a18, m=0x7ffff7ce59f0, ts=0x0) at src/thread/pthread_cond_ti
medwait.c:100
#5  0x00007ffff6f2d5ad in ?? ()
#6  0x0000000000000000 in ?? ()

Thread 4 (LWP 26562 "ld-musl-x86_64."):
#0  __cp_end () at src/thread/x86_64/syscall_cp.s:29
#1  0x00007ffff7fb74fc in __syscall_cp_c (nr=202, u=<optimized out>, v=<optimized out>, w=<optimized out>, x=<optimized out>,
 y=<optimized out>, z=0) at src/thread/pthread_cancel.c:33
#2  0x00007ffff7fb6a2e in __futex4_cp (to=<optimized out>, val=2, op=128, addr=0x7fed9adfe654) at src/thread/__timedwait.c:24
#3  __timedwait_cp (addr=addr@entry=0x7fed9adfe654, val=val@entry=2, clk=clk@entry=0, at=at@entry=0x0, priv=128, priv@entry=1
) at src/thread/__timedwait.c:52
#4  0x00007ffff7fb7894 in __pthread_cond_timedwait (c=0x7ffff7ce5a18, m=0x7ffff7ce59f0, ts=0x0) at src/thread/pthread_cond_ti
medwait.c:100
#5  0x00007ffff6f2d5ad in ?? ()
#6  0x0000000000000000 in ?? ()

Thread 2 (LWP 26560 "ld-musl-x86_64."):
#0  __cp_end () at src/thread/x86_64/syscall_cp.s:29
#1  0x00007ffff7fb74fc in __syscall_cp_c (nr=202, u=<optimized out>, v=<optimized out>, w=<optimized out>, x=<optimized out>,
 y=<optimized out>, z=0) at src/thread/pthread_cancel.c:33
#2  0x00007ffff7fb6a2e in __futex4_cp (to=<optimized out>, val=2, op=128, addr=0x7ffff7e66884) at src/thread/__timedwait.c:24
#3  __timedwait_cp (addr=addr@entry=0x7ffff7e66884, val=val@entry=2, clk=clk@entry=0, at=at@entry=0x0, priv=128, priv@entry=1
) at src/thread/__timedwait.c:52
#4  0x00007ffff7fb7894 in __pthread_cond_timedwait (c=0x7ffff7ec5b38, m=0x7ffff7ec5b10, ts=0x0) at src/thread/pthread_cond_ti
medwait.c:100
#5  0x00007ffff6e8da98 in ?? ()
#6  0x0000000000000000 in ?? ()

Thread 1 (LWP 26557 "ld-musl-x86_64."):
#0  __cp_end () at src/thread/x86_64/syscall_cp.s:29
#1  0x00007ffff7fb74fc in __syscall_cp_c (nr=202, u=<optimized out>, v=<optimized out>, w=<optimized out>, x=<optimized out>,
 y=<optimized out>, z=0) at src/thread/pthread_cancel.c:33
#2  0x00007ffff7fb6a2e in __futex4_cp (to=<optimized out>, val=2, op=128, addr=0x7fffffffd134) at src/thread/__timedwait.c:24
#3  __timedwait_cp (addr=addr@entry=0x7fffffffd134, val=val@entry=2, clk=clk@entry=0, at=at@entry=0x0, priv=128, priv@entry=1
) at src/thread/__timedwait.c:52
#4  0x00007ffff7fb7894 in __pthread_cond_timedwait (c=0x7fed93850470, m=0x7fed93850448, ts=0x0) at src/thread/pthread_cond_ti
medwait.c:100
#5  0x00007ffff6b16716 in ?? ()
#6  0x00007fed93851588 in ?? ()
#7  0x00007fed93850448 in ?? ()
#8  0x00007ffff7eda9f0 in ?? ()
#9  0x00007fed93850448 in ?? ()
#10 0x0000000000500000 in ?? ()
#11 0x0000000000002000 in ?? ()
#12 0x0000000000000000 in ?? ()
(gdb)


## selsta | 2024-01-30T16:55:08+00:00
Can you use paste.debian.net to share the backtrace? Also is this the full log? I'm specifically looking for thread 39, it seems to be missing from your comment.

## tczee36 | 2024-01-30T17:07:45+00:00
> Can you use paste.debian.net to share the backtrace? Also is this the full log? I'm specifically looking for thread 39, it seems to be missing from your comment.

sry about that, some parts of the log got cut off.
full log posted here http://paste.debian.net/1305799/
also updated the log comment above
thanks!

## 0xFFFC0000 | 2024-01-30T19:53:39+00:00
Can you make sure everything is updated in your alpine? I see a similar error due to ABI [compatibility](https://github.com/lovell/sharp/issues/2570#issuecomment-792659786).

And what version of Alpine are you using?

## tczee36 | 2024-01-30T22:42:51+00:00
> Can you make sure everything is updated in your alpine? I see a similar error due to ABI [compatibility](https://github.com/lovell/sharp/issues/2570#issuecomment-792659786).
> 
> And what version of Alpine are you using?

$ cat /etc/alpine-release
3.19.1
$ uname -r
6.6.14-0-lts


## 0xFFFC0000 | 2024-01-31T11:48:24+00:00
Great. I downloaded the exact version and sync'ed monerod with my local node. But was not able to reproduce. How familiar are you with package compilation in Alpine? Can you build a debug monero package? I am not familiar with alpine at all, I did a quick search and saw this [1]. 

1. https://che-adrian.medium.com/how-to-cross-compile-alpine-linux-apk-packages-fae8a75aee88 

## tczee36 | 2024-02-01T03:33:07+00:00
> Great. I downloaded the exact version and sync'ed monerod with my local node. But was not able to reproduce. How familiar are you with package compilation in Alpine? Can you build a debug monero package? I am not familiar with alpine at all, I did a quick search and saw this [1].
> 
>     1. https://che-adrian.medium.com/how-to-cross-compile-alpine-linux-apk-packages-fae8a75aee88

Hi, thanks for the response. I'm not familiar at all with package compilation in Alpine. 
The link medium link is lacking some details on creating a debug monero package. Please provide few more tips, and i'll try to get it done.

## 0xFFFC0000 | 2024-02-01T06:23:13+00:00
> > Great. I downloaded the exact version and sync'ed monerod with my local node. But was not able to reproduce. How familiar are you with package compilation in Alpine? Can you build a debug monero package? I am not familiar with alpine at all, I did a quick search and saw this [1].
> > ```
> > 1. https://che-adrian.medium.com/how-to-cross-compile-alpine-linux-apk-packages-fae8a75aee88
> > ```
> 
> Hi, thanks for the response. I'm not familiar at all with package compilation in Alpine. The link medium link is lacking some details on creating a debug monero package. Please provide few more tips, and i'll try to get it done.

If we change this line [1]:
```
		-DCMAKE_BUILD_TYPE=None \
```
 to
```
		-DCMAKE_BUILD_TYPE=Debug \
``` 

that would at least generate better debugging information when you are debugging it. 


It seems the official link for how to build `APKBUILD` packages is here [2]. The overall steps are quite simple IMHO. Since we are building just for the sake of debugging, I believe you can skip most of the signature/verification steps.

1. https://git.alpinelinux.org/aports/tree/community/monero/APKBUILD#n46
2. https://wiki.alpinelinux.org/wiki/Creating_an_Alpine_package

In the meantime, I left my AlpineOS vm running, but so far no luck. If you are using any specific flags or config to run `monerod` please let me know.

![image](https://github.com/monero-project/monero/assets/136067098/41d3420e-9115-49f6-9fe5-fa082275336e)


## Haraade | 2024-02-04T14:56:54+00:00
Strange, I see the same behavior.

I [165.232.190.164:50514 INC] Sync data returned a new top block candidate: 3076846 -> 3493679 [Your node is 416833 blocks (1.6 years) behind]

? 3493679

## selsta | 2024-02-04T15:55:02+00:00
@Haraade you can ignore it, it's just a node sending false data. It's harmless.

## tczee36 | 2024-02-07T19:54:21+00:00
switched to debian, problem solved itself.
i'd avoid alpine linux for now 

## 0xFFFC0000 | 2024-02-08T10:40:35+00:00
I am closing this issue as it looks like it is alpine issue. 

## kayabaNerve | 2024-02-18T10:11:14+00:00
My guess is the pthread stack size is too small as musl (not Alpine) has a much lower default than glibc.

The (presumed) fix is for Monero to explicitly increase its stack size if the system default is presumably too low.

This is monerod failing to run on a widely used environment. While we can declare the environment at fault (an entire libc which has a lot of reasons to use it), I'm affected and would like monerod + musl to work as expected.

## 0xFFFC0000 | 2024-02-18T10:37:51+00:00
> My guess is the pthread stack size is too small as musl (not Alpine) has a much lower default than glibc.
> 
> The (presumed) fix is for Monero to explicitly increase its stack size if the system default is presumably too low.
> 
> This is monerod failing to run on a widely used environment. While we can declare the environment at fault (an entire libc which has a lot of reasons to use it), I'm affected and would like monerod + musl to work as expected.

What are the steps that reproduce this bug?

## kayabaNerve | 2024-02-18T11:09:28+00:00
Run monerod on Alpine.

If you have a rootless Docker and Rust toolchain, the following will do that:

```rs
git clone https://github.com/serai-dex/serai
cd serai
git checkout f0694172ef2cdf7dfde0d286e693243e4bdcacca
cargo run -p serai-orchestrator -- key_gen testnet
cargo run -p serai-orchestrator -- setup testnet
cargo run -p serai-orchestrator -- start testnet monero-daemon
```

This will create a key in a file under `~/.serai`, generate some Dockerfiles within the directory, and spawn a container for monerod. It will start no other services nor run any binaries other than `serai-orchestrator` and `docker`.

The container should SIGSEGV, presumably due to the pthread stack size, within a few minutes (<30, I'd expect, yet I think likely as soon as 5-10).

Effectively all of users complained of this, and @j-berman can confirm trivial replication. While we've moved to Debian, that has an increased surface, increased memory requirements, and slower bootup times. This isn't specific to Serai either as Alpine is largely preferred for Docker containers.

Alpine is also a Linux distro not exclusive to Docker, so this does potentially have impact to personal machines. If it is the theorized issue (pthread stack size defaults), this actually effects all musl systems.

## 0xFFFC0000 | 2024-02-18T11:14:26+00:00
> Run monerod on Alpine.
> 
> If you have a rootless Docker and Rust toolchain, the following will do that:
> 
> ```rust
> git clone https://github.com/serai-dex/serai
> cd serai
> git checkout f0694172ef2cdf7dfde0d286e693243e4bdcacca
> cargo run -p serai-orchestrator -- key_gen testnet
> cargo run -p serai-orchestrator -- setup testnet
> cargo run -p serai-orchestrator -- start testnet monero-daemon
> ```
> 
> This will create a key in a file under `~/.serai`, generate some Dockerfiles within the directory, and spawn a container for monerod. It will start no other services nor run any binaries other than `serai-orchestrator` and `docker`.
> 
> The container should SIGSEGV, presumably due to the pthread stack size, within a few minutes (<30, I'd expect, yet I think likely as soon as 5-10).
> 
> Effectively all of users complained of this, and @j-berman can confirm trivial replication. While we've moved to Debian, that has an increased surface, increased memory requirements, and slower bootup times. This isn't specific to Serai either as Alpine is largely preferred for Docker containers.
> 
> Alpine is also a Linux distro not exclusive to Docker, so this does potentially have impact to personal machines. If it is the theorized issue (pthread stack size defaults), this actually effects all musl systems.

Thanks, I ran and synced the entire mainnet blockchain on Alpine and didn't have this issue  [1]. If you have specific *steps* that reproduce this issue I am happy to take a look at it.


1. https://github.com/monero-project/monero/issues/9141#issuecomment-1920594568

## kayabaNerve | 2024-02-18T14:02:57+00:00
Given that effectively every participant I've had has reported the SIGSEGV, that's my current recommendation. I'll also note that configuration doesn't sync the mainnet blockchain and does have a variety of CLI flags.

# Action History
- Created by: tczee36 | 2024-01-29T20:05:32+00:00
- Closed at: 2024-02-08T10:40:49+00:00
