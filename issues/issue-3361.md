---
title: something error
source_url: https://github.com/xmrig/xmrig/issues/3361
author: calojohn806
assignees: []
labels: []
created_at: '2023-11-17T10:25:37+00:00'
updated_at: '2025-06-18T22:33:11+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:33:11+00:00'
---

# Original Description
./xmrig 
./xmrig: /lib/x86_64-linux-gnu/libc.so.6: version `GLIBC_2.35' not found (required by ./xmrig)
./xmrig: /lib/x86_64-linux-gnu/libc.so.6: version `GLIBC_2.36' not found (required by ./xmrig)
./xmrig: /lib/x86_64-linux-gnu/libc.so.6: version `GLIBC_2.33' not found (required by ./xmrig)
./xmrig: /lib/x86_64-linux-gnu/libc.so.6: version `GLIBC_2.32' not found (required by ./xmrig)
./xmrig: /lib/x86_64-linux-gnu/libc.so.6: version `GLIBC_2.34' not found (required by ./xmrig)

I compile with static mode but it is ok from ubuntu but i change to another linux , it show that error

# Discussion History
## SChernykh | 2023-11-17T10:54:03+00:00
The only way to make a full static build is an advanced build on Alpine: https://xmrig.com/docs/miner/build/alpine
Otherwise you'll still have GLIBC dependencies. You can try to build it on Ubuntu 16.04 or even older to be compatible with as many distros as possible.

# Action History
- Created by: calojohn806 | 2023-11-17T10:25:37+00:00
- Closed at: 2025-06-18T22:33:11+00:00
