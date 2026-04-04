---
title: Error "wrong miner tx in block"
source_url: https://github.com/monero-project/monero/issues/6419
author: AntlerDM
assignees: []
labels: []
created_at: '2020-04-02T18:33:40+00:00'
updated_at: '2022-05-26T23:22:36+00:00'
type: issue
status: closed
closed_at: '2022-02-19T04:40:07+00:00'
---

# Original Description
A few days ago, I got the following error message...

`2020-03-31 17:09:55.436	E wrong miner tx in block: <fb877ea3400f731c2b948e87655368f1c0486e3c114bb3f8f3839bec1b2f9596>, b.miner_tx.vin.size() != 1`

The exact same message appeared again today (with the same block hash)...

`2020-04-02 06:17:42.401	E wrong miner tx in block: <fb877ea3400f731c2b948e87655368f1c0486e3c114bb3f8f3839bec1b2f9596>, b.miner_tx.vin.size() != 1`

I am using the pre-compiled CLI Wallet from getmonero.org (v.0.15.0.5) on a MacPro. Mining is being done by xmrig v.5.10.0.

# Discussion History
## moneromooo-monero | 2020-04-02T18:50:47+00:00
You likely connected to a peer that's sending you a bad block. You can ignore that. I assume your node is otherwise synced, and not dropping off the network ?


## AntlerDM | 2020-04-02T19:12:56+00:00
I believe sync is okay (I get 'SYNCRONIZATION OK' messages) , but I am also getting a fairly frequent warning...

`2020-04-02 06:46:32.732	W No incoming connections - check firewalls/routers allow port 18080`

Even though the firewall has a rule allowing port 18080 to the computer. Maybe the firewall rule is not correct?

## moneromooo-monero | 2020-04-02T19:21:20+00:00
I wouldn't know. You might also need to set routers in the way to forward.
If you set log level to 1, you'll likely get the IP address from which that block is coming from, should it happen again. Chances are it'll be the same.


## ronohara | 2020-06-04T11:11:44+00:00
I just got the **exact** same message ...

2020-06-04 10:34:13.427	E wrong miner tx in block: <fb877ea3400f731c2b948e87655368f1c0486e3c114bb3f8f3839bec1b2f9596>, b.miner_tx.vin.size() != 1

So completely different node ...and I am on 'Nitrogen Nebula' (v0.16.0.0-release)  ... whereas 3 months ago you would have been on v0.15  ...  


# Action History
- Created by: AntlerDM | 2020-04-02T18:33:40+00:00
- Closed at: 2022-02-19T04:40:07+00:00
