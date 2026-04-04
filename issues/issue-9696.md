---
title: '[Discussion] White and Gray List is confusing'
source_url: https://github.com/monero-project/monero/issues/9696
author: ohchase
assignees: []
labels:
- discussion
created_at: '2025-01-12T16:15:51+00:00'
updated_at: '2026-02-07T17:58:49+00:00'
type: issue
status: closed
closed_at: '2026-02-07T17:58:49+00:00'
---

# Original Description
The Monero Project should consider editing the usage of "white" and "gray" in the code base.

Primarily, the usage of "white" and "gray" are confusing and do not thoroughly communicate intent.
Additionally, "gray" is very confusing without more context and the spelling is only popular in American English.
I particularly think "gray" is the most confusing wording across the project, because without further research and understanding of the project, one could easily consider "gray" peers to be ones identified as potentially dangerous but not yet proven banned nodes. 

As some initial suggestions I believe the project should move towards using the below naming conventions. 
1. "online" for "white"
2. "offline" for "gray"
3. "banned" for "banned" , *already implemented and used*

--- 

1. "active" for "white"
2. "inactive" for "gray"
3. "banned" for "banned" , *already implemented and used*

---
Large scale considerations:
- Massive breaking changes to the RPC Json API
- Invalidates a ton of historical information, guides, and discussions





# Discussion History
## SyntheticBird45 | 2025-01-12T16:23:13+00:00
I can understand the endeavor but your suggestions do not make sense.

Gray means that monerod received this node from another node address book, and therefore we haven't established contact with it before (if successful it get added to the white address book, if not it means that it get banned).

A gray peer is always offline per definition, but a white peer can be offline as well. Therefore it do not make sense to map active or online to an offline white peer.

## ohchase | 2025-01-16T11:22:20+00:00
@SyntheticBird45 thank you for your feedback, and clarifications.

Continuing to think about possible synonyms that better communicate "White" versus "Gray"

Trying to summarize what they represent

White -> A daemon we have connected to, BUT does not mean it is an honest node. So we Recognize this as a daemon node but again in no way confirm it is trustworthy.
Gray -> A node we have been told about, but have not yet connected to. 


Maybe 
White -> recognized
Gray -> announced

## iamamyth | 2025-01-17T23:19:13+00:00
Would say it's more like:
reached
unreached
banned (think this is being renamed to blocked in other work)

## iamamyth | 2025-01-17T23:26:47+00:00
This is the PR which proposes renaming ban to block: https://github.com/monero-project/monero/pull/9591.

Note the discussion on the difficulty of altering RPC fields, which very much applies here, as this proposal, unlike that PR, pretty much exclusively targets the RPC.

## jeffro256 | 2025-01-20T21:22:35+00:00
> This is the PR which proposes renaming ban to block: https://github.com/monero-project/monero/pull/9591.

That PR does the opposite: it renames blocklist to banlist 

# Action History
- Created by: ohchase | 2025-01-12T16:15:51+00:00
- Closed at: 2026-02-07T17:58:49+00:00
