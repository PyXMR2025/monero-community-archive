---
title: monerod hogging CPU on OpenBSD after synchronisation
source_url: https://github.com/monero-project/monero/issues/7027
author: tdog8622
assignees: []
labels: []
created_at: '2020-11-18T16:20:12+00:00'
updated_at: '2025-11-01T05:39:37+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I compiled v0.17.1.3 on OpenBSD 6.8 (current).

After starting monerod by invoking

monerod --hide-my-port --in-peers 0 --limit-rate 500 --max-concurrency 1 --max-concurrency 1 --block-sync-size 1

the monerod daemon syncs up with reasonable CPU usage but after the message that it is synchronised to the network it starts hogging my CPU and my machine freezes until I manage to kill the proccess.



# Discussion History
## moneromooo-monero | 2020-12-05T19:13:13+00:00
If you have the perf tool (not sure it's linux only): sudo perf top -a
You might have something similar.

## moneromooo-monero | 2020-12-05T19:13:55+00:00
Failing that, getting a dozen stack traces should probabilistically show one or two in the hot code.

## tdog8622 | 2020-12-20T04:58:50+00:00
perf is Linux only; Here are the traces I did with ktrace:

( https://man.openbsd.org/ktrace.1 )
( https://man.openbsd.org/kdump )

[kdump001.txt](https://github.com/monero-project/monero/files/5720508/kdump001.txt)
[kdump002.txt](https://github.com/monero-project/monero/files/5720509/kdump002.txt)
[kdump003.txt](https://github.com/monero-project/monero/files/5720510/kdump003.txt)
[kdump004.txt](https://github.com/monero-project/monero/files/5720511/kdump004.txt)
[kdump005.txt](https://github.com/monero-project/monero/files/5720512/kdump005.txt)
[kdump006.txt](https://github.com/monero-project/monero/files/5720513/kdump006.txt)
[kdump007.txt](https://github.com/monero-project/monero/files/5720514/kdump007.txt)
[kdump008.txt](https://github.com/monero-project/monero/files/5720515/kdump008.txt)
[kdump009.txt](https://github.com/monero-project/monero/files/5720516/kdump009.txt)
[kdump010.txt](https://github.com/monero-project/monero/files/5720518/kdump010.txt)
[kdump011.txt](https://github.com/monero-project/monero/files/5720519/kdump011.txt)
[kdump012.txt](https://github.com/monero-project/monero/files/5720520/kdump012.txt)

ktrace.out files (which I renamed from .out to .gz in order to be able to upload them):

[ktrace001.gz](https://github.com/monero-project/monero/files/5720535/ktrace001.gz)
[ktrace002.gz](https://github.com/monero-project/monero/files/5720536/ktrace002.gz)
[ktrace003.gz](https://github.com/monero-project/monero/files/5720537/ktrace003.gz)
[ktrace004.gz](https://github.com/monero-project/monero/files/5720538/ktrace004.gz)
[ktrace005.gz](https://github.com/monero-project/monero/files/5720539/ktrace005.gz)
[ktrace006.gz](https://github.com/monero-project/monero/files/5720540/ktrace006.gz)
[ktrace007.gz](https://github.com/monero-project/monero/files/5720541/ktrace007.gz)
[ktrace008.gz](https://github.com/monero-project/monero/files/5720542/ktrace008.gz)
[ktrace009.gz](https://github.com/monero-project/monero/files/5720543/ktrace009.gz)
[ktrace010.gz](https://github.com/monero-project/monero/files/5720545/ktrace010.gz)
[ktrace011.gz](https://github.com/monero-project/monero/files/5720554/ktrace011.gz)
[ktrace012.gz](https://github.com/monero-project/monero/files/5720555/ktrace012.gz)

(The freezing behaviour happens every time that I run moneord and should be present in every of the above traces)


I further observed that monerod seems to cause my WiFi connection to drop after my system freezes. While the PC is not connected to the network the systems become responsive again, only to freeze again shortly after a network connection is reestablished.



## moneromooo-monero | 2020-12-20T16:44:49+00:00
That looks like an strace equivalent, not quite what I was after. Your observation is interesting. Does it still happen if you set --limit and/or --out-peers/--in-peers to small values ? Also "--disable-dns-checkpoints --check-updates disabled" will test whether the problem is due to DNS queries (though it'll still check the seed domains, I don't think there's an off switch for that).

## tdog8622 | 2020-12-20T19:07:45+00:00
It stills happens if I invoke:

monerod --out-peers 5 --in-peers 5 --disable-dns-checkpoints --check-updates disabled --limit-rate 100

If I run monerod --offline my system does not freeze.

I have to admit that I do not know which tool to use to get the stack trace that you wanted.

## moneromooo-monero | 2020-12-21T12:48:29+00:00
It's not a stack trace, but a profile. To see where the CPU is going.
In any case, I have another quick and dirty patch elsewhere that's meant to address some CPU issues to do with the net layer, so maybe it will happen to help: 

https://paste.debian.net/hidden/da8b1aa6/

xxd -r < FILENAME > net-patch.gz
gzip -d net-patch.gz
patch -p1 < net-patch



## selsta | 2022-04-25T17:47:36+00:00
@BebeSparkelSparkel can you help with producing the profile moneromooo is asking for? that would help us find the issue

## BebeSparkelSparkel | 2022-04-26T12:01:58+00:00
There was a [suggestion on reddit](https://www.reddit.com/r/openbsd/comments/txdt4o/comment/i3srq9g/?utm_source=share&utm_medium=web2x&context=3)

*Welcome to OpenBSD. SMP is much better than it used to be, but development is not as advanced as some other OS. You may be able to help figure out what's going on with some information from btrace (https://marc.info/?l=openbsd-misc&m=164181728803834 has some tips about running it). Or you might find this workload works better running a GENERIC kernel rather than GENERIC.MP.*

I have tried without multiprocessing but with the same result.

`btrace` may produce the profile that you are looking for. I will try to get that profile soon.

## BebeSparkelSparkel | 2022-04-26T12:06:58+00:00
An OpenBSD developer gave this insight to me reporting that the system was in a state of 100% Sys and 100% Spin

*the daemon is doing something that is tying up system resources. Spinning is when something is trying to grab a kernel lock but is unable to.*

https://www.reddit.com/r/openbsd/comments/txdt4o/comment/i3orkh0/?utm_source=share&utm_medium=web2x&context=3



## offshoremonero | 2022-11-30T07:19:36+00:00
I think it has something to do with lmdb and WRITEMAP.

If you comment out the MDB_WRITEMAP lines in src/blockchain_db/lmdb/db_lmdb.cpp the issue goes away, but you end up with a broken lmdb. :(

## hhartzer | 2025-09-30T19:05:36+00:00
Only remedy I have found is something along the lines of: `--db-sync-mode=fast:async:10000`

If you want to make your system completely unresponsive, try replacing `fast` with `safe`.

## nahuhh | 2025-09-30T19:18:29+00:00
> Only remedy I have found is something along the lines of: `--db-sync-mode=fast:async:10000`
> 
> If you want to make your system completely unresponsive, try replacing `fast` with `safe`.

it switches to `safe` after synced, unless overridden with the aforementioned flag



## amrfti | 2025-10-31T22:22:09+00:00
This is still a problem as of monerod `v0.18.4.3` and OpenBSD `7.8`
Huge CPU usage completely bogging down system unless something like `--db-sync-mode=fast:async:10000` is set

## hhartzer | 2025-11-01T05:39:37+00:00
Interestingly, on a synced blockchain I've found that stopping monerod (not starting or running) will cause OpenBSD to be completely unresponsive to network traffic or other activity. This can take 30-60 seconds, in my experience.

Probably not a Monero bug, but interesting nonetheless.

# Action History
- Created by: tdog8622 | 2020-11-18T16:20:12+00:00
