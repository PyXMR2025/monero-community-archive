---
title: '`cuprated` killswitch removal'
source_url: https://github.com/Cuprate/cuprate/issues/468
author: hinto-janai
assignees: []
labels:
- C-discussion
created_at: '2025-05-12T22:43:09+00:00'
updated_at: '2025-11-26T19:40:03+00:00'
type: issue
status: closed
closed_at: '2025-11-26T19:40:02+00:00'
---

# Original Description
## What
Some questions on the removal of `cuprated`'s [killswitch](https://github.com/Cuprate/cuprate/pull/365).

- When should the killswitch be removed?
- Is `cuprated` safe to release to the public without a killswitch?
- How close are network split bugs to 0% chance? How close does it have to be to remove the killswitch?
- Will other bugs occur that justify having a killswitch?
- Are there other things that justify having killswitch?
- Regardless of the chance of bugs, is it still worth releasing `cuprated` without a killswitch?

# Discussion History
## SyntheticBird45 | 2025-05-13T10:21:09+00:00
> Is cuprated safe to release to the public without a killswitch?

> Regardless of the chance of bugs, is it still worth releasing cuprated without a killswitch?

Starting with the obvious question. We can't do that from an ethical pov as this can be assimilated to planned obsolescence, even if for good reasons. There is also the conundrum of having a Free and open source software that is purposefully limiting freedom of use to its user.

If you take GrapheneOS as an example, they do make it as smooth as possible for you to install security updates and annoy you with notifications about it, but they don't force you onto installing it.

So while it would be interesting from a security pov, this is unethical and frankly this would probably spark some anger.

>  When should the killswitch be removed?

So IMO, the killswitch can be removed at stable or during beta. Probably not at the start of beta, as RPC will bring a lot more users for testing and we would get more chance to catch consensus bugs in this period.

I don't an answer or comment on the other questions.

# Action History
- Created by: hinto-janai | 2025-05-12T22:43:09+00:00
- Closed at: 2025-11-26T19:40:02+00:00
