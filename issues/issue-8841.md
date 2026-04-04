---
title: 'Synchronization went to the current level ( 99% ) and then the problem started. '
source_url: https://github.com/monero-project/monero/issues/8841
author: motogon
assignees: []
labels: []
created_at: '2023-05-06T09:34:19+00:00'
updated_at: '2024-10-03T23:22:54+00:00'
type: issue
status: closed
closed_at: '2023-05-23T14:47:55+00:00'
---

# Original Description

How can it be explained, up to 99% works, and at the last percentage " crashes ".
Perhaps monerod is trying to do, which leads to a crash

2023-05-05 19:46:14.516 [P2P3] INFO global src/cryptonote_protocol/cryptonote_protocol_handler.inl:1687 Synced 2850688/2879431 (99%, 28743 left)
2023-05-05 19:46:14.782 [P2P3] INFO global src/cryptonote_protocol/cryptonote_protocol_handler.inl:1687 Synced 2850708/2879431 (99%, 28723 left)
2023-05-05 19:46:15.720 [P2P0] INFO global src/cryptonote_protocol/cryptonote_protocol_handler.inl:1687 Synced 2850728/2879431 (99%, 28703 left)
2023-05-05 19:46:16.068 [P2P0] INFO global src/cryptonote_protocol/cryptonote_protocol_handler.inl:1687 Synced 2850748/2879431 (99%, 28683 left)
2023-05-05 19:46:16.431 [P2P0] INFO global src/cryptonote_protocol/cryptonote_protocol_handler.inl:1687 Synced 2850768/2879431 (99%, 28663 left)
2023-05-05 19:46:16.846 [P2P0] INFO global src/cryptonote_protocol/cryptonote_protocol_handler.inl:1687 Synced 2850788/2879431 (99%, 28643 left)
2023-05-05 19:46:17.269 [P2P0] INFO global src/cryptonote_protocol/cryptonote_protocol_handler.inl:1687 Synced 2850808/2879431 (99%, 28623 left)
2023-05-06 05:46:46.703 0x7ff84b4a65c0 INFO logging contrib/epee/src/mlog.cpp:273 New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2023-05-06 05:46:46.705 0x7ff84b4a65c0 INFO global src/daemon/main.cpp:296 Monero 'Fluorine Fermi' (v0.18.2.2-release)
2023-05-06 05:46:46.705 0x7ff84b4a65c0 INFO msgwriter src/common/scoped_message_writer.h:102 Forking to background...
2023-05-06 05:46:46.707 0x7ff84b4a65c0 WARNING daemon src/daemon/executor.cpp:61 Monero 'Fluorine Fermi' (v0.18.2.2-release) Daemonised
2023-05-06 05:46:46.708 0x7ff84b4a65c0 INFO global src/daemon/protocol.h:53 Initializing cryptonote protocol...
2023-05-06 05:46:46.708 0x7ff84b4a65c0 INFO global src/daemon/protocol.h:58 Cryptonote protocol initialized OK
2023-05-06 05:46:46.709 0x7ff84b4a65c0 INFO global src/daemon/core.h:64 Initializing core...
2023-05-06 05:46:46.709 0x7ff84b4a65c0 INFO global src/cryptonote_core/cryptonote_core.cpp:523 Loading blockchain from folder /Users/dend/.bitmonero/lmdb ...
2023-05-06 05:46:46.860 0x7ff84b4a65c0 INFO global src/cryptonote_core/cryptonote_core.cpp:698 Loading checkpoints
2023-05-06 05:46:48.593 0x7ff84b4a65c0 INFO logging contrib/epee/src/mlog.cpp:273 New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2023-05-06 05:46:48.59
5 0x7ff84b4a65c0 INFO global src/daemon/main.cpp:296 Monero 'Fluorine Fermi' (v0.18.2.2-release)

[monerod-2023-05-06-092746.ips.zip](https://github.com/monero-project/monero/files/11411978/monerod-2023-05-06-092746.ips.zip)

# Discussion History
## selsta | 2023-05-06T12:45:16+00:00
> How can it be explained, up to 99% works, and at the last percentage " crashes ".

It doesn't crash, macOS kills it. My first guess was anti-virus but you said you don't have one so I don't know currently.

## motogon | 2023-05-06T12:59:26+00:00
> It doesn't crash, macOS kills it.

But why, 99% of synchronization passes, no problem? 
What happens at the last percent? 

## motogon | 2023-05-06T13:01:32+00:00
I run in sudo , the problem remains 

## selsta | 2023-05-06T13:02:31+00:00
> But why, 99% of synchronization passes, no problem?

Because that's when the checkpoints end, see here https://github.com/monero-project/monero/pull/8805/files#diff-e6e8140963756b6f6cb97bb2253240db5b0bd63e17fdd99df29cd51941aea637R248

## selsta | 2023-05-06T13:05:48+00:00
@motogon Can you try this version? https://github.com/monero-project/monero-gui/releases/tag/v0.18.1.2

## motogon | 2023-05-06T13:11:22+00:00
I assume that this problem is related to the update of the operating system to version 13.3.
I tried with the previous version (0.18.2.1), which worked a month ago (before the os update), I had to disable the firewall, otherwise there was an error connecting to localhost. 
The problem with crashing/killing os is also on the build version. 

If not fixed, then - with the new version of mac os - will not work :(. 


 

## motogon | 2023-05-06T13:13:54+00:00
How can I help you, localize the problem?


 

## selsta | 2023-05-06T13:14:45+00:00
> I tried with the previous version (0.18.2.1)

Did you also try v0.18.1.2?

> I assume that this problem is related to the update of the operating system to version 13.3.

I'm not sure, so far not a single other person has reported a problem with this OS version.

## motogon | 2023-05-06T13:18:06+00:00
> Did you also try v0.18.1.2?

yes 

## selsta | 2023-05-06T13:20:23+00:00
Can you try to start `monerod` like this?

```
MONERO_RANDOMX_UMASK=1 /Applications/monero-wallet-gui.app/Contents/MacOS/monerod
```

If this doesn't work try with `=2`, `=8` and `=16` instead of `=1`.

## motogon | 2023-05-06T13:25:50+00:00
2023-05-06 13:24:52.385	I Monero 'Fluorine Fermi' (v0.18.2.2-release)
2023-05-06 13:24:52.385	I Initializing cryptonote protocol...
2023-05-06 13:24:52.385	I Cryptonote protocol initialized OK
2023-05-06 13:24:52.386	I Initializing core...
2023-05-06 13:24:52.387	I Loading blockchain from folder /Users/dend/.bitmonero/lmdb ...
2023-05-06 13:24:55.176	I Loading checkpoints
2023-05-06 13:24:55.176	I Core initialized OK
2023-05-06 13:24:55.176	I Initializing p2p server...
2023-05-06 13:24:55.199	I p2p server initialized OK
2023-05-06 13:24:55.199	I Initializing core RPC server...
2023-05-06 13:24:55.202	I Binding on 127.0.0.1 (IPv4):18081
2023-05-06 13:24:55.238	I core RPC server initialized OK on port: 18081
2023-05-06 13:24:55.241	I Starting core RPC server...
2023-05-06 13:24:55.241	I core RPC server started ok
2023-05-06 13:24:55.244	I Starting p2p net loop...
2023-05-06 13:24:56.246	I 
2023-05-06 13:24:56.246	I **********************************************************************
2023-05-06 13:24:56.246	I The daemon will start synchronizing with the network. This may take a long time to complete.
2023-05-06 13:24:56.246	I 
2023-05-06 13:24:56.246	I You can set the level of process detailization through "set_log <level|categories>" command,
2023-05-06 13:24:56.246	I where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).
2023-05-06 13:24:56.246	I 
2023-05-06 13:24:56.246	I Use the "help" command to see the list of available commands.
2023-05-06 13:24:56.246	I Use "help <command>" to see a command's documentation.
2023-05-06 13:24:56.247	I **********************************************************************
2023-05-06 13:24:56.735	I [162.218.65.25:18180 OUT] Sync data returned a new top block candidate: 2850808 -> 2879921 [Your node is 29113 blocks (1.3 months) behind] 
2023-05-06 13:24:56.735	I SYNCHRONIZATION started
2023-05-06 13:25:19.697	I Synced 2850828/2879921 (98%, 29093 left)
2023-05-06 13:25:30.080	I Synced 2850848/2879921 (98%, 29073 left)
2023-05-06 13:25:41.880	I Synced 2850868/2879921 (98%, 29053 left)


## selsta | 2023-05-06T13:37:43+00:00
Did you try all 4 values?

## motogon | 2023-05-06T13:50:00+00:00
also synchronization with value =1 

2023-05-06 13:48:15.621	I Synced 2852408/2879931 (99%, 27523 left, 5% of total synced, estimated 6.7 hours left)
2023-05-06 13:48:46.271	I Synced 2852428/2879931 (99%, 27503 left)
2023-05-06 13:48:53.160	I Synced 2852448/2879931 (99%, 27483 left)
2023-05-06 13:49:02.943	I Synced 2852468/2879931 (99%, 27463 left)
2023-05-06 13:49:16.207	I Synced 2852488/2879931 (99%, 27443 left)
2023-05-06 13:49:24.144	I Synced 2852508/2879931 (99%, 27423 left)
2023-05-06 13:49:34.962	I Synced 2852528/2879931 (99%, 27403 left)
2023-05-06 13:49:49.427	I Synced 2852548/2879931 (99%, 27383 left)
2023-05-06 13:49:55.827	I Synced 2852568/2879932 (99%, 27364 left)


## selsta | 2023-05-06T14:06:50+00:00
So does it work?

## motogon | 2023-05-06T14:09:50+00:00
it looks like it works . 

2023-05-06 14:09:33.841	I Synced 2855148/2879940 (99%, 24792 left)
2023-05-06 14:09:38.680	I Synced 2855168/2879940 (99%, 24772 left)
2023-05-06 14:09:48.657	I Synced 2855188/2879940 (99%, 24752 left, 14% of total synced, estimated 4.2 hours left)
2023-05-06 14:09:52.426	I Synced 2855208/2879940 (99%, 24732 left)
2023-05-06 14:09:56.209	I Synced 2855228/2879941 (99%, 24713 left)



## motogon | 2023-05-06T17:49:56+00:00
> So does it work?

The synchronization completely passed, there were no problems 

## selsta | 2023-05-06T17:51:39+00:00
MONERO_RANDOMX_UMASK=1 disables LargePageAllocator, which was the reason why monerod got killed. I don't know why this happening. My first suggestion would be to try again with the next macOS update to see if the issue is still present.

## motogon | 2023-05-06T18:02:29+00:00
ok 
thanks

## motogon | 2023-05-11T12:08:25+00:00
after updating mocos to version 13.3.1 - the problem with default startup of monerod - remained 

## motogon | 2023-05-23T14:47:51+00:00
After upgrading to 13.4 - it started normally from the gui 

Now, the ticket can be closed. 
thanks 

## johnstef99 | 2024-10-03T22:49:23+00:00
I am on macos 15.0 (macbook M1) and I had the same issue at 90% synchronization. With MONERO_RANDOMX_UMASK=1 is running ok but is weird that this problem comes up again for every new macos. Here are the logs from lldb

```gdb
$ lldb monerod
(lldb) target create "monerod"
Current executable set to '/Users/johnstef/Downloads/monero-aarch64-apple-darwin11-v0.18.3.4/monerod' (arm64).
(lldb) run
Process 8557 launched: '/Users/johnstef/Downloads/monero-aarch64-apple-darwin11-v0.18.3.4/monerod' (arm64)
2024-10-03 22:44:44.391 I Monero 'Fluorine Fermi' (v0.18.3.4-release)
2024-10-03 22:44:44.391 I Initializing cryptonote protocol...
2024-10-03 22:44:44.391 I Cryptonote protocol initialized OK
2024-10-03 22:44:44.391 I Initializing core...
2024-10-03 22:44:44.391 I Loading blockchain from folder /Users/johnstef/.bitmonero/lmdb ...
2024-10-03 22:44:44.417 I Loading checkpoints
2024-10-03 22:44:44.417 I Core initialized OK
2024-10-03 22:44:44.417 I Initializing p2p server...
2024-10-03 22:44:44.421 I p2p server initialized OK
2024-10-03 22:44:44.422 I Initializing core RPC server...
2024-10-03 22:44:44.422 I Binding on 127.0.0.1 (IPv4):18081
2024-10-03 22:44:44.437 I core RPC server initialized OK on port: 18081
2024-10-03 22:44:44.438 I Starting core RPC server...
2024-10-03 22:44:44.438 I core RPC server started ok
2024-10-03 22:44:44.438 I Starting p2p net loop...
2024-10-03 22:44:45.439 I
2024-10-03 22:44:45.440 I **********************************************************************
2024-10-03 22:44:45.440 I The daemon will start synchronizing with the network. This may take a long time to complete.
2024-10-03 22:44:45.440 I
2024-10-03 22:44:45.440 I You can set the level of process detailization through "set_log <level|categories>" command,
2024-10-03 22:44:45.440 I where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).
2024-10-03 22:44:45.440 I
2024-10-03 22:44:45.440 I Use the "help" command to see the list of available commands.
2024-10-03 22:44:45.440 I Use "help <command>" to see a command's documentation.
2024-10-03 22:44:45.440 I **********************************************************************
2024-10-03 22:44:45.650 I [88.99.105.74:18080 OUT] Sync data returned a new top block candidate: 3201410 -> 3251264 [Your node is 49854 blocks (2.3 months) behind]
2024-10-03 22:44:45.650 I SYNCHRONIZATION started
Process 8557 stopped
* thread #17, stop reason = EXC_GUARD (code=11529215050363437056, subcode=0x0)
    frame #0: 0x0000000188fd97e8 libsystem_kernel.dylib`__munmap + 8
libsystem_kernel.dylib`:
->  0x188fd97e8 <+8>:  b.lo   0x188fd9808               ; <+40>
    0x188fd97ec <+12>: pacibsp
    0x188fd97f0 <+16>: stp    x29, x30, [sp, #-0x10]!
    0x188fd97f4 <+20>: mov    x29, sp
  thread #29, stop reason = EXC_GUARD (code=11529215050363437056, subcode=0x0)
    frame #0: 0x0000000188fd97e8 libsystem_kernel.dylib`__munmap + 8
libsystem_kernel.dylib`:
->  0x188fd97e8 <+8>:  b.lo   0x188fd9808               ; <+40>
    0x188fd97ec <+12>: pacibsp
    0x188fd97f0 <+16>: stp    x29, x30, [sp, #-0x10]!
    0x188fd97f4 <+20>: mov    x29, sp
  thread #30, stop reason = EXC_GUARD (code=11529215050363437056, subcode=0x0)
    frame #0: 0x0000000188fd97e8 libsystem_kernel.dylib`__munmap + 8
libsystem_kernel.dylib`:
->  0x188fd97e8 <+8>:  b.lo   0x188fd9808               ; <+40>
    0x188fd97ec <+12>: pacibsp
    0x188fd97f0 <+16>: stp    x29, x30, [sp, #-0x10]!
    0x188fd97f4 <+20>: mov    x29, sp
  thread #35, stop reason = EXC_GUARD (code=11529215050363437056, subcode=0x0)
    frame #0: 0x0000000188fd97e8 libsystem_kernel.dylib`__munmap + 8
libsystem_kernel.dylib`:
->  0x188fd97e8 <+8>:  b.lo   0x188fd9808               ; <+40>
    0x188fd97ec <+12>: pacibsp
    0x188fd97f0 <+16>: stp    x29, x30, [sp, #-0x10]!
    0x188fd97f4 <+20>: mov    x29, sp
Target 0: (monerod) stopped.
(lldb)
error: No auto repeat.
(lldb) continue ^C
(lldb) ^D
[johnstef@jmb ~/Downloads/monero-aarch64-apple-darwin11-v0.18.3.4]$
[johnstef@jmb ~/Downloads/monero-aarch64-apple-darwin11-v0.18.3.4]$ lldb monerod
[johnstef@jmb ~/Downloads/monero-aarch64-apple-darwin11-v0.18.3.4]$ lldb monerod
(lldb) target create "monerod"
Current executable set to '/Users/johnstef/Downloads/monero-aarch64-apple-darwin11-v0.18.3.4/monerod' (arm64).
(lldb) run
Process 8566 launched: '/Users/johnstef/Downloads/monero-aarch64-apple-darwin11-v0.18.3.4/monerod' (arm64)
2024-10-03 22:45:08.413 I Monero 'Fluorine Fermi' (v0.18.3.4-release)
2024-10-03 22:45:08.413 I Initializing cryptonote protocol...
2024-10-03 22:45:08.413 I Cryptonote protocol initialized OK
2024-10-03 22:45:08.413 I Initializing core...
2024-10-03 22:45:08.413 I Loading blockchain from folder /Users/johnstef/.bitmonero/lmdb ...
2024-10-03 22:45:08.439 I Loading checkpoints
2024-10-03 22:45:08.439 I Core initialized OK
2024-10-03 22:45:08.439 I Initializing p2p server...
2024-10-03 22:45:08.443 I p2p server initialized OK
2024-10-03 22:45:08.443 I Initializing core RPC server...
2024-10-03 22:45:08.443 I Binding on 127.0.0.1 (IPv4):18081
2024-10-03 22:45:08.460 I core RPC server initialized OK on port: 18081
2024-10-03 22:45:08.460 I Starting core RPC server...
2024-10-03 22:45:08.460 I core RPC server started ok
2024-10-03 22:45:08.460 I Starting p2p net loop...
2024-10-03 22:45:09.462 I
2024-10-03 22:45:09.462 I **********************************************************************
2024-10-03 22:45:09.462 I The daemon will start synchronizing with the network. This may take a long time to complete.
2024-10-03 22:45:09.462 I
2024-10-03 22:45:09.462 I You can set the level of process detailization through "set_log <level|categories>" command,
2024-10-03 22:45:09.462 I where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).
2024-10-03 22:45:09.462 I
2024-10-03 22:45:09.462 I Use the "help" command to see the list of available commands.
2024-10-03 22:45:09.462 I Use "help <command>" to see a command's documentation.
2024-10-03 22:45:09.462 I **********************************************************************
2024-10-03 22:45:09.643 I [88.99.105.74:18080 OUT] Sync data returned a new top block candidate: 3201410 -> 3251264 [Your node is 49854 blocks (2.3 months) behind]
2024-10-03 22:45:09.643 I SYNCHRONIZATION started
Process 8566 stopped
* thread #13, stop reason = EXC_GUARD (code=11529215050363437056, subcode=0x0)
    frame #0: 0x0000000188fd97e8 libsystem_kernel.dylib`__munmap + 8
libsystem_kernel.dylib`:
->  0x188fd97e8 <+8>:  b.lo   0x188fd9808               ; <+40>
    0x188fd97ec <+12>: pacibsp
    0x188fd97f0 <+16>: stp    x29, x30, [sp, #-0x10]!
    0x188fd97f4 <+20>: mov    x29, sp
  thread #29, stop reason = EXC_GUARD (code=11529215050363437056, subcode=0x0)
    frame #0: 0x0000000188fd97e8 libsystem_kernel.dylib`__munmap + 8
libsystem_kernel.dylib`:
->  0x188fd97e8 <+8>:  b.lo   0x188fd9808               ; <+40>
    0x188fd97ec <+12>: pacibsp
    0x188fd97f0 <+16>: stp    x29, x30, [sp, #-0x10]!
    0x188fd97f4 <+20>: mov    x29, sp
  thread #30, stop reason = EXC_GUARD (code=11529215050363437056, subcode=0x0)
    frame #0: 0x0000000188fd97e8 libsystem_kernel.dylib`__munmap + 8
libsystem_kernel.dylib`:
->  0x188fd97e8 <+8>:  b.lo   0x188fd9808               ; <+40>
    0x188fd97ec <+12>: pacibsp
    0x188fd97f0 <+16>: stp    x29, x30, [sp, #-0x10]!
    0x188fd97f4 <+20>: mov    x29, sp
  thread #35, stop reason = EXC_GUARD (code=11529215050363437056, subcode=0x0)
    frame #0: 0x0000000188fd97e8 libsystem_kernel.dylib`__munmap + 8
libsystem_kernel.dylib`:
->  0x188fd97e8 <+8>:  b.lo   0x188fd9808               ; <+40>
    0x188fd97ec <+12>: pacibsp
    0x188fd97f0 <+16>: stp    x29, x30, [sp, #-0x10]!
    0x188fd97f4 <+20>: mov    x29, sp
Target 0: (monerod) stopped.
(lldb) continue
Process 8566 resuming
Process 8566 stopped
* thread #1, queue = 'com.apple.main-thread', stop reason = signal SIGKILL
    frame #0: 0x0000000188fd95cc libsystem_kernel.dylib`__psynch_cvwait + 8
libsystem_kernel.dylib`:
->  0x188fd95cc <+8>:  b.lo   0x188fd95ec               ; <+40>
    0x188fd95d0 <+12>: pacibsp
    0x188fd95d4 <+16>: stp    x29, x30, [sp, #-0x10]!
    0x188fd95d8 <+20>: mov    x29, sp
Target 0: (monerod) stopped.
(lldb) continue
Process 8566 resuming
Process 8566 exited with status = 9 (0x00000009) Terminated due to signal 9
```

## selsta | 2024-10-03T22:57:19+00:00
@johnstef99 we have not received any bug reports yet for macOS 15 and I do not have this issue on my M1 Mac. I don't think this is related to this issue here, it seems to be a file descriptor issue based on searching for EXC_GUARD.

## johnstef99 | 2024-10-03T23:22:18+00:00
@selsta oh ok I thought because MONERO_RANDOMX_UMASK=1 disables LargePageAllocator and when I am running it with that umask it works, that it would be the same bug.

# Action History
- Created by: motogon | 2023-05-06T09:34:19+00:00
- Closed at: 2023-05-23T14:47:55+00:00
