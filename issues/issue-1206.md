---
title: Default-Mixin set to 0 by default but behaving like 4
source_url: https://github.com/monero-project/monero/issues/1206
author: RandomRun
assignees: []
labels: []
created_at: '2016-10-11T05:10:01+00:00'
updated_at: '2017-10-15T18:06:21+00:00'
type: issue
status: closed
closed_at: '2017-10-15T18:06:21+00:00'
---

# Original Description
I just tried this in my wallet (latest version, testnet). I ran `set`, and it printed `default-mixin = 0`. So I set it to a few different values to check that indeed only 4 and higher are accepted. Then I tried returning to the original setup by doing `set default-mixin = 0`, but after that, after I enter `set` it prints `default-mixin = 4`, like it is the same thing. It was working fine before I started playing with that, so I think even though it was set to 0 before, it was actually sending transactions with mixin 4.

(This is my first try with using Github. Please let me know if there is a specific form for these issues that I should observe.)


# Discussion History
## moneromooo-monero | 2016-10-11T19:03:26+00:00
0 means default, and the default is 4, but the default might change later, so it's a bug, yes. Thanks.


## RandomRun | 2016-10-12T00:23:39+00:00
Maybe this is a basic question, but if the wallet is not reading the default mixin value directly from the default-mixin variable, where does it get the value of 4, after reading 0 from the variable?


## ghost | 2016-10-12T00:40:02+00:00
I tried to check this out myself when I saw the default setting was 0 in wallet2.cpp - it looks like default mixin is set in a number of different places:

`api/wallet.cpp` sets `static const size_t DEFAULT_MIXIN = 4;` on line 48

`simplewallet/simplewallet.cpp` defines `DEFAULT_MIX 4` on line 78

`wallet/wallet2.h` sets `default_mixin(0)` in the public and private declarations of the `wallet2` class
`wallet/wallet2.cpp` sets `default_mixin` to 0 on line 1519

Having played around with the defaults elsewhere (#1185) I think that we should probably define defaults in just one location - but this is a job for some point in the future.

I'll try to fix the behaviour you've seen within the bounds of the existing code soon.


## moneromooo-monero | 2017-10-03T10:48:12+00:00
Better late than never: https://github.com/monero-project/monero/pull/2569

> Maybe this is a basic question, but if the wallet is not reading the default mixin value directly from the
> default-mixin variable, where does it get the value of 4, after reading 0 from the variable?

The wallet sets its default when it's given 0 as mixin. This is done in transfer_main:

      fake_outs_count = m_wallet->default_mixin();
      if (fake_outs_count == 0)
        fake_outs_count = DEFAULT_MIX;


## moneromooo-monero | 2017-10-15T17:58:17+00:00
+resolved

# Action History
- Created by: RandomRun | 2016-10-11T05:10:01+00:00
- Closed at: 2017-10-15T18:06:21+00:00
