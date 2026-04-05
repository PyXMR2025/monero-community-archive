---
title: xmrig 3.0.0 hard lockup on Ryzen 3000 cpu
source_url: https://github.com/xmrig/xmrig/issues/1118
author: jims23211
assignees: []
labels: []
created_at: '2019-08-16T15:26:20+00:00'
updated_at: '2019-08-16T16:17:19+00:00'
type: issue
status: closed
closed_at: '2019-08-16T16:17:19+00:00'
---

# Original Description
O/S -- Ubuntu 18.0.4.3 & Windows 10
CPU's tested -- Ryzen 3700x & 3900x  
RAM -- 16GB 3600 CL16

Stock speeds and memory settings.  Build from github repo following ubuntu and windows per instructions.  When starting up with the following parameters on any of the systems 

./xmrig --algo=cn/r --donate-level 1 --api-port=5555 --max-cpu-usage 80 -o pool.supportxmr.com:5555 -u 43CcGPhWwVQDtTKxDkcEW1gD33RxMU1D1Zbjc9PEiCQeN2rRjv4ruEMQZUtCffScCQK95DksBPcE7e1YV7vVgu7hJYQR1ZS -p dellr815:talino23211@gmail.com -k

loki
./xmrig --algo=rx/loki --donate-level 1 --max-cpu-usage 80 -o  donate.v2.xmrig.com:3333 -u 4ADFnuC1kDQGtkncbETsHnTt7qmQFvwjUMn7Awvh3GAZMRuSaGqTo2j9K2wW4qjpMEQCDPzJmhr2cXEKJqUe9uJvBrdeD3o -p dellr815:talino23211@gmail.com -k

Hard locks after startup (example below)

* ABOUT XMRig/3.0.0 gcc/7.4.0
* LIBS libuv/1.18.0 OpenSSL/1.1.1 hwloc/1.11.9
* CPU AMD Ryzen 9 3900X 12-Core Processor (1) x64 AES
L2:6.0 MB L3:64.0 MB 12C/24T NUMA:1
* DONATE 1%
* ASSEMBLY auto:ryzen
* POOL #1 donate.v2.xmrig.com:3333 algo rx/loki
* COMMANDS hashrate, pause, resume
[2019-08-16 10:14:26.561] use pool donate.v2.xmrig.com:3333 185.92.222.223
[2019-08-16 10:14:26.561] new job from donate.v2.xmrig.com:3333 diff 1000225 algo rx/loki height 337896
[2019-08-16 10:14:26.562] rx init dataset algo rx/loki (24 threads) seed b57d3b678cce6553...
[2019-08-16 10:14:26.562] cpu use profile rx (24 threads) scratchpad 2048 KB
[2019-08-16 10:14:26.562] rx #0 allocate 2336 MB (2080+256) for RandomX dataset & cache
[2019-08-16 10:14:26.711] rx #0 allocate done huge pages 1168/1168 100% +JIT (150 ms)
[2019-08-16 10:14:26.716] cpu READY threads 24(24) huge pages 24/24 100% memory 49152 KB (155 ms)
[2019-08-16 10:14:28.469] rx #0 init done (1907 ms) 

# Discussion History
## xmrig | 2019-08-16T15:43:42+00:00
`--max-cpu-usage` option removed.
24 threads in optimal for this CPU since it have enough cache for all threads, if you like use less threads, better option is use config file and remove some of them from profile `rx`.
Thank you.

## jims23211 | 2019-08-16T16:09:35+00:00
I have no idea what your trying to convey to me.  Are you saying starting the xmrig with fewer threads will prevent lock up?  Then then I would be running suboptimal for hashing.

## jims23211 | 2019-08-16T16:17:19+00:00
okay, I remove that parameter and ran again, its is working fine with all 24 threads active.



# Action History
- Created by: jims23211 | 2019-08-16T15:26:20+00:00
- Closed at: 2019-08-16T16:17:19+00:00
