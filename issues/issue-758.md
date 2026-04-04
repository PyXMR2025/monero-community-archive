---
title: 'PR #756: improve version handling'
source_url: https://github.com/monero-project/monero/issues/758
author: fluffypony
assignees: []
labels:
- enhancement
- wontfix
created_at: '2016-03-25T06:24:53+00:00'
updated_at: '2019-07-05T19:09:35+00:00'
type: issue
status: closed
closed_at: '2019-07-05T19:09:35+00:00'
---

# Original Description
Per: https://github.com/monero-project/bitmonero/pull/756#discussion-diff-57412861

> This feels like something that shouldn't be hard-coded.


# Discussion History
## moneromooo-monero | 2016-03-25T09:18:42+00:00
It's the version of what the current code knows about. You can't pass that on a command line, it doesn't make sense. So I think it makes sense to put a const int with it.How would you make it less hard coded ?


## tewinget | 2016-03-25T19:06:20+00:00
Looking at it now, I guess all I'd question is the scoping of that constant, but I'm not sure where all it would be used, so it may be fine.  Woops.


## ghost | 2018-01-07T10:58:22+00:00
Is this issue still relevant?

## ghost | 2019-06-25T12:28:36+00:00
Please be aware that "ancient" help wanted issues make a super-strange impression to newcomers.

## moneromooo-monero | 2019-07-05T19:07:38+00:00
I guess it can be closed. It was opened from a comment by tewinget, who's long gone, and the code's OK IMHO.

+wontfix

# Action History
- Created by: fluffypony | 2016-03-25T06:24:53+00:00
- Closed at: 2019-07-05T19:09:35+00:00
