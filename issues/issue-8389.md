---
title: Memory leak in monerod v0.17.3.2-release
source_url: https://github.com/monero-project/monero/issues/8389
author: daemonserj
assignees: []
labels: []
created_at: '2022-06-17T12:32:01+00:00'
updated_at: '2022-06-18T03:05:24+00:00'
type: issue
status: closed
closed_at: '2022-06-18T03:05:05+00:00'
---

# Original Description
Hi.
I ran node a couple of days and monerod allocated all awailable RAM on server and swap kept growing.
On the first day it increased from zero to 512M, on the second day to 812M.

Top output:
```
PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
14100 monero    20   0  149.3g   9.6g   8.9g S  15.6  82.3 374:36.40 monerod
```

free -m output:
```
              всего        занято        свободно      общая  буф./врем.   доступно
Память:       11893        1713         136          40       10043        9816
Подкачка:        3856         812        3044

```

monerod status

```
2022-06-17 12:12:15.633 I Monero 'Oxygen Orion' (v0.17.3.2-release)
Height: 2647697/2647697 (100.0%) on mainnet, not mining, net hash 2.56 GH/s, v14, 16(out)+90(in) connections, uptime 2d 1h 31m 30s

```

[monerod.conf.zip](https://github.com/monero-project/monero/files/8927451/monerod.conf.zip)

# Discussion History
## selsta | 2022-06-17T12:33:51+00:00
How much RAM does your server have overall?

## daemonserj | 2022-06-17T12:34:53+00:00
12gb with zswap enabled

## selsta | 2022-06-17T12:36:21+00:00
And how much free RAM do you have available without monerod running?

## daemonserj | 2022-06-17T12:37:31+00:00
Almost all of RAM is free because there is no other worlkloads on server.

## selsta | 2022-06-17T12:40:26+00:00
Did you try mining?

## daemonserj | 2022-06-17T12:43:07+00:00
No. Actually it's small nettop with low perf CPU, so mining is not suitable for me.

## hyc | 2022-06-17T14:00:28+00:00
Doesn't look like any leak to me. 9.6G resident, 8.9G shared. Majority of usage is shared memory, not a leak.

## daemonserj | 2022-06-17T14:05:09+00:00
What is your uptime and swap usage ?
I don't worry about RAM usage at all, but swap growing is a bad symptom

## hyc | 2022-06-17T14:12:42+00:00
If there's no other busy processes on the machine, it doesn't mean much. You can set /proc/sys/vm/swappiness = 0 if it bothers you but it won't have any impact.

## daemonserj | 2022-06-17T15:33:12+00:00
I've disabled swap by `swapoff -a `and saw that ~500M loaded back into RAM which decrease cache amount:

RAM:  1713 -> 2201
cache: 10043 ->  9522

prev free -m
```
              всего        занято        свободно      общая  буф./врем.   доступно
Память:       11893        **1713**         136          40       **10043**        9816
Подкачка:        3856         812        3044
```

last free -m:
```
              всего        занято        свободно      общая  буф./врем.   доступно
Память:       11893        **2201**         168         139        **9522**        9229
Подкачка:        3856           0        3856

```
I'll keep an eye on it but if trend continues it will cause the system to run out of memory.


## selsta | 2022-06-17T16:01:09+00:00
Try to limit your incoming connections. In general, more connections means higher RAM usage. And the longer your node is up the more incoming connections you will have.

Also try `--enable-dns-blocklist`.

## daemonserj | 2022-06-17T16:17:11+00:00
These options are already configured to:

enable-dns-blocklist=1
out-peers=16
in-peers=128




## selsta | 2022-06-17T16:18:34+00:00
Your config was in a zip so I didn't want to download it. 128 in peers is a lot, my nodes don't even reach 128 in peers with months of uptime. Try a smaller limit and see if it makes a difference.

## daemonserj | 2022-06-17T16:27:14+00:00
I see incoming peers count floating around ~90 right now.
I don't want to restart service, I'll watch for overall RAM usage.
If it continues growing then I'll limit in-peers to 32 and try to find some leaks with memleax.

## hyc | 2022-06-17T17:07:54+00:00
> I'll keep an eye on it but if trend continues it will cause the system to run out of memory.

No, it won't. The OS will reclaim cache memory as needed. There is no leak here, there is no problem here.

## daemonserj | 2022-06-18T03:05:05+00:00
I've checked monerod by memleax with 1 minute memblock expiration.
There is no leaks right now, so you guys was right.
I'll return to it after some weeks, if some wrong happens I'll reopen this issue.

# Action History
- Created by: daemonserj | 2022-06-17T12:32:01+00:00
- Closed at: 2022-06-18T03:05:05+00:00
