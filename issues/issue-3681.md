---
title: ' monero-wallet-rpc: Created Subadresses won''t be listed after  RPC is restarting'
source_url: https://github.com/monero-project/monero/issues/3681
author: krtschmr
assignees: []
labels: []
created_at: '2018-04-22T08:29:55+00:00'
updated_at: '2018-04-22T09:23:25+00:00'
type: issue
status: closed
closed_at: '2018-04-22T09:23:24+00:00'
---

# Original Description
- opened RPC and simultanously the CLI.
- create subadresses `create_address`  on cli and rpc
- closed  cli
- closed  rpc
- opened RPC
- `get_adddress` will only return 4 addresses
- create more addresses `create_address`
- close / restart RPC
- `get_adddress` will only return 4 addresses


it seems that the `account_index` isn't correctly written when we restart the RPC.

is there any possibility to generate a subaddress for given `i` ? if customer  with ID 18934 signs up, we can automatically generate him his subaddress. if the RPC would be restarted and then the index is wrong, we would generate a subadress and get i=3 (which belongs to customerID 3) then we need to run the `create_address` command just 18931 times to finally arrive at index 18934. 

in case this is a bug and not just a random mistake i produced because i kept CLI open, the RPC can't be used in production mode for subaddresses

# Discussion History
## krtschmr | 2018-04-22T08:54:21+00:00
i can replicate it with my ruby gem which simply wraps curl commands

```
....
2.4.1 :011 > Monero::Wallet.create_address 
 => {"address"=>"BbA5UF5yNd7CG13bMzA2XX8SkHbqUS29HDVWeQ1N6BSNVPccy39EfmWCoBndpd2rDRdAQkXfJmekFMP5eGjKJjbyLQZ2Zb8", "address_index"=>10} 
2.4.1 :012 > Monero::Wallet.create_address
 => {"address"=>"BajoJBmAN6EWsPpHqa6EzHAyiQ2XbRYt2U1LKnaHHqn5Nm4LVJUJEnBPGTnjS3xxZXGULbnrB57etVU1et1Kn8E47xK4RAe", "address_index"=>11} 

```

now i close the RPC Client and start it again, then load the wallet

```

2.4.1 :013 > Monero::Wallet.create_address 
RuntimeError: No wallet file | code: -13
2.4.1 :014 > Monero::Wallet.open_wallet "testnet"
 => # true

```
generate more addresses and however, it starts at index 5 again
```

2.4.1 :015 > Monero::Wallet.create_address 
 => {"address"=>"BdVvQdMCQZnMxCqm8w8dBhETzpiFbgMiF4RNPiTxWFxxCuTNiey3aBkKKQTed8DRCNGgEWzTdcpKVJSPp5GkrjoVUKdHL8F", "address_index"=>5} 
2.4.1 :017 > Monero::Wallet.create_address
 => {"address"=>"Bbw7yscBgYwUxF4soUSpDdZFdFpReTgNeSmwtZqNMVDvfV74oTKWcjQYjMvNRg5UvojUnLWvBYt4mJnoseTX9dyL1qhERjL", "address_index"=>6} 

```

## krtschmr | 2018-04-22T09:23:24+00:00
might be problem with my windows shell. propably ^C didn't trigger correct so the index wasn't written.

# Action History
- Created by: krtschmr | 2018-04-22T08:29:55+00:00
- Closed at: 2018-04-22T09:23:24+00:00
