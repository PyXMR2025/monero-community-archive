---
title: Improve P2P address book
source_url: https://github.com/Cuprate/cuprate/issues/178
author: Boog900
assignees:
- willco-1
- SyntheticBird45
labels:
- A-p2p
- C-feature
- E-medium
created_at: '2024-06-19T21:09:37+00:00'
updated_at: '2024-11-06T23:43:25+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
This is a tracking issue of things that should be improved in our P2P address book:

## Don't replace addresses unless unreachable

We should not replace peers in either peer list (white or gray) unless they are unreachable, this should reduce an attackers ability to fill our peer list.

We should set up a task that periodically pulls unused peers from either the gray or white lists and attempts to ping them to see if they are reachable. If they are not we will keep them removed from the address book. When a new addresses come in they should only be added if there is space in the address book.

The function to ping peers: 

https://github.com/Cuprate/cuprate/blob/4653ac58849c81b6ab993a1d23f061a97962524b/p2p/p2p-core/src/client/handshaker.rs#L195

## Bucket addresses

We should use a bucket system [like Bitcoin](https://bitcoin.stackexchange.com/questions/115539/bucketing-algorithm-in-bitcoin) to store our p2p address, so that we guarantee a more diverse range of addresses.

## Persist banned peers

Currently banned peers are forgotten on restarts, we should keep them in the `p2p_store`.

The functions where the peer filer is saved and loaded: 

https://github.com/Cuprate/cuprate/blob/4653ac58849c81b6ab993a1d23f061a97962524b/p2p/address-book/src/store.rs#L24-L55

These functions should be changed to allow the ban list to be stored as well:

https://github.com/Cuprate/cuprate/blob/4653ac58849c81b6ab993a1d23f061a97962524b/p2p/address-book/src/book.rs#L63

## Properly implement an anchor system

TODO 


# Discussion History
## willco-1 | 2024-09-07T16:50:33+00:00
i'll take a shot at this!

## SyntheticBird45 | 2024-11-06T23:43:24+00:00
Heyo @willco-1 are you still working on persistent ban list ?

# Action History
- Created by: Boog900 | 2024-06-19T21:09:37+00:00
