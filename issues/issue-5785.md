---
title: Mining on Testnet seems to be broken
source_url: https://github.com/monero-project/monero/issues/5785
author: krtschmr
assignees: []
labels: []
created_at: '2019-08-01T05:34:43+00:00'
updated_at: '2019-08-19T15:13:37+00:00'
type: issue
status: closed
closed_at: '2019-08-19T15:13:37+00:00'
---

# Original Description
1. sync daemon `--testnet`
2. create wallet with `--testnet` 

3. daemon: `start_mining ADDR` 
-> found several blocks, balance always 0

4. wallet-cli `start_mining` 
-> found several blocks, balance always 0


is this just me?


# Discussion History
## dEBRUYNE-1 | 2019-08-01T06:29:53+00:00
Did you wait until the blocks matured (i.e. 60 blocks)? 

## krtschmr | 2019-08-01T09:14:50+00:00
absolutely. still no balance. it's >150 blocks

## trasherdk | 2019-08-01T11:57:30+00:00
I'm mining on testnet, no problems.
```
Height 1268005, txid <3b983d6124bd427de4885d25e8d28cd137d59b181e2c9a4445ae90d81d04a0fb>, 10.803137894759, idx 0/0
Height 1268011, txid <4ceab180eba2fba9df322c5d84d4be44845482bffeadf1a1aa54ec6b712d73b3>, 5.401480538990, idx 0/0
Height 1268017, txid <781ec3a9ff63ee9f31c06cc42994420673cd5c262d0aef16bd173ce757408715>, 27.007114226205, idx 0/0
Height 1268024, txid <61a3da83ad669b58a813b75d8e560f843dce899a5a7a77ac6ae28db19ffac880>, 10.802724122744, idx 0/0
[wallet 9zwQfv]: balance        
Currently selected account: [0] Primary account
Tag: (No tag assigned)
Balance: 17743.621771749103, unlocked balance: 17732.819047626359 (6 block(s) to unlock)
```
![image](https://user-images.githubusercontent.com/5003891/62291444-29bb3080-b48e-11e9-8ea1-d7788093937b.png)


## dEBRUYNE-1 | 2019-08-01T12:46:48+00:00
@krtschmr - Can you check what the wallet creation height is (use `set`)? 

## krtschmr | 2019-08-01T13:01:13+00:00
@dEBRUYNE-1 it's all from today in the morning. so 12 hours ago. 
i don't have access to it right now can tell you tomorrow morning (so in 12 hours)

## moneromooo-monero | 2019-08-19T15:11:50+00:00
It's very likely your creation height is bogus as dEBRUYNE said.

## krtschmr | 2019-08-19T15:13:37+00:00
yes. this was the same issue.

# Action History
- Created by: krtschmr | 2019-08-01T05:34:43+00:00
- Closed at: 2019-08-19T15:13:37+00:00
