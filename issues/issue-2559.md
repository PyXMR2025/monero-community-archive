---
title: Add "print_tx_sh" command for a short version of "print_tx" in the daemon
source_url: https://github.com/monero-project/monero/issues/2559
author: binaryFate
assignees: []
labels: []
created_at: '2017-10-01T14:12:54+00:00'
updated_at: '2017-11-05T23:55:00+00:00'
type: issue
status: closed
closed_at: '2017-11-05T23:55:00+00:00'
---

# Original Description
Currently `print_tx` spits the whole tx. 
Often one wants only to check the block height of the transaction, or simply to check whether it is known to the daemon at all. A one-liner version would be practical so as not to scroll up and search among a large blob.  
Anyone would find it useful? If so what info do we want to be returned? txid, payment id, fees amount, ring size, block height (or time received if not confirmed yet)?


# Discussion History
## moneromooo-monero | 2017-10-02T12:02:51+00:00
It'd be useful. Maybe everything except the JSON and hex. Or just add options to print_tx to select json and/or hex in addition to the "human text" data.


## binaryFate | 2017-10-02T12:26:28+00:00
> Or just add options to print_tx to select json and/or hex in addition to the "human text" data.

I like it, better than creating more commands IMO.

Would it be worth being consistent with the print_pool command(s)? Currently print_pool and print_pool_sh.

## moneromooo-monero | 2017-10-02T14:00:57+00:00
I wouldn't care much either way. They're different commands. New ones don't have to slavishly try to mimic if another way seems better. In that case, there's not a huge amount of difference, since they'll all go through the same RPC anyway.

## binaryFate | 2017-10-04T08:03:43+00:00
I'll do this one soon

# Action History
- Created by: binaryFate | 2017-10-01T14:12:54+00:00
- Closed at: 2017-11-05T23:55:00+00:00
