---
title: monerod is auto killed
source_url: https://github.com/monero-project/monero/issues/7224
author: dungdang95
assignees: []
labels: []
created_at: '2020-12-29T07:55:02+00:00'
updated_at: '2022-06-26T17:19:24+00:00'
type: issue
status: closed
closed_at: '2021-01-16T18:03:33+00:00'
---

# Original Description
My ./monerod was killed. I start again and it exits again. Here my log:

![image](https://user-images.githubusercontent.com/60590661/103268293-cf593300-49e5-11eb-9a88-15017b00609d.png)


# Discussion History
## rblaine95 | 2020-12-29T11:13:04+00:00
There is an ongoing attack on the Monero Network where malicious nodes are creating memory bombs (very large packets that cause high memory usage) which causes the `monerod` process to get `OOMKilled`

Current mitigation is to update to the latest stable release of Monero ([`v0.17.1.7`](https://github.com/monero-project/monero/releases/tag/v0.17.1.7)) and to apply the Tor Blocklist
```
wget https://gui.xmr.pm/files/block_tor.txt -O ~/.bitmonero/block_tor.txt
monerod --ban-list ~/.bitmonero/block_tor.txt
```
Or, add the following line to your `bitmonero.conf`
```
ban-list=/path/to/block_tor.txt
```

## janfiedler | 2020-12-30T10:17:05+00:00
@rblaine95 Thanks, this must be massive attack, even with your solution it give me only few minutes more. Then my node is memory bombed and killed.

## ghost | 2020-12-30T18:28:09+00:00
Are there any fixes in the works for this? I'm definitely running into this as well.

## selsta | 2020-12-30T18:29:09+00:00
Yes, we tagged v0.17.1.8 and it should be released in the next hours.

## ghost | 2020-12-30T18:30:52+00:00
Awesome, thank you!!

## selsta | 2020-12-30T22:58:44+00:00
v0.17.1.8 is out: https://www.getmonero.org/downloads/

## ghost | 2020-12-30T23:39:49+00:00
I just upgraded. I'll write back with my findings. It was being OOM killed every hour or two before, seemingly.

## selsta | 2020-12-31T13:47:50+00:00
New attack, seems like the tor block list is required again: https://gui.xmr.pm/files/block_tor.txt

This does not seem related to the attack fixed in v0.17.1.8

## ghost | 2020-12-31T18:11:00+00:00
My node has been up since I restarted it. No issues yet.

Edit: Also, I've never used the Tor blocklist.

## tempname1024 | 2021-01-02T00:33:51+00:00
> New attack, seems like the tor block list is required again: https://gui.xmr.pm/files/block_tor.txt
> 
> This does not seem related to the attack fixed in v0.17.1.8

Indeed, had a crash today after ~36 hours of uptime running v0.17.1.8 without the block list.

> 2021-01-01 16:57:45.638 W There were 0 blocks in the last 20 minutes, there might be large hash rate changes, or we might be partitioned, cut off from the Monero network or under attack, or your computer's time is off. Or it could be just sheer bad luck.

## selsta | 2021-01-02T00:45:49+00:00
> There were 0 blocks in the last 20 minutes, there might be large hash rate changes, or we might be partitioned, cut off from the Monero network or under attack, or your computer's time is off. Or it could be just sheer bad luck.

This is unrelated and happens sometimes.

## ghost | 2021-01-02T14:51:49+00:00
No crashes but my block height got near 2265577 and the daemon is unresponsive, even to a block height command.

I just restarted it. Will see what it does.

## selsta | 2021-01-02T15:00:58+00:00
@teran-mckinney 

Next time this happens please don’t restart and use gdb:

```
gdb /path/to/monerod `pidof monerod`

thread apply all bt
```

so that we can see where it freezes.

## ghost | 2021-01-02T15:10:20+00:00
Ok, will do! It's moving forward now at least. I wonder if anyone else will get this and they can try it. Or maybe I'll get it again.

## selsta | 2021-01-02T15:11:00+00:00
I have only read of one other person having this freeze issue.

## Masterbob79 | 2021-01-02T16:11:14+00:00
I have noticed monerod got killed the other day, but I haven't checked the logs yet

## voidzero | 2021-01-03T13:48:28+00:00
Unfortunately I'm still getting repeated OOM kills. 

Monero 'Oxygen Orion' (v0.17.1.8-ef1ba5142)

Memory cgroup out of memory: Killed process 17408 (monerod) total-vm:127917672kB, anon-rss:7748416kB, file-rss:7668kB, shmem-rss:0kB, UID:xxxx pgtables:107460kB oom_score_adj:0

Monero is running in a cgroup with a 6GB memory soft limit and a 8GB hard limit.

## komatom | 2021-01-04T11:32:51+00:00
Still kills itself, added tor block list to try with it

Monero 'Oxygen Orion' (v0.17.1.8-release)


## dEBRUYNE-1 | 2021-01-04T14:19:20+00:00
@komatom @voidzero - Can you try compiling the release branch?

https://github.com/monero-project/monero#compiling-monero-from-source

## voidzero | 2021-01-04T14:36:11+00:00
@dEBRUYNE-1 you betcha. I'll check back in a few minutes.

## voidzero | 2021-01-04T14:59:37+00:00
Built correctly; version v0.17.1.9 confirmed to be running and I've disabled using the tor blocklist. "Now we wait." If it crashes I will let you know and if not, well, I'll let you know too. It usually crashed after no more than an hour. If you can add a debug message "caught exploit such and so" then I can let you know more quickly.

## voidzero | 2021-01-04T17:22:00+00:00
2 hosts were blocked so far, and I got a bunch of warnings saying 
> _there were (0|1|2) blocks in the last 30 minutes, there might be large hash rate changes (...)_

I guess that might actually indicate that stuff is working properly - no more DoS now. Just curious, Is the network under such a heavy attack or is something else going on? Anyway. Seems to be working now, if it does bug out, I'll let you know but it doesn't look like it will.

## selsta | 2021-01-04T17:29:21+00:00
It just happens sometimes that blocks come in slower rates. Can have various reasons, does not seem attack related.

## komatom | 2021-01-04T20:11:27+00:00
@dEBRUYNE-1 I have also compiled .9 version and had it run without the ban list, we will see if it will be ok for a day..

## voidzero | 2021-01-05T06:51:48+00:00
Alright, hosts being blocked properly, no crashes, if it were up to me I'd say "push it!"

## komatom | 2021-01-05T08:00:59+00:00
same here no crashes and hosts are blocked:

`
2021-01-04 22:43:19.061        I Host 142.44.144.199 blocked.
2021-01-05 01:08:28.374        I Host 51.91.33.151 blocked.
2021-01-05 01:11:12.678        I Host 51.77.192.92 blocked.
2021-01-05 02:10:51.069        I Host 54.36.150.238 blocked.
2021-01-05 02:47:45.731        I Host 54.38.217.119 blocked.
2021-01-05 02:58:04.829        I Host 51.178.251.7 blocked.
2021-01-05 03:03:38.514        I ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 2267555
2021-01-05 03:03:38.514        I id:     <050d9bc8248ac34e18445846899634d6f8380debf8cad59d4e63b731477214a1>
2021-01-05 03:03:38.514        I PoW:    <3899e894f1f71a365d1995123857c5c6d560d71cc08f08c275c8600300000000>
2021-01-05 03:03:38.514        I difficulty:     206074715525
2021-01-05 03:46:57.432        I Host 51.77.227.128 blocked.
2021-01-05 04:00:24.403        I Host 188.165.17.204 blocked.
2021-01-05 05:12:59.958        I Host 145.239.118.5 blocked.
2021-01-05 05:23:37.785        I Host 146.59.211.239 blocked.
2021-01-05 05:50:06.436        I Host 87.98.224.123 blocked.
2021-01-05 06:10:33.432        I Host 178.32.215.155 blocked.
2021-01-05 06:35:47.146        I Host 217.182.9.71 blocked.
2021-01-05 06:44:09.102        I Host 51.255.233.156 blocked.
2021-01-05 06:47:38.347        I Host 51.255.126.219 blocked.
2021-01-05 07:21:16.827        I Host 79.137.53.34 blocked.
2021-01-05 07:54:55.539        I Host 5.196.124.241 blocked.
2021-01-05 07:56:42.273        I Host 51.91.8.178 blocked.
`

## selsta | 2021-01-05T19:50:55+00:00
We are working on fixing more attack vectors before putting the release out.

## voidzero | 2021-01-05T22:41:06+00:00
Okay, whatever you decide is best. I just want to make this one point - so far 76 hosts have been banned on my host (my in_peers and out_peers are both 32), and I don't know how many hosts on the network are crashing as a result but these crashes could have a significant impact. So if this critical one is fixed and legitimate nodes won't crash anymore, then perhaps push this one out, then fix the less critical attack vectors. Of course I have no idea which other vectors for attack there are so I hope I don't sound rude or imposing. Leaving this to your judgement.

## voidzero | 2021-01-16T16:52:04+00:00
I'd say this is fixed!

## moneromooo-monero | 2021-01-16T18:03:33+00:00
Thanks for testing, closing.

## holdengreen | 2022-06-24T16:56:01+00:00
I think I'm having the same issue from debian 11 stable.

## selsta | 2022-06-24T16:59:43+00:00
@holdengreen You will have to post more information. What hardware are you using? How often does this issue show up?

## holdengreen | 2022-06-25T00:34:04+00:00
@selsta

It's the cheapest Linux VPS from Hostens.

```
cpu family      : 6
model           : 85
model name      : Intel Xeon Processor (Skylake, IBRS)
stepping        : 4
```

https://www.hostens.com/knowledgebase/what-hardware-are-you-using/

sorry submitted before finishing.

It happens whenever I try to run it for any significant amount of time.
I'm not able to discern out anything of much interest from the log.

## holdengreen | 2022-06-25T00:38:46+00:00
configuration:

```
# /etc/monerod.conf

# Data directory (blockchain db and indices)
data-dir=/data/1/monero/data  # Remember to create the monero user first

#
prune-blockchain=1
public-node=1

# performance
sync-pruned-blocks=0
max-concurrency=1
prep-blocks-threads=1
fast-block-sync=1


# Log file
log-file=/var/log/monero/monerod.log
log-level=4
max-log-file-size=2147483648            # Prevent monerod from managing the log files; we want logrotate to take care of that

# P2P full node
p2p-bind-ip=0.0.0.0            # Bind to all interfaces (the default)
p2p-bind-port=18080            # Bind to default port

# RPC open node
rpc-bind-ip=0.0.0.0            # Bind to all interfaces
rpc-bind-port=18081            # Bind on default port
confirm-external-bind=1        # Open node (confirm)
restricted-rpc=1               # Prevent unsafe RPC calls
no-igd=1                       # Disable UPnP port mapping

# Slow but reliable db writes
db-sync-mode=safe
rpc-ssl=autodetect
#tx-proxy=tor,127.0.0.1:9050,16


# Emergency checkpoints set by MoneroPulse operators will be enforced to workaround potential consensus bugs
# Check https://monerodocs.org/infrastructure/monero-pulse/ for explanation and trade-offs
enforce-dns-checkpointing=1

out-peers=64              # This will enable much faster sync and tx awareness; the default 8 is suboptimal nowadays
in-peers=1024             # The default is unlimited; we prefer to put a cap on this

limit-rate-up=2048     # 1048576 kB/s == 1GB/s; a raise from default 2048 kB/s; contribute more to p2p network
limit-rate-down=8192   # 1048576 kB/s == 1GB/s; a raise from default 8192 kB/s; allow for faster initial sync
```

Running as root user just passing config and pidfile.

## selsta | 2022-06-25T10:30:46+00:00
@holdengreen And how much RAM does your VPS have? It might be too weak to run a full node.

Set the log level to 0, limit in and out peers to 12, both of these should help with using less resources.

## holdengreen | 2022-06-25T19:53:47+00:00
It has 2GB of RAM, most of which is not being used already.
I took your advice and it's syncing. But says it needs 18 days to do that just running in tmux for now.
(I don't think it'll take that long.)

## selsta | 2022-06-25T21:43:56+00:00
2GB without swap might not be enough for sync.

## holdengreen | 2022-06-26T17:19:24+00:00
I'll have to see if I can get a swap on this thing but it's 17% through with 771 mega available and 104 free.

# Action History
- Created by: dungdang95 | 2020-12-29T07:55:02+00:00
- Closed at: 2021-01-16T18:03:33+00:00
