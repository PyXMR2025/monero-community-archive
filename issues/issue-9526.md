---
title: How many blocklists should the average public node operator apply?
source_url: https://github.com/monero-project/monero/issues/9526
author: li5lo
assignees: []
labels:
- question
created_at: '2024-10-21T02:36:24+00:00'
updated_at: '2024-10-28T22:08:47+00:00'
type: issue
status: closed
closed_at: '2024-10-28T22:08:46+00:00'
---

# Original Description
There is:

- enable-dns-blocklist
- https://gui.xmr.pm/files/block.txt
- https://gui.xmr.pm/files/block_tor.txt
- https://paste.debian.net/hidden/359f2fb0 from [a random reddit post](https://www.reddit.com/r/Monero/comments/1g82047/malicious_node_ips_discovered/)

Let alone the fact that static blocklists are useless at best, overblocking at worst,
neither of them explains when they should be set or unset, who maintains them, how often or if they get updated or what they protect against.

If blocklist(s) are necessary or advisable there should be a clear policy and communication at least about the points mentioned above and only one trusted and reliable source for them.

# Discussion History
## selsta | 2024-10-22T18:06:36+00:00
> https://gui.xmr.pm/files/block.txt

Is the one I'm maintaining, it gets regularly updated and is complete of all known IPs. So if you want to apply block list, this one.

The DNS one currently missing some IPs due to limitations, which we will fix in an upcoming update.

> how often or if they get updated or what they protect against.

The lists include nodes that are fingerprinted as running custom software with the goal of spying.

## li5lo | 2024-10-26T07:10:51+00:00
> The lists include nodes that are fingerprinted as running custom software with the goal of spying.

So every node operator who trusts the core team to not intentionally include arbitrary IPs should enable
`enable-dns-blocklist` on all their mainnet/stagenet/testnet nodes and can consider to temporarily apply a static blocklist with the IP addresses from  https://gui.xmr.pm/files/block.txt

## selsta | 2024-10-28T22:08:46+00:00
Correct. Also the block lists are compiled by developers, not the core team. Theoreatically the core team has access to the DNS so they are somewhat involved.

# Action History
- Created by: li5lo | 2024-10-21T02:36:24+00:00
- Closed at: 2024-10-28T22:08:46+00:00
