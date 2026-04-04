---
title: 'Getting this error, rpc-client-secret-key: RPC client secret key should be
  32 byte in hex format'
source_url: https://github.com/monero-project/monero/issues/8150
author: TimyIsCool
assignees: []
labels: []
created_at: '2022-01-18T22:35:50+00:00'
updated_at: '2022-02-18T22:57:18+00:00'
type: issue
status: closed
closed_at: '2022-02-18T22:57:18+00:00'
---

# Original Description
Hey there, Im trying to setup rpc but im getting this error: rpc-client-secret-key: RPC client secret key should be 32 byte in hex format
How would i fix this?

Also what is the blockchain size?

# Discussion History
## reemuru | 2022-01-21T19:13:13+00:00
@TimyIsCool I think this error message is about rpc payments key. If you want to pass `--rpc-client-secret-key` for RPC payments it must be hex format and 32 bytes. So if you did something like `--rpc-client-secret-key 123` that would yield an error. The key can be acquired from `monero-wallet-cli` by running `rpc_payment_info`

```bash
RPC client ID: <abc...>
RPC client secret key: <abc...>
```

There are more details in the commit message 2899379791b7542e4eb920b5d9d58cf232806937

## reemuru | 2022-01-21T19:19:43+00:00
> Also what is the blockchain size?

mainnet - 123G
stagenet - 9G

## TimyIsCool | 2022-01-22T22:22:30+00:00
> @TimyIsCool I think this error message is about rpc payments key. If you want to pass `--rpc-client-secret-key` for RPC payments it must be hex format and 32 bytes. So if you did something like `--rpc-client-secret-key 123` that would yield an error. The key can be acquired from `monero-wallet-cli` by running `rpc_payment_info`
> 
> ```shell
> RPC client ID: <abc...>
> RPC client secret key: <abc...>
> ```
> 
> There are more details in the commit message [2899379](https://github.com/monero-project/monero/commit/2899379791b7542e4eb920b5d9d58cf232806937)

Thank you, what would the config file look like for monero-wallet-rpc?

## reemuru | 2022-01-22T22:57:44+00:00
 > Thank you, what would the config file look like for monero-wallet-rpc?

@TimyIsCool  StackExchange would be a better resource for user setup stuff.

https://monero.stackexchange.com/questions/9857/is-there-a-monerod-config-file-to-change-certain-settings-when-you-run-monerod-i

# Action History
- Created by: TimyIsCool | 2022-01-18T22:35:50+00:00
- Closed at: 2022-02-18T22:57:18+00:00
