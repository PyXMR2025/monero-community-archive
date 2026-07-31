---
title: notify::send_txs provided message exceeding covert fragment size
source_url: https://github.com/monero-project/monero/issues/7708
author: selsta
assignees: []
labels:
- daemon
created_at: '2021-05-06T23:00:03+00:00'
updated_at: '2026-07-29T18:24:40+00:00'
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

## jpk68 | 2026-07-09T17:35:25+00:00
I have also been running into this issue on occasion while testing I2P SAM integration, especially over slow connections.

## vtnerd | 2026-07-29T18:24:26+00:00
The speed of the connection is irrelevant. The limiting factor is that the tx size exceeded 60 KiB. This is _mostly_ a sender policy that can be fixed by bumping up the local config `CRYPTONOTE_MAX_FRAGMENTS` value. Additional `static_assert`s trigger if you exceed values that can be sent using the noise protocol.

# Action History
- Created by: selsta | 2021-05-06T23:00:03+00:00
