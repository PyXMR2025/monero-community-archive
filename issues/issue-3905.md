---
title: Taking too long to make a cold sign due to export_outputs file size is big
  if there are too many outputs.
source_url: https://github.com/monero-project/monero/issues/3905
author: zhongqiuwood
assignees: []
labels: []
created_at: '2018-06-02T00:45:04+00:00'
updated_at: '2022-04-08T14:49:37+00:00'
type: issue
status: closed
closed_at: '2022-04-08T14:49:36+00:00'
---

# Original Description
The 4 operations export_outputs/import_outputs/export_key_images/import_key_images on hot & cold wallets handle all the history outputs of the account every time before making a valid cold sign.

It will take a very very long time if there are many outputs.

I am not sure if it is necessary that do them from the first transfer output of the account every time.

Is there any way that only does the 4 operations on delta outputs and can still make a valid cold sign afterwards?

So that we do not waste time on the outputs already handled.

# Discussion History
## zhongqiuwood | 2018-06-02T03:21:25+00:00
Thank you @stoffu for your support!

My understanding is the transfers stored in wallet2::m_transfers are sorted by timestamps. The m_transfers[0] is the earliest one, m_transfers[m_transfers.size() - 1] the last one.

If the understanding is correct, my proposal is enhance below 2 commands:
```
export_outputs <file> [<txid>]
export_key_images <file> [<txid>]
```
The 'txid' means only handling the transfer txid and the transfers that happend after the txid in wallet2::m_transfers.
If txid is empty, then handles all the history tx(the current behavior).	

import_outputs/import_key_images commands keep with no change.
However the exported output file is an increment, import_outputs/import_key_images should find the right transfers in wallet2::m_transfers to update.


## moneromooo-monero | 2018-10-24T20:55:28+00:00
https://github.com/monero-project/monero/pull/4720

## zhp1254 | 2018-12-27T09:43:32+00:00
dose the[ wallet rpc api](https://ww.getmonero.org/resources/developer-guides/wallet-rpc.html#export_outputs) has the params txid? 
the document show me the export_outputs has none params and return all outputs

## moneromooo-monero | 2018-12-27T13:03:42+00:00
No, there is no txid parameter to export_outputs.
If you want to get help about monero, try #monero on Freenode. This is a bug tracker.

## zhp1254 | 2018-12-28T02:21:55+00:00
> No, there is no txid parameter to export_outputs.
> If you want to get help about monero, try #monero on Freenode. This is a bug tracker.

do you know any python 、nodejs or golang sdk to hex vout as export_outputs

## selsta | 2022-04-08T14:49:36+00:00
#4720 and #8179

# Action History
- Created by: zhongqiuwood | 2018-06-02T00:45:04+00:00
- Closed at: 2022-04-08T14:49:36+00:00
