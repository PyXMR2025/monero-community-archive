---
title: monero-wallet-cli refresh doesn't work
source_url: https://github.com/monero-project/monero/issues/6217
author: spartucus
assignees: []
labels: []
created_at: '2019-12-05T09:51:16+00:00'
updated_at: '2019-12-10T02:50:35+00:00'
type: issue
status: closed
closed_at: '2019-12-10T02:50:34+00:00'
---

# Original Description
This is local test.
 
* Environment: 
  MacOS, Ubuntu 16.04 
* version:
 newer than v0.15.0.1 411f1b0ee30f1d424621eb856841dc82d2f161c2

* How to reproduce:
  1. start monero-wallet-cli with `--testnet`, and create a new wallet, save the address (primary account), we call it `NEW_CREATED_ADDRESS`.
  2. start monerod with `--offline`, `--testnet`, `--fixed-difficulty 50` and `--start-mining NEW_CREATED_ADDRESS`.
  3. use `start_mining` daemon-rpc to start mining, don't forget, use NEW_CREATED_ADDRESS in `miner_address ` field.
  4. after some block mined, login monero-wallet-cli, and refresh, you see no balance, 0 money.
  5. however, when you use generate-from-spend-key to restore wallet, the balance is display well, all money is there. 
  6. monero-wallet-rpc does same




# Discussion History
## dEBRUYNE-1 | 2019-12-05T11:48:00+00:00
What is the wallet creation height of the initial wallet? You can check by typing `set`. 

## spartucus | 2019-12-06T01:17:12+00:00
Hi @dEBRUYNE-1 , here is output:
```
[wallet 9wzQgc]: refresh
Starting refresh...
Refresh done, blocks received: 0                                
Currently selected account: [0] Primary account
Tag: (No tag assigned)
Balance: 0.000000000000, unlocked balance: 0.000000000000
[wallet 9wzQgc]: set
seed = English
always-confirm-transfers = 1
print-ring-members = 0
store-tx-info = 1
default-ring-size = 0
auto-refresh = 1
refresh-type = optimize-coinbase
priority = 0 (default)
confirm-missing-payment-id = 1
ask-password = 2 (decrypt)
unit = monero
min-outputs-count = 0
min-outputs-value = 0.000000000000
merge-destinations = 0
confirm-backlog = 1
confirm-backlog-threshold = 0
confirm-export-overwrite = 1
refresh-from-block-height = 1359503
auto-low-priority = 1
segregate-pre-fork-outputs = 1
key-reuse-mitigation2 = 1
subaddress-lookahead = 50:200
segregation-height = 0
ignore-fractional-outputs = 1
track-uses = 0
setup-background-mining = yes (set this to support the network and to get a chance to receive new monero)
device_name = 
[wallet 9wzQgc]: bc_height
264
[wallet 9wzQgc]: 

```

## moneromooo-monero | 2019-12-06T13:15:27+00:00
Is 1359503 later than your tx's block ? Is that, that is why. Since you created your wallet while moenrod was not running, the wallet could not get the current height, and had to guess. For testnet, the guess is bad since testnet was reorg'd away multiple times. I think we might be better off removing this for testnet, or at least making it much more forgiving.

## spartucus | 2019-12-09T02:39:43+00:00
Hi @moneromooo-monero , as you can see, the whole height for now is just 264, so yes, 1359503 is later than tx's block.

## moneromooo-monero | 2019-12-09T16:10:41+00:00
https://github.com/monero-project/monero/pull/6224 will help in cases like this.

## spartucus | 2019-12-10T01:38:33+00:00
![image](https://user-images.githubusercontent.com/6071887/70487519-9a571580-1b30-11ea-9f92-79f99b0b53a0.png)
 It warns.
But in this case, are there any chances that we can set `refresh-from-block-height` to a lower height, like 0?

## moneromooo-monero | 2019-12-10T02:32:40+00:00
Yes, this will fix it. Better to set it to something near when you created the wallet though, for speed.

## spartucus | 2019-12-10T02:50:34+00:00
Ok, in my case, set `refresh-from-block-height` to `0`, and refresh works well.

# Action History
- Created by: spartucus | 2019-12-05T09:51:16+00:00
- Closed at: 2019-12-10T02:50:34+00:00
