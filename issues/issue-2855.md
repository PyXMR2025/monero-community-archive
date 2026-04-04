---
title: monerod running with --restricted-rpc makes monero-wallet-rpc error "failed
  to get random outs"
source_url: https://github.com/monero-project/monero/issues/2855
author: shigutso
assignees: []
labels: []
created_at: '2017-11-23T17:55:00+00:00'
updated_at: '2017-12-26T12:24:24+00:00'
type: issue
status: closed
closed_at: '2017-12-26T12:24:24+00:00'
---

# Original Description
Similar to the issue #2028, even if `monero-wallet-rpc` is running with the `--trusted-daemon` option, I can't make payments because the error `Issue making payments{"code":-4,"message":"failed to get random outs"}` shows up.

The only way I can make the payments correctly is if I remove the `--restricted-rpc` option from monerod

Is this intended or a bug?

Thank you

# Discussion History
## moneromooo-monero | 2017-11-23T19:04:11+00:00
You're probably asking for more fake outs than the restricted limit. Which probably should get increased anyway, so I'll do that.

## moneromooo-monero | 2017-11-23T19:17:46+00:00
https://github.com/monero-project/monero/pull/2856

## moneromooo-monero | 2017-12-26T12:15:13+00:00
+resolved

It'll still happen for even larger amounts of outs, but there's got to be a sane limit somewhere.

# Action History
- Created by: shigutso | 2017-11-23T17:55:00+00:00
- Closed at: 2017-12-26T12:24:24+00:00
