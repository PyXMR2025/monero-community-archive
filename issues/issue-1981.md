---
title: KawPoW Speed on 6.6.2 slower than on 6.5.0
source_url: https://github.com/xmrig/xmrig/issues/1981
author: UselessGuru
assignees: []
labels: []
created_at: '2020-12-15T10:04:18+00:00'
updated_at: '2020-12-16T08:52:31+00:00'
type: issue
status: closed
closed_at: '2020-12-16T08:52:31+00:00'
---

# Original Description
Measured KawPow speed on 6.6.2 slower than on 6.5.0.

Same Driver / OS / OC settings.

Tested on 
- RX5700:         6.5.0: 15.39 MH/s   6.6.2: 14.72 MH/s
- RX580 (8GB): 6.5.0: 8.58 MH/s     6.6.2: 8.38 MH/s

Command lines used:
xmrig.exe --algo kawpow --no-cpu --opencl --opencl-devices=0 --url=mine.zergpool.com:3638 --user=****************************--pass=Blackbox,c=BTC,mc=RVN --keepalive --http-enabled --http-host=127.0.0.1 --http-port=4001 --api-worker-id=*****************--api-id=XmRig-v6.5.0-1xRadeonRX5808GB --retries=90 --retry-pause=1

# Discussion History
## SChernykh | 2020-12-16T08:37:58+00:00
KawPow OpenCL code hasn't changed between these two versions. Hashrate changes a lot between different RVN blocks because of how KawPow works.

# Action History
- Created by: UselessGuru | 2020-12-15T10:04:18+00:00
- Closed at: 2020-12-16T08:52:31+00:00
