---
title: segmentation fault v6.18, but v6.7 works?
source_url: https://github.com/xmrig/xmrig/issues/3095
author: bigbot20
assignees: []
labels: []
created_at: '2022-07-24T09:05:29+00:00'
updated_at: '2025-06-18T22:54:55+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:54:55+00:00'
---

# Original Description
Haven't had the chance to try other versions, but v6.18 (dynamically compiled) crashes on my Linux PC right after "* COMMANDS", v6.7 (dynamically compiled) works as usual.
Any ideas? How can I debug this? Thank you.

OS: Centos 8. CPU mining.


# Discussion History
## Spudz76 | 2022-07-24T14:35:12+00:00
Why does it matter if an antique version works or not?  Probably some bug that was already fixed, or you are using weird versions of the deps... for best results always use the included `./scripts/build_deps.sh` so that hwloc/libuv/openssl are known good versions, RHEL based things always have old libs.

# Action History
- Created by: bigbot20 | 2022-07-24T09:05:29+00:00
- Closed at: 2025-06-18T22:54:55+00:00
