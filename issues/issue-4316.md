---
title: monero-wallet-rpc does not appear to store the tx private keys by default
source_url: https://github.com/monero-project/monero/issues/4316
author: plavirudar
assignees: []
labels: []
created_at: '2018-08-30T03:55:00+00:00'
updated_at: '2018-08-31T14:45:12+00:00'
type: issue
status: closed
closed_at: '2018-08-31T14:17:41+00:00'
---

# Original Description
As a result of the title, it would therefore appear that a user who is using `monero-wallet-rpc` to send transactions and does not manually and explicitly enable the `get_tx_keys` option in the `sweep_all` or `transfer` methods would lose all of their tx private keys and therefore will not be able to trustlessly prove that they have sent a payment using a block explorer or wallet tool. 

When I look at the RPC wallet itself, the data does appear to still be stored within the wallet somewhere, since the RPC method `get_transfer_by_txid` does in fact decode the destinations, payment_id, amount and fee. I am however also unable to retrieve the tx private key in order to prove payment. 

Is there a way to retrieve the tx private key from a transaction sent by `monero-wallet-rpc` without the option `get_tx_keys` enabled? If not, will it be possible to enable this option by default to prevent users from irretrievably losing the tx private key? 

# Discussion History
## moneromooo-monero | 2018-08-30T12:03:28+00:00
Works for me. Did you kill monero-rpc-wallet without saving after transfer ?

## plavirudar | 2018-08-30T16:40:01+00:00
@moneromooo-monero I had shut down with ctrl-c (not killed) `monero-wallet-rpc` after my transactions in an attempt to retrieve the key from `monero-wallet-cli`, since there was no apparent way to retrieve it from `monero-wallet-rpc`.

When running `get_tx_key` in `monero-wallet-cli`, the function fails with the error message `no tx keys found for this txid`

May I ask what method you used to retrieve the tx private key? 

## moneromooo-monero | 2018-08-30T19:09:15+00:00
The get_tx_key RPc.

## jtgrassie | 2018-08-30T19:09:34+00:00
@plavirudar `get_tx_key` is an input parameter for the wallet RPC method `transfer`. Part of the response (if get_tx_key is set to true) is the tx_key. If you then wanted to check this tx in the wallet cli, you would use `check_tx_key <txid> <txkey> <address>`.

## moneromooo-monero | 2018-08-30T22:34:27+00:00
I've also tried with monero-wallet-cli after exiting monero-wallet-rpc, and I also see the tx key (with the get_tx_key command).


## plavirudar | 2018-08-31T14:17:41+00:00
@jtgrassie Yes, my point is that the parameter is set to `false` by default, and does not return the key unless it's explicitly set to `true`, as I have now done. 

@moneromooo-monero Thanks for the update, I have tried the RPC call `get_tx_key` and it does work on the RPC wallet to retrieve the previously assumed lost tx private key. I was unable to find it and assumed such a RPC call did not exist as it was not part of the [official documentation](https://getmonero.org/resources/developer-guides/wallet-rpc.html). It appears that an update to the docs is already in the works here https://github.com/monero-project/monero-site/pull/854

I had to try a couple of guesses to the param names (without which they returned `"TX ID has invalid format"`), but the params appeared to be `{"txid":"your_tx_id"}`


# Action History
- Created by: plavirudar | 2018-08-30T03:55:00+00:00
- Closed at: 2018-08-31T14:17:41+00:00
