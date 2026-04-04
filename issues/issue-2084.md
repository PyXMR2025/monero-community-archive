---
title: documentation of the start_height field to the refresh RPC method is incomplete
source_url: https://github.com/monero-project/monero-site/issues/2084
author: dimalinux
assignees: []
labels:
- '📚 docs: dev guides'
created_at: '2022-10-22T03:02:07+00:00'
updated_at: '2022-12-01T07:14:23+00:00'
type: issue
status: closed
closed_at: '2022-12-01T07:14:23+00:00'
---

# Original Description
Reference:
https://github.com/monero-project/monero-site/blob/7535c4c62623166af4ce12033e30af2d7d19c40b/resources/developer-guides/wallet-rpc.md#L2514

Right now the description of `start_height` to the `refresh` wallet RPC method says:
> The block height from which to start refreshing.

It should say something like:
> The block height from which to start refreshing. Passing no value or a value less than the last block scanned by the wallet refreshes from the last block scanned.

This change will prevent anyone from incorrectly thinking that `refresh` can  be used to force rescan the block chain.

# Discussion History
## plowsof | 2022-10-23T13:58:46+00:00
Thank you. Confused me also.. its clear that its meant to be used in combination with auto_refresh disabled OR - skip / fast forward the sync process (i believe featherwallet utilises this for insta-syncing if the user is certain theyv'e received no funds since the last time they opened their wallet). I've updated my PR with your addition and credited you.

# Action History
- Created by: dimalinux | 2022-10-22T03:02:07+00:00
- Closed at: 2022-12-01T07:14:23+00:00
