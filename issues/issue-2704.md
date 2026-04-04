---
title: Segmentation fault after trying to sync blockchain
source_url: https://github.com/monero-project/monero/issues/2704
author: RickDaRuler21
assignees: []
labels: []
created_at: '2017-10-22T16:49:05+00:00'
updated_at: '2017-11-24T17:40:23+00:00'
type: issue
status: closed
closed_at: '2017-11-24T17:40:23+00:00'
---

# Original Description
Hello all, I am a newb with all of this and I've spent the last two days waiting for the blockchain to sync/download on my tails usb. I went out and bought an expensive 128 gig usb drive to ensure I would have enough space on my usb for the whole block chain download. I've literally been sitting here for two days waiting for it and I wake up this morning to see tons of errors "server failure, connection timeout, etc." so I decide to restart my computer and try to start syncing again... then I received a segmentation fault and now the sync won't even start. please tell me I did not waste all that money and time for it just to corrupt at the very end of the download! please somebody help me solve this :(

# Discussion History
## moneromooo-monero | 2017-10-22T17:23:29+00:00
Try https://github.com/monero-project/monero/pull/2672

## RickDaRuler21 | 2017-10-22T17:27:54+00:00
thanks, but I dont understand what I'm supposed to do.... I don't see any downloads or anything on that page.

## moneromooo-monero | 2017-10-22T17:30:53+00:00
Then wait for next release, should be tomorrow.

## radfish | 2017-10-22T18:16:35+00:00
I would not recommend using a 128GB USB drive as you sole blockchain storage. It is likely to die in near future. Also, some of them have incredibly poor controllers that cause extremely slow read/write performance in non-uniform way (so some requests are fast, some take multiple seconds). I stopped this USB-drive approach after witnessing one 128GB SD card and one 128GB drive get destroyed.
Use an SSD.

## moneromooo-monero | 2017-11-24T17:38:51+00:00
All known crashes were fixed, and no reply.

+resolved

# Action History
- Created by: RickDaRuler21 | 2017-10-22T16:49:05+00:00
- Closed at: 2017-11-24T17:40:23+00:00
