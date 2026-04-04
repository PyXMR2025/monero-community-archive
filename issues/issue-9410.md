---
title: Useful hard fork
source_url: https://github.com/monero-project/monero/issues/9410
author: developergames2d
assignees: []
labels:
- question
- low priority
created_at: '2024-07-29T15:49:02+00:00'
updated_at: '2024-08-17T14:49:58+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Can you make a Monero hard fork so that for each transaction you can add an encrypted message (~80-160 Bytes) that only the recipient can read?

# Discussion History
## vtnerd | 2024-07-30T01:19:47+00:00
You can do that now with `tx_extra`. Use the existing ECDH+hash as the shared-key, and then encrypt and stash into `tx_extra`.

## developergames2d | 2024-07-30T01:23:42+00:00
> You can do that now with `tx_extra`. Use the existing ECDH+hash as the shared-key, and then encrypt and stash into `tx_extra`.

How can I do it in monero-gui?

## vtnerd | 2024-07-30T14:44:30+00:00
>> You can do that now with tx_extra. Use the existing ECDH+hash as the shared-key, and then encrypt and stash into tx_extra.
>
> How can I do it in monero-gui?

You can't, this something that would require custom tools to be written.

## moneromooo-monero | 2024-08-17T14:49:57+00:00
There is a monero fork that implements exactly this:
https://git.townforge.net/townforge/townforge/commit/7c70d0ef6e4900434e54cb7cf071074d3d4da66b


# Action History
- Created by: developergames2d | 2024-07-29T15:49:02+00:00
