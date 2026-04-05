---
title: IPv4 retry/fallback?
source_url: https://github.com/xmrig/xmrig/issues/3058
author: incith
assignees: []
labels: []
created_at: '2022-05-22T19:49:08+00:00'
updated_at: '2025-06-20T11:01:56+00:00'
type: issue
status: closed
closed_at: '2025-06-20T11:01:56+00:00'
---

# Original Description
When it can't connect to a pool (my proxy) on IPv6 it seems to just skip it instead of retrying IPv4?  Both protocols are definitely working, clients can connect with either v6 or v4 but, if the client is having IPv6 issues (and can still resolve the IPv6 hostname) then it doesn't seem to retry on IPv4.

# Discussion History
## Spudz76 | 2022-05-22T23:51:25+00:00
Yes the resolve [code just takes the first record](https://github.com/xmrig/xmrig/blob/dev/src/base/net/stratum/Client.cpp#L326) of whatever was returned by DNS.  There is zero decision or introspection into which family of addr it is at all.

Probably could be smarter but I'm not exactly sure how to do so within the existing constructs, maybe by adding a reference list to track usage of each record, and not re-try any of them until they have even "try-counts" (always try the next-least-tried result).

If your resolver was set to randomize results it would eventually retry an A record... you can wedge something like dnsmasq in between to forcibly randomize result sets even if nothing else upstream of you does so.  Some routers have a DNS randomizer option, since they mostly use dnsmasq anyway under the hood (just depends if they "wired" it up to the GUI).  Perhaps the result set could be randomized forcibly in xmrig to acheive similar "randomly eventually" behavior.  The tracking real retry counts would be better if possible without breaking things.

I think it should also sort AAAA records first and A records last to be more like how everything else works (only use v4 when v6 doesn't work at all).  Probably much of this result-set sorting or randomizing could be fixed up in one place within the "Dns" class since it's separate from the "stratum Client" where connection attempts (and their result) would have to be tracked.

## incith | 2022-05-31T03:27:06+00:00
What about adding an ipv6 (boolean, default null (use dns config setting?) of course or some such) configuration flag to the pools, and then I can just add the pool twice for now?

Anyway, appreciate your acknowledgement.  This can be closed at your discretion.

## xmrig | 2025-06-20T11:01:56+00:00
#3678 

# Action History
- Created by: incith | 2022-05-22T19:49:08+00:00
- Closed at: 2025-06-20T11:01:56+00:00
