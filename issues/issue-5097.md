---
title: Integrating Monero with our wallet
source_url: https://github.com/monero-project/monero/issues/5097
author: DanielMazurFL4RE
assignees: []
labels:
- invalid
created_at: '2019-01-26T16:18:49+00:00'
updated_at: '2019-03-19T14:58:01+00:00'
type: issue
status: closed
closed_at: '2019-03-19T14:58:01+00:00'
---

# Original Description
Hello there, Monero contributors, I wanted to add Monero to Hodler Wallet which is multicoin lightwallet without need to have any blockchain data stored on user's device. Moneros way to build transaction is very complicated for me, since I'm not native english language speaker, but I understand code. Monero code base is huge, so that's why I'm asking for simpler code for RingCT etc. in C or Python. Every integration that I have found is basing on local RPC communication (except this one https://github.com/emesik/monero-python/blob/master/monero/transaction.py but I'm not sure if it is valid code for monero, is still up to date? Someone tried that code?), but that is useless for me. Monero is important coin, we want to add integrated DEX to exchange BTC for XMR inside the wallet. 

Thanks in advice, Daniel
hodler.tech team

# Discussion History
## moneromooo-monero | 2019-01-26T17:08:10+00:00
This is a bug tracker, not a help desk. If you have particular questions, try #monero on Freenode. If those questions are particularly about specific code, #monero-dev on Freenode.

If you want the code which creates a tx, see construct_tx_and_get_tx_key in cryptonote_tx_utils.cpp. This calls the rct API, etc, as needed. It is called by transfer_selected_rct, which is called from create_transactions_2, both in wallet2.cpp.


## moneromooo-monero | 2019-03-19T14:19:25+00:00
Not a bug. See IRC for questions.

+invalid

# Action History
- Created by: DanielMazurFL4RE | 2019-01-26T16:18:49+00:00
- Closed at: 2019-03-19T14:58:01+00:00
