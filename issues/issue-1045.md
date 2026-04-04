---
title: '[Feature Request] Please make ''exit'' and ''logout'' protected keywords in
  simplewallet.'
source_url: https://github.com/monero-project/monero/issues/1045
author: ghost
assignees: []
labels: []
created_at: '2016-09-03T23:25:36+00:00'
updated_at: '2016-09-25T03:39:21+00:00'
type: issue
status: closed
closed_at: '2016-09-25T03:39:21+00:00'
---

# Original Description
Please make `exit` and `logout` protected keywords in simplewallet.

At present the wallet tries to create new wallets with these names when one would it expect it to quit immediately.


# Discussion History
## moneromooo-monero | 2016-09-04T06:55:08+00:00
My wallet has never tried to create a wallet named exit. Include details...


## ghost | 2016-09-04T10:26:46+00:00
Type `monero-wallet-cli`, followed by `exit` or `logout`

The wallet doesn't exist, generating new one
password:


## moneromooo-monero | 2016-09-10T16:33:36+00:00
You mean... when it prompts you for a wallet name ? Or am I missing something here ?


## ghost | 2016-09-14T21:43:00+00:00
Sorry @moneromooo-monero, only just seen your comment now. Yes that's right - seems a bit silly that 'exit' or 'logout' should be allowed as wallet names.


## moneromooo-monero | 2016-09-18T09:07:54+00:00
Makes sense to me. The only exceptions to names would be attempts to exploit something, or an empty string (which I don't think is tested for right now). I don't think there should be any attempt to have a list of names we decide we won't name wallets after. If you decide you changed your mind and don't want to create a wallet after all, just ^C.


## ghost | 2016-09-18T21:48:35+00:00
So is there any chance of this being implemented (including a test for 'no name') or should I close this?


## moneromooo-monero | 2016-09-21T20:19:33+00:00
As far as I'm concerned, this will not get in. Empty string, at a push. But maybe someone else will have a different opinion.


# Action History
- Created by: ghost | 2016-09-03T23:25:36+00:00
- Closed at: 2016-09-25T03:39:21+00:00
