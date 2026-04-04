---
title: GUI does not sync with my remote node
source_url: https://github.com/monero-project/monero/issues/7064
author: moneroentusi
assignees: []
labels: []
created_at: '2020-12-03T19:56:46+00:00'
updated_at: '2020-12-03T21:45:47+00:00'
type: issue
status: closed
closed_at: '2020-12-03T21:45:47+00:00'
---

# Original Description
I open GUI, I connect to my private remote node on my VPS. It connects but is stuck at "Waiting for daemon to syns" , Daemon blocks remaining: 2. Whatever I do is not getting past this.....

Please help.

If I use a public node is working just fine.

# Discussion History
## selsta | 2020-12-03T19:58:20+00:00
Download: https://gui.xmr.pm/files/block.txt

Start daemon with --ban-list /path/to/block.txt

We will put out a release to fix this properly in the next days, in the meantime you have to use the ban list workaround.

## moneroentusi | 2020-12-03T21:45:47+00:00
Now is everything is working properly. Thank you!

# Action History
- Created by: moneroentusi | 2020-12-03T19:56:46+00:00
- Closed at: 2020-12-03T21:45:47+00:00
