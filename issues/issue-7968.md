---
title: 'bug: I have a transaction that is not recognised by the wallet that the transaction
  is spending to'
source_url: https://github.com/monero-project/monero/issues/7968
author: kklash
assignees: []
labels: []
created_at: '2021-09-23T05:47:22+00:00'
updated_at: '2021-12-20T08:02:07+00:00'
type: issue
status: closed
closed_at: '2021-09-28T22:11:33+00:00'
---

# Original Description
I have a transaction that is not recognized by the wallet that the transaction is spending to.

Here is the transaction id: `47edd623ead491914660a78fbb767dc4686b2c2112d385b0aa8795f231e57a2a`
The wallet was created using generate_from_keys.

I was able to decode the transaction using the view-key and wallet-address on https://melo.tools/explorer/mainnet/.

What do I need to provide so we can debug why the monero-wallet-rpc does not recognize the transaction?

# Discussion History
## selsta | 2021-09-23T13:06:47+00:00
Are you using subaddresses?

## kklash | 2021-09-23T14:29:01+00:00
I believe so, yes. 

## kklash | 2021-09-24T15:26:00+00:00
Correction, it is not a subaddress

## selsta | 2021-09-24T15:26:54+00:00
Can you restore the wallet in monero-wallet-cli and check if it shows up?

## kklash | 2021-09-25T23:16:47+00:00
I tried restoring using `--generate-from-keys` and `--generate-from-spend-key` and I get different results

49hpY9TsAcyHpBUwZFrs9QXjkfnz2q3bv1GsUiq1zLND7ikpZLBithzdxC4iPkw998dadYPHyY2YB7US9vdV5efpN8EKZ7g - This is the address the funds are actually in. Restoring using this address, plus spend & view keys discovers the UTXO.

49hpY9TsAcyHpBUwZFrs9QXjkfnz2q3bv1GsUiq1zLND7qPrSrm7yXsFUvFJW3AV38byU2JGMoNfj25ecbXK15di2FiEEsp - this is the address shown by monero-wallet-cli when restoring using only the spend key (`--generate-from-spend-key`). Restoring this address shows nothing. 


## selsta | 2021-09-25T23:29:41+00:00
What if you restore from seed?

## kklash | 2021-09-25T23:38:23+00:00
I don't have the seed for this wallet, only the address + view + spend keys

## selsta | 2021-09-25T23:39:53+00:00
As far as I know you have to use `--generate-from-keys` in this case.

## kklash | 2021-09-28T22:11:33+00:00
Thanks, i tested and confirmed this is working on the latest version of the monero wallet tools. I believe the bug i experienced was caused by a specific version of `monero-wallet-rpc` and has since been fixed

## yokoloho | 2021-12-20T08:02:07+00:00
Hello, I have this problem: https://github.com/comit-network/xmr-btc-swap/issues/879
Could you please hint me how to open correct wallet after my `monero-wallet-rpc` didn't pick monero from atomic swap?
I have `seed.pem`, `<swap-id>` `<swap-id>.keys`, `swap-tool-blockchain-monitoring-wallet.keys` and `swap-tool-blockchain-monitoring-wallet`.  
When I try `monero-wallet-cli --generate-from-keys monero-data/swap-tool-blockchain-monitoring-wallet` it asks me about standard address, which I can't decode from blockchain because it was atomic swap and I don't know private view key.  
And when I open `<swap-id>` or `swap-tool-blockchain-monitoring-wallet` they are empty.

# Action History
- Created by: kklash | 2021-09-23T05:47:22+00:00
- Closed at: 2021-09-28T22:11:33+00:00
