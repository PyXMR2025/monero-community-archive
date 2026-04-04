---
title: monero-wallet-rpc "create_wallet" method does not generate *.address.txt on
  mainnet
source_url: https://github.com/monero-project/monero/issues/6257
author: dginovker
assignees: []
labels:
- invalid
created_at: '2019-12-20T06:05:53+00:00'
updated_at: '2019-12-20T11:33:47+00:00'
type: issue
status: closed
closed_at: '2019-12-20T11:33:47+00:00'
---

# Original Description
Problem description: I generate wallets from the command line using `create_wallet` from the `monero-wallet-rpc` for one of my services, and it relies on opening the `address.txt` file to get the wallet address. On testnet this works fine, on mainnet the file never gets generated.

Running the Linux CLI 0.15.1, downloaded from [getmonero.org/downloads](https://getmonero.org/downloads). Hash is `8d61f992a7e2dbc3d753470b4928b5bb9134ea14cf6f2973ba11d1600c0ce9ad` (matches).

**Mainnet example:**

Terminal 1:
```
$ ./monero-wallet-rpc --wallet-dir . --rpc-bind-port 9998 --disable-rpc-login
```

Terminal 2:
```
$ curl -X POST http://localhost:9998/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"create_wallet","params":  {"filename":"mainnetwallet","password":"pass","language":"English"}}' -H 'Content-Type: application/json'
$ ls | grep .address.txt
```

No `mainnetwallet.address.txt` is generated.



**Testnet example:**

Terminal 1:
```
$ ./monero-wallet-rpc --wallet-dir . --rpc-bind-port 9998 --disable-rpc-login --testnet
```

Terminal 2:
```
$ curl -X POST http://localhost:9998/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"create_wallet","params":  {"filename":"testnetwallet","password":"pass","language":"English"}}' -H 'Content-Type: application/json'
$ ls | grep .address.txt
testnetwallet.address.txt
```

`testnetwallet.address.txt` is generated.

# Discussion History
## selsta | 2019-12-20T06:13:02+00:00
AFAIK this is intended behaviour, most likely for privacy reasons. Use https://web.getmonero.org/resources/developer-guides/wallet-rpc.html#get_address to get the address or save the address + wallet name in a separate db.

## moneromooo-monero | 2019-12-20T11:29:15+00:00
Intended. You can use --create-address-file if you want it.

+invalid

# Action History
- Created by: dginovker | 2019-12-20T06:05:53+00:00
- Closed at: 2019-12-20T11:33:47+00:00
