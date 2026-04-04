---
title: 'monero-wallet-cli + ledger Wrong Device Status : SW=6930 (EXPECT=9000, MASK=ffff)'
source_url: https://github.com/monero-project/monero/issues/6123
author: sorinsrn7
assignees: []
labels: []
created_at: '2019-11-11T21:42:39+00:00'
updated_at: '2019-11-12T19:46:07+00:00'
type: issue
status: closed
closed_at: '2019-11-12T19:46:07+00:00'
---

# Original Description
I am unable to open wallet using ledger nano S.
OS: Arch linux (`5.3.8-arch1-1`)
Ledger Monero App version: `1.3.2` I tried with `1.3.1` as well.

```sh
$ monero-wallet-cli --version
Monero 'Carbon Chamaeleon' (v0.15.0.0-release)
```
The error is:
```sh
Error: failed to load wallet: Wrong Device Status : SW=6930 (EXPECT=9000, MASK=ffff)
```



# Discussion History
## xiphon | 2019-11-11T21:49:07+00:00
The latest available Ledger Monero app supports only "0.14.1.0", "0.14.1.2" Monero versions.

https://github.com/LedgerHQ/ledger-app-monero/blob/0be8f379222e4a6d6f06b1150c926f53e68472b6/src/monero_init.c#L160

Related: https://github.com/LedgerHQ/ledger-app-monero/issues/43

## dEBRUYNE-1 | 2019-11-11T22:10:56+00:00
v0.15.0.0 requires Ledger Monero App v1.4, which should be out this week. See:

https://www.reddit.com/r/Monero/comments/dtt2j3/cli_v01500_carbon_chamaeleon_released/f70qywl/?context=3

# Action History
- Created by: sorinsrn7 | 2019-11-11T21:42:39+00:00
- Closed at: 2019-11-12T19:46:07+00:00
