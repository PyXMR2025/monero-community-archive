---
title: 2 wallets 1 local node; transfer problems
source_url: https://github.com/monero-project/monero/issues/3795
author: Staz1st
assignees: []
labels: []
created_at: '2018-05-11T19:37:19+00:00'
updated_at: '2018-05-12T19:28:04+00:00'
type: issue
status: closed
closed_at: '2018-05-12T19:28:04+00:00'
---

# Original Description
I made 2 different xmr-wallets using same local node. 
Wanted to transfert all xmr from wallet1 to wallet2 but getting following errorcode (dutch content says "transaction error") 

> Transactie kan niet worden aangemaakt: no connection to daemon. Please make sure daemon is running.

 But daemon is running, wallet is correctly synced. Running and syncing of both wallets seem to work fine. What am I missing? Is there another way to transfer between 2 wallets on same blockchain.db?

# Discussion History
## moneromooo-monero | 2018-05-11T20:58:03+00:00
Use current release-0.12 code, it's likely a timeout which was fixed there.

## Staz1st | 2018-05-11T21:02:38+00:00
I'm sorry I should have mentioned i'm using _monero-gui-v0.12.0.0_
Which I think is the version you mention

## dEBRUYNE-1 | 2018-05-11T21:05:21+00:00
Moneromooo means that you ought to compile the release-v0.12 branch. 

## Staz1st | 2018-05-11T21:41:00+00:00
updated files in GUI-dir to v0.12. Still same error. 

## moneromooo-monero | 2018-05-11T22:17:46+00:00
Does "updated files in GUI-dir to v0.12" mean you're now using the current release-0.12 branch code ? It is not the same as a v0.12.0.0 tag nor the prevuilt 0.12.0.0 binaries.

## Staz1st | 2018-05-11T22:40:31+00:00
I took latest release: **v0.12.0.0 - c29890c** and used _monero-win-x64-v0.12.0.0.zip_ to extract in the GUI-v0.12.0.0 map. Do you mean I used v0.12.0.0 tag? 
I think you mean this page [[https://github.com/monero-project/monero/tree/release-v0.12](https://github.com/monero-project/monero/tree/release-v0.12)] which means I have to compile of which I have very little experience. 


## moneromooo-monero | 2018-05-12T09:07:30+00:00
Yes, you used that tag, which is not what I asked. If you can't/won't build, then you can also pluck a build from the build.getmonero.org site, or wait for a new release.

## Staz1st | 2018-05-12T19:28:04+00:00
Problem solved itself...

# Action History
- Created by: Staz1st | 2018-05-11T19:37:19+00:00
- Closed at: 2018-05-12T19:28:04+00:00
