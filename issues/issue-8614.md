---
title: creating a view only wallet on 18.1.2 always returns an error
source_url: https://github.com/monero-project/monero/issues/8614
author: anycolo
assignees: []
labels: []
created_at: '2022-10-18T12:14:29+00:00'
updated_at: '2023-06-06T01:34:05+00:00'
type: issue
status: closed
closed_at: '2023-06-06T01:34:05+00:00'
---

# Original Description
	E offset >= num_outputs. THROW EXCEPTION: error::wallet_internal_error
	E Error creating view only wallet: Offset is larger than total outputs


# Discussion History
## j-berman | 2022-10-18T14:49:47+00:00
I see one way to trigger this error -- does the wallet that you're trying to create a view only wallet have 0 txs (is it a totally new wallet)?

## j-berman | 2022-10-18T16:36:52+00:00
Here are the errors I'm seeing in the GUI. When creating a view-only wallet from:

- A wallet with 0 transfers triggers: `Offset is larger than total outputs`
- A wallet with >1 transfer(s) triggers: `Imported outputs omit more outputs that we know of. Try using export_outputs all.`

I see the causes of the above two errors. Will PR fixes shortly but want to confirm this is what you're seeing as well.

## anycolo | 2022-10-18T16:54:51+00:00
Yes!!!

## anycolo | 2022-10-18T19:38:46+00:00
I've been having other issues as well:
https://github.com/monero-project/monero/issues/8613
Even if it returns an error, the gui still creates a wallet, which seems usable. I have used that wallet. Was it safe to use, or will i lose funds?

## j-berman | 2022-10-18T20:25:08+00:00
I don't see how you could lose funds. The issue of the view-only wallet displaying too high of a balance in #8613 seems entirely to do with not importing key images into the view-only wallet as mentioned in the comments there.

# Action History
- Created by: anycolo | 2022-10-18T12:14:29+00:00
- Closed at: 2023-06-06T01:34:05+00:00
