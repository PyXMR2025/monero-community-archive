---
title: systemd service loads blockchain from wrong path
source_url: https://github.com/monero-project/monero/issues/3291
author: blacksheepvision
assignees: []
labels:
- invalid
created_at: '2018-02-18T19:35:50+00:00'
updated_at: '2018-07-19T22:01:05+00:00'
type: issue
status: closed
closed_at: '2018-07-19T22:01:05+00:00'
---

# Original Description
I downloaded the systemd file on debian linux. Set working dir as /root/ however monero starts in /.bitmonero/ not in /root/.bitmonero also the log path is /.bitmonero/var/log/monero/monero.log

How can I fix ?

# Discussion History
## moneromooo-monero | 2018-07-19T21:49:55+00:00
Add --data-dir to point where you want.

+invalid

# Action History
- Created by: blacksheepvision | 2018-02-18T19:35:50+00:00
- Closed at: 2018-07-19T22:01:05+00:00
