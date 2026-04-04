---
title: Allow users to send money before the daemon finishes synchronizing
source_url: https://github.com/monero-project/monero-gui/issues/745
author: fresheneesz
assignees: []
labels:
- resolved
created_at: '2017-05-25T18:30:44+00:00'
updated_at: '2018-11-18T16:45:35+00:00'
type: issue
status: closed
closed_at: '2018-11-18T16:45:35+00:00'
---

# Original Description
There's no good reason I can see to keep people from attempting to make transactions before their blockchain is fully synced. As long as the client knows they *did* have some monero, it can be 99.9999% certain they still have that monero. Even if they spent that xmr from a different wallet or are syncing a new instance from a wallet backup, the user is almost certainly going to know if they have enough xmr to spend. And the 1 in a million times someone makes a mistake? The network will reject the transaction, nbd. 

So please don't lock up the application just cause it needs to sync

# Discussion History
## Jaqueeee | 2017-05-29T12:00:48+00:00
The wallet asks daemon for fake outputs to use in the ring signature. Sending before daemon has finished syncing is therefore not recommended. If the daemon has synced passed your own outputs the tx could be sent, but i think there's a risk that your non-fake output will stand out in the ring signature. I'm not sure about that last part though. Maybe @moneromooo-monero could answer?


## fresheneesz | 2017-05-29T20:46:23+00:00
Ah, hm I see. Perhaps the client could sync up a few of the most recent blocks up front so it can pull good outputs for use in the ring? I suppose this would require trusting that you're sent good blocks since you can't verify until you have the entire thing.. 

If someone could be warned that their transaction might not be private, they could at least make the choice whether to wait or not themselves? 

## Jaqueeee | 2017-05-30T16:36:36+00:00
AFAIK the random fake outputs are picked from the whole blockchain. Not just the last part. It might be a better idea to ask a fully synced remote node for the outputs instead. 

## erciccione | 2018-11-18T13:39:01+00:00
resolved with bootrasp nodes.

+resolved

# Action History
- Created by: fresheneesz | 2017-05-25T18:30:44+00:00
- Closed at: 2018-11-18T16:45:35+00:00
