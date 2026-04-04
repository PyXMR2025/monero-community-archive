---
title: monero-wallet-rpc doesn't exit after --generate-from-json (0.14.1)
source_url: https://github.com/monero-project/monero/issues/5852
author: dginovker
assignees: []
labels: []
created_at: '2019-08-26T01:39:57+00:00'
updated_at: '2020-05-17T14:42:34+00:00'
type: issue
status: closed
closed_at: '2020-05-17T14:42:34+00:00'
---

# Original Description
Example:

Put the following in `wallet.json`, same directory as `monero-wallet-rpc`:
```
{
  "version": 1,
  "filename": "monerowallettestnoexit",
  "scan_from_height": 0,
  "password": "pass",
  "seed": "azure amidst laboratory coexist intended science damp habitat opus liar bubble plus dash females tell threaten sapling cactus fully dosage plywood tolerant seventh slower cactus"
}
```

Execute the following:
`./monero-wallet-rpc --daemon-address opennode.xmr-tw.org:18089 --rpc-bind-port 12388 --generate-from-json wallet.json`

After warnings about duplicate prefixes, I get:
```
2019-08-26 01:35:01.345 I Generating SSL certificate
2019-08-26 01:35:02.114 I Generating SSL certificate
```
And it hangs until `^C`; worth noting it generates the wallet just fine.

# Discussion History
## moneromooo-monero | 2019-08-26T09:31:51+00:00
It's a long timeout in boost ssl handshake. I made an attempt at making this async but it didn't work, so either vtnerd will get to it as he groks boost fairly well or I'll get back to it at some point. In the meantime, use your own node :)

## moneromooo-monero | 2019-10-10T12:49:55+00:00
This should now be fixed after some changes from xiphon.

## normoes | 2019-11-28T12:29:57+00:00
I experience the same in `v0.15.0.1` with the RPC call to `generate_from_keys`.

I cannot, for example, create two wallets that way. The RPC just stops reacting, only a restart helps.

```
curl -i -X POST http://localhost:38083/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"generate_from_keys", "params":{"viewkey":"c007....", "address":"57P8D5z...", "filename": "wallet"}}'
```

My problem was resolved. My fault: #6193

# Action History
- Created by: dginovker | 2019-08-26T01:39:57+00:00
- Closed at: 2020-05-17T14:42:34+00:00
