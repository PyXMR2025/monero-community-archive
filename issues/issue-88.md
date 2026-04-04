---
title: nodetool::peerlist_entry relies on time_t being a specific size.
source_url: https://github.com/monero-project/monero/issues/88
author: greatwolf
assignees: []
labels: []
created_at: '2014-08-07T19:48:23+00:00'
updated_at: '2014-08-24T15:55:44+00:00'
type: issue
status: closed
closed_at: '2014-08-24T15:55:44+00:00'
---

# Original Description
As discussed on irc with fluffypony and rfreemanw, `nodetool::peerlist_entry`, defined in p2p_protocol_defs.h, uses `time_t last_seen;`.

On mingw-gcc 32-bit, `time_t` is 4 bytes while on msvc it's 8 bytes. This causes issues in other places, like in keyvalue_serialization_overloads.h. For example, in the template function `unserialize_stl_container_pod_val_as_blob`, `CHECK_AND_ASSERT_MES` expects `loaded_size` to be divisible by `sizeof(value_type)` with `value_type = nodetool::peerlist_entry`. This assert passes on msvc since `peerlist_entry` is 24 bytes but will fail on mingw because it's 4 bytes shorter than expected.

As answered [here](http://stackoverflow.com/questions/471248/what-is-ultimately-a-time-t-typedef-to) the type of `time_t` and by extension its size, is implementation defined.


# Discussion History
## mikezackles | 2014-08-20T14:42:53+00:00
Unfortunately I don't see a short-term solution to this without resorting to dirty tricks.

To me it looks like peerlist_entry is going out over the wire, so unless I'm mistaken we're kind of stuck using time_t until we have a strategy for updating the wire protocol.

I also looked into getting MinGW to use a 64-bit time_t as a temporary solution.  It does on 64-bit, and it seems as if they're working on it for 32-bit, but so far I haven't found a compiler-level workaround.

So as of right now my plan is to try to manually serialize/deserialize back and forth from the 64-bit value to a 32-bit one on platforms where time_t is 32-bit.  This sounds dangerous to me, but hopefully it won't end up being any more dangerous than using time_t as part of the wire protocol in the first place.

I'm definitely open to alternative ideas.


## fluffypony | 2014-08-20T14:45:24+00:00
What are the chances of a time_t value exceeding 32-bits? That's the only time I can see serialising/deserialising between the two as being an issue.


## mikezackles | 2014-08-20T14:47:02+00:00
I don't think it will be an issue until 2038.


## fluffypony | 2014-08-20T14:49:40+00:00
If there are any 32-bit users in 2038 I'll personally hunt them down and give them a 64-bit computer. Let's go along with that solution and see how it goes:)


## mikezackles | 2014-08-20T14:50:44+00:00
Hahaha -- OK, sounds good to me :)


## mikezackles | 2014-08-20T16:56:42+00:00
The commit above seems to work on my system.

I thought about it some more, and, as I outlined in the commit message, by serializing time_t directly, the existing code was implicitly assuming that time_t is int64_t since that's what the major compilers use.  So to me the cleanest solution seemed to be serializing int64_t directly and casting as appropriate.

Assuming this works for everyone, I'll merge it into the mingw/daemonize branch.


# Action History
- Created by: greatwolf | 2014-08-07T19:48:23+00:00
- Closed at: 2014-08-24T15:55:44+00:00
