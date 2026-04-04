---
title: 24 word seed phrase may be confused with BIP-39
source_url: https://github.com/monero-project/monero-gui/issues/2852
author: jonathancross
assignees: []
labels: []
created_at: '2020-04-23T22:38:38+00:00'
updated_at: '2020-12-28T19:41:31+00:00'
type: issue
status: closed
closed_at: '2020-12-28T19:41:31+00:00'
---

# Original Description

![Screen Shot 2020-04-24 at 12 34 03 AM](https://user-images.githubusercontent.com/5115470/80156148-7ff37500-85c3-11ea-8d68-da4916e889e5.png)

Is the 24 word seed phrase option really just the removal of the checksum as suggested here:
https://github.com/monero-project/monero-gui/pull/1909#discussion_r257314571 ?

If so, seems like we should consider removing this.

**My confusion:** too similar to the 24-word [BIP-39](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki) seed phrases used by hardware wallets.  These can be used with [SLIP-44](https://github.com/satoshilabs/slips/blob/master/slip-0044.md) to encode Monero wallets.

# Discussion History
## crocket | 2020-12-06T03:53:32+00:00
Are you suggesting that it's possible to embed monero wallet in a bitcoin HD wallet through SLIP-44?

## jonathancross | 2020-12-14T16:37:11+00:00
@crocket It is _possible_ to generate keys for Monero using index `128` as listed in SLIP-44.  Hardware wallets for example do this.  They also give the user a "24 word seed backup".  But that "24 word seed backup" cannot be used in the Monero GUI wallet dialog I show above.

# Action History
- Created by: jonathancross | 2020-04-23T22:38:38+00:00
- Closed at: 2020-12-28T19:41:31+00:00
