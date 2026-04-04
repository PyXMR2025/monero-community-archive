---
title: Wallet can miss processing spend txs in the pool
source_url: https://github.com/monero-project/monero/issues/8670
author: j-berman
assignees: []
labels: []
created_at: '2022-12-07T08:48:46+00:00'
updated_at: '2022-12-07T23:08:18+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
When the user has a spend tx in the pool that their wallet hasn't scanned yet (e.g. if the user rescans the chain, or uses the same seed in a different wallet), the wallet won't process the spend tx correctly. The user could end up trying to re-spend output(s) in this case and the daemon will reject the tx as a double spend.

The wallet process receive txs as expected. This issue appears isolated to spends.

# Discussion History
## afungible | 2022-12-07T23:08:18+00:00
I have noticed this behavior a couple months ago and I can confirm this occured. This results in double spend that the daemon rejects. I used same wallet file twice and used two monero-cli instances while fiddling around, on same PC.

Note, this also sort of corrupted my LMDB database (i.e. it showed a double spend txn) but I couldn't repair the DB locally. The only way was to download the whole Blockchain again, as whenever I spent from wallets outputs, it randomly popped up outputs are being double spent (when I clearly wasn't then) and was annoying.

Basically, one issue followed another in such a case.

# Action History
- Created by: j-berman | 2022-12-07T08:48:46+00:00
