---
title: 'Restore: date inadvertently entered as YYYYMMDD is accepted as restore blockheight'
source_url: https://github.com/monero-project/monero-gui/issues/3207
author: rating89us
assignees: []
labels: []
created_at: '2020-11-02T19:22:23+00:00'
updated_at: '2021-06-16T19:54:00+00:00'
type: issue
status: closed
closed_at: '2021-06-16T19:54:00+00:00'
---

# Original Description
I've already seen two users reporting that they had problems restoring a wallet after entering YYYYMMDD instead of the expected YYYY-MM-DD (one is here: https://github.com/monero-project/monero-gui/issues/3206#issuecomment-720559061). The other user reported that he typed YYYYMMDD because his keyboard was not typing the "-" separator.

Monero GUI accepts the YYYYMMDD number as a restore blockheight that is ~10x higher that current blockheight:
- Current blockheight: 2221943
- Restore blockheight: 20201102 (~10x higher; user should have entered 2020-11-02)

As a temporary workaround, I'd suggest the restore wallet page should convert the entered number to a date (YYYY-MM-DD) if:
1. entered number is too high to be a restore blockheight (>current blockheight)
2. entered number starts with 4 digits that seems to represent years (2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021).



# Discussion History
## rating89us | 2021-06-15T11:51:11+00:00
Another user with this issue:
https://www.reddit.com/r/monerosupport/comments/nzmr3q/xmr_blockchain_inconsistency/h1tcvus

# Action History
- Created by: rating89us | 2020-11-02T19:22:23+00:00
- Closed at: 2021-06-16T19:54:00+00:00
