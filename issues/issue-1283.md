---
title: GUI glitch when resizing window to small size
source_url: https://github.com/monero-project/monero-gui/issues/1283
author: rex4539
assignees: []
labels:
- resolved
created_at: '2018-04-06T15:47:58+00:00'
updated_at: '2020-01-16T03:18:48+00:00'
type: issue
status: closed
closed_at: '2020-01-16T03:18:48+00:00'
---

# Original Description
GUI version: v0.12.0.0
macOS 10.13.5 (17F35e)

Reproducibility: always

Steps:
Resize window to small size.

What happened:
GUI glitch.

https://www.dropbox.com/s/jqkhimvj25l5hy8/Monero%20GUI%20glitch%202.mp4?dl=0

Expected result:
No glitch.

# Discussion History
## sanderfoobar | 2018-04-06T20:02:59+00:00
It tries to switch to 'mobile mode' which is currently being worked on.

## dEBRUYNE-1 | 2018-07-04T08:35:49+00:00
Probably fixed by #1491. 

## dEBRUYNE-1 | 2019-07-04T06:54:02+00:00
Can you check if this is still an issue in GUI v0.14.1.0? 


## rex4539 | 2019-07-04T07:38:24+00:00
Unfortunately not. I'm not running `monerod` anymore. I use Cake Wallet instead.

## dEBRUYNE-1 | 2019-07-05T13:31:58+00:00
@rex4539 - Would you have some time to quickly test it though? 

## rex4539 | 2019-07-05T19:36:39+00:00
Unfortunately not.

## sanderfoobar | 2019-07-05T20:07:49+00:00
This is still unfixed. Reproduce: make the window smaller. It jumps to 'mobile' mode. Happens when having a wallet opened.

## selsta | 2020-01-16T02:19:12+00:00
Mobile view got removed.

+resolved

# Action History
- Created by: rex4539 | 2018-04-06T15:47:58+00:00
- Closed at: 2020-01-16T03:18:48+00:00
