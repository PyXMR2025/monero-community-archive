---
title: monerod v0.13.0.4 being killed / crashed randomly it seems
source_url: https://github.com/monero-project/monero/issues/4725
author: patoshii
assignees: []
labels:
- invalid
created_at: '2018-10-25T15:47:00+00:00'
updated_at: '2018-10-26T20:57:03+00:00'
type: issue
status: closed
closed_at: '2018-10-26T20:57:03+00:00'
---

# Original Description
Below is the screenshot of when it got killed and also the bitmonero.log file. 

I started monerod with the command:

**./monerod --block-sync-size 10**

What could the issue be? 

[![enter image description here][1]][1]


[![enter image description here][2]][2]


  [1]: https://i.stack.imgur.com/RfN1C.png
  [2]: https://i.stack.imgur.com/dfxGr.png

# Discussion History
## moneromooo-monero | 2018-10-25T16:00:07+00:00
That's the OOM killer. Free more memory.

## moneromooo-monero | 2018-10-26T20:44:23+00:00
And btw you'll see more info in dmesg about it when it happens.

+invalid


# Action History
- Created by: patoshii | 2018-10-25T15:47:00+00:00
- Closed at: 2018-10-26T20:57:03+00:00
