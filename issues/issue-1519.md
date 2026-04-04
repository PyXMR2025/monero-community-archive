---
title: '[Feature request] Starting block height for rescan_bc?'
source_url: https://github.com/monero-project/monero/issues/1519
author: kenshi84
assignees: []
labels: []
created_at: '2016-12-31T10:41:47+00:00'
updated_at: '2017-01-02T02:16:53+00:00'
type: issue
status: closed
closed_at: '2017-01-02T02:16:53+00:00'
---

# Original Description
Recently my wallet suddenly started to show an incorrect balance. I don't know why this was caused, but doing `rescan_bc` gave me the correct balance. (Btw, is this the primary use case for this command?)

I created the wallet a few months ago, so it seemed to me like a waste of time that the wallet rescans blocks from the genesis height. Wouldn't it make sense to allow the user to optionally specify the starting block height for rescanning?

# Discussion History
## moneromooo-monero | 2017-01-01T16:29:37+00:00
rescan_bc is not supposed to be used unless you really need it. People started using it every time there's something off, even if not needed. It's better to debug why something is off in the first place. Now, we've got no idea what went wrong.
Still, maybe worth doing.

## kenshi84 | 2017-01-02T02:16:53+00:00
I see. Since it's not supposed to be used frequently, maybe it's OK to force the user to start the rescanning from the genesis block. Closing.

# Action History
- Created by: kenshi84 | 2016-12-31T10:41:47+00:00
- Closed at: 2017-01-02T02:16:53+00:00
