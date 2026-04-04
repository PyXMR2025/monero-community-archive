---
title: 'PR #756: sanity check scan-from height'
source_url: https://github.com/monero-project/monero/issues/759
author: fluffypony
assignees: []
labels:
- bug
created_at: '2016-03-25T06:25:33+00:00'
updated_at: '2017-12-02T07:26:07+00:00'
type: issue
status: closed
closed_at: '2017-12-02T07:26:07+00:00'
---

# Original Description
Per https://github.com/monero-project/bitmonero/pull/756#discussion-diff-57412912

> May want a sanity check on scan_from_height.


# Discussion History
## moneromooo-monero | 2016-03-25T09:20:15+00:00
Beyond type checking as other JSON fields, what you would have ? It's unsigned to can't be negative, and the whole range is valid (if maybe very, very late in the future).


## tewinget | 2016-03-25T19:08:45+00:00
Well, while I suppose you _could_ create a wallet for which you only care
about transactions a year from now or later, it doesn't seem very
practical.  My thought was that one could at the very least inform the user
that the height doesn't make sense (if it's too far above the current chain
height).

On Fri, Mar 25, 2016 at 5:20 AM, moneromooo-monero <notifications@github.com

> wrote:
> 
> Beyond type checking as other JSON fields, what you would have ? It's
> unsigned to can't be negative, and the whole range is valid (if maybe very,
> very late in the future).
> 
> —
> You are receiving this because you are subscribed to this thread.
> Reply to this email directly or view it on GitHub
> https://github.com/monero-project/bitmonero/issues/759#issuecomment-201214969

## 

Thomas Winget
Computer Engineering
Purdue University '12


## moneromooo-monero | 2016-03-26T22:23:39+00:00
I suppose it could, but the wallet doesn't know the blockchain height (unless there's a daemon running), and it's meant to be an unattended process. Still, it could consider something from 2100 to be too far away, though it seems rather arbitrary.


## Cifrita | 2017-11-02T18:06:52+00:00
@fluffypony Is this still needed?

# Action History
- Created by: fluffypony | 2016-03-25T06:25:33+00:00
- Closed at: 2017-12-02T07:26:07+00:00
