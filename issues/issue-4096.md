---
title: Two minor issues
source_url: https://github.com/monero-project/monero-gui/issues/4096
author: VOC-LINK
assignees: []
labels: []
created_at: '2023-01-07T12:30:13+00:00'
updated_at: '2023-01-08T03:43:33+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
1. When I close Monero-GUI I have only the options „Force stop” and „Keep it running” (in the background) — no chance to get back to GUI if I change my mind. Could be possible to bind to „Esc” key the possibility to „don't exit” (get back to still running GUI)?
2. From what I see the failed transactions are — for the reason unknown to me — kept at the very beginning of transactions list, and there's no possibility to delete them. They are meant to stay there, at the very beginning, forever, like kind of remorse. If I can't delete the „failed transaction” entries — could they be at least NOT forced to stay at the beginning of transactions list? It's nothing but irritating.

# Discussion History
## plowsof | 2023-01-07T12:49:47+00:00
1. yes ive accidentally been here once or twice
2. how long have they been showing for? have you tried resyncing your wallet - settings -> info -> change restore height -> ok -> ok

## VOC-LINK | 2023-01-07T13:04:56+00:00
2. It's kept for 64 days now, and I have to watch it again and again, like it was something beautiful(?), worth of admiration. Could you, please, at least make failed transaction being treated as any other transaction and NOT forcefully kept at the beginning of the list? They are marked with that „red X” anyway, so the user can easily find them.

No, I didn't try to change any setting, there's '0' at that entry you're writing about.

## plowsof | 2023-01-08T03:43:33+00:00
lets resync your wallet. but as your height is 0, this would be slow. to quicken the process, find the first translation in your wallets history, expand the details, and click on the blockheight to copy it. now go to settings to change your restore height again with this value.  

This problem usually 'fixes itself' - a quick fix solution could be to add an optional filter to hide transactions that are unknown to remove the annoyance.

# Action History
- Created by: VOC-LINK | 2023-01-07T12:30:13+00:00
