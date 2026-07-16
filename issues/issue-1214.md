---
title: monero-wallet-cli asks for input when restoring deterministic password, when
  data is supplied in command invocation
source_url: https://github.com/monero-project/monero/issues/1214
author: athanclark
assignees: []
labels:
- bug
created_at: '2016-10-12T22:53:19+00:00'
updated_at: '2026-07-15T17:03:09+00:00'
type: issue
status: closed
closed_at: '2026-07-15T17:03:09+00:00'
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

## munzzyy | 2026-07-15T03:36:55+00:00
This looks like it was already fixed as a side effect of 60b35c91b ("Add --restore-date param", 2018-12-14).

Current simplewallet.cpp checks `command_line::is_arg_defaulted(vm, arg_restore_height)` (in the `m_restoring` block around line 4327) instead of the old `!m_restore_height` truthiness check from 2016. `is_arg_defaulted` returns `vm[arg.name].defaulted()` (src/common/command_line.h:264), which boost sets to false whenever the user actually supplied the option on the command line, no matter what value they passed - so `--restore-height=0` is now correctly distinguished from not passing `--restore-height` at all.

I traced the original repro (`--restore-deterministic-wallet ... --restore-height=0`) through the current code by hand and can't find a path that still hits the interactive prompt. Might be worth closing unless there's some other invocation still tripping the old behavior.


## selsta | 2026-07-15T17:03:09+00:00
@munzzyy thank you for looking into this

# Action History
- Created by: athanclark | 2016-10-12T22:53:19+00:00
- Closed at: 2026-07-15T17:03:09+00:00
