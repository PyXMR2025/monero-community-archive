---
title: Cannot use `show_transfers in` without being connected to daemon
source_url: https://github.com/monero-project/monero/issues/6878
author: muff1nman
assignees: []
labels: []
created_at: '2020-10-11T20:47:13+00:00'
updated_at: '2022-02-19T01:08:08+00:00'
type: issue
status: closed
closed_at: '2022-02-19T01:08:08+00:00'
---

# Original Description
With an offline wallet `--offline`, that I've imported outputs for, I cannot show my incoming transfers:

```
[ wallet XXXXXX (no daemon)]: show_transfers in
Error: Failed to get pool state:no connection to daemon
```

# Discussion History
## moneromooo-monero | 2020-10-12T16:15:03+00:00
Works for me, with --offline and with both a daemon running and not.

## jonathancross | 2020-11-11T15:46:23+00:00
I see `Error: Failed to get pool state:no connection to daemon` as well in v0.17.1.1 (wallet is on a system that is air-gapped)

## moneromooo-monero | 2020-12-07T03:08:30+00:00
That's normal if you don't have a daemon connected.

## muff1nman | 2020-12-07T17:52:37+00:00
Regardless of expected or not, is that desired? I would argue that should be a warning instead of an error and it should at least show transfers that were imported.

## moneromooo-monero | 2020-12-08T13:22:06+00:00
It shows in/out transfers either way, so... if it doesn't for you, then you'll have to supply more info as to how you're doing it, there might be a particular set of circumstances which cause those txes not to be displayed, but since it works for, I can't fix it.

# Action History
- Created by: muff1nman | 2020-10-11T20:47:13+00:00
- Closed at: 2022-02-19T01:08:08+00:00
