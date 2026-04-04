---
title: Couldn't allocate RandomX dataset for miner on Rpi 4B
source_url: https://github.com/monero-project/monero/issues/7293
author: w3irdrobot
assignees: []
labels: []
created_at: '2021-01-08T15:29:41+00:00'
updated_at: '2021-01-09T20:08:29+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I'm running `monerod` on a 2GB Raspberry Pi 4B and keep getting the error `Couldn't allocate RandomX dataset for miner` when attempting to background mine. This has been going on for a while, and I have just not been all that worried about it. However, I'd like to start mining to help the network but seem to be unable to. Looking through other issues, I noticed it could be the version of `gcc`, but as far as I can tell, I'm using one that should work. 

```shell
$ uname -a
Linux rasppi1 5.4.83-v7l+ #1379 SMP Mon Dec 14 13:11:54 GMT 2020 armv7l GNU/Linux

$ gcc --version
gcc (Raspbian 8.3.0-6+rpi1) 8.3.0
Copyright (C) 2018 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

$ monerod --version
Monero 'Oxygen Orion' (v0.17.1.9-release)
```

Relevant logs (log-level=1):

```
...
2021-01-08 15:17:56.034	[P2P8]	INFO	miner	src/cryptonote_basic/miner.cpp:409	Mining has started with 1 threads, good luck!
2021-01-08 15:17:56.034	[P2P8]	WARNING	miner	src/cryptonote_basic/miner.cpp:414	Background mining controller thread started
2021-01-08 15:17:56.034	[P2P8]	INFO	miner	src/cryptonote_basic/miner.cpp:419	Ignoring battery
...
2021-01-08 15:17:56.434	[miner 0]	INFO	global	src/cryptonote_basic/miner.cpp:548	background mining is enabled, but not started, waiting until start triggers
...
2021-01-08 15:18:10.832	[miner 0]	WARNING	randomx	contrib/epee/src/mlog.cpp:503	Couldn't allocate RandomX dataset for miner
...
```


# Discussion History
## moneromooo-monero | 2021-01-08T15:52:04+00:00
It tries to allocate 2 GB. Not gonna work.

## hyc | 2021-01-08T15:55:26+00:00
It will fallback to mining in slow mode with only the 256MB caches. So it should still work, it just won't be fast enough to be worth anything.

## w3irdrobot | 2021-01-08T16:27:23+00:00
@moneromooo-monero is there a log I'm missing that shows it's allocating 2GB?

## w3irdrobot | 2021-01-08T18:51:17+00:00
I moved this to a 8GB Rpi 4B and am still having this issue.

## moneromooo-monero | 2021-01-08T19:42:33+00:00
No, memory allocations aren't logged. Logging does indeed allocate memory so it wouldn't go well :)

About the 8 GB one, do you have huge pages enabled in the kernel ? 

## w3irdrobot | 2021-01-08T20:11:33+00:00
I'm going to guess since I'm not sure what that is. Looking up how to enable it, but I don't quite understand it.

## moneromooo-monero | 2021-01-08T22:35:55+00:00
The contents of /proc/sys/vm/nr_hugepages is the number of huge pages allocated by the system. If the pseudo file does not exist, your kernel does not support them.

## w3irdrobot | 2021-01-08T23:52:42+00:00
Well shoot. Then I may need to change kernels or something. Thanks for the help.

## w3irdrobot | 2021-01-09T18:57:02+00:00
@moneromooo-monero I have enabled hugepages in the kernel and allocated 6GB to them and still seem to be having the issue. 

```
cat /proc/sys/vm/nr_hugepages
3072
```

## moneromooo-monero | 2021-01-09T20:08:29+00:00
Run with strace then, to see what syscall fails right before it. If no syscall fails, it's likely memory. Or if mmap does.
strace -o FILENAME monerod usual-arguments

# Action History
- Created by: w3irdrobot | 2021-01-08T15:29:41+00:00
