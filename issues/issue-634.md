---
title: Config Question - E5-2680
source_url: https://github.com/xmrig/xmrig/issues/634
author: lukelat
assignees: []
labels: []
created_at: '2018-05-17T03:34:26+00:00'
updated_at: '2018-06-17T18:03:12+00:00'
type: issue
status: closed
closed_at: '2018-06-17T18:03:12+00:00'
---

# Original Description
Firstly, thanks so much for creating xmrig!

Have read some really useful responses regarding optimal configurations so I thought I would see if you can get my Hash rate up!

The Server is running Ubuntu 16.04 with
Intel(R) Xeon(R) CPU E5-2680 v2 @ 2.80GHz (1) x64 AES-N

I've tried a lot of variations on Thread Count / Max CPU Usage and cpu-affinity but it seems like I'm running waay under optimal... from looking at benchmarks I should be getting at least 700 h/s
No other processes running.

My basic command is
./xmrig -a cryptonight-heavy --max-cpu-usage=100 --donate-level=5 -o loki.miner.rocks:5555 -u L4yaW7Qm8dB3h8d2jXRYcp7SU6oLtEv8C1GsMe4vrzE6eLHmdX5XyvJjbyTxWco9fwBqCFuwUDRKvUwj8Fc6efPZUp9BcL8 -p x --log-file=./xmrig.log -cpu-priority=5 

Here's the log output.

VERSIONS:     XMRig/2.6.2 libuv/1.8.0 gcc/5.4.0
 * CPU:          Intel(R) Xeon(R) CPU E5-2680 v2 @ 2.80GHz (1) x64 AES-NI
 * CPU L2/L3:    2.5 MB/25.0 MB
 * THREADS:      6, cryptonight-heavy, av=0, donate=1%
 * POOL #1:      loki.miner.rocks:5555
 * COMMANDS:     hashrate, pause, resume
[2018-05-17 03:16:21] READY (CPU) threads 6(6) huge pages 12/12 100% memory 24.0 MB
[2018-05-17 03:16:21] use pool loki.miner.rocks:5555 51.38.205.26
[2018-05-17 03:16:21] new job from loki.miner.rocks:5555 diff 30000 algo cn-heavy
[2018-05-17 03:16:23] speed 2.5s/60s/15m n/a n/a n/a H/s max: n/a H/s
[2018-05-17 03:16:26] speed 2.5s/60s/15m 70.5 n/a n/a H/s max: n/a H/s




# Discussion History
## zurajm | 2018-05-17T17:53:26+00:00
Hi,
I could be wrong, but I think that when switching algo to **cryptonight-heavy** hash rate gets almost halved and I think that is "by design", cryptonight-heavy algo should be more difficult to solve. For instance, I'm mining sumo and before switching to -heavy algo my combined speed (proxy, multiple CPU miners) was around 3Khash, now I only get from 1-1.4Khash/s.
I also had to manually specify **threads** otherwise I get even lower hash rate, bacause not all cores are active. My config is like this:
```json
{
    "algo": "cryptonight-heavy",
    "api": {
        "port": 0,
        "access-token": null,
        "worker-id": null,
        "ipv6": false,
        "restricted": true
    },
    "av": 0,
    "background": false,
    "colors": true,
    "cpu-affinity": 21845,
    "cpu-priority": null,
    "donate-level": 1,
    "huge-pages": true,
    "hw-aes": null,
    "log-file": null,
    "max-cpu-usage": 100,
    "pools": [
        {
            "url": "x.x.x.x:3333",
            "user": "sc1",
            "pass": "x",
            "rig-id": "sc1",
            "nicehash": true,
            "keepalive": true,
            "variant": -1
        }
    ],
    "print-time": 60,
    "retries": 5,
    "retry-pause": 5,
    "safe": false,
    "threads": 6,
    "user-agent": null,
    "watch": false
}
```
I hope it is helpful.

## lukelat | 2018-05-17T21:30:55+00:00
Thanks @zurajm - this is really helpful.

I guess cryptonight-heavy affects everyone so it's not so bad :)

# Action History
- Created by: lukelat | 2018-05-17T03:34:26+00:00
- Closed at: 2018-06-17T18:03:12+00:00
