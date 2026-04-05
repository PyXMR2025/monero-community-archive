---
title: Xmrig segfaults if fed password longer than 490 characters
source_url: https://github.com/xmrig/xmrig/issues/757
author: mardarfar
assignees: []
labels:
- bug
created_at: '2018-09-19T10:00:01+00:00'
updated_at: '2018-09-22T05:40:59+00:00'
type: issue
status: closed
closed_at: '2018-09-20T09:59:23+00:00'
---

# Original Description
# ./xmrig -o pool.supportxmr.com:5555 -u 43QGgipcHvNLBX3nunZLwVQpF6VbobmGcQKzXzQ5xMfJgzfRBzfXcJHX1tUHcKPm9bcjubrzKqTm69JbQSL4B3f6E3mNCbU -p $(perl -e "print 'A' x 490")
 * VERSIONS     XMRig/2.6.4 libuv/1.22.0 gcc/5.4.0
 * CPU          Intel(R) Core(TM) i7-3770 CPU @ 3.40GHz (1) x64 AES-NI
 * CPU L2/L3    1.0 MB/8.0 MB
 * THREADS      4, cryptonight, av=0, donate=5%
 * POOL #1      pool.supportxmr.com:5555 variant 1
 * COMMANDS     hashrate, pause, resume
Segmentation fault

0x000000000047cc5f in Client::parseResponse(long, rapidjson::GenericValue<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator> > const&, 
                       rapidjson::GenericValue<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator> > const&) ()

Using static build from https://github.com/xmrig/xmrig/releases/download/v2.6.4/xmrig-2.6.4-xenial-amd64.tar.gz on centos 7 3.10.0-862.9.1.el7.x86_64




# Discussion History
## xmrig | 2018-09-20T04:36:00+00:00
Fixed https://github.com/xmrig/xmrig/commit/0adad684711ed9507e17d270955f68d909f58267. Fix will be included into next v2.8 release.
Thank you.

# Action History
- Created by: mardarfar | 2018-09-19T10:00:01+00:00
- Closed at: 2018-09-20T09:59:23+00:00
