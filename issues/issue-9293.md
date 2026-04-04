---
title: 'Suggestion: When there is a backlog at the current fee level, print a menu
  showing backlogs and costs at each fee level'
source_url: https://github.com/monero-project/monero/issues/9293
author: phytohydra
assignees: []
labels:
- wallet
created_at: '2024-04-15T21:17:34+00:00'
updated_at: '2024-04-15T22:33:19+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
`set` shows `priority = 0 (default)`

Trying a transfer without fee specified says there is a 211 block backlog.
With fee specified,
unimportant: 262 block backlog
normal: 209 block backlog
elevated: no backlog

The automatic fee selection is not bumping the priority up past normal.

I saw someone complaining on reddit that monero is unusable right now.  If they don't know that they have to manually try higher priorities until there is no backlog, that will be their experience.

# Discussion History
## selsta | 2024-04-15T21:33:43+00:00
Automatic fee selection switches between fee level 0 and 1. If there are a lot of fee level 1 transactions users have to manually set a higher fee.

I'm open for suggested changes, but what you are reporting is intentional behaviour.

## phytohydra | 2024-04-15T22:05:25+00:00
I suggest that if there is a backlog at the current fee level, the wallet should automatically check what the backlog would be at each higher fee level, until it finds a level without a backlog or reaches the top priority, then print a menu for the user listing the cost & backlog at each level, and asking what fee to use.

```
There is currently a 236 block backlog at that fee level.
Fee level         Backlog        Fee
1 Unimportant     262 blocks     x 
2 Normal          236 blocks     y
3 Elevated        0 blocks       z

Fee to use for this transaction (1-3): 
```

If automatic fee selection still ends up with a 236 block backlog, it isn't enough by itself.

The flood has shown that many users are unaware they can manually increase the fee level.  Instead of hoping they will all start finding it in the manual, the UI can just show them the option when they need it.  My experience is that the people who know that automatic fee selection exists expect it to go as high as needed to get their transaction through without a backlog.  The manual is long, and people don't look for features they don't expect to exist.

## selsta | 2024-04-15T22:09:27+00:00
One thing to keep in mind if the person that creates these transactions also uses automatic fee selction then there would be the exact same backlog, just at a higher fee level.

## phytohydra | 2024-04-15T22:10:59+00:00
Would it cause the blocks to grow faster?

# Action History
- Created by: phytohydra | 2024-04-15T21:17:34+00:00
