---
title: addressing monerod "Killed" / OOM
source_url: https://github.com/monero-project/monero/issues/2137
author: itdaniher
assignees: []
labels: []
created_at: '2017-07-01T17:02:14+00:00'
updated_at: '2021-03-24T19:22:06+00:00'
type: issue
status: closed
closed_at: '2017-07-06T22:40:54+00:00'
---

# Original Description
Running Monerod with less than 4GB of RAM and the stock settings seems to pretty reliably result in the kernel / OS killing the daemon with an OOM error.

This is what dmesg looks like on my machine when this happens:
```
[242652.974908] monerod invoked oom-killer: gfp_mask=0x201da, order=0, oom_score_adj=0
[242652.974925] monerod cpuset=/ mems_allowed=0
[242652.974934] CPU: 1 PID: 26389 Comm: monerod Tainted: G         C   3.10.xx #2
[242652.974938] Call trace:
[242652.977715] [<ffffffc000088bd0>] dump_backtrace+0x0/0x120
[242652.977722] [<ffffffc000088d14>] show_stack+0x24/0x30
[242652.977732] [<ffffffc00017a594>] dump_header.isra.6+0x9c/0x1f8
[242652.977738] [<ffffffc00017ac50>] oom_kill_process+0x248/0x3c0
[242652.977744] [<ffffffc00017b2b0>] out_of_memory+0x2d0/0x300
[242652.977752] [<ffffffc000180110>] __alloc_pages_nodemask+0x938/0x948
[242652.977758] [<ffffffc000178e38>] filemap_fault+0x140/0x3c8
[242652.977767] [<ffffffc00019c408>] __do_fault+0x78/0x658
[242652.977774] [<ffffffc00019fac0>] handle_pte_fault+0x98/0xa58
[242652.977780] [<ffffffc0001a1728>] handle_mm_fault+0x140/0x278
[242652.977789] [<ffffffc00009498c>] do_page_fault+0x24c/0x320
[242652.977795] [<ffffffc000081248>] do_mem_abort+0x50/0xa8
```

Here's some conversation about this happening on [reddit](https://www.reddit.com/r/Monero/comments/6ki2s1/monerod_crashing/).

It seems like running with ```--limit-rate=400``` and ```--max-concurrency=1``` resolve my issues, allowing monerod to sync using 1.3GB of my 2GB of RAM.




# Discussion History
## hyc | 2017-07-01T18:42:30+00:00
I see you're on a pine64. I've been running git rev e3da0ca8280d0a68a750ffe48b8bc432ce1b3d0e for about a month on a Beelink GT1. No special measures needed.

## itdaniher | 2017-07-01T19:57:48+00:00
Interesting! I am, indeed, on a pine64. I'll compile from source and report back. Does that patch reduce memory usage somehow?

## hyc | 2017-07-01T23:01:40+00:00
Mainly it includes b52abd1370cc21484d64f45504adbab47240debf which definitely reduces RAM use.

## itdaniher | 2017-07-02T07:48:57+00:00
Very cool, thanks for the information. I've finished building from source and am now running without any extra flags. I'll report peak RAM usage from my logs after letting it run awhile. Thanks @hyc!

## itdaniher | 2017-07-02T08:02:29+00:00
My build from master at a0b494aa71355ce4237764297f715fc0b19a5dac did not last very long...

```
SYNCHRONIZATION started
[1]    6955 bus error  ./build/release/bin/monerod
```

## itdaniher | 2017-07-02T08:07:33+00:00
On the next run, it segfaulted.

Building with debug symbols now and getting a traceback with gdb. Out of the OOM frying pan and into the segfault fire!

## hyc | 2017-07-02T11:21:48+00:00
Yeah current master is broken. PR #2130 might help you but there's a lot of other stuff changed that I don't think is stable yet.  I suggest you just use e3da0ca for a while. Or maybe up to 3fc22e7.

## itdaniher | 2017-07-06T22:31:03+00:00
disregard the last version of this comment where I erroneously stated I was still seeing OOM.


monerod is still syncing (3 days uptime, new record on the pine64) with e3da0ca. Gotten all the way to 689001/1348576 blocks. It's using 80+% of the 2GB of RAM and maxing out the four cores. It's kind of a shame monerod doesn't play well with smaller computers, but such is the price.

Closing this issue as OOM issues seem to have been largely alleviated since the last release.

Thanks @hyc!

## hyc | 2017-07-06T22:39:21+00:00
Yeah that's definitely odd. I guess you should try what others have suggested, and just use --block-sync-size 20 (or 10, if needed).

## itdaniher | 2017-07-06T22:42:55+00:00
(it was my other pine64 with the latest stable release that was still ooming, not surprising. ssh'd into wrong box)

## renecannao | 2017-08-08T21:45:44+00:00
I am having a similar issue, but I am not sure if it is related or not.

The box has 16GB of RAM, yet `monerod` is being killed by OOM killer after a couple of days.
The node is fully synced. Here is an example where I restarted `monerod` and it was just 5 blocks behind.
In case it is useful, I started it with [heaptrack](http://milianw.de/blog/heaptrack-a-heap-memory-profiler-for-linux) , output attached.
Interestingly, process immediately starts with 35GB (thirtyfive!) of virtual memory.
Resident memory ramp up slowly, and after 1 hour is already at 2.6GB .
```
root@scw-f25b17:~/monero-v0.10.3.1# heaptrack ./monerod --max-concurrency=1 --confirm-external-bind --rpc-bind-ip 0.0.0.0
heaptrack output will be written to "/root/monero-v0.10.3.1/heaptrack.monerod.24494.gz"
starting application, this might take some time...
2017-08-08 20:21:01.637     7faf13610780        INFO    global  contrib/epee/src/mlog.cpp:145   New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
2017-08-08 20:21:01.638     7faf13610780        INFO    global  src/daemon/main.cpp:282 Monero 'Wolfram Warptangent' (v0.10.3.1-release)
2017-08-08 20:21:01.643     7faf13610780        INFO    global  src/daemon/protocol.h:55        Initializing cryptonote protocol...
2017-08-08 20:21:01.643     7faf13610780        INFO    global  src/daemon/protocol.h:60        Cryptonote protocol initialized OK
2017-08-08 20:21:01.651     7faf13610780        INFO    global  src/daemon/p2p.h:63     Initializing p2p server...
2017-08-08 20:21:05.918     7faf13610780        INFO    global  src/daemon/p2p.h:68     P2p server initialized OK
2017-08-08 20:21:05.919     7faf13610780        INFO    global  src/daemon/rpc.h:58     Initializing core rpc server...
2017-08-08 20:21:05.920     7faf13610780        INFO    global  contrib/epee/include/net/http_server_impl_base.h:70     Binding on 0.0.0.0:18081
2017-08-08 20:21:05.921     7faf13610780        INFO    global  src/daemon/rpc.h:63     Core rpc server initialized OK on port: 18081
2017-08-08 20:21:05.921     7faf13610780        INFO    global  src/daemon/core.h:73    Initializing core...
2017-08-08 20:21:05.955     7faf13610780        INFO    global  src/cryptonote_core/cryptonote_core.cpp:326     Loading blockchain from folder /root/.bitmonero/lmdb ...
2017-08-08 20:21:08.207     7faf13610780        INFO    global  src/daemon/core.h:78    Core initialized OK
2017-08-08 20:21:08.207     7faf13610780        INFO    global  src/daemon/rpc.h:68     Starting core rpc server...
2017-08-08 20:21:08.214 [SRV_MAIN]      INFO    global  src/daemon/rpc.h:73     Core rpc server started ok
2017-08-08 20:21:08.223 [SRV_MAIN]      INFO    global  src/daemon/p2p.h:78     Starting p2p net loop...
2017-08-08 20:21:09.225 [P2P0]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1098
**********************************************************************
The daemon will start synchronizing with the network. It may take up to several hours.

You can set the level of process detailization* through "set_log <level|categories>" command*,
where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING)

Use the "help" command to see the list of available commands.
**********************************************************************

2017-08-08 20:21:10.097 [P2P6]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:293     [173.247.232.234:18080 OUT] Sync data returned a new top block candidate: 1372314 -> 1372319 [Your node is 5 blocks (0 days) behind] 
SYNCHRONIZATION started
2017-08-08 20:21:16.623 [P2P3]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1004    [173.247.232.234:18080 OUT]  Synced 1372319/1372319
2017-08-08 20:21:16.624 [P2P3]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1099    SYNCHRONIZED OK
2017-08-08 20:21:16.625 [P2P3]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1115
**********************************************************************
You are now synchronized with the network. You may now start monero-wallet-cli.

Use the "help" command to see the list of available commands.
**********************************************************************
2017-08-08 20:21:16.798 [P2P5]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:293     [90.114.26.225:18080 OUT] Sync data returned a new top block candidate: 1372319 -> 1372320 [Your node is 1 blocks (0 days) behind] 
SYNCHRONIZATION started
2017-08-08 20:21:17.574 [P2P9]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1004    [104.238.164.10:18080 OUT]  Synced 1372320/1372320
2017-08-08 20:21:17.575 [P2P9]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1099    SYNCHRONIZED OK
```

Running few `ps` along the way to monitor memory growth:
```
root@scw-f25b17:~# ps aux | grep monero
root     24494  0.0  0.0   4340  1588 pts/17   S+   20:21   0:00 /bin/sh /usr/local/bin/heaptrack ./monerod --max-concurrency=1 --confirm-external-bind --rpc-bind-ip 0.0.0.0
root     24507 31.3  0.9 37027848 161948 pts/17 Sl+ 20:21   0:26 ./monerod --max-concurrency=1 --confirm-external-bind --rpc-bind-ip 0.0.0.0
root     24552  0.0  0.0  12736  2116 pts/18   S+   20:22   0:00 grep monero
```
```
root@scw-f25b17:~# ps aux | grep monero
root     24494  0.0  0.0   4340  1588 pts/17   S+   20:21   0:00 /bin/sh /usr/local/bin/heaptrack ./monerod --max-concurrency=1 --confirm-external-bind --rpc-bind-ip 0.0.0.0
root     24507 30.8  2.0 37029904 340072 pts/17 Sl+ 20:21   0:46 ./monerod --max-concurrency=1 --confirm-external-bind --rpc-bind-ip 0.0.0.0
root     24575  0.0  0.0  12736  2100 pts/18   S+   20:23   0:00 grep monero
```
```
root@scw-f25b17:~# ps aux | grep monero
root     24494  0.0  0.0   4340  1588 pts/17   S+   20:21   0:00 /bin/sh /usr/local/bin/heaptrack ./monerod --max-concurrency=1 --confirm-external-bind --rpc-bind-ip 0.0.0.0
root     24507 31.0  3.4 37057064 563488 pts/17 Sl+ 20:21   2:42 ./monerod --max-concurrency=1 --confirm-external-bind --rpc-bind-ip 0.0.0.0
root     24686  0.0  0.0  12736  2248 pts/18   S+   20:29   0:00 grep monero
```
```
root@scw-f25b17:~# ps aux | grep monero
root     24494  0.0  0.0   4340  1588 pts/17   S+   20:21   0:00 /bin/sh /usr/local/bin/heaptrack ./monerod --max-concurrency=1 --confirm-external-bind --rpc-bind-ip 0.0.0.0
root     24507 30.7  7.9 37057064 1306520 pts/17 Sl+ 20:21   6:59 ./monerod --max-concurrency=1 --confirm-external-bind --rpc-bind-ip 0.0.0.0
root     24883  0.0  0.0  12736  2244 pts/18   S+   20:43   0:00 grep monero
```
```
root@scw-f25b17:~# ps aux | grep monero
root     24494  0.0  0.0   4340  1588 pts/17   S+   20:21   0:00 /bin/sh /usr/local/bin/heaptrack ./monerod --max-concurrency=1 --confirm-external-bind --rpc-bind-ip 0.0.0.0
root     24507 30.2 11.2 37057064 1846372 pts/17 Sl+ 20:21  13:08 ./monerod --max-concurrency=1 --confirm-external-bind --rpc-bind-ip 0.0.0.0
root     25150  0.0  0.0  12736  2112 pts/18   R+   21:04   0:00 grep monero
```
```
root@scw-f25b17:~# ps aux | grep monero
root     24494  0.0  0.0   4340  1588 pts/17   S+   20:21   0:00 /bin/sh /usr/local/bin/heaptrack ./monerod --max-concurrency=1 --confirm-external-bind --rpc-bind-ip 0.0.0.0
root     24507 30.7 16.2 37057064 2659836 pts/17 Sl+ 20:21  20:47 ./monerod --max-concurrency=1 --confirm-external-bind --rpc-bind-ip 0.0.0.0
root     25500  0.0  0.0  12740  2248 pts/18   S+   21:28   0:00 grep monero
```


Finally I manually killed the process to get `heaptrack` output:
```
heaptrack stats:
        allocations:            26181829
        leaked allocations:     1143
        temporary allocations:  20599012
```

`heaptrack_print` output is attached.

Thanks.

[heaptrack.monerod.24494.txt.gz](https://github.com/monero-project/monero/files/1209652/heaptrack.monerod.24494.txt.gz)

## itdaniher | 2017-08-08T21:49:51+00:00
@renecannao Hey, I know that hosting provider! Love them! But what architecture are you running? I think they offer both ARM and x86 in up to 16GB. I've used the same release on x86 with 8GB without issues.

## renecannao | 2017-08-08T21:53:07+00:00
Good provider indeed! :)
I am using x86:
```
root@scw-f25b17:~# lsb_release -a
No LSB modules are available.
Distributor ID:	Debian
Description:	Debian GNU/Linux 8.9 (jessie)
Release:	8.9
Codename:	jessie
root@scw-f25b17:~# lscpu 
Architecture:          x86_64
CPU op-mode(s):        32-bit, 64-bit
Byte Order:            Little Endian
CPU(s):                8
On-line CPU(s) list:   0-7
Thread(s) per core:    1
Core(s) per socket:    8
Socket(s):             1
Vendor ID:             GenuineIntel
CPU family:            6
Model:                 77
Model name:            Intel(R) Atom(TM) CPU  C2750  @ 2.40GHz
Stepping:              8
CPU MHz:               2393.905
BogoMIPS:              4788.69
Virtualization:        VT-x
root@scw-f25b17:~# free -m
             total       used       free     shared    buffers     cached
Mem:         15989      15252        737        173         62      14630
-/+ buffers/cache:        559      15430
Swap:            0          0          0
```

## itdaniher | 2017-08-08T22:00:03+00:00
I'm running x86_64 - Debian 8.7. I somehow doubt the small lib bumps from 8.7 to 8.9 matter. I checked and we have roughly the same set of CPU extensions.

Something low-fi might be to `mv ~/.bitmonero ~/.bitmonero.bk` and resync.

## renecannao | 2017-08-08T22:07:58+00:00
Thank you for the advise, but somehow I would like to exclude it is related to syncing, as the node is already in sync.
Someone knowing the code can find the `heaptrack` profiling very useful to figure our where memory is being used/wasted/leaked.

## hyc | 2017-08-08T22:31:28+00:00
You're still running vanilla v0.10.3.1? Memory use in current git master is vastly different already, so there's very little to be gained by looking at 0.10.31. now. I looked through your heaptrack output but it seems to me that it didn't identify any actual leaks, only overall allocations.

If you can build your own binaries, try compiling current git master. And if you're still seeing OOM issues, also attach the relevant dmesg output - the kernel will log when OOM killer selects a process for termination.

On my VPS with 4GB RAM, monerod only uses 2.6GB RES, of which 1.77GB is shared memory (and  therefore unimportant for RAM usage calculations.) 

My mleak tracer is faster and smaller footprint than heaptrack. https://github.com/hyc/mleak


## renecannao | 2017-08-09T09:27:37+00:00
Yes, I was sill running vanilla  v0.10.3.1 .
I compiled from master branch, and things looks absolutely better.
After 9+ hours of uptime, RSS is around 1.4GB:
```
root@scw-f25b17:~/monero# ps aux | grep monero
root      1263  0.0  0.0  12736  2120 pts/18   S+   09:19   0:00 grep monero
root     25919 16.3  8.8 40269808 1442688 pts/17 Sl+ 00:05  90:43 ./bin/monerod --max-concurrency=1 --confirm-external-bind --rpc-bind-ip 0.0.0.0
```
I also investigated a bit the big virtual memory, and it seems related to an `mmap()` call:
```
open("/root/.bitmonero/lmdb/data.mdb", O_RDWR|O_CREAT, 0644) = 17
fstatfs(17, {f_type="EXT2_SUPER_MAGIC", f_bsize=4096, f_blocks=11982489, f_bfree=1599062, f_bavail=984615, f_files=3055616, f_ffree=2684364, f_fsid={-498122322, -280718307}, f_namelen=255, f_frsize=4096}) = 0
uname({sys="Linux", node="scw-f25b17", ...}) = 0
pread(17, "\0\0\0\0\0\0\0\0\0\0\10\0\0\0\0\0\336\300\357\276\1\0\0\0\0\0\0\0\0\0\0\0"..., 152, 0) = 152
pread(17, "\1\0\0\0\0\0\0\0\0\0\10\0\0\0\0\0\336\300\357\276\1\0\0\0\0\0\0\0\0\0\0\0"..., 152, 4096) = 152
mmap(NULL, 40062132224, PROT_READ, MAP_SHARED, 17, 0) = 0x7f21581c6000
madvise(0x7f21581c6000, 40062132224, MADV_RANDOM) = 0
```
I wonder why it calls `mmap()` for 37.3GB if the file is just 22GB .
I am not familiar with lmdb and I am not sure if it can be tuned.

Conclusion:
Issue can be considered solved.

Thanks

## hyc | 2017-08-09T10:38:14+00:00
The mmap call is normal for LMDB. The size of the mapped region is somewhat irrelevant; on a 64bit OS you currently have a 256TB address space so this is trivial.

## renecannao | 2017-08-09T12:42:18+00:00
@hyc : thank you for the reply.
Is there a way to limit the amount of RSS memory used by LMDB ?

Some more context about this question.
I intentionally executed `rescan_bc` on `monero-wallet-cli` connected from a different host to trigger a full re-scan.
Before running `rescan_bc`:
```
root@scw-f25b17:~# ps aux | grep monero
root      2207  0.0  0.0  12736  2136 pts/18   S+   10:48   0:00 grep monero
root     25919 15.8  9.0 40269808 1485816 pts/17 Sl+ 00:05 101:41 ./bin/monerod --max-concurrency=1 --confirm-external-bind --rpc-bind-ip 0.0.0.0
```
While `scan_bc` is running:
```
root@scw-f25b17:~# date ; ps aux | grep monerod ; grep -A 10 data.mdb /proc/`pidof monerod`/smaps ; free -m
Wed Aug  9 12:24:54 UTC 2017
root      3648  0.0  0.0  12736  2224 pts/18   S+   12:24   0:00 grep monerod
root     25919 17.1 95.0 40282092 15565520 pts/17 Sl+ 00:05 126:54 ./bin/monerod --max-concurrency=1 --confirm-external-bind --rpc-bind-ip 0.0.0.0
7feef41c6000-7ff848000000 r-xs 00000000 2b:00 1197120                    /root/.bitmonero/lmdb/data.mdb
Size:           39123176 kB
Rss:            15390432 kB
Pss:            15390432 kB
Shared_Clean:          0 kB
Shared_Dirty:          0 kB
Private_Clean:  15390124 kB
Private_Dirty:       308 kB
Referenced:     15380872 kB
Anonymous:             0 kB
AnonHugePages:         0 kB
             total       used       free     shared    buffers     cached
Mem:         15989      15797        191        173          1      15271
-/+ buffers/cache:        524      15464
Swap:            0          0          0
```
Basically, `monerod` is using all available memory.

LMDB [doc](https://lmdb.readthedocs.io/en/release/#memory-usage) is very clear in saying that this is not an issue.
Nonetheless, would be great if LMDB could free some memory.
So, back to my initial question: is there a way to limit the amount of RSS memory used by LMDB ?
Perhaps calling `madvise()` with `MADV_DONTNEED` ?

To be clear, I consider this not a bug, but a feature request.
My point is that just checking RSS won't give a clear answer to possible questions like "why monerod is using all my memory?" and differentiate cases of real memory leak vs LMDB using as much memory as possible.

## hyc | 2017-08-09T16:12:15+00:00
No. The amount of RAM used by LMDB is irrelevant - it all resides in the OS page cache and the OS will reclaim it for other purposes whenever any other process asks for memory.

As for your latter concern - the memory used by LMDB is shared memory. Private memory is something else entirely, and any leaks you're looking for would be reflected there. If the memory profile you included here is to be believed, with a process using 0kb of shared memory, it would imply that all of LMDB's data has already been paged out, and all of monerod's memory use is due to regular allocations. I'm not sure I believe that, but it's always possible. Try getting the same output shortly after startup.

edit: I see, these are the stats specifically for the data.mdb file. Still it's odd that it's reported as Private instead of Shared.

## garmoshka-mo | 2017-09-01T15:11:01+00:00
just in case, if wasn't mentioned here - swap is 0 - so all applications which widely expand in ram - will be killed once they reach (total - ~100 mb) RAM edge
typical issue for Digital Ocean, where swap is disabled because of SSDs

## Engelberg | 2017-09-07T21:51:12+00:00
I've been having a similar problem on webfaction.  Webfaction is a shared host, that provides each user with 1GB RAM (and, supposedly, monerod can run in under 1GB of RAM).

When I run monerod, it gradually eats up RAM until it exceeds 1GB, at which point, webfaction kills off the process.

I don't know to communicate to monerod (or the underlying lmdb) that it must stay within 1GB.  I've tried ulimit, but that didn't accomplish anything.  (ulimit -v makes it so monerod won't even run, and ulimit -m has no effect).

I gave up, waiting for the new release, because everyone here said the new release would be much more memory efficient.  0.11.0 was just released today, and I immediately tried it out --- same problem.

How do I get monerod to run on a VPS with 1GB of RAM?

## Engelberg | 2017-09-07T23:12:35+00:00
Even once monerod itself is fully up-to-date with the p2p network, monerod uses gobs of memory very quickly whenever a wallet connects to it that is behind a large number of blocks and the wallet needs to synchronize all those blocks with the server.

## garmoshka-mo | 2017-09-08T08:20:05+00:00
@Engelberg for now you can use flag `--block-sync-size 10` - this will significantly decrease pressure to RAM

What happens is - default amount of blocks to download and keep in memory is 200 - which is very fine for early blocks (before 1 200 000 block) - it allows to quickly download a lot of small blocks and efficiently process them. But when blocks become huge (because of growing popularity at 1,2M blocks point) - 200 blocks require a lot of RAM as well as time to be downloaded.

## Engelberg | 2017-09-08T09:17:18+00:00
@garmoshka-mo It appears like the new default for block-sync-size is 20 in the latest version, but yes, I found that adding `--block-sync-size 10` did indeed help it complete the synchronization within a reasonable amount of memory.

But now, I'm finding that when a wallet connects to the fully synchronized node, and the wallet is behind and needs to download thousands of blocks from the node, the node's RAM usage again goes through the roof.

So, now I need to find a way to limit the node's RAM usage *after* the node is synchronized, when wallets are interacting with it.

## bitkevin | 2017-11-02T03:23:26+00:00
It took so much memory, see:

```
  PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND
   31 root      20   0 58.076g 6.013g 5.303g S   3.7  4.8   1580:45 monerod
```

Run it in a docker, the OS version is:

```
$ lsb_release -a
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 16.04 LTS
Release:	16.04
Codename:	xenial

$ uname -a
Linux 27801231e750 4.4.0-85-generic #108~14.04.1-Ubuntu SMP Tue Jul 4 12:02:58 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux
```
`monerod` version:

```
$ monerod --help
Monero 'Helium Hydra' (v0.11.0.0-release)
```

I have restart the node after synced all blocks. Is it usual?

## bitsanity | 2020-12-28T12:10:30+00:00
This is still a problem with latest monerod release 0.17.1.7



## anviar | 2020-12-29T07:00:45+00:00
@bitsanity this time it is an attack on the network 

## bitsanity | 2020-12-29T13:53:16+00:00
@anviar yes, I found a discussion about it on [reddit](https://www.reddit.com/r/monerosupport/comments/kjstfc/monerod_new_attack_suddenly_out_of_memory/)

## sijanec | 2021-03-24T17:01:35+00:00
Any updates on this network attack?

## selsta | 2021-03-24T17:02:48+00:00
@sijanec the attack vector has been fixed in v0.17.1.9

## sijanec | 2021-03-24T17:14:54+00:00
Well my issue is probably unrelated, but I am running a freshly compiled `Monero 'Oxygen Orion' (v0.17.1.9-9ec4ce36c)` on `Linux of 4.4.167-1213-rockchip-ayufan-g34ae07687fce #1 SMP Tue Jun 18 20:44:49 UTC 2019 aarch64 GNU/Linux` on Rock64 4 GB and `monerod` caused a kernel panic when synchronising. Note that it was ran as a non-root user without root priviledges with rpc-payment enabled and on a rotating drive.

Thanks for the response, @selsta 

P. S.: Apart from that the blockchain was corrputed and further starts of `monerod` before deleting data-dir were exited this way:

```
2021-03-24 16:59:37.882 I Monero 'Oxygen Orion' (v0.17.1.9-9ec4ce36c)
2021-03-24 16:59:37.883 I Initializing cryptonote protocol...
2021-03-24 16:59:37.883 I Cryptonote protocol initialized OK
2021-03-24 16:59:37.885 I Initializing core...
2021-03-24 16:59:37.885 I Loading blockchain from folder /mnt/disk/shramba/a/monero/db/lmdb ...
2021-03-24 16:59:37.886 W The blockchain is on a rotating drive: this will be very slow, use an SSD if possible
2021-03-24 16:59:37.889 F Existing lmdb database is incompatible with this version.
2021-03-24 16:59:37.889 F Please delete the existing database and resync.
2021-03-24 16:59:37.897 I Stopping cryptonote protocol...
2021-03-24 16:59:37.897 I Cryptonote protocol stopped successfully
2021-03-24 16:59:37.898 E Exception in main! Failed to initialize core
```

P. S.: The node that crashed the computer was ran without any command line options for optimized work on a low-end setup, I am trying this now and it is still in the process of syncing.

## sijanec | 2021-03-24T19:12:51+00:00
Okay, it crashed again, it's not usable for me on a rock64. Anyone else?

```
2021-03-24 19:07:37.434        I Synced 318190/2324175 (13%, 2005985 left)
2021-03-24 19:07:37.520        I Synced 318200/2324175 (13%, 2005975 left)
2021-03-24 19:07:37.594        I Synced 318210/2324175 (13%, 2005965 left)
2021-03-24 19:07:37.670        I Synced 318220/2324175 (13%, 2005955 left)
2021-03-24 19:07:37.746        I Synced 318230/2324175 (13%, 2005945 left)
2021-03-24 19:07:37.823        I Synced 318240/2324175 (13%, 2005935 left)
2021-03-24 19:07:37.962        I Synced 318250/2324175 (13%, 2005925 left)

Message from syslogd@rock64 at Mar 24 19:11:26 ...
 kernel:[ 9240.838055] Kernel panic - not syncing: hung_task: blocked tasks

Message from syslogd@rock64 at Mar 24 19:11:26 ...
 kernel:[ 9241.554516] Kernel Offset: disabled

Message from syslogd@rock64 at Mar 24 19:11:26 ...
 kernel:[ 9241.558059] Memory Limit: none

```

## selsta | 2021-03-24T19:22:06+00:00
@sijanec another person reported similar issues with a rock64. Can you join #monero on IRC then someone might be able to help with debugging this issue.

# Action History
- Created by: itdaniher | 2017-07-01T17:02:14+00:00
- Closed at: 2017-07-06T22:40:54+00:00
