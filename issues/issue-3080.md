---
title: newbie help
source_url: https://github.com/xmrig/xmrig/issues/3080
author: ServerNut
assignees: []
labels: []
created_at: '2022-07-02T08:22:27+00:00'
updated_at: '2025-06-28T10:43:08+00:00'
type: issue
status: closed
closed_at: '2025-06-28T10:43:08+00:00'
---

# Original Description
Hi there started using xmrig on my dual xeon 5690 machine and it only uses 5 cores,  any ideas guys

have put it startup for details

![xmr](https://user-images.githubusercontent.com/108569821/176992884-afb17d74-8a1c-416f-9986-bee0d8141122.jpg)


thanks in advance


# Discussion History
## Spudz76 | 2022-07-04T04:33:20+00:00
6 is max anyway (12MB / 2MB = 6)

Unclear why it chose less, if you didn't use any of the hint options (`--cpu-max-threads-hint=N` or `--threads=N`) during firstrun.

Erase config.json algorithm thread definitions and re-run the firstrun it should use 6 per CPU (12 total).

## ServerNut | 2022-07-04T07:39:40+00:00
OK i understand that part by why wont it use the 2nd cpu and L3 cache 

Thanks

## SChernykh | 2022-07-04T07:51:12+00:00
> why wont it use the 2nd cpu and L3 cache

Probably for the same reason it runs 10 threads and not 12. You're using some weird incorrect config for this CPU. Regenerate it from scratch, use https://xmrig.com/wizard

## Spudz76 | 2022-07-04T23:40:46+00:00
it is using the second cpu (10 threads = 5 * 2 cpus)

## ServerNut | 2022-07-05T08:35:46+00:00
thanks guys played around with it  like you told me too and got it sorted

Thanks

## Spudz76 | 2022-07-05T16:26:31+00:00
I wonder if you thought `5 tx` meant 5 threads?  (that is transaction count for block `2658376`)

## Lonnegan | 2022-07-07T23:55:06+00:00
Anyway, the Intel Westmere architecture, although it already supports AES, seems to be not suitable for RandomX mining. I have an Intel Xeon E5-2600 in my pool which is based on the one year younger Sandy Bridge architecture, it's running at 1200 H/s using only 3 of its 4 cores. Your Intel Xeon X5690 reaches the same output, but needs 10 cores for that. That cannot be true. Something seems to be really going wrong here! Perhaps it's memory bandwidth limited due to that strange allocation, placing the JIT memory only on one node?

# Action History
- Created by: ServerNut | 2022-07-02T08:22:27+00:00
- Closed at: 2025-06-28T10:43:08+00:00
