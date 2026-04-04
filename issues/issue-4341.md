---
title: '[GUI][Restore wallet] ''Create wallet'' stays disabled until monero-wallet-gui
  is closed'
source_url: https://github.com/monero-project/monero-gui/issues/4341
author: b4n6-b4n6
assignees: []
labels: []
created_at: '2024-08-22T21:54:15+00:00'
updated_at: '2025-02-24T17:59:43+00:00'
type: issue
status: closed
closed_at: '2025-02-24T17:59:43+00:00'
---

# Original Description
Kindly observe video @ 00:37 where 'Create wallet' button stays disabled even though mnemonic seed has been corrected
[restore-bug-2.webm](https://github.com/user-attachments/assets/4ec8af69-94a4-41c2-aaec-9f8dda5d2d51)

# Discussion History
## nahuhh | 2024-08-23T04:54:16+00:00
Confirmed

## plowsof | 2024-08-23T07:50:33+00:00
newlines / extra whitespaces can be stripped from the users seed to pass verification and sent to the wallet api. there would be concerns with merging this as we are modifying the structure of the users seed and potentially creating a different wallet. there is always 1 person who will enter words 1, 6, 11, 16, 21 on the first line lol

to avoid that concern, the restore wallet from seed screen would be the same window as the seed preview with numbers next to each word. 

## nahuhh | 2024-08-23T08:59:13+00:00
The whitepaces and lines seem to be stripped properly

the problem is that the "create wallet" button remains greyed out indefinitely (until restarting the wallet)

## b4n6-b4n6 | 2024-08-23T09:32:27+00:00
> newlines / extra whitespaces can be stripped from the users seed to pass verification and sent to the wallet api. there would be concerns with merging this as we are modifying the structure of the users seed and potentially creating a different wallet. there is always 1 person who will enter words 1, 6, 11, 16, 21 on the first line lol
> 
> to avoid that concern, the restore wallet from seed screen would be the same window as the seed preview with numbers next to each word.

Kindly
Whitespace in seed is not relevaant to this issue

the problem is that the "create wallet" button remains greyed out indefinitely (until restarting the monero-wallet-gui)

## b4n6-b4n6 | 2024-09-10T04:18:19+00:00
Fix [PR](https://github.com/monero-project/monero-gui/pull/4346)

# Action History
- Created by: b4n6-b4n6 | 2024-08-22T21:54:15+00:00
- Closed at: 2025-02-24T17:59:43+00:00
