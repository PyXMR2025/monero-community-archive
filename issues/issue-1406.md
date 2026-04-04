---
title: problems with view wallet if cache is deleted (e.g. rescan_bc)
source_url: https://github.com/monero-project/monero/issues/1406
author: rndbr
assignees: []
labels: []
created_at: '2016-12-05T17:54:24+00:00'
updated_at: '2016-12-10T20:03:30+00:00'
type: issue
status: closed
closed_at: '2016-12-10T20:03:30+00:00'
---

# Original Description
if you have a view wallet, perform a transaction on it, with the new code things work well, and the outgoing tx shows in `show_transfers`, no problem. if you then call `rescan_bc`, and then re-import the key images from the cold wallet, the problems begin:

problem 1: subsequent `transfer` statements seem to break, in the cli I see: `Error: transaction was not constructed`

in the logs I see:

```
2016-Dec-05 18:06:12.225547 ERROR /home/l/monero.src/src/cryptonote_core/cryptonote_format_utils.cpp:558 derived public key mismatch with output public key!
[...]
2016-Dec-05 18:06:12.225575 ERROR /home/l/monero.src/src/wallet/wallet2.cpp:3655 !r. THROW EXCEPTION: error::tx_not_constructed
2016-Dec-05 18:06:12.225663 /home/l/monero.src/src/wallet/wallet2.cpp:3655:N5tools5error18tx_not_constructedE: transaction was not constructed
[...]
2016-Dec-05 18:06:12.225811 Error: transaction was not constructed
```

problem 2: it appears that `show_transfers` doesn’t show outgoing transactions. `balance` output is correct, though.... 


# Discussion History
## rndbr | 2016-12-05T19:17:26+00:00
problem 1 above happens on one offline wallet I have where I did this `rescan_bc`, but not another, so it may not be 100% related. on the wallet where I failed, I still cannot fix it even when I restore the hot version via the viewkey, and restore the cold version via the deterministic words, so it's something with what's actually on the blockchain with this it seems.

## moneromooo-monero | 2016-12-09T18:25:51+00:00
I think that should be fixed by https://github.com/monero-project/monero/pull/1419. You will have to rescan again I'm afraid.

## rndbr | 2016-12-10T20:03:30+00:00
that seemed to do it. thanks!

# Action History
- Created by: rndbr | 2016-12-05T17:54:24+00:00
- Closed at: 2016-12-10T20:03:30+00:00
