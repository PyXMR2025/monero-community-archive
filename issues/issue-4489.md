---
title: Downloading Blockchain impossible due to speed
source_url: https://github.com/monero-project/monero-gui/issues/4489
author: trvllr777
assignees: []
labels: []
created_at: '2025-08-20T14:04:38+00:00'
updated_at: '2025-08-20T14:24:29+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hello,

I have started to download the Blockchain 36 hours ago. The download was very fast first but gradually got slower. 12 hours ago, I had around 25.000 blocks left. Now there are still 20.000. The log shows now clear error.

It is not my network, since I tried a different one. Restarted the machine, killed the GUI multiple times. Nothing works.

# Discussion History
## nahuhh | 2025-08-20T14:24:29+00:00
Type `sync_info` into the monerod (or, if on linux/mac, navigate to the folder containing monerod and run `./monerod sync_info`)

there be be a list IP addresses, followed by a line that says [moooooooo] or similar. Post the [mooooo] line here please.

# Action History
- Created by: trvllr777 | 2025-08-20T14:04:38+00:00
