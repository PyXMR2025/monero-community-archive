---
title: 'monero-wallet-cli: unclear what "suggested threshold" means'
source_url: https://github.com/monero-project/monero/issues/8668
author: imfiesh
assignees: []
labels: []
created_at: '2022-12-05T00:24:33+00:00'
updated_at: '2022-12-08T03:50:21+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
```show_transfer``` includes a _suggested threshold_ number but it's unclear what it signifies. For example a recent incoming transaction has around 300 confirmations and suggested threshold is shown as 40. What am I supposed to do with that information? Some googling shows that it is the suggested number of confirmations to wait for the transaction to be "super extra confirmed", given the amount transferred (compared to just waiting for the normal 10 confirmations). I suggest the wording made more clear and at the least I suggest it not be shown at all if the threshold has already been reached.


# Discussion History
## plowsof | 2022-12-05T01:46:52+00:00
the definition on -site for threshold was wrong, its a bit more nuanced than that but in summary: "Number of confirmations needed for the amount received to be lower than the accumulated block reward (or close to that)." as per [this](https://github.com/monero-project/monero-site/pull/2083/commits/d2ed963087ed952c589f62a40ed6a879ec8a2ba5)


## trasherdk | 2022-12-05T23:53:07+00:00
Okay, but why do we want to know this?

## jtgrassie | 2022-12-08T03:50:20+00:00
I tend to agree that this (and #8667) are a little misleading insofar as just showing the actual confirmation count (depth) would be clearer. Anything spendable (so over 10 blocks deep) shouldn't really need a "suggested threshold", regardless of amount or block reward, and if a user wants to be extra cautious, simply presenting the actual confirmation count (depth) should suffice.

# Action History
- Created by: imfiesh | 2022-12-05T00:24:33+00:00
