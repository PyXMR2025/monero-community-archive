---
title: Failed to connect to any of seed peers, continuing without seeds
source_url: https://github.com/monero-project/monero/issues/1661
author: anonimal
assignees: []
labels: []
created_at: '2017-02-02T02:49:50+00:00'
updated_at: '2017-02-18T05:43:58+00:00'
type: issue
status: closed
closed_at: '2017-02-18T05:43:58+00:00'
---

# Original Description
TL;DR: monero node no longer syncs over Tor (tested over multiple circuits and exits)
```
anonimal        "Failed to connect to any of seed peers, continuing without seeds"
anonimal        Multiple Tor circuits, same message. If this is because of #1572, I will shake my fist in the air rapidly.
 *      anonimal using same commit that worked fine several days ago 2806842200d848b02c2c9c1816dbbc6e4803c923
anonimal        If it looks like #1572, smells like #1572, I'm assuming for now it's #1572.
anonimal        If so, this is a blow to privacy and to Tor users everywhere. If so, then using Tor to sync now requires a 3rd party to host an onionsite to their public node.
anonimal        Syncing over I2P, that could take weeks to months to finish. Not very appealing
```
Built against 2806842200d848b02c2c9c1816dbbc6e4803c923, I don't want to jump to conclusions but possibly #1572 related?

# Discussion History
## ghost | 2017-02-02T05:10:44+00:00
Try manually bumping the limit and feed back here. 

## anonimal | 2017-02-02T06:25:01+00:00
Since this is a P2P issue, if nodes are running #1572, I can set the limit to infinity and it wouldn't matter because *they* would need to set the limit too, correct?

## ghost | 2017-02-02T08:41:19+00:00
I doubt every node out there has updated to include that patch. I'd argue the majority will be running vanilla 0.10.1

## IPGlider | 2017-02-02T17:30:28+00:00
@anonimal your limit does not affect remote nodes, they would still have the limit, but as @NanoAkron said I doubt many nodes are running master.

Anything I can do to help?

## anonimal | 2017-02-04T14:25:51+00:00
Two notes:

1. The commit I mentioned above was the same commit I used when there wasn't an issue
2. In `#monero-dev`, @Jaqueeee noted that recently received the same message but Jaquee's solution was to change DNS resolver

`anonimal | Since I can't change which resolver a Tor exit uses, I can't test your solution. I *can* test at the application level though if monero/unbound can somehow do that.`

## anonimal | 2017-02-10T22:58:04+00:00
I can't reproduce this issue now. Was this DNSSEC related? Who runs moneroseeds?

# Action History
- Created by: anonimal | 2017-02-02T02:49:50+00:00
- Closed at: 2017-02-18T05:43:58+00:00
