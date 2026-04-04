---
title: '[monerod crashing] last thread post'
source_url: https://github.com/monero-project/monero-gui/issues/1877
author: SBSeed
assignees: []
labels:
- resolved
created_at: '2018-12-31T03:01:39+00:00'
updated_at: '2019-01-14T08:31:28+00:00'
type: issue
status: closed
closed_at: '2019-01-14T06:09:27+00:00'
---

# Original Description
whatever, might as well create another thread for whatever good it will do...

monerod.exe connects to specific nodes/machines to download specific hashes (most of which seem to be on the monero project machines since they are the same 2-3 for the most part) one of the nodes/machines is DENYING connection i have shown this to be the case in the last thread via the pic i had from the log file end...

what i was asking is:
- is it possible to force a connection to a node/machine
- is it possible to bypass a connection or force download from a different source
- is it possible to use the blockchain.raw to patch an already in-progress download of the imdb blockchain/data files

any information would be nice (frankly at this point i am not expecting much)...
this will most likely be the last time i ask for help here, getting any coherency here has been so unproductive and mentally draining that my depression is almost to the depths.... unbearable.

# Discussion History
## sanderfoobar | 2019-01-14T06:00:37+00:00
> monerod.exe connects to specific nodes/machines to download specific hashes (most of which seem to be on the monero project machines since they are the same 2-3 for the most part)

I assume you refer to P2P nodes. It is true that upon startup, the client will first contact so called 'seed nodes'. These are monero project owned machines and indeed, not all of them are up. This should however not pose a problem in terms of blockchain syncing.

> is it possible to force a connection to a node/machine

Use monerod flag `--add-priority-node <ip>` to specify/force connection to a specific p2p node.

> is it possible to bypass a connection or force download from a different source

See above answer.

> is it possible to use the blockchain.raw to patch an already in-progress download of the imdb blockchain/data files

I don't know. This issue tracker is for GUI problems (development and bugs only). For these type of questions, best to head to [our stackexchange](https://monero.stackexchange.com). 

+resolved


# Action History
- Created by: SBSeed | 2018-12-31T03:01:39+00:00
- Closed at: 2019-01-14T06:09:27+00:00
