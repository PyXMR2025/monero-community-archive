---
title: Advanced threads mode
source_url: https://github.com/xmrig/xmrig/issues/563
author: xmrig
assignees: []
labels:
- META
created_at: '2018-04-19T13:21:27+00:00'
updated_at: '2024-07-23T20:22:47+00:00'
type: issue
status: closed
closed_at: '2018-05-05T06:46:44+00:00'
---

# Original Description
In **v2.6.0-beta3** added **advanced threads mode** and extended low power modes.

## Advanced threads mode
Now `threads` field in config can accept object with individual threads configuration:
```json
"threads": [
        {"low_power_mode": true,  "affine_to_cpu": 0 },
        {"low_power_mode": false, "affine_to_cpu": 1 },
        {"low_power_mode": 1,     "affine_to_cpu": 2 },
        {"low_power_mode": 3,     "affine_to_cpu": false }
],
```

**low_power_mode** number between `1` and `5` or boolean, `false` equal to `1` and `true` equal to `2`. When set to a number N greater than 1, this mode will increase the cache usage and single thread performance by N times.
**affine_to_cpu** This can be either false (no affinity), or the CPU core number.

Changed huge pages allocation strategy, now each thread allocate huge pages by self.

### Backward compatibility
* Miner can work with config from previous versions, where is threads set as number or `null`.
* Options `av` and `cpu-affinity` has no effect in advanced mode.
* New option `hw-aes` works only in advanced mode.
* Threads array compatible with xmr-stak.

### New --av modes
* `--av=5` Triple hash mode
* `--av=6` Quard hash mode
* `--av=7` Penta hash mode
* `--av=8` Triple hash mode (Software AES)
* `--av=9` Quard hash mode  (Software AES)
* `--av=10` Penta hash mode  (Software AES)


# Discussion History
## septuig | 2018-04-20T13:44:42+00:00
How to config "Advanced threads mode" with CN7. 
My CPUs: 
CPU: Intel(R) Xeon(R) CPU E5-2680 v2 @ 2.80GHz (2) x64 AES-NI
CPU L2/L3: 10.0 MB/50.0 MB
Thank you.

## sergneo | 2018-04-20T20:24:53+00:00
the beta3 version does not have AES CPU like Core2 Duo Quad Xeon running a bit slower

## 2010phenix | 2018-04-22T13:08:21+00:00
Who extremely want Advanced threads mode for big L3 cache and without L4 cache
Any test and good Hashrate up ?


## xmrig | 2018-04-22T14:20:23+00:00
Advanced mode it not just additional x3 x4 and x5 hashing modes, it possibility to mix together threads with different memory requirements and human friendly CPU affinity. Very common case mix x1 and x2 threads was not possible before.

* It good for Aeon (cryptonight-lite) x4 (lite) equal to x2 mode, both require same 4 MB of cache.
* It may useful in no so good case, virtual servers where number of vCPU cores limited, but it depends very much on neighbors.
* CPUs with big L4 cache (128 MB) was successfully tested, when it was added in xmr-stak.

## nsummy | 2018-04-23T06:42:19+00:00
I want to personally thank you for adding in the pentahash mode.  I am testing it out right now.  The XMR-Stak version has an issue where it will eventually dip down to half the hash rate.  Stopping and starting the miner fixes it immediately.  They claim its throttling or overheating, but I know its not.  I'll update here as to whether the same thing happens.  Thank you!

## artcannibal | 2018-05-03T04:13:59+00:00
Hi, 
how to set "affine_to_cpu":  to CPU socket 2 or 3 or 4 in multiprocessor platform?
And additiona question:
New Intel CPU (like Xeon Silver 4114) has a lot of L2 cache +L3 cache (20Mb+28Mb in dual platform), will new versions of xmrig support to use them for more prefomance?

## DarthMiner88 | 2020-02-18T16:53:59+00:00
Guyz, what should be the instruction for cpu-affinity, if i want to start xmrig from the 5th core, i have a Ryzen 5 2600, but the first 4th cores im planning to use another miner for a different algo

## bitcoin981 | 2022-04-17T02:17:46+00:00
Hola buenas noches quisiera saber ya obtener mis criptomonedas ethereum y bitcóin USDT. Att Julio Cesar Mena Diaz 
Juliocesarmenadiaz03@gmail.com
+524774807526

## makhamakha | 2024-07-23T20:22:46+00:00
makhamakha colbertmakhale@gmail.com +27734308622

# Action History
- Created by: xmrig | 2018-04-19T13:21:27+00:00
- Closed at: 2018-05-05T06:46:44+00:00
