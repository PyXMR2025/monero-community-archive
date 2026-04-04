---
title: 'feature request: progress updates during refresh on ledger'
source_url: https://github.com/monero-project/monero/issues/5067
author: thedavidmeister
assignees: []
labels: []
created_at: '2019-01-13T01:57:50+00:00'
updated_at: '2019-01-14T09:07:20+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
this is especially an issue when using ledger without exporting the view key

the cli wallet appears to hang with:

`Starting refresh...`

some update on where the status of the refresh is at would be great e.g. `monerod` block downloading updates

# Discussion History
## thedavidmeister | 2019-01-13T02:27:24+00:00
hmmm looks like the update shows when i export the view key, but not if i don't

also the ledger locks itself long before the refresh finishes, unsure if this breaks refresh because the refresh isn't finishing and there is no visual feedback

## dEBRUYNE-1 | 2019-01-13T07:28:04+00:00
>also the ledger locks itself long before the refresh finishes

Does this occur when the view key is exported or when it's kept on the device?

## moneromooo-monero | 2019-01-13T14:52:00+00:00
The wallet refreshes 1000 blocks at once. When using a ledger in slow mode, it could do so, say, only 10 at a time, so the progress would happen more often. If using a third party daemon, this would leak the fact the wallet is using a ledger, but then it probably can tell by the speed anyway.

## thedavidmeister | 2019-01-14T09:07:20+00:00
when i export the view key the refresh shows a progress report and finishes within a few seconds

if i don't export the view key

- there is no progress update in the wallet cli
- the process takes a very long time (or hangs, i can't tell?)
- the scrolling text and GUI of the ledger can freeze and become unresponsive to button presses until a power cycle
- the process can take so long that the ledger locks itself, it isn't clear if it is doing anything at this point and if it is i expect most people would assume it isn't because a passphrase is needed to access the device

i've managed to get the non-export version working only about 2 or 3 times, it usually hangs and i need to do whatever i was doing, so i end up being forced to export the key when i don't really want to :(

# Action History
- Created by: thedavidmeister | 2019-01-13T01:57:50+00:00
