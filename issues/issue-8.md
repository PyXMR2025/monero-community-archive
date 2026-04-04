---
title: 'Kovri: setup cubieboard 2 for testing'
source_url: https://github.com/monero-project/meta/issues/8
author: anonimal
assignees: []
labels: []
created_at: '2016-11-12T06:28:02+00:00'
updated_at: '2016-11-17T10:33:23+00:00'
type: issue
status: closed
closed_at: '2016-11-17T10:33:23+00:00'
---

# Original Description
@danrmiller knows the details. This includes min req for boost, a current openssl, and vastly increased swap space (probably 2gig min). cmake and gcc-4.9 have already been installed.

# Discussion History
## danrmiller | 2016-11-15T20:06:40+00:00
I think we are talking about the cubieboard 2 device.

OpenSSL: /usr/lib/arm-linux-gnueabihf/libssl.so;/usr/lib/arm-linux-gnueabihf/libcrypto.so (version "1.0.1f") 
Boost (system/thread) version: 1.62.0 is in /usr/local/lib/
Swap:      2068476


## anonimal | 2016-11-16T11:38:02+00:00
Yes, I was unsure if you wanted that info public.


## anonimal | 2016-11-17T07:45:11+00:00
Deps are installed and swap was setup to spec but the build is still crashing because of low memory. Can we increase swap to 3GiB?


## danrmiller | 2016-11-17T08:02:27+00:00
Swap:      4194300          0    4194300


## anonimal | 2016-11-17T10:33:22+00:00
Darn, gcc needs more but that's ok: I'll use clang instead (which doesn't even require the previous 2GiB swap).

We're up and running, thanks @danrmiller!

Note: fortunately, I cannot reproduce https://github.com/monero-project/kovri/issues/434.


# Action History
- Created by: anonimal | 2016-11-12T06:28:02+00:00
- Closed at: 2016-11-17T10:33:23+00:00
