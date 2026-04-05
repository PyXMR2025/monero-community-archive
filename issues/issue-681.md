---
title: How and where to provide test hash input to the cryptonight algorithm to run
  without pool information?
source_url: https://github.com/xmrig/xmrig/issues/681
author: ganapathy-mani
assignees: []
labels:
- question
created_at: '2018-06-07T01:02:00+00:00'
updated_at: '2018-10-10T22:18:37+00:00'
type: issue
status: closed
closed_at: '2018-10-10T22:18:37+00:00'
---

# Original Description
I found few hash inputs here: https://github.com/monero-project/monero/tree/master/tests/hash and I want to give them as inputs to CryptoNight algorithms and test the algorithm in action without pool information. 

Where and how can I provide these inputs in the XMRig code?  

# Discussion History
## xmrig | 2018-06-07T01:13:39+00:00
Test vectors defined there https://github.com/xmrig/xmrig/blob/master/src/crypto/CryptoNight_test.h and self check located there https://github.com/xmrig/xmrig/blob/dev/src/workers/MultiWorker.cpp#L51
Thank you,

## ganapathy-mani | 2018-06-07T01:27:57+00:00
How can I input hashes like this: https://github.com/monero-project/monero/blob/master/tests/hash/tests-extra-blake.txt ?

## xmrig | 2018-06-07T01:47:16+00:00
Read file, parse it, feed result to cryptonight hash function and verify hashes, should not be a big deal with C/C++ knowledge.
Thank you.

## mikegscott | 2018-06-07T02:20:03+00:00
From my network, its not possible to connect to poo.something.com:port. Is it possible to by bass it and just do the hash calculations? get the hash rate and stuff?  

## xmrig | 2018-06-07T09:20:01+00:00
No, but you can create fake pool on any language, just need implement reply to login request, protocol is really simple https://github.com/xmrig/xmrig-proxy/blob/master/doc/STRATUM.md
Thank you.

# Action History
- Created by: ganapathy-mani | 2018-06-07T01:02:00+00:00
- Closed at: 2018-10-10T22:18:37+00:00
