---
title: Segmentation fault (core dumped) with latest build after restoring a wallet
  from keys and trying to check balance
source_url: https://github.com/monero-project/monero/issues/3026
author: phloatingman
assignees: []
labels: []
created_at: '2017-12-29T04:08:31+00:00'
updated_at: '2018-01-26T19:08:01+00:00'
type: issue
status: closed
closed_at: '2018-01-26T19:08:01+00:00'
---

# Original Description
I'm running Ubuntu Mate 16.04.3 64-bit in virtualbox

After I build from master, this is the cli version...
Monero 'Helium Hydra' (v0.11.1.0-master-a0a8706)

After I run this command..
./monero-wallet-cli --log-level 4 --generate-from-keys fromkeys

I am able to input the standard address, secret spend key, and secret view key.. however, when I run the balance command, it gives me segmentation fault (core dumped)

Here is the log file..
https://gist.github.com/phloatingman/440f695ea21fe0342454ace52c764402

Here is a screenshot of my terminal session...
https://i.imgur.com/sb3JBvp.png

After the Segmentation fault (core dumped) error, I can open the wallet normally and see balance without issue.. as seen here...
https://i.imgur.com/HdOnsIy.png

# Discussion History
## stoffu | 2017-12-29T07:17:48+00:00
This is a bug. #3028
Thank you for reporting!

## moneromooo-monero | 2018-01-26T19:04:57+00:00
+resolved

# Action History
- Created by: phloatingman | 2017-12-29T04:08:31+00:00
- Closed at: 2018-01-26T19:08:01+00:00
