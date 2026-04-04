---
title: monero-wallet-rpc `--password-file` should be disallowed with `--wallet-dir`
  present
source_url: https://github.com/monero-project/monero/issues/7624
author: da-kami
assignees: []
labels: []
created_at: '2021-03-24T04:08:14+00:00'
updated_at: '2021-09-09T19:14:29+00:00'
type: issue
status: closed
closed_at: '2021-09-09T19:14:29+00:00'
---

# Original Description
The following `monero-wallet-rpc` options are mutually exclusive: `--wallet-file`, `--generate-from-json` or `--wallet-dir`

From my understanding the option `--password-file` (used to provide a wallet's password) should be reserved to starting he RPC with `--wallet-file`. 
However, it is possible to start the RPC with `--wallet-dir` and `--password-file` - when trying to open a wallet with `open_wallet` this error is thrown:

```
2021-03-24 03:45:26.458	E THROW EXCEPTION: tools::error::wallet_internal_error
```

Note that it is irrelevant if the wallet which password file was provided is opened, or any other wallet, the error is always the same.

With both `--wallet-dir` and `--password-file` present, when creating a new wallet with `create_wallet` this error is thrown:

```
2021-03-24 03:59:29.128	E THROW EXCEPTION: tools::error::wallet_internal_error
2021-03-24 03:59:29.132	E [127.0.0.1:59048 INC] Failed to on_create_wallet(): can't specify more than one of --password and --password-file
```

Expected behavior: Fail early by restricting the `--password-file` option be disallowed if `--wallet-dir` is present.


# Discussion History
# Action History
- Created by: da-kami | 2021-03-24T04:08:14+00:00
- Closed at: 2021-09-09T19:14:29+00:00
