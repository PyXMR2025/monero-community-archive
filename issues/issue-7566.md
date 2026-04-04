---
title: Tails OS workaround for using remote nodes (CLI)
source_url: https://github.com/monero-project/monero/issues/7566
author: thoughtmaker5
assignees: []
labels: []
created_at: '2021-03-14T06:17:18+00:00'
updated_at: '2021-10-06T02:31:19+00:00'
type: issue
status: closed
closed_at: '2021-10-06T02:31:19+00:00'
---

# Original Description
I've used the CLI without many issues connecting to remote nodes, but recently my transactions aren't being sent.  I get an error "outgoing tcp: connect: connection refused for [IP address]".
Through research I learned that Tails has "very restrictive firewall settings." I found tutorials about how to customize settings using monerod and running a full node. I didn't find much like that for using remote nodes. 
I tried "--no-dns" which removes the error.  My transactions appear to work and show as pending. But the funds don't leave my wallet.  

Help me plz

# Discussion History
## tobtoht | 2021-03-14T15:57:29+00:00
Follow the guide here to set up the CLI with a remote node on Tails: http://xmrguide42y34onq.onion/tails/cli/install/manual

> My transactions appear to work and show as pending

Which remote node are you using? Some may consistently fail to relay transactions.

## thoughtmaker5 | 2021-03-14T21:37:37+00:00
> 
> 
> Follow the guide here to set up the CLI with a remote node on Tails: http://xmrguide42y34onq.onion/tails/cli/install/manual
> 
> > My transactions appear to work and show as pending
> 
> Which remote node are you using? Some may consistently fail to relay transactions.

Thanks for replying. The steps in the guide match up with what I'm doing, I don't see anything I can correct. I'm alternating 3 or 4 nodes. I'll try finding some other nodes to use.

## selsta | 2021-10-06T02:31:19+00:00
Closing this, if this issue is still relevant please comment.

# Action History
- Created by: thoughtmaker5 | 2021-03-14T06:17:18+00:00
- Closed at: 2021-10-06T02:31:19+00:00
