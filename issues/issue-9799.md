---
title: Support elevated and extra elevated priorities in automatic fee priority algorithm
source_url: https://github.com/monero-project/monero/issues/9799
author: woodser
assignees: []
labels: []
created_at: '2025-02-14T13:27:35+00:00'
updated_at: '2025-03-16T00:33:22+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
This issue requests supporting `elevated` or even extra elevated fee priority in wallet2's automatic fee priority algorithm, [`adjust_priority`](https://github.com/monero-project/monero/blob/257db6dff257bc9f60641b16d199ffde252655b2/src/wallet/wallet2.cpp#L8635).

Currently only `unimportant` and `normal` levels are supported, which might be insufficient during severe congestion.

# Discussion History
## nahuhh | 2025-02-14T13:49:20+00:00
I'm working this out for a future pr, but the idea was:

not sure if these are the specifics i want to stick with yet, which is why i havent pushed this in a pr.
Something like:
If > 360 block backlog and avg fee-rate in the tx pool is > 2x low, then return priority 3 ("elevated")

this would ensure that we aren't growing blocks unnecessarily fast due to low fee spam.

iirc, "normal fee" is enough to hit 3mb blocks within 72hrs, but there are times when using "elevated" makes sense imo.

i also feel there's absolutely no time when auto should elevate to priority 4. That would be horribly expensive and unexpected ux. Opt-in only. At "elevated" fee tier(3), blocks grow 4x as fast as "normal"(2), so any backlog should be negligible. 

## Tzadiko | 2025-03-15T21:09:59+00:00
> I'm working this out for a future pr, but the idea was:

Hey, are you still working on this? I wouldn't mind taking a look at it myself as well, but I don't want to step on your toes.

## nahuhh | 2025-03-15T23:18:16+00:00
> Hey, are you still working on this? I wouldn't mind taking a look at it myself as well, but I don't want to step on your toes.

Are you on matrix or irc?

## Tzadiko | 2025-03-16T00:33:21+00:00
> > Hey, are you still working on this? I wouldn't mind taking a look at it myself as well, but I don't want to step on your toes.
> 
> Are you on matrix or irc?

Just joined!

# Action History
- Created by: woodser | 2025-02-14T13:27:35+00:00
