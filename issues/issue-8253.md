---
title: Is there any method for monero wallet rpc that returns transactions on ALL
  subaccounts?
source_url: https://github.com/monero-project/monero/issues/8253
author: Ext7
assignees: []
labels: []
created_at: '2022-04-10T14:07:10+00:00'
updated_at: '2024-12-08T19:42:17+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Actually the problem is defined in topic. I didn't find any method that returns **all transactions of all subaccounts of one wallet**. Is there any?
It's hard to monitor all subaccounts if they are hundreds or even thousands - you need to call get_transfers on each account separately.
Setting **--tx-notify** for /monero-wallet-cli doesn't help either because it gives only tx id and **_get_transfer_by_txid_** also requires account_index


# Discussion History
## selsta | 2022-04-10T17:04:49+00:00
Any reason for using different subaccounts instead of subaddresses?

## Ext7 | 2022-04-10T22:46:02+00:00
Why subaccounts exists then, if subaddresses are "preferrable"? :)

For example subscription service for authors. Each author has subaccount and first subaddress of it used to pay for subscription. But also user without subscription can pay for particular post to subaddress generated specifically for this post and user. 
So many authors == many subaccounts.

P.S. Another question regarding all this isssues - is there any limit on subaddresses count of one wallet that won't lead to slowing responces from wallet?

## trasherdk | 2022-04-11T02:46:57+00:00
Sounds like a use-case for integrated addresses.

## Ext7 | 2022-04-11T05:59:15+00:00
Aren't they deprecated? Or it doesn't matter and this functionality will remain intact in future?

## trasherdk | 2022-04-13T01:29:29+00:00
@Ext7 Discussion #7889 has been going on for quite some time now, and to my knowledge, no consensus has been reached.

## selsta | 2022-04-18T23:13:39+00:00
> Why subaccounts exists then, if subaddresses are "preferrable"? :)

They have different use cases, subaccounts all have a separate balance and transaction history, which is usually something you don't want as a merchant. It's more for organization as a user, or if you don't want to mix outputs.

> P.S. Another question regarding all this isssues - is there any limit on subaddresses count of one wallet that won't lead to slowing responces from wallet?

Not really, but more subaddresses will require more RAM. Scanning speed should stay constant.

## Ext7 | 2022-04-19T08:41:24+00:00
@selsta @trasherdk - Ok, thank you very much for your answers.

## DJVova | 2024-12-08T19:42:16+00:00
> Any reason for using different subaccounts instead of subaddresses?

I have a wallet in which I use several accounts for my purposes. When -tx_notify reports about new incoming transaction in the wallet, I don't know the transaction account, I know only Txid. I am trying to use the "Get_Transfer_by_TXID" method, but it suggests that I should know account of transaction. I think it would be good to add in this method possibility of a request "all_accounts - boolean; (Optional) (Defaults to false)". Otherwise, how can I find out the transaction account with a simple method?

# Action History
- Created by: Ext7 | 2022-04-10T14:07:10+00:00
