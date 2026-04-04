---
title: monerod Segmentation fault in libzmq.so
source_url: https://github.com/monero-project/monero/issues/8238
author: othello777
assignees: []
labels: []
created_at: '2022-04-05T16:07:42+00:00'
updated_at: '2023-08-09T16:22:00+00:00'
type: issue
status: closed
closed_at: '2023-08-09T16:22:00+00:00'
---

# Original Description
I've been experiencing segfaults every 1-5 days after starting the monero daemon. 

arguments:
`--zmq-pub tcp://<local ip>:18083 --disable-dns-checkpoints --enable-dns-blocklist --rpc-bind-ip <local ip> --restricted-rpc --confirm-external-bind`
gdb output:
```
--Type <RET> for more, q to quit, c to continue without paging--c

Thread 11 "monerod" received signal SIGSEGV, Segmentation fault.
[Switching to Thread 0x7fdc9f7fe700 (LWP 49359)]
0x00007ffff7dc8483 in ?? () from /lib/x86_64-linux-gnu/libzmq.so.5
```
I got this far but I'm a bit stumped. thanks

# Discussion History
## selsta | 2022-04-05T18:01:45+00:00
Which monero version are you using? Where did you get it? Is it custom compiled?

## othello777 | 2022-04-05T18:22:58+00:00
oh right, yes it is compiled from source. originally it was compile from source the latest release (0.17) but after it was crashing a bunch I pulled the rest of the changes and recompiled. but it still crashes every 1-5 days. I think I've been on 319b831e65437f1c8e5ff4b4cb9be03f091f6fc6
my libzmq info:
`libzmq3-dev/focal,now 4.3.2-2ubuntu1 amd64 [installed]`
`libzmq5/focal,now 4.3.2-2ubuntu1 amd64 [installed,automatic]`

## selsta | 2022-04-05T18:25:43+00:00
Can you try to compile with

```
make depends target=x86_64-linux-gnu
```

It will build static binaries and the dependencies get also compiled from scratch. That will make sure you have to latest version of libzmq, or at least close to latest.

## othello777 | 2022-04-08T17:35:20+00:00
It gave errors about libtool and gperf not being installed. I recompiled successfully and will be testing now. if it doesn't crash within a week it will be solved. thanks

## othello777 | 2022-04-08T20:56:45+00:00
ok it still crashed. its notable that I am running p2pool and monerod on a PC with only 4GB of RAM (and 4GB swap)

## othello777 | 2022-04-09T03:22:29+00:00
OS: Ubuntu Server 20.04
CPU: Intel Core2 Duo E6750
RAM: 4x1GB DDR2
Storage: 2 HDDs in a software RAID1

## selsta | 2022-04-09T15:41:00+00:00
As far as I know if RAM is an issue it would usually get killed by OOM, not a segfault in libzmq.

## SChernykh | 2022-04-09T15:41:11+00:00
You can try to run p2pool with `--no-randomx --no-cache` parameteres to use minimum RAM.

## othello777 | 2022-04-11T15:37:50+00:00
@selsta good to know that. I notice the CPU on the machine isn't used much so that wouldnt be an issue either.
@SChernykh thanks I'll try that.

## othello777 | 2022-04-13T02:09:03+00:00
I tried running p2pool with the arguments and monerod still crashed

## selsta | 2023-08-09T00:04:59+00:00
Do you still have this issue? Can you reproduce with release binaries from getmonero.org?

## othello777 | 2023-08-09T16:22:00+00:00
Sorry the machine that was running this has long since been repurposed. I'm pretty sure it didn't segfault like this on anything else. Seeing as I am unable to reproduce it at the moment, I'll close the issue.

# Action History
- Created by: othello777 | 2022-04-05T16:07:42+00:00
- Closed at: 2023-08-09T16:22:00+00:00
