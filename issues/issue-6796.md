---
title: Testnet multisig wallet block height is higher than the daemon's height
source_url: https://github.com/monero-project/monero/issues/6796
author: OxMarco
assignees: []
labels: []
created_at: '2020-09-03T16:30:51+00:00'
updated_at: '2022-02-19T04:07:27+00:00'
type: issue
status: closed
closed_at: '2022-02-19T04:07:27+00:00'
---

# Original Description
When creating a 2/3 set of multisig wallets using _monero-gen-trusted-multisig_ under testnet and later opening the wallets I always get:
`
The wallet's refresh-from-block-height setting is higher than the daemon's height: this may mean your wallet will skip over transactions
`
Moreover, the balance is stuck at 0 despite sending multiple XMR. The daemon was working and synchronised with testnet.

# Discussion History
## dEBRUYNE-1 | 2020-09-03T17:58:17+00:00
By typing `set` in `monero-wallet-cli` you will be able to see the wallet creation height (I think it is called refresh height in the CLI). You will further be able to change it to a value that is in advance of the first transaction to your wallet. The wallet will, thereafter, perform a rescan and your transactions should properly appear. 

For debugging purposes, can you list the initial value of the wallet creation height? 

## OxMarco | 2020-09-03T18:34:05+00:00
The wallet restore height is 1556332. How can I restore the wallet to a safe status and see the incoming transactions?

## moneromooo-monero | 2020-09-03T23:32:38+00:00
set refresh-from-block-height N
rescan_bc

Did you have a daemon up when you created the wallets ? If not, it'll try to guess at the current height using the local time, and this estimation is a bit wonky for testnet as it was forcibly reorged a number of times.

## OxMarco | 2020-09-04T06:12:55+00:00
Yes I had the daemon synchronised and running on testnet. Do I need monero-wallet-rpc too?

## moneromooo-monero | 2020-09-04T22:07:14+00:00
Assuming you did not create the wallets with monero-wallet-rpc, no. The wallet should connect to the daemon to get the current height. Maybe it's buggy then. Can you detail the steps youu took to create those wallets ?

## OxMarco | 2020-09-05T11:17:29+00:00
I think it may be due to the local daemon not working.
As of now 11:15 GMT, this is the info:

```
print_height
1543985
version
0.16.0.3-release
status
Height: 1543985/1543985 (100.0%) on testnet, not mining, net hash 3.51 kH/s, v12, 8(out)+0(in) connections, uptime 1d 0h 15m 10s
```
while the current block height is 1545264

no errors reported in bit _monero.log_

## selsta | 2020-09-05T13:06:49+00:00
@grcasanova Testnet forked to v14, you have to compile latest git master to connect to testnet currently. This happened yesterday so it does not explain your initial issue.

## apertamono | 2020-09-08T09:54:47+00:00
Don't we have a stagenet for this type of testing? The testnet is rather wild because it's used to test protocol development. Either I'm missing something, or you're all too clever to give the obvious answer.

## selsta | 2022-02-19T04:07:27+00:00
We improved the testnet / stagenet height approximation.

# Action History
- Created by: OxMarco | 2020-09-03T16:30:51+00:00
- Closed at: 2022-02-19T04:07:27+00:00
