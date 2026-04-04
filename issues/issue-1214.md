---
title: monero-wallet-cli asks for input when restoring deterministic password, when
  data is supplied in command invocation
source_url: https://github.com/monero-project/monero/issues/1214
author: athanclark
assignees: []
labels:
- bug
created_at: '2016-10-12T22:53:19+00:00'
updated_at: '2018-01-08T12:32:34+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
If you try something like the following:

``` bash
$ monero-wallet-cli --wallet-file ~/.moneybit/wallets/foo --restore-deterministic-wallet --password="asdf" --electrum-seed="gypsy annoyed renting delayed object ostrich vinegar suffice enigma excess paradise five ruling ulcers upon gotten eskimos unquoted plotting cinema jamming bimonthly skulls sleepless delayed" --restore-height=0
```

`monero-wallet-cli` will still ask for input regarding what block height should be for restoration.


# Discussion History
## ghost | 2016-10-12T23:35:51+00:00
Hah. Interesting - it's because there's a comparison for `!m_restore_height` on line `1317` of `simplewallet.cpp`, meaning that _any_ value other than `0` will result in the expected behaviour...

I guess we could add a test for zero but how often are people going to ask for restore height to be zero? Also...it's a little tricky because the restore height is an unsigned int meaning it's not possible to just pre-initialise it at -1 and wait for user input


## ghost | 2016-10-13T00:08:07+00:00
@moneromooo-monero or @fluffypony do you know what the checks from line 1609-1616 in `simplewallet.cpp` are meant to accomplish?

It seems to read:
If we're creating a new wallet, set refresh from block height 0 (done in a very convoluted way)
But if we have a restore height, refresh from the height supplied

I don't like `if`/`if-else` statements where the two variables are independent and not all combinations are caught, and the entire purpose of the function is to create a new wallet, already abrogating the need for the first `if`


## ghost | 2016-10-17T21:26:24+00:00
Also, see #759 


## dEBRUYNE-1 | 2018-01-08T12:28:49+00:00
+bug

# Action History
- Created by: athanclark | 2016-10-12T22:53:19+00:00
