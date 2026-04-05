---
title: 6.2.1 API cause segfault
source_url: https://github.com/xmrig/xmrig/issues/1742
author: tymoteuszrogalewski
assignees: []
labels:
- bug
created_at: '2020-06-23T09:07:14+00:00'
updated_at: '2020-08-19T01:11:03+00:00'
type: issue
status: closed
closed_at: '2020-08-19T01:11:03+00:00'
---

# Original Description
at first connection to API using below command line
curl -s http://127.0.0.1:3333/1/summary
...the miner crash with segfault
without using API script....miner works fine.

running miner using this command:
./xmrig --opencl --cuda --no-cpu -o stratum.ravenminer.com:3838 -a kawpow -u xxxxxxxxxxx -p x --http-port=3333

using Ubuntu16

miner was compiled using those options:
cd cmake && cmake .. -DCMAKE_C_COMPILER=gcc-5 -DCMAKE_CXX_COMPILER=g++-5 && make

all prev versions was compiled and running in same way without this issue

# Discussion History
## xmrig | 2020-06-23T09:20:01+00:00
Fixed, v6.2.2 will be released soon.
Thank you.

## xmrig | 2020-06-23T09:35:34+00:00
https://github.com/xmrig/xmrig/releases/tag/v6.2.2

# Action History
- Created by: tymoteuszrogalewski | 2020-06-23T09:07:14+00:00
- Closed at: 2020-08-19T01:11:03+00:00
