---
title: Monero testnet doesn't sync to latest height
source_url: https://github.com/monero-project/monero/issues/8363
author: ghost
assignees: []
labels: []
created_at: '2022-05-29T15:51:26+00:00'
updated_at: '2022-05-29T19:16:24+00:00'
type: issue
status: closed
closed_at: '2022-05-29T19:16:15+00:00'
---

# Original Description
Hello,

So this is what is happening:

```
2022-05-27 18:35:08.481 I Synced 1067618/1989519 (53%, 921901 left)
2022-05-27 18:35:08.744 I Synced 1067638/1989519 (53%, 921881 left)
```

But the current testnet height [at the time of writing this] is [1990185](https://community.rino.io/explorer/testnet/block/1990185).

I first thought my node database is corrupted so I removed blockchain files and it is syncing again.

The peers are also at height 1989519, I think this is the reason my node is syncing up to an old height.

Also I am using latest version 0.17.3.2.


# Discussion History
## ghost | 2022-05-29T16:08:02+00:00
I just removed the whole blockchain again, and still no luck, I don't know why all the peers it connects to, are old.
I even tried different servers from different data centers.
Edit: server time is OK and is set to UTC timezone.

## selsta | 2022-05-29T19:16:15+00:00
You have to use master branch, we forked already to v0.18 for testing purposes.

# Action History
- Created by: ghost | 2022-05-29T15:51:26+00:00
- Closed at: 2022-05-29T19:16:15+00:00
