---
title: sweep_all confirmation doesn't accept enter key
source_url: https://github.com/monero-project/monero/issues/7211
author: w3irdrobot
assignees: []
labels: []
created_at: '2020-12-27T20:16:29+00:00'
updated_at: '2021-10-06T02:41:39+00:00'
type: issue
status: closed
closed_at: '2021-10-06T02:41:38+00:00'
---

# Original Description
When attempting to run `sweep_all`, I am asked to confirm I want to do this. When I press `y` and then hit Enter, It shows `y^M` instead of accepting the input. When I use `^c` to get out of there, I get a seg fault.

```shell
[wallet <redacted>]: sweep_all outputs=3 <redacted>
Wallet password:
Transaction spends more than one very old output. Privacy would be better if they were sent separately.
Spend them now anyway?  (Y/Yes/N/No): y^M^CError: transaction cancelled.
zsh: segmentation fault  monero-wallet-cli --daemon-address opennode.xmr-tw.org:18089 --wallet-file
```

System information:

```shell
➜ uname -srvmpio
Darwin 20.2.0 Darwin Kernel Version 20.2.0: Wed Dec  2 20:39:59 PST 2020; root:xnu-7195.60.75~1/RELEASE_X86_64 x86_64 i386 MacBookPro16,1 Darwin
➜ monero-wallet-cli --version
Monero 'Oxygen Orion' (v0.17.1.7-release)
```

# Discussion History
## moneromooo-monero | 2020-12-27T22:51:55+00:00
Does it work with another shell ?

## w3irdrobot | 2020-12-28T00:56:41+00:00
It does appear to work fine when executed from a bash shell.

## selsta | 2021-10-06T02:41:38+00:00
We don't get any other reports about this so I assume it's some issue with the local environment.

# Action History
- Created by: w3irdrobot | 2020-12-27T20:16:29+00:00
- Closed at: 2021-10-06T02:41:38+00:00
