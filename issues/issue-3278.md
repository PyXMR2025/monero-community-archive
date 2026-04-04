---
title: 'System freeze / intimidate shutdown cause: Couldn''t connect to daemon'
source_url: https://github.com/monero-project/monero-gui/issues/3278
author: ckorder
assignees: []
labels: []
created_at: '2020-12-21T22:35:58+00:00'
updated_at: '2021-05-25T01:10:10+00:00'
type: issue
status: closed
closed_at: '2021-05-25T01:10:10+00:00'
---

# Original Description
**Monero 'Oxygen Orion' (v0.17.1.7-release)
Error: Couldn't connect to daemon: 127.0.0.1:18081**
Ubuntu 20.04

Using advance mode obviously

How to reproduce: Use the gui and let the application crash or let the system freeze / intimidate shutdown while sync the blockchain

Please consider fixing this, relating to fact that with rising time its getting more likely to occur for users.

Split the downloaded volume and make hash checks from the parts or stuff like that to ensure the daemon to start correctly otherwise its quite annoying, if linux users face this issue. Maybe it occur on other os as well.

Error to fix:
close process
`rm -rf ~/.bitmonero`
Restart client
Start downloading from zero to hero genius 👎   !!!

[12/22/20 12:20 AM] 2020-12-21 22:20:11.989 I Monero 'Oxygen Orion' (v0.17.1.7-release)
Error: Couldn't connect to daemon: 127.0.0.1:18081
[12/22/20 12:20 AM] 2020-12-21 22:20:27.237 I Monero 'Oxygen Orion' (v0.17.1.7-release)
Height: 1, target: 1 (100%)
Downloading at 0 kB/s
Next needed pruning seed: 1
0 peers
0 spans, 0 MB
[]

`Give your wallet a password` **please add enter key pres support!**
`Node starting in default 10 seconds blabla` **please remove this annoying message!**

Thanks for looking into the issue.

# Discussion History
## selsta | 2021-05-25T01:10:10+00:00
Thanks or the report. You can add `--db-sync-mode safe` to your custom daemon startup settings (Settings -> Node) if you are having an unstable system. We are not going to make it default because it slows down sync.

Apart from that is isn't obvious what you are reporting exactly. Deleting the blockchain results in syncing from scratch, there is nothing to fix here.

# Action History
- Created by: ckorder | 2020-12-21T22:35:58+00:00
- Closed at: 2021-05-25T01:10:10+00:00
