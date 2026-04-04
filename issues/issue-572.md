---
title: Feature Request - Smart Nodes/Wallet
source_url: https://github.com/monero-project/monero-gui/issues/572
author: DaveyJonesXMR
assignees: []
labels:
- in progress
- resolved
created_at: '2017-03-19T14:25:55+00:00'
updated_at: '2018-11-18T18:09:34+00:00'
type: issue
status: closed
closed_at: '2018-11-18T18:09:34+00:00'
---

# Original Description
While surfing our reddit i stumbled over some comment that brought me to this request. Can`t find it sadly.

Request:

Implement smart-nodeing - former means that at first and future sync up the wallet automatically will use a remote node ( probably hosted by core or sth like node.moneroworld.com ) to connect at start so especially new users can have a wallet user experience right from the start, but also starts syncing a local node in the background and once fully synced will switch to the local node, 

This way especially people with slower HDD will still have a easy first-time  or once-in-a-month user-experience, on the other hand it will enhance our node network when people leave those wallets/nodes open because of the ease of use and may generally attract people that would not have the time/nerves to go through a full-sync at start.

As usual their should be disclaimers in the software about disk-usage, ram-usage etc.

# Discussion History
## Jaqueeee | 2017-03-22T15:52:54+00:00
I like this idea, but I'd like to have some input from @fluffypony and other core devs before implementing this. 

My suggestion is that we add a page in the wizard after creating a new wallet where we explain in 2-3 sentences why the user should run a local node. And after that 2 checkboxes:

1. (checked) Run local daemon. + info about the drawbacks. i.e diskspace, network usage, time until wallet can be used. 

2. (unchecked) Connect to remote daemon while local daemon in syncing. + info about the lesser privacy. 

It would be great if @xmr-eric or any other native speaker could provide the copy for this page. 


## hyc | 2017-03-25T19:57:02+00:00
We definitely need to get away from the notion of a "wallet" being separate from a "daemon." I.e., the part of the wallet that interacts with a daemon today, should be running 24/7 and should always have a local daemon (also running 24/7) to talk to. Everything else is just UI, talking via RPC to the wallet server. That solves our mobile use case as well as every other PC use case.

In the meantime - yes, we can explain why the user should run a local node. But for usability, we're going to need to separate the UI from the wallet sync and cache files. Nobody wants to wait for their wallet to sync over 3G.

## Jaqueeee | 2017-03-26T18:51:19+00:00
@DaveyJonesXMR this was discussed today at [dev meeting](https://monerobase.com/wiki/DevMeeting_2017-03-26) where @fluffypony made clear #605 is not going to be merged. 
Also #605

## dEBRUYNE-1 | 2017-08-09T13:29:57+00:00
+in progress

## iBobik | 2018-02-02T13:24:43+00:00
Just a suggestion: When sync starts in a background it should be more gentle to CPU usage, so it will not eat all of it and starts loudly fans (periodical sleeping daemon process for ⅔ of time seems ok on my MacBook Air 2016).

Also it should pause if laptop is on battery.

## iBobik | 2018-02-02T13:27:19+00:00
And maybe naive question: Is it really needed for privacy and security to sync whole blockchain for maintaining a full node? Is not enough to have only some X last blocks?

## erciccione | 2018-11-18T13:15:25+00:00
Resolved with bootrstap nodes

+resolved

# Action History
- Created by: DaveyJonesXMR | 2017-03-19T14:25:55+00:00
- Closed at: 2018-11-18T18:09:34+00:00
