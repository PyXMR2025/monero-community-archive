---
title: usage of tx-notify
source_url: https://github.com/monero-project/monero/issues/4911
author: peterpan0708
assignees: []
labels: []
created_at: '2018-11-28T08:18:13+00:00'
updated_at: '2018-11-29T12:59:34+00:00'
type: issue
status: closed
closed_at: '2018-11-29T12:59:34+00:00'
---

# Original Description
I want to listen all the incoming transactions to my wallet, and I plan to use tx-notify, I will generate an address for each user ,  but all I can get from tx-notify is a tx_hash, can i know how much and which address of my wallet the user send to me?thanks very much!

# Discussion History
## peterpan0708 | 2018-11-28T08:58:39+00:00
I got it. I can use rpc method get_transfer_by_txid to do that. 

## dEBRUYNE-1 | 2018-11-28T16:04:24+00:00
@peterpan0708 - Can this be closed? 

## peterpan0708 | 2018-11-29T08:17:41+00:00
@dEBRUYNE-1  I have a question, when i config --tx-notify, for every incoming transaction, it triggers more than 10 times , that's to much for me, do i have a choice to config it.

## dEBRUYNE-1 | 2018-11-29T11:05:21+00:00
Can you illustrate your issue with an example? 

# Action History
- Created by: peterpan0708 | 2018-11-28T08:18:13+00:00
- Closed at: 2018-11-29T12:59:34+00:00
