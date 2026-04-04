---
title: Suggestion for block sync progress bar
source_url: https://github.com/monero-project/monero-gui/issues/387
author: voidzero
assignees: []
labels: []
created_at: '2017-01-06T22:47:02+00:00'
updated_at: '2017-02-27T20:25:18+00:00'
type: issue
status: closed
closed_at: '2017-02-27T20:25:18+00:00'
---

# Original Description
Right now, the progress bar is at almost 100% every time I start up the GUI because it's technically correct - right now I am at block 1217730 and need to sync to 1218152.

My idea is to make the progress bar instance specific. So when the GUI is started, the current block (1217730) could be 0% or 1%. That makes the progress bar a heck of a lot nicer.

# Discussion History
## thoriumbr | 2017-01-12T20:13:48+00:00
I think showing `Updating block 4 of 175` is more user friendly than `Updating block 1217730 of 1218152.`


## voidzero | 2017-01-12T23:06:30+00:00
Ooh, yes, I like that one too.

# Action History
- Created by: voidzero | 2017-01-06T22:47:02+00:00
- Closed at: 2017-02-27T20:25:18+00:00
