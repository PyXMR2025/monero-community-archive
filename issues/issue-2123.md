---
title: '[Trezor] - Proceed to device not shown after TX signature'
source_url: https://github.com/monero-project/monero-gui/issues/2123
author: ph4r05
assignees: []
labels: []
created_at: '2019-04-28T11:41:20+00:00'
updated_at: '2020-06-14T22:39:55+00:00'
type: issue
status: closed
closed_at: '2020-06-14T22:39:55+00:00'
---

# Original Description
After the spending transaction is signed with the Trezor, GUI prompts for a wallet password and freezes, as Trezor device expects user input (accept live refresh request). GUI does not show "Proceed to the device" splash from some reason.

After the user clicks the Trezor button process continues normally.
I will try to address this but if you happen to know why is it happening it might be useful. Thanks! :) 

# Discussion History
## ph4r05 | 2019-04-28T19:24:00+00:00
I think I found the reason - `transaction.commit()` is blocking call, this prevents the popup from showing.  

## ph4r05 | 2019-04-29T16:06:08+00:00
@selsta @xmrdsc @xiphon do you think it would be beneficial to make an async wrapper for the PendingTransaction.commit() and commit in async way?

## selsta | 2019-04-30T06:57:40+00:00
I know nothing about async, would there be any downsides? If not, it probably would be beneficial.

## xiphon | 2019-04-30T16:26:42+00:00
> do you think it would be beneficial to make an async wrapper for the PendingTransaction.commit() and commit in async way?

Sure, async wrapper would definitely be beneficial.

## selsta | 2020-06-14T22:39:55+00:00
Seems resolved.

# Action History
- Created by: ph4r05 | 2019-04-28T11:41:20+00:00
- Closed at: 2020-06-14T22:39:55+00:00
