---
title: Blockchain taking days to download
source_url: https://github.com/monero-project/monero-gui/issues/4356
author: ghost
assignees: []
labels: []
created_at: '2024-09-19T13:11:12+00:00'
updated_at: '2024-09-21T07:18:27+00:00'
type: issue
status: closed
closed_at: '2024-09-20T11:57:18+00:00'
---

# Original Description
I'm trying to setup for the first time, but the blockchain is taking far too long (days) to download and sync. I have a 300mb/s fibre connection so that isn't the problem.

I've tried both `--prune-blockchain` and `--db-sync-mode=fastest` in the daemon startup flags, I also tried running `./monerod --prune-blockchain --db-sync-mode=fastest ` and `./monero-wallet-gui.AppImage --prune-blockchain`. I've also tried changing the `wallet restore height` but every time I start the blockchain download, the log says it's going to take between 2 and up to 4 days to complete.

![prune](https://github.com/user-attachments/assets/b129a554-7946-4c5f-9f01-5226912ad427)

[bitmonero.log](https://github.com/user-attachments/files/17059500/bitmonero.log)

`2024-09-19 12:44:49.310	[P2P7]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1697	Synced 49984/3240906 (1%, 3190922 left, 1% of total synced, estimated 2.5 days left)`

I don't want to use third party nodes, but neither do I want to spend days waiting for the blockchain to download and sync, is there any way to fix this?

Edit: Ok so I guess this is 'normal' and required to use monero-gui, but there's no way am I devoting my desktop to downloading a blockchain for the next number of days, this is an insurmountable barrier to entry that the vast majority of people will say "no way " to.

At this point I'd much rather use feather wallet... absolutely zero hassle and it connects to a curated list of remote nodes, which I'm presuming is better than a non-curated list that comes with monero-gui.

# Discussion History
## selsta | 2024-09-20T11:57:19+00:00
The fastest way to sync up is by having a fast SSD, it should take around 24h, the flags you added won't help with sync speed.

> I don't want to use third party nodes, but neither do I want to spend days waiting for the blockchain to download and sync, is there any way to fix this?

No, using monero requires a node. Either you sync your own or you use a public third party one.

> At this point I'd much rather use feather wallet... absolutely zero hassle and it connects to a curated list of remote nodes, which I'm presuming is better than a non-curated list that comes with monero-gui.

You can set your own remote node in monero-gui. Feather Wallet is also a great choice if you don't want to deal with searching for remote nodes.

## ghost | 2024-09-21T07:18:26+00:00
> The fastest way to sync up is by having a fast SSD, it should take around 24h

Not for me it won't because there's not a snowballs chance in hell am I going to do it.

"Either use a potentially malicious node or spend days with your PC completely locked up while it downloads and stores hundreds of gb of data"

RAIN CHECK - No chance on Earth would I ever use this software.



# Action History
- Created by: ghost | 2024-09-19T13:11:12+00:00
- Closed at: 2024-09-20T11:57:18+00:00
