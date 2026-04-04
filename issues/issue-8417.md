---
title: 'feature request: Set `store-tx-info` in config file.'
source_url: https://github.com/monero-project/monero/issues/8417
author: zmrocze
assignees: []
labels: []
created_at: '2022-07-04T21:32:40+00:00'
updated_at: '2022-07-21T04:25:22+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
There is an option in `monero-wallet-cli` turned on with 
```
set store-tx-info 1
```

The option is not mentioned in `monero-wallet-cli --help` so I only assume it can't be turned on in config file.
I think it would be good to set this in wallet config. Or - if it already is so - document this in the help. 

Also what is the lifetime of this setting when set in wallet-cli?

Thanks!

# Discussion History
## jtgrassie | 2022-07-21T04:25:22+00:00
It _is_ documented in the wallet (see `help set`). The reason why it wouldn't be a _program_ runtime flag (which can be set via the config file or the flags documented in `--help`), is because anything set with the `set` command is persisted in the _wallet file_ (which answers your question of lifetime). 

# Action History
- Created by: zmrocze | 2022-07-04T21:32:40+00:00
