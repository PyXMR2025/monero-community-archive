---
title: Changing subaddress-lookahead on existing wallet does not result in correct
  blockchain rescan
source_url: https://github.com/monero-project/monero/issues/7364
author: michnovka
assignees: []
labels: []
created_at: '2021-02-01T17:55:49+00:00'
updated_at: '2025-07-10T12:20:55+00:00'
type: issue
status: closed
closed_at: '2025-07-10T12:20:55+00:00'
---

# Original Description
Using latest v0.17.1.9 cli wallet, I had issues that my BTCPay gateway was using larger offsets than the default 200, so I opened the wallet in monero-wallet-cli and used

`set subaddress-lookahead 3:50000`
`rescan_bc`

And this did nothing. The same transactions were found, no missing transactions were actually added.

Afetr restarting wallet few times and rescanning bc few times, I tried to create new wallet from the same seed using

`monero-wallet-cli --restore-deterministic-wallet --subaddress-lookahead 3:50000`

And voila! This did the trick, all the missing transactions were found.

So the issue is that for existing wallet, changing the subaddress-lookahead has no real effect. I confirmed the change is saved properly by typing `set` into wallet-cli, and this did show the value I configured. However, the `rescan_bc` was always rather quick and never found any new transactions.

# Discussion History
## michnovka | 2021-02-01T20:23:46+00:00
I ran `addres new` few times on both accounts, then did `rescan_bc` and this seems to have fixed the issue. however changing the subaddress-lookahead on its own does nothing.

## plowsof | 2025-06-17T18:16:47+00:00
on current master, i did not observe this, it worked as expected. increasing `set subaddress-lookahead` to detect inputs outside of the expanded index range, then `rescan_bc` - outputs are found. the total balance was sanity checked by then deleting the wallet cache to force a full resync with the ~~new larger lookahead and the balance was equal. ~~ *deleting the cache so the default of 200 is used, which was enough to pick up all the outputs to confirm total balance is correct

## plowsof | 2025-06-17T21:00:56+00:00
>changing the subaddress-lookahead on its own does nothing.

i am also seeing this with current master

## plowsof | 2025-06-17T21:14:30+00:00
to play with lookahead / which index the wallet is expanded to, we need 2 wallets, `create_address` output dumped to a file and a small jq script to 'get address index N'. 

create a new wallet with cli, then open it with rpc:

- ```./monero-wallet-rpc --rpc-bind-port 18082 --wallet-file new --daemon-host node3.monerodevs.org:28089 --testnet --disable-rpc-login --password ""```
create addresses / dump output to file: 
- `curl -X POST http://127.0.0.1:18082/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"create_address","params":{"account_index":0,"label":"new-subs","count":1100}}' -H 'Content-Type: application/json' >> index_list.json`
the shell script to parse it: (note the `- 1` - i am matching the idx as displayed from inside the cli e.g. in `address all`
```bash
INDEX=$1
jq -r ".result.addresses[$((INDEX - 1))]" index_list.json
```
- save as `get_index.sh` and `chmod +x` it
- `./get_index.sh 100` etc 
close the rpc wallet / delete the new wallets cache ~ `rm new`.
open `new` and your other wallet with some testnet coins in. lets say you opened the default wallet with 200. 
- `./monero-wallet-cli --wallet-file new --daemon-host node3.monerodevs.org:28089 --password "" --testnet`
- `./get_index.sh 200`
- send coins to this address, and `refresh` in the receiving wallet several times. no output should be detected in pool (note* does not expand lookahead until at least one confirmation)
- `./get_index.sh 199`
- send coins, `refresh` will show an output in the pool.
- confirm `show_transfers all` that index 199 has incoming.


# Action History
- Created by: michnovka | 2021-02-01T17:55:49+00:00
- Closed at: 2025-07-10T12:20:55+00:00
