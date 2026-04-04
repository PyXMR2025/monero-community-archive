---
title: 'Error: internal error: histogram reports more recent outs than outs for 0'
source_url: https://github.com/monero-project/monero/issues/4121
author: tobtoht
assignees: []
labels:
- invalid
created_at: '2018-07-09T17:54:36+00:00'
updated_at: '2019-08-27T16:25:55+00:00'
type: issue
status: closed
closed_at: '2019-08-27T16:25:55+00:00'
---

# Original Description
Operating system: Tails
Wallet: monero-linux-x64-v0.12.2.0
Remote node: xmrag4hf5xlabmob.onion:18081

Restored wallet from pre-fork seed. Wallet refreshed successfully.

When trying to send a transaction:
"Error: internal error: histogram reports more recent outs than outs for 0"

# Discussion History
## moneromooo-monero | 2018-07-11T14:10:59+00:00
Add --log-level 2, and post the relevant part of the log, showing the counts.

## tobtoht | 2018-07-11T23:19:37+00:00
I'm posting this issue on someone else's behalf.
I suggested they try CLI 12.0, which worked fine without issue. I will contact them and ask if they can provide the log.

## tobtoht | 2018-07-12T21:57:22+00:00
Just had a second person report this issue. Same conditions. Asking them for logs as well.

Edit: they where upgrading from v0.11.1.0 to v.0.12.3.0

## gigafunk | 2018-07-17T02:58:33+00:00
edit

I had the 12.0.0 gui version. For some reason the official [64 bit link](https://getmonero.org/downloads/) was giving me the wrong package version. With firefox. If I go to the site with a new private browser window, then it gives me the 12.2.0 version, so its a cookie or something in my web browser cache on my local machine.  Same web address and everything.  Just posting in case it helps someone.


## stoffu | 2018-07-20T04:41:58+00:00
Some easy things to try:

- Disable the key-reuse mitigation schemes by doing `set segregate-pre-fork-outputs 0` and `set key-reuse-mitigation2 0` in `monero-wallet-cli`

- Use different versions of `monerod` (0.12.x)

If these things make differences, it hints where the problem lies.


## dselyuzhitskiy | 2018-07-26T06:33:55+00:00
We had the same issue, there was only one error  on monero wallet log

`ERROR	wallet.wallet2	src/wallet/wallet2.cpp:6024	num_recent_outs > num_outs. THROW EXCEPTION: error::wallet_internal_error`

`WARN net.http	src/wallet/wallet_errors.h:794	/DISTRIBUTION-BUILD/src/wallet/wallet2.cpp:6024:N5tools5error21wallet_internal_errorE: histogram reports more recent outs than outs for 0
`

Monero daemon 0.12.1.0
Monero wallet 0.12.1.0

## moneromooo-monero | 2018-08-16T20:32:24+00:00
As the second comment says. Without logs, I can't tell what's wrong.

## moneromooo-monero | 2018-09-26T09:14:13+00:00
All the cases I've seen logs for before were when using mismatched node and wallet version. If nothing else comes in with matching versions, I'll close this later since everything will be using compatible versions very soon anyway due to the coming update.

## moneromooo-monero | 2019-08-27T15:58:04+00:00
Use matched wallet+daemon versions.

+invalid

# Action History
- Created by: tobtoht | 2018-07-09T17:54:36+00:00
- Closed at: 2019-08-27T16:25:55+00:00
