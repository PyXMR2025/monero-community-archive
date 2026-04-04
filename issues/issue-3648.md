---
title: Unable to sync with Monero network
source_url: https://github.com/monero-project/monero-gui/issues/3648
author: ch9PcB
assignees: []
labels: []
created_at: '2021-07-29T01:39:35+00:00'
updated_at: '2021-07-29T11:18:02+00:00'
type: issue
status: closed
closed_at: '2021-07-29T11:17:30+00:00'
---

# Original Description
Starting from about 0045 hours (UTC) till now on July 29, 2021, I have been unable to sync my computer with the Monero network.

The error message is:

`There were 0 blocks in the last 90 minutes, there might be large hash rate changes, or we might be partitioned, cut off from the Monero network or under attack, or your computer's time is off. Or it could be just sheer bad luck.`

Note: As usual, after launching Tor Browser, activating torsocks and in a new terminal, I typed the command:

`DNS_PUBLIC=tcp://1.1.1.1 TORSOCKS_ALLOW_INBOUND=1 torsocks ./monerod --p2p-bind-ip 127.0.0.1 --no-igd --hide-my-port --ban-list block.txt --data-dir    /path/to/Monero/data`

The above steps have always worked for me, the last time being about 3.5 days ago (according to the log)

Question: What happened to the Monero network? Has it been under attack?


# Discussion History
## selsta | 2021-07-29T01:41:26+00:00
It's not an issue with the network, blocks are coming in as normal.

Can you post the output of sync_info ?

## ch9PcB | 2021-07-29T11:17:25+00:00
Thanks for your reply.

> It's not an issue with the network, blocks are coming in as normal.
> 
Good to know. It means something is wrong with my local node?

> Can you post the output of sync_info ?

When I saw your reply, it was already almost 0200 hours (UTC) by which time my local node over Tor was able to sync with the Monero network.

The next time the exact same issue happens, I shall remember to give you the output of sync_info.


## ch9PcB | 2021-07-29T11:18:01+00:00
About 1.5 hours later, my local node over Tor was able to sync with the Monero network.

# Action History
- Created by: ch9PcB | 2021-07-29T01:39:35+00:00
- Closed at: 2021-07-29T11:17:30+00:00
