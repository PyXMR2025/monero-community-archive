---
title: slow sync with blockchain import
source_url: https://github.com/monero-project/monero/issues/4085
author: yura-sutnuk
assignees: []
labels: []
created_at: '2018-06-30T08:20:16+00:00'
updated_at: '2018-07-03T04:33:19+00:00'
type: issue
status: closed
closed_at: '2018-07-03T04:33:19+00:00'
---

# Original Description
I downloaded the monero and blockchain from the official site and I try to start importing the blockchain for faster synchronization but the synchronization is still slower than if I just started the daemon.
i run import with command 

`sudo ./monero-blockchain-import --input-file ./blockchain.raw  --guard-against-pwnage 0`
i do something wrong?

# Discussion History
## moneromooo-monero | 2018-06-30T09:08:33+00:00
Yes, you're using --guard-against-pwnage 0 with a file you got from the internet. Why are you doing this when the name is clearly telling you it's dangerous ?

## yura-sutnuk | 2018-06-30T09:30:15+00:00
but if the file is obtained from a reliable source (in this case, the official site), then you can turn it off to speed up the synchronization or am I wrong?

## moneromooo-monero | 2018-06-30T09:37:17+00:00
It's reliable till it's not. The Gentoo github repo was just pwned for instance.
Anyway, it should speedup, yes.
When you say "slow", can you quantify that a bit ?
Are you using a HDD or SSD ?

## yura-sutnuk | 2018-06-30T10:23:18+00:00
with import speed was about 100 blocks per minute, with monerod speed was 200 blocks per minute, i am using HDD (unfortunatly i have not SSD)

## moneromooo-monero | 2018-06-30T10:28:04+00:00
Try a larger --batch-size

## yura-sutnuk | 2018-06-30T16:40:24+00:00
increased batch-size to 100,000, the speed increased to 600 blocks per minute

# Action History
- Created by: yura-sutnuk | 2018-06-30T08:20:16+00:00
- Closed at: 2018-07-03T04:33:19+00:00
