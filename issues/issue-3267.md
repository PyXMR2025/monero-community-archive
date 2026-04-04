---
title: testnet stop working - which node to sync from now?
source_url: https://github.com/monero-project/monero/issues/3267
author: moneroexamples
assignees: []
labels: []
created_at: '2018-02-15T03:20:19+00:00'
updated_at: '2018-02-23T05:16:54+00:00'
type: issue
status: closed
closed_at: '2018-02-23T05:16:54+00:00'
---

# Original Description
guess due to recent rollback. 

But know I'm stuck, cant sync, no peers. Are there are recommended peers to sync from?

# Discussion History
## Gingeropolous | 2018-02-15T04:16:40+00:00
i managed to sync..., well i just started synchronizing. No idea if it'll finish or what fork it'll end up on..

 try deleting p2pstate.bin etc.

## moneroexamples | 2018-02-15T04:39:35+00:00
What block are you at? For me `status` shows

```
Height: 1098875/1098875 (100.0%) on testnet, not mining, net hash 195 H/s, v8, up to date, 1(out)+0(in) connections, uptime 0d 0h 0m 15s
```

but not going past it.

## stoffu | 2018-02-15T04:44:54+00:00
Hope this helps?

```
status 
Height: 1099510/1099510 (100.0%) on testnet, not mining, net hash 208 H/s, v7, up to date, 3(out)+0(in) connections, uptime 0d 0h 0m 14s
sync_info
Height: 1099510, target: 1099510 (100%)
Downloading at 9 kB/s
5 peers
212.53.140.36:28080       d601c13720db8c50  1099510  2 kB/s, 0 blocks / 0 MB queued
163.172.28.245:28080      c327ab882d8f9cb5  1099510  0 kB/s, 0 blocks / 0 MB queued
104.236.186.62:28080      b35e30b776d8ed31  1099510  2 kB/s, 0 blocks / 0 MB queued
52.18.127.168:18080       c98af27e0a32dd54  1099510  2 kB/s, 0 blocks / 0 MB queued
185.183.159.234:28080     97d54ef093f7cb93  1099510  3 kB/s, 0 blocks / 0 MB queued
0 spans, 0 MB
```

## moneroexamples | 2018-02-15T05:15:11+00:00
@stoffu 

You are on v7. Current fork is v8 which does not sync further.

## stoffu | 2018-02-15T05:59:49+00:00
Ah, I didn't know that. Sorry :P

## moneroexamples | 2018-02-15T06:25:01+00:00
@stoffu 

Its ok. I did `git pull` today, and testnet is broken for me now. I think its related to these PRs:
 - https://github.com/monero-project/monero/commit/c70f03cacf234d184bb0b5d4a5a11928ef147bf6
 - https://github.com/monero-project/monero/commit/19ff243f52556562c3aa87e22e0d4b1fd2eeb7df

Later will try syncing testnet from scratch. 

## moneromooo-monero | 2018-02-15T08:13:58+00:00
You need to wait for the seed nodes to be updated, if not yet done.

## moneroexamples | 2018-02-16T01:21:20+00:00
@moneromooo-monero 

Thanks. I will wait few days and see. No change for now.

## moneroexamples | 2018-02-23T05:16:54+00:00
Seems to be back to normal.

# Action History
- Created by: moneroexamples | 2018-02-15T03:20:19+00:00
- Closed at: 2018-02-23T05:16:54+00:00
