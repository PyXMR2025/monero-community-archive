---
title: '[Scratchpad] `monerod` and `cuprated` sync performance'
source_url: https://github.com/Cuprate/cuprate/issues/195
author: hinto-janai
assignees: []
labels:
- C-discussion
- I-perf
created_at: '2024-06-26T15:21:38+00:00'
updated_at: '2024-12-28T13:11:57+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
## What
This issue is a scratch pad for writing down `monerod` and `monerod` sync performance tests.

# Discussion History
## hinto-janai | 2024-06-26T15:24:40+00:00
### VPS
| CPU                    | Core/thread count | Memory           | Disk (sequential read, write) | Disk (random read, write) |
|------------------------|-------------------|------------------|-------------------------------|---------------------------|
| Intel Xeon E5 2698 v3  | 8/16              | 32 GB, 4000 MT/s | 350 MB/s, 100 MB/s            | 100 MB/s, 44 MB/s

### `monerod.conf`
```bash
fast-block-sync=0 # Enabled/disabled depending on test

prune-blockchain=false
db-sync-mode=fastest:async
max-concurrency=0
prep-blocks-threads=16
log-level=1
no-zmq=true
disable-dns-checkpoints=true
enable-dns-blocklist=true
out-peers=512
in-peers=0
limit-rate-up=1280000
limit-rate-down=1280000

add-priority-node= # ... lots and lots of fast nodes
```

### 2024-06-19 -> 2024-06-26
- `fast-block-sync` was disabled
- 543600s wall clock uptime (6.29 days)
- 1192061s CPU time (2.19 CPU usage, 13% out of total)
- 3179629 height (chain-tip at the time) (5.84 blocks per second)
- Peak memory usage was ~30GB, only around 5-10GB being required, the rest was cache

## hinto-janai | 2024-06-27T01:40:59+00:00
### 2024-06-26
- `fast-block-sync` was enabled
- 37692s wall clock uptime (~10 hours)
- 55877s CPU time (1.48 CPU usage, 9.3% out of total)
- 3109975 height (82.5 blocks per second)
- Peak memory usage was ~23GB, only around ~8GB being required, the rest was cache

At the current rate of 5 blocks / second, it will take another 3.86 hours to finish to the previous height, 3179629, for a total of 51622s wall clock uptime or 14.33 hours.

### 2024-06-27
It took a total wall clock time of ~22 hours to reach the previous height (3179629).

## hinto-janai | 2024-12-18T14:30:59+00:00
### 2024-12-18
Some `cuprated` stats on https://github.com/Cuprate/cuprate/pull/344.

- No fast sync
- 387553s wall clock uptime (4.48 days)
- 3179629 height (8.2 BPS)
- 1133244s CPU time
- Read speeds average at 33% of max sequential
- Write speeds average at 9% of max sequential

Compared to https://github.com/Cuprate/cuprate/issues/195#issuecomment-2191989227:
- Amortized BPS is x1.4 faster
- Amortized CPU usage is similar, within 5%
- BPS speed up is pre-RandomX
- Post-RandomX, BPS = ~5
- Residential and shared memory usage is similar to https://github.com/Cuprate/cuprate/issues/195#issuecomment-2192893288



## SyntheticBird45 | 2024-12-19T16:01:06+00:00
## Virtual Machine (QEMU/KVM)

- AMD Ryzen 9th gen, 16 threads
- Ubuntu Server 24.04 LTS
- 10 GB RAM, 4 GB SWAP
- 300GB NVMe SSD (Logical linux layer. Observed in practice 3GB/s, 2GB/s with logical layer)
- 1 GB/s networking (outbound only)

### `cuprated` (#344) 2024-12-17

- No fast sync
- Synced in 137627.2s | 38.2 hours | ~1.6 days
- Maximum write speed observed 1.6 GB/s (PreRCT started with constant 1.4 GB/s write speed, continuously decreased over time down to ~120 MB/s at the end)
- All CPU cores at a stable average of 17%. (15% preRCT, around 18% postRCT)
- 6GB of RAM used (including active memory mapping), 260GB of used without active pages.
- Database size: 256GB.
- Observed download spike of 80MB/s

![syncing20241217](https://github.com/user-attachments/assets/6067f283-c05b-4b70-8886-53547eb2d595)


## sneurlax | 2024-12-21T17:29:35+00:00
- cuprated (https://github.com/Cuprate/cuprate/pull/344) 2024-12-19
- about 36 hours
- 3-4 internet outages during that time, affecting the graph below. will need to redo "clean"
- 100mbps residential wireless "fiber" (ha)
- i5-13400F on Ubuntu 20.04 with 128gb RAM

![output](https://github.com/user-attachments/assets/713731a3-6c96-481f-bb34-c70b1a2f97c6)

edit: after altering parse_logs.py to skip batch verification time gaps of over 500 seconds:
![output](https://github.com/user-attachments/assets/32e29bcc-bf09-474a-83fb-02f44880dd15)


## sneurlax | 2024-12-23T17:26:34+00:00
- cuprated (https://github.com/Cuprate/cuprate/pull/344) 2024-12-21
- about 36 hours
- 100mbps residential wireless "fiber"
- M2 Max with 96gb RAM
![output](https://github.com/user-attachments/assets/4b978f43-543d-41db-b457-0343fd18738e)


## maogo | 2024-12-24T19:13:05+00:00
cuprated syncing  by default config, How large should a log file be? right now ~ 460M at block height ~ 255264

## SyntheticBird45 | 2024-12-24T20:13:43+00:00
> cuprated syncing by default config, How large should a log file be? right now ~ 460M at block height ~ 255264

All logs are located in `~/.local/share/cuprate/logs/`. There should be multiple files in there. For each day passed, the log file corresponding to that day should be between 2 and 5 GB.

## SyntheticBird45 | 2024-12-24T20:15:05+00:00
@hinto-janai Can I rename this issue into "[Scratchpad] `monerod` and `cuprated` sync performance"

## maogo | 2024-12-26T02:04:45+00:00
- cuprated (https://github.com/Cuprate/cuprate/pull/344) 2024-12-25
- Debian 12, ryzen 1800X 8C/16T, 16 GB RAM, 1 GB SWAP
- NVMe SSD 1.2TiB free
- rustc version 1.83.0 
- Peak cuprated usage: VIRT 127 GiB; RES 10 GiB; CPU 65%. (SWAP 100%)
- Interrupted exception: Segmentation fault happened three times
- 28 hours to reach 2467816  height
- DB size 123.6 GiB

Edit: fully synced ~3.5 days

## SyntheticBird45 | 2024-12-26T10:41:53+00:00
> * cuprated ([cuprated: Init #344](https://github.com/Cuprate/cuprate/pull/344)) 2024-12-25
> 
>     * Debian 12, ryzen 1800X 8C/16T, 16 GB RAM, 1 GB SWAP
> 
>     * NVMe SSD 1.2TiB free
> 
>     * rustc version 1.83.0
> 
>     * Peak cuprated usage: VIRT 127 GiB; RES 10 GiB; CPU 65%. (SWAP 100%)
> 
>     * Interrupted exception: Segmentation fault happened three times
> 
>     * 28 hours to reach 2467816  height
> 
>     * DB size 123.6 GiB

Thanks for the report. We also had another report of segfault during sync on Debian.

# Action History
- Created by: hinto-janai | 2024-06-26T15:21:38+00:00
