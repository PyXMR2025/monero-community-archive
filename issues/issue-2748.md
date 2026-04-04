---
title: Disguise password length in 'Wallet password:' prompt
source_url: https://github.com/monero-project/monero/issues/2748
author: leonklingele
assignees: []
labels: []
created_at: '2017-11-03T02:21:44+00:00'
updated_at: '2017-11-14T13:35:55+00:00'
type: issue
status: closed
closed_at: '2017-11-14T13:35:55+00:00'
---

# Original Description
```sh
./monero-wallet-cli
Monero 'Helium Hydra' (v0.11.1.0-release)
Logging to /path/to/monero-wallet-cli.log
Wallet password: **** # <-- Leaks password length
```

Better use a suitable readline prompt instead.

# Discussion History
## iamsmooth | 2017-11-04T19:45:42+00:00
It looks like you removed backspace handling altogether in the second commit. This is arguably okay (requiring the user to type the password without any errors) but should at least be noted in the commit title/comment.

## leonklingele | 2017-11-04T20:22:24+00:00
> you removed backspace handling altogether in the second commit

Correct, but that change got reverted again a few minutes later because it didn't work out as expected.
The most current version can be found here: https://github.com/monero-project/monero/pull/2749/files

# Action History
- Created by: leonklingele | 2017-11-03T02:21:44+00:00
- Closed at: 2017-11-14T13:35:55+00:00
