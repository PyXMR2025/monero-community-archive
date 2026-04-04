---
title: '[Feature suggestion] --wallet-dir flag'
source_url: https://github.com/monero-project/monero/issues/7674
author: selsta
assignees: []
labels: []
created_at: '2021-04-19T20:19:08+00:00'
updated_at: '2021-09-06T16:08:45+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
From IRC

```
22:11 <clavi> can I set a wallet directory for monero-wallet-cli?
22:11 <clavi> the config file only lets me set a single wallet
22:13 <clavi> I want to be able to run something like "monerocli <walletname>" from any directory
22:13 <clavi> without typing the full paths each time
22:17 <clavi> would be neat to have a "--wallet-dir" option in the CLI config file
```

# Discussion History
## trasherdk | 2021-04-21T05:55:54+00:00
Or a search path for `config-file` if only a filename is given.

Something like `./filename` `~/.bitmonero/filename` `.....`

## mj-xmr | 2021-07-06T05:23:34+00:00
> Or a search path for `config-file` if only a filename is given.
> 
> Something like `./filename` `~/.bitmonero/filename` `.....`

Makes sense, although `--wallet-dir` is quite a known standard originating from BTC and all its forks.

## hyc | 2021-07-06T10:52:23+00:00
This option exists for monero-wallet-rpc already. Should be easy enough to add to monero-wallet-cli.

Would be even easier, to avoid duplication of effort, to undo the split and consolidate both of the programs back into a single executable.

## ghost | 2021-09-06T16:08:45+00:00
I think it'd be easier if it was an environment variable; e.g. `MONERO_WALLET_DIR=.local/share/monero monero-wallet-cli`, as it could be set in e.g. your `.zshrc` or `.bashrc`. I suppose having both could work though

# Action History
- Created by: selsta | 2021-04-19T20:19:08+00:00
