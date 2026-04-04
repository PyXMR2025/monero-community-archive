---
title: TX_EXTRA_TAG_ADDITIONAL_PUBKEYS is being added unnessery
source_url: https://github.com/monero-project/monero/issues/2801
author: moneroexamples
assignees: []
labels: []
created_at: '2017-11-14T00:51:44+00:00'
updated_at: '2017-11-14T19:56:29+00:00'
type: issue
status: closed
closed_at: '2017-11-14T19:56:29+00:00'
---

# Original Description
@stoffu 

I think TX_EXTRA_TAG_ADDITIONAL_PUBKEYS code is added to extra for no reason, and it breaks comparability with previous monero version for decoding payments id.

Example here: have a look at extra (notice last 400), this is current monero master (so extra works):
http://139.162.32.245:8082/tx/181a0961cac103a6b9f922f6846567fc9de7d51867dffdf9c2c132017824faee

Older monero release:
https://testnet.xmrchain.com/tx/181a0961cac103a6b9f922f6846567fc9de7d51867dffdf9c2c132017824faee

will not find encrypted payment id, because `parse_tx_extra` returns false due to last `400`.

I think this could be fixed, if its not intentional, by adding if statement around `add_additional_tx_pub_keys_to_extra(tx.extra, additional_tx_public_keys);` in `construct_tx_and_get_tx_key`

```
    if (need_additional_txkeys)
        add_additional_tx_pub_keys_to_extra(tx.extra, additional_tx_public_keys);
```




# Discussion History
## stoffu | 2017-11-14T01:46:33+00:00
@moneroexamples 
That change makes sense; currently it adds 2 wasted bytes to tx extra when the additional tx pubkeys is empty. Please submit a pull request!

Regarding compatibility, the old wallet can't recognize the new field anyway, but it should still get the payment ID field read in `tx_extra_fields` even when `parse_tx_extra` returns `false` because of the unrecognized field (as far as I can see from the code). After all, one can put arbitrary data into tx extra that are unrecognizable to the official wallet.

## moneroexamples | 2017-11-14T05:35:38+00:00
@stoffu 

Thanks. just added the pull request. I also checked older wallets, and you are correct, they do detect the payment id. 

## moneromooo-monero | 2017-11-14T18:21:52+00:00
https://github.com/monero-project/monero/pull/2681

## moneromooo-monero | 2017-11-14T19:52:07+00:00
+resolved

# Action History
- Created by: moneroexamples | 2017-11-14T00:51:44+00:00
- Closed at: 2017-11-14T19:56:29+00:00
