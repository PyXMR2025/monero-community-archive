---
title: Sending with Ledger too many inputs timeout
source_url: https://github.com/monero-project/monero/issues/4734
author: Zarkoob
assignees: []
labels: []
created_at: '2018-10-27T02:14:44+00:00'
updated_at: '2021-08-13T04:33:46+00:00'
type: issue
status: closed
closed_at: '2021-08-13T04:33:46+00:00'
---

# Original Description
I'm trying to send with the CLI Monero 'Beryllium Bullet' (v0.13.0.4-release) and I think I have too many inputs for the current timeout as on my ledger it displays:
`Monero: 45f7fds!`
forever when sending...

The command line interface has been issued the command (shorted for privacy etc):
`transfer wallet_address amount`

If I'm sending around 1 XMR or less then it works fine every time. But anything over 4-5 then then wallet will get stuck with the last entry and hang and Ledger shows above.

Here is the last part of the wallet file log. I'm not sure what parts of the CLI wallet file log I need to provide? A lot looks to be very sensitive info. However I think below is here in the log it takes over 2 mins to make the transaction:

```
2018-10-27 02:00:59.382             0x1044e95c0        INFO    perf    src/common/perf_timer.cpp:140   PERF    80266      PROVE_step4
2018-10-27 02:04:10.333             0x1044e95c0        INFO    construct_tx    src/cryptonote_core/cryptonote_tx_utils.cpp:599 transaction_created: <66gcsmfj624a
```

It seems to take too long to go from the Prove step to transaction created. 

# Discussion History
## iDunk5400 | 2018-10-27T09:06:09+00:00
Try increasing the timeout [here](https://github.com/monero-project/monero/blob/master/src/device/device_ledger.cpp#L179) and see if it works.

## Zarkoob | 2018-10-27T09:07:33+00:00
Yes I was working with support on IRC and we tested that and about a 6 min increase appears to work. 

## selsta | 2021-08-13T04:33:46+00:00
#4918

# Action History
- Created by: Zarkoob | 2018-10-27T02:14:44+00:00
- Closed at: 2021-08-13T04:33:46+00:00
