---
title: '[bug] wallet-rpc exchange multisig_keys input'
source_url: https://github.com/monero-project/monero-site/issues/2172
author: creating2morrow
assignees: []
labels: []
created_at: '2023-05-29T09:51:13+00:00'
updated_at: '2023-05-29T09:51:13+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
In the wallet rpc docs the input `multisig_info` is shown to be a string but it should be a json array

actual:

* multisig_info - string;

```bash
curl http://localhost:18082/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"exchange_multisig_keys","params":{"password":"","multisig_info":"MultisigxV2R1hSyd7Zdx5A92zWF7E9487XQg8zZRDYM6c9aNfEShmCKoUx9ftccXZvH9cRcadd5veh6mwk9sXuGzWZRo57MdvSkJi3ABLt8wZPv8FTkBqVDVcgUdXm4tS81HdJ5WQXboQJJQQd5JKoySKJ4S9xHGojL2i3VUvbWAyduaWGjMK4hrLQA1"}}' -H 'Content-Type: application/json'
```

expected:

* multisig_info - array of string;

```bash
curl http://localhost:18082/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"exchange_multisig_keys","params":{"password":"","multisig_info":["MultisigxV2R1hSyd7Zdx5A92zWF7E9487XQg8zZRDYM6c9aNfEShmCKoUx9ftccXZvH9cRcadd5veh6mwk9sXuGzWZRo57MdvSkJi3ABLt8wZPv8FTkBqVDVcgUdXm4tS81HdJ5WQXboQJJQQd5JKoySKJ4S9xHGojL2i3VUvbWAyduaWGjMK4hrLQA1"]}}' -H 'Content-Type: application/json'
```

Docs
https://www.getmonero.org/resources/developer-guides/wallet-rpc.html#exchange_multisig_keys

monero source:
https://github.com/monero-project/monero/blob/master/src/wallet/wallet_rpc_server_commands_defs.h#L2537


# Discussion History
# Action History
- Created by: creating2morrow | 2023-05-29T09:51:13+00:00
