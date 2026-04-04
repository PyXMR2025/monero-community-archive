---
title: Delayed transaction broadcast with --tx-proxy
source_url: https://github.com/monero-project/monero/issues/7223
author: Ashaman-
assignees: []
labels: []
created_at: '2020-12-29T06:35:01+00:00'
updated_at: '2022-07-19T19:58:27+00:00'
type: issue
status: closed
closed_at: '2022-07-19T19:58:16+00:00'
---

# Original Description
A transaction sent with a daemon that was just launched with i2pzero --tx-proxy flags will fail to broadcast if the node has not yet made connections to any other nodes over i2p. While I've had this happen a few times, it was never a problem until today wnen it did eventually broadcast - hours later, well after the merchant invoice it was for had expired. I'm not sure what eventually dislodged it and got it broadcast, the only event I can attribute it to was my triggering of 'systemctl restart monerod'

It seems like better handling of tx-proxy transactions is needed rather urgently. Perhaps some kind of detection to identify failed broadcasts and rebroadcast them, along with the option to automatically drop any tx that has failed to broadcast for a user defined quantity of minutes.

# Discussion History
## ghost | 2021-01-04T00:14:00+00:00
See #6938. A workaround for this issue is adding the `disable_noise` parameter to the `--tx-proxy` option.

## xanoni | 2021-08-16T03:57:17+00:00
Would this also happen if the node had two `--tx-proxy` flags, one for Tor and one for I2P?

## selsta | 2022-07-19T19:58:16+00:00
Should be solved by #8326, the re-relay logic was broken.

# Action History
- Created by: Ashaman- | 2020-12-29T06:35:01+00:00
- Closed at: 2022-07-19T19:58:16+00:00
