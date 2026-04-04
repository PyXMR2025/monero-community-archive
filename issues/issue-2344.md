---
title: Improvements when denying "Export View Key" on hardware wallet
source_url: https://github.com/monero-project/monero-gui/issues/2344
author: ghost
assignees: []
labels: []
created_at: '2019-08-09T16:50:28+00:00'
updated_at: '2019-09-04T21:05:31+00:00'
type: issue
status: closed
closed_at: '2019-09-04T16:31:59+00:00'
---

# Original Description
[Updated]
![image](https://user-images.githubusercontent.com/46682965/64254398-9a3aee80-cf1f-11e9-99c0-b64f049a1c1f.png)
When you deny "Export View Key"...
- the user should be informed _"You have denied the export of your public view key, therefore calculations will have to be done on your hardware wallet. This may take a very long time."_
- `Wallet blocks remaining: 12345 blocks` should be updated every block - not every 999 blocks. (1 block takes about 1 second with Ledger Nano S and subaddress lookahead 1:1)
- clicking on the "close wallet" icon in the balance card shouldn't close the whole GUI.



# Discussion History
## selsta | 2019-08-11T21:39:08+00:00
When you deny it, the calculations are all done on your Ledger and scanning gets really slow. Last time I tried it, it was unusably slow.

## ghost | 2019-08-17T10:28:14+00:00
Thx! Issue updated.

## ghost | 2019-09-04T12:32:59+00:00
I guess nobody uses this anyway, right? Close? It just gets ugly if some poor noob doesn't know what he's doing. 

## selsta | 2019-09-04T16:21:02+00:00
AFAIK the GUI doesn’t know if the view key gets exported or not. Changing this behavior isn’t trivial, I think it’s unlikely that this will get changed soon. People export their view key anyway.

## ghost | 2019-09-04T16:23:45+00:00
I see, and I wouldn't recommend putting any work in it. So close, right?

## ghost | 2019-09-04T16:34:40+00:00
Closed and moved to #2209.

# Action History
- Created by: ghost | 2019-08-09T16:50:28+00:00
- Closed at: 2019-09-04T16:31:59+00:00
