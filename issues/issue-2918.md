---
title: '"net no active pools, stop mining" from XMrig-6.16.3 Ubuntu 20.04 version'
source_url: https://github.com/xmrig/xmrig/issues/2918
author: sunbearc22
assignees: []
labels: []
created_at: '2022-02-03T14:14:30+00:00'
updated_at: '2022-02-06T08:09:57+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**Describe the bug**
I noticed several `net no active pools, stop mining` from XMrig-6.16.3 linux Ubuntu 20.04 version. Regular occurrences consistently happen per day. All the jobs just stop and then new batches of jobs are started up. CPU cores load drops to 0 and then ramp back up again.

**To Reproduce**
`$ sudo ./xmrig -o pool.xmrfast.com:9000 -u <mywallet> -k --tls --rig-id white -a rx/0 --huge-pages-jit --randomx-1gb-pages --randomx-mode=fast --astrobwt-avx2 --astrobwt-max-size=600`

**Expected behavior**
Continuous mining operation without `net no active pools, stop mining` issue



# Discussion History
## Spudz76 | 2022-02-03T20:50:28+00:00
If pool sends huge difficulty and you don't have results every 60-120 seconds max, the connection will time out.  Nanopool is usually the problem maybe xmrfast is just as badly configured (no autodiff, no manually selected diff).

If xmrfast supports specifying a diff via user or pass set that to 30 times your hashrate.  Then it should keep alive.  Sometimes `keepalive` itself doesn't actually work so then you need actual result traffic to keep the hangup timer on the server end from hitting the trigger time.

You could also verify that your own router isn't set to timeout TCP connections way too early, like less than 300 or 600 seconds so that only the other side could ever timeout.  Then you're limited by the server side setting usually 120 seconds but they could set it less if they want to kick idle miners as soon as possible (35 seconds lol)

## sunbearc22 | 2022-02-05T07:56:27+00:00
I found XMRFAST allows a user to define the difficulty. I had set it to 333333 via the below command. The `net no active pools, stop mining` issue still occurs.

`$ sudo ./xmrig -o pool.xmrfast.com:9000 -u <mywallet>+333333 -k --tls --rig-id white -a rx/0 --huge-pages-jit --randomx-1gb-pages --randomx-mode=fast --astrobwt-avx2 --astrobwt-max-size=600`

## Spudz76 | 2022-02-05T18:55:03+00:00
So then your hashrate would be 11111.1H/s ?

## sunbearc22 | 2022-02-06T06:25:43+00:00
@Spudz76 Can you explain to me how you had derived the 11111.1H/s hashrate when the difficulty is 333333? I chose 333333 because this was the range of diff that XMRIG had reported when shares were accepted and when diff was not specified. 

XMRig reports  `miner    speed 10s/60s/15m 10711.8 10661.1 10650.8 H/s max 10782.5 H/s` 

On XMRFAST dashboard, the average hashrate per 8 hrs is ~10.4KH/s but the average hashrate per 5 mins fluctuates btw 4.6KH/s to 14.6KH/s. 


## Spudz76 | 2022-02-06T08:09:29+00:00
Standard 30 times your hashrate (or backward, difficulty divided by 30)

This would result in an average of one result every 30 seconds.

# Action History
- Created by: sunbearc22 | 2022-02-03T14:14:30+00:00
