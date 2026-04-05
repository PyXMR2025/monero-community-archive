---
title: Cryptonight light FX8350
source_url: https://github.com/xmrig/xmrig/issues/241
author: gregtap
assignees: []
labels: []
created_at: '2017-12-06T10:39:20+00:00'
updated_at: '2018-03-14T23:32:31+00:00'
type: issue
status: closed
closed_at: '2018-03-14T23:32:31+00:00'
---

# Original Description
It detects 6 threads as the optimum, but 8 is the right number.
Out of the box, 6 threads, 650 mh/s

8 threads, 950 mh/s

AEON stak does 1320 mh/s


# Discussion History
## xmrig | 2017-12-06T15:39:14+00:00
It rare case when `--max-cpu-usage` option really works, 75% by default.
Thank you. 

## gregtap | 2017-12-06T15:50:42+00:00
I had this one set to 100% but I will try again and report. Thks.

## lisergey | 2017-12-07T12:04:07+00:00
I've seen hashrate 1235 H/s with
VERSIONS:     XMRig/2.4.2 libuv/1.14.1 gcc/7.2.0
HUGE PAGES:   available, enabled
CPU:          AMD FX(tm)-8350 Eight-Core Processor            (1) x64 AES-NI
THREADS:      4, cryptonight-lite, av=2, donate=2%, affinity=0xCA
or affinity=0xAA

## RyokoZekem | 2018-02-19T17:55:49+00:00
I run into issues trying to run it on cryptonight-lite. It says share is above target. The hash rate is 900 h/s with cryptonight-lite but it just doesnt want to play nice.  I've tried disabling huge pages, changing thread count, changing to av=4 ect. Its the cryptonight-lite settings. Am I doing something wrong here? 

## lisergey | 2018-02-19T18:34:03+00:00
@RyokoZekem, try to reboot. It's weird, it should not be so, but my FX8350 sometimes slows with no reason. Simple stupid reboot helps, sometimes several times until hashrate is normal.
I tried many options, diagnosis, anything to find reasons why - not yet found.

with
    "algo": "cryptonight-lite", // cryptonight (default) or cryptonight-lite
    "av": 2,                    // algorithm variation, 0 auto select
    "threads": 4,               // number of miner threads
    "cpu-affinity": "0x55",     // set process affinity to CPU core(s), mask "0x3" for cores 0 and 1
it's stable 1234 h/s

## xmrig | 2018-02-19T18:58:05+00:00
`cryptonight-lite` only for AEON coin, not usable for other coins like Monero, etc.
Spontaneous slow down can caused because background activity in OS, updates, antivirus scans or something like that.
Thank you.

## lisergey | 2018-02-19T19:26:21+00:00
@xmrig, it is not slow down during run, it is when launched, and keeping it low. Re-launch does not help. Reboot usually helps, but sometimes two or three times.
I think it's kinda bug in the CPU handling/assinging L3 cache to cores.
I've seen in per-thread reports through API that some threads were running with "double cache" speed while in config was av=1. I think it does not relate to xmrig.

@xmrig, thank you for the great program! It's awesome, while simple and effective. My deep respect to you.

## RyokoZekem | 2018-02-20T05:20:30+00:00
Okay thanks. I figured it out. As xmrig pointed out I was using it improperly. Its running fine now using just the normal cryptonight. 7 threads and -a 1 seems to work best for 377 h/s. 4.0ghz with a -1.18v undervolt and turbo disabled. Thank you very much for the awesome tool xmrig. †God bless you.

# Action History
- Created by: gregtap | 2017-12-06T10:39:20+00:00
- Closed at: 2018-03-14T23:32:31+00:00
