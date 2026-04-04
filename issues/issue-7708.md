---
title: notify::send_txs provided message exceeding covert fragment size
source_url: https://github.com/monero-project/monero/issues/7708
author: selsta
assignees: []
labels: []
created_at: '2021-05-06T23:00:03+00:00'
updated_at: '2021-05-16T08:13:50+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
```
00:52 <[r|y`a_n]> 2021-05-06 22:50:52.315 E notify::send_txs provided message exceeding covert fragment size
00:53 <[r|y`a_n]> my transactions are stuck and monerod is telling me this when I try to relay_tx
00:55 <[r|y`a_n]> did a huge sweep_all which generated loads of transactions
```

Starting with `disable_noise` allowed them to relay the transactions.

ping @vtnerd

# Discussion History
## vtnerd | 2021-05-15T15:54:45+00:00
This should be fixable on the sender side via configurable policy. Change [`CRYPTONOTE_MAX_FRAGMENTS`](https://github.com/monero-project/monero/blob/master/src/cryptonote_config.h#L125) to some higher value, rebuild, and retry. The receiver limit is determined by the standard max receive payload size which is much higher.

I will submit a PR shortly that ups to the default policy to twice the current average block size. This will likely come up again, however, if someone is trying to send a tx twice the blocksize via fragments its unlikely to work and a quick error log is more helpful (this was the rationale for the existing limit).

## vtnerd | 2021-05-16T08:13:50+00:00
So I was too quick to post that PR as the `static_assert` showed. I'm not sure this can be fixed easily due to the design. Your transaction can still be sent, but not over the most private method. Use `--tx-proxy ...,disable_noise` to send over I2P/Tor without the white noise feature, which is currently the limiting factor. 

The issue is that its unlikely that the entire transaction will be sent before switching to another node for white noise.

# Action History
- Created by: selsta | 2021-05-06T23:00:03+00:00
