---
title: Bus error (Core Dump), when starting monerod
source_url: https://github.com/monero-project/monero/issues/6382
author: cavapoo2
assignees: []
labels: []
created_at: '2020-03-11T17:21:44+00:00'
updated_at: '2020-03-11T18:56:06+00:00'
type: issue
status: closed
closed_at: '2020-03-11T18:56:06+00:00'
---

# Original Description
Ubuntu 1804, managed to download 50% of blockchain yesterday, today it just core dumps.

2020-03-11 17:17:26.002 I Monero 'Carbon Chamaeleon' (v0.15.0.1-release)
2020-03-11 17:17:26.002 I Moving from main() into the daemonize now.
2020-03-11 17:17:26.003 I Initializing cryptonote protocol...
2020-03-11 17:17:26.003 I Cryptonote protocol initialized OK
2020-03-11 17:17:26.003 T Blockchain::Blockchain
2020-03-11 17:17:26.003 I Initializing core...
2020-03-11 17:17:26.003 T BlockchainLMDB::BlockchainLMDB
2020-03-11 17:17:26.003 T BlockchainLMDB::get_db_name
2020-03-11 17:17:26.003 I Loading blockchain from folder /home/base/.bitmonero/lmdb ...
2020-03-11 17:17:26.003 D option: fast
2020-03-11 17:17:26.003 D option: async
2020-03-11 17:17:26.003 D option: 250000000bytes
2020-03-11 17:17:26.003 T BlockchainLMDB::open
2020-03-11 17:17:26.003 W The blockchain is on a rotating drive: this will be very slow, use an SSD if possible
2020-03-11 17:17:26.004 T BlockchainLMDB::need_resize
2020-03-11 17:17:26.004 D DB map size: 10035043072
2020-03-11 17:17:26.004 D Space used: 8835379200
2020-03-11 17:17:26.004 D Space remaining: 1199663872
2020-03-11 17:17:26.004 D Size threshold: 0
2020-03-11 17:17:26.004 D Percent used: 88.0453 Percent threshold: 90.0000
Bus error (core dumped)

where is coredump located nowadays ? not much in that log. 

# Discussion History
## sumogr | 2020-03-11T17:31:50+00:00
if i was you i would read the last log line again (you are out of disk space or your chain is corrupt due to a bad hard disk most likely)

## cavapoo2 | 2020-03-11T18:30:58+00:00
Cant be out of disk space, only got well over 600 gig  free. Get the feeling this might have been caused by shutdown. CTRL-C just hangs. 

## sumogr | 2020-03-11T18:53:21+00:00
> Cant be out of disk space, only got well over 600 gig free. Get the feeling this might have been caused by shutdown. CTRL-C just hangs.

Yeap either try salvaging it or delete it and try to resync from scratch

# Action History
- Created by: cavapoo2 | 2020-03-11T17:21:44+00:00
- Closed at: 2020-03-11T18:56:06+00:00
