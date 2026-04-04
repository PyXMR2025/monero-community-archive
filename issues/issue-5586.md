---
title: 'prepare_multisig overwrote used wallet '
source_url: https://github.com/monero-project/monero/issues/5586
author: aaronovz1
assignees: []
labels: []
created_at: '2019-05-29T21:56:30+00:00'
updated_at: '2019-06-06T19:39:28+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Due to a misunderstanding of how wallet RPC works I managed to turn a simple/regular wallet into a multisig wallet. I had two apps simultaneously connected to the same Wallet RPC instance. One app controlled a simple wallet, the other app was working with multisig wallets. In the process, one app called **open_wallet** on the simple wallet, and the other app must have called **prepare_multisig** which to my surprise succeeded in overwriting the simple wallet and turning it into a 2/3 multisig wallet.

I would have expected prepare_multisig/make_multisig to have failed, because the simple wallet had balances and transactions, so should not have been classified as unused.

Is there any way to revert the wallet back to a simple wallet? Am I right in that I would need to separate Wallet RPC instances running so there are no concurrency issues like this?

# Discussion History
## moneromooo-monero | 2019-05-29T22:34:22+00:00
prepare_multisig does not change anything. I assume make_multisig was called. I could add a check for "has it been used before", and fail the call, but generally RPC is more "do what I say", rather than "ask the user for confirmation" like monero-wallet-cli.

You can restore your wallet from seed or keys to get access to it back.

If you want to use several wallets, you have to either run several monero-wallet-rpc instances, or load/save the wallets when appropriate. Like a file editor. If you want to edit a file and you have another file loaded, you load the other file you want to modify first.


## aaronovz1 | 2019-05-29T22:42:09+00:00
Looking at the code it looks like both functions do a check.

https://github.com/monero-project/monero/blob/5fbfa8a65663e807c6500ae9485e898df9b7c470/src/simplewallet/simplewallet.cpp#L1021

This check doesn't seem to work from what I just experienced. I think if the wallet is used/not empty then it should always fail and not overwrite. It just seems too risky for the user.

## aaronovz1 | 2019-06-06T16:37:41+00:00
@moneromooo-monero any comments on why the check doesn't work?

## moneromooo-monero | 2019-06-06T17:29:19+00:00
Did you test it ? You mentioned using RPC, but not the CLI wallet.

## aaronovz1 | 2019-06-06T17:37:44+00:00
No, I assumed RPC went through the same code path and into `simple_wallet::make_multisig`. I can test with CLI.

## moneromooo-monero | 2019-06-06T19:39:28+00:00
RPC is wallet_rpc_server.cpp. Both it and simplewallet.cpp use the wallet2 library.

# Action History
- Created by: aaronovz1 | 2019-05-29T21:56:30+00:00
