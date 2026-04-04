---
title: Unlocked balance wait time
source_url: https://github.com/monero-project/monero-gui/issues/406
author: ghost
assignees: []
labels: []
created_at: '2017-01-15T03:41:57+00:00'
updated_at: '2017-03-03T14:30:16+00:00'
type: issue
status: closed
closed_at: '2017-03-03T14:30:16+00:00'
---

# Original Description
I noticed how this awesome estimated wait time has been added to the GUI. So if there's 1/10 confirmations, and we have a 2 minute block time, then there are an estimated eighteen minutes remaining until my funds unlock "(~18 minutes)".

The problem is it says "~20 minutes" if it hasn't been mined yet, and there is a lot of congestion on the blockchain mempool at the moment.

What about having it say "> 20 minutes" when it hasn't been mined yet, and then once it has, going to ~18 minutes, ~16 minutes, etc. That way the GUI isn't saying people are going to get their funds in 20 minutes when in fact it could take an hour, as some transactions are currently taking.

# Discussion History
## Jaqueeee | 2017-02-01T14:40:52+00:00
You closed this? Can't recall it's implemented yet.

## ghost | 2017-02-01T17:50:43+00:00
@Jaqueeee I thought more about it, and realized that "> 20 minutes" sounds a bit dramatic. People could look at ">20 minutes" and think, "Oh man, how long is this going to take?!?" when in fact it'll probably take ~20 minutes.

**Perhaps instead we could have the "~20 minutes" time be "Waiting for mined block" or something to that effect. And then once the block is mined, it clicks to ~18, ~16 etc.**

I'll repoen this task.

# Action History
- Created by: ghost | 2017-01-15T03:41:57+00:00
- Closed at: 2017-03-03T14:30:16+00:00
