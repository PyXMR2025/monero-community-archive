---
title: xmrig is not preferring ipv6 over ipv4
source_url: https://github.com/xmrig/xmrig/issues/2883
author: gucki
assignees: []
labels:
- question
created_at: '2022-01-21T11:03:52+00:00'
updated_at: '2022-04-03T14:36:27+00:00'
type: issue
status: closed
closed_at: '2022-04-03T14:36:27+00:00'
---

# Original Description
**Describe the bug**
It seems xmrig is not preferring ipv6 over ipv4. Running it on a ipv6-only host with a pool that has an A and an AAAA record (ipv4 + ipv6) xmrig is not able to connect because it tries to connect using the ipv4 address. Passing the ipv6 address instead of the domain to xmrig makes it work.

**To Reproduce**
Run xmrig with a pool that has an ipv4 and ipv6 address. Xmrig will try to use the ipv4 instead of the ipv6 address.

**Expected behavior**
If an ipv6 address (AAAA record) exists it should always be preferred.

**Required data**
XMRig 6.16.2
 built on Dec 20 2021 with GCC 10.3.1
 features: 64-bit AES

libuv/1.42.0
OpenSSL/1.1.1l
hwloc/2.5.0


# Discussion History
## xmrig | 2022-01-21T13:21:11+00:00
To prefer IPv6 change `ipv6` option in `dns` to `true` https://github.com/xmrig/xmrig/blob/dev/src/config.json#L98 or if you use command line, use option `--dns-ipv6`.
Thank you.

## gucki | 2022-01-22T07:14:00+00:00
Thanks, I wasn't aware of that option because I only checked https://xmrig.com/docs/miner/command-line-options and it's not mentioned there. Is it also available as a cli option?

Anyway, the recommended (and general?) approach is to prefer ipv6 over ipv4. Shouldn't xmrig behave the same?

# Action History
- Created by: gucki | 2022-01-21T11:03:52+00:00
- Closed at: 2022-04-03T14:36:27+00:00
