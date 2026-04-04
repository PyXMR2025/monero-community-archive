---
title: Stuck at "Creating Transaction"
source_url: https://github.com/monero-project/monero-gui/issues/553
author: dternyak
assignees: []
labels: []
created_at: '2017-03-11T23:57:59+00:00'
updated_at: '2017-03-12T20:15:38+00:00'
type: issue
status: closed
closed_at: '2017-03-12T20:14:02+00:00'
---

# Original Description
Using a remote node. Not sure how to provide additional debug info. 

Using master 897bc582f042cdcecbaf8048bd9ab73f3f9b302b

Edit: Eventually timed out (5 mins or so, but crashed once before): 

```Can't create transaction: no connection to daemon. Please make sure daemon is running.```. 

I was able to sync with the same remote node, so I feel like there still might have been something client side that caused this. 

Somone else testing sending a transaction and confirming it does indeed work should be enough to close this issue, as remote nodes should not be relied upon. 

# Discussion History
## Jaqueeee | 2017-03-12T13:14:41+00:00
Can you try with a different remote node? Any of these for example: node.moneroworld.com node.supportxmr.com node.xmrbackb.one


## dternyak | 2017-03-12T20:12:25+00:00
I tried with local daemon and it seemed to work.

Failed with both of those remote nodes. In one case it failed because the GUI crashed, in the other case it failed with `Can't create transaction: no connection to daemon. Please make sure daemon is running..`

## Jaqueeee | 2017-03-12T20:15:38+00:00
Sounds like a timeout issue indeed. Will try to reproduce, thanks. 

# Action History
- Created by: dternyak | 2017-03-11T23:57:59+00:00
- Closed at: 2017-03-12T20:14:02+00:00
