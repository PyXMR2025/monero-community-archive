---
title: wallet2 import_key_images erases incoming transfers
source_url: https://github.com/monero-project/monero/issues/5812
author: woodser
assignees: []
labels: []
created_at: '2019-08-14T22:11:29+00:00'
updated_at: '2019-08-14T22:17:37+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Exporting and re-importing key images from the wallet erases incoming transfers.

1) Open a wallet
2) Export key images using RPC export_key_images (or wallet2::export_key_images)
3) Import key images using RPC import_key_images (or wallet2::import_key_images)
4) The wallet will return fewer incoming transfers than before importing key images

Here's a test which demonstrates the issue: [testImportKeyImagesAndTransfers](https://github.com/monero-ecosystem/monero-java/blob/2548adacd8a98deae62ab0523b417d6b5941162a/src/test/java/test/TestMoneroWalletJni.java#L69)

It's likely to be related to wallet2.cpp:11957 (line number too big to link?) which erases an incoming payment with `m_payments.erase(j);`.

# Discussion History
## woodser | 2019-08-14T22:13:17+00:00
Referencing #4500 where incoming transfers to outgoing counterparts sent from/to the same wallet are not reported, in case they are related.

# Action History
- Created by: woodser | 2019-08-14T22:11:29+00:00
