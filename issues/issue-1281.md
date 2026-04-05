---
title: 'error: ''randomx::JitCompilerA64'' has not been declared on ARM'
source_url: https://github.com/xmrig/xmrig/issues/1281
author: OTLabs
assignees: []
labels:
- bug
- arm
created_at: '2019-11-13T18:55:00+00:00'
updated_at: '2019-12-22T19:29:20+00:00'
type: issue
status: closed
closed_at: '2019-12-22T19:29:20+00:00'
---

# Original Description
I am compiling v5.0.0 for Alpine Linux, https://github.com/alpinelinux/aports/pull/12102,  and get following error for aarch64, armv7, and armhf:

`/home/buildozer/aports/testing/xmrig/src/xmrig-5.0.0/src/crypto/randomx/randomx.cpp:212:38: error: 'randomx::JitCompilerA64' has not been declared`

Build logs are available here:
aarch64 - https://cloud.drone.io/alpinelinux/aports/13302/3/1 (build is stalled at the time of writing)
armv7 - https://cloud.drone.io/alpinelinux/aports/13302/5/1
armhf - https://cloud.drone.io/alpinelinux/aports/13302/4/1

# Discussion History
## andypost | 2019-11-19T13:11:06+00:00
aarch64 still fails to build https://cloud.drone.io/alpinelinux/aports/13356/3/1

## xmrig | 2019-11-19T19:21:01+00:00
Something wrong with builder, in log just warnings and no single error and seems build was killed by timeout.
Thank you.

# Action History
- Created by: OTLabs | 2019-11-13T18:55:00+00:00
- Closed at: 2019-12-22T19:29:20+00:00
