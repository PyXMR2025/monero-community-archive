---
title: Add arbitrary data support + tx memo functionality
source_url: https://github.com/monero-project/monero/issues/2494
author: fluffypony
assignees: []
labels: []
created_at: '2017-09-20T15:47:32+00:00'
updated_at: '2017-09-20T17:36:42+00:00'
type: issue
status: closed
closed_at: '2017-09-20T16:02:10+00:00'
---

# Original Description
This is low-hanging fruit for anyone that is up to it.

1. Add the ability to arbitrarily serialise key-value pairs, encrypt it the same way we encrypt payment IDs, and pack it in to the tx_extra serialised set.
2. Add the ability to decrypt and unserialise this data.
3. Make sure the CLI wallet notifies users of encrypted data on receipt / lookup of a tx.
4. Add support for this to the transfer RPC call.
5. Possibly add CLI support for this, but I think that might be a little chunky from a UX perspective.
6. Add support for tx memos by merely using this encrypted data functionality with a specific named field called "memo"
7. Make sure the CLI wallet separately notifies users of tx memo data on receipt / lookup of a tx (and doesn't show both the memo AND the encrypted data, it only needs to be shown once)
8. Add support for tx memos to the transfer RPC call (yes, a memo could be added manually through encrypted data, but since it's a standardised field it makes sense to have it in the RPC call as a separate option)
9. Add support for tx memos to the transfer CLI call, be sure to wrap memo input in inverted commas or similar otherwise you won't be able to separate arguments
10. Add unit tests for encrypted data and tx memos

# Discussion History
## fluffypony | 2017-09-20T16:02:10+00:00
Actually requirements are more complex than this, closing for now

## monerobby | 2017-09-20T17:36:42+00:00
Can you expand on what the issue was that makes it more complex than originally thought? I am interested.

> On Sep 20, 2017, at 11:02 AM, Riccardo Spagni <notifications@github.com> wrote:
> 
> Actually requirements are more complex than this, closing for now
> 
> —
> You are receiving this because you are subscribed to this thread.
> Reply to this email directly, view it on GitHub, or mute the thread.
> 


# Action History
- Created by: fluffypony | 2017-09-20T15:47:32+00:00
- Closed at: 2017-09-20T16:02:10+00:00
