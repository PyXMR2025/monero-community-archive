---
title: XMR wallet GUI not working anymore... Please HELP!!!
source_url: https://github.com/monero-project/monero/issues/6899
author: dariensc
assignees: []
labels: []
created_at: '2020-10-14T18:16:53+00:00'
updated_at: '2020-10-15T22:34:42+00:00'
type: issue
status: closed
closed_at: '2020-10-15T22:34:42+00:00'
---

# Original Description
I've just downloaded the most recent version of the wallet GUI and now it doesn't allow me to sign in with my previous password. It says: 

"Couldn't open wallet: Wrong Device Status:0x6a30 (UNKNOWN), EXPECTED 0x9000 (SW_OK), MASK 0xffff"

I've also tried to restore wallet from device, with restore height but haven't succeded either. Shows "Error writing wallet from hardware device. Check applications logs".

I'm really new to all this tech and has no background coding, so I'm really desperate and afraid I can't recover my money. So please, any help would be greatly appreciated


# Discussion History
## selsta | 2020-10-14T18:17:53+00:00
Update Monero Ledger app to v1.7.4 using Ledger Live

## dariensc | 2020-10-14T18:19:23+00:00
Oh, thanks... I'll do it right now. Hope it helps

## iDunk5400 | 2020-10-14T18:36:39+00:00
As there have been a number of GUI issues opened here recently, I suggest directing users to the [proper repo](https://github.com/monero-project/monero-gui/issues) and closing GUI issues here.

## dariensc | 2020-10-14T18:52:41+00:00
@selsta Awesome!! IT WORKED THANKS!!

Now I have some issues with the DOUBLE SPENDING... Yesterday I was having troubles with sending XMR and I followed your workaround entering the address (node.xmr.to) and Port (18081) as you suggested in another posts.

I'm guessing it has to do with the stucked TXNs (Waiting confirmation). Is there any way to solve this issue?

## dariensc | 2020-10-14T18:54:13+00:00
@iDunk5400 Oh, thanks, I'll move there then.

## selsta | 2020-10-14T19:01:39+00:00
Go to Settings -> Info, click on "(Change)" next to restore height and then simply click on okay, don’t change the number.

Afterwards it will refresh and your issue should be resolved.

# Action History
- Created by: dariensc | 2020-10-14T18:16:53+00:00
- Closed at: 2020-10-15T22:34:42+00:00
