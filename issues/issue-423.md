---
title: xmrig-2.4.4-gcc-win64 dual xeon e5-2679 40core/80threads
source_url: https://github.com/xmrig/xmrig/issues/423
author: mzik91
assignees: []
labels:
- NUMA
created_at: '2018-03-02T11:51:17+00:00'
updated_at: '2019-08-02T12:39:39+00:00'
type: issue
status: closed
closed_at: '2019-08-02T12:39:39+00:00'
---

# Original Description
👋 hello to all, I tried to start the mines with autoconfiguration, it works only a 50% processor (only 20core physical of one, the other 20 threads 0%) i use the graphics cards with nicehash, but the program does not support. can anyone help me with the configuration?

# Discussion History
## g5-freemen | 2018-03-03T12:24:03+00:00
"algo": "cryptonight",
"av": 0,
"background": false,
"colors": true,
"cpu-affinity": null,
"cpu-priority": null,
"donate-level": 5,
"log-file": null,
"max-cpu-usage": 100,
"print-time": 60,
"retries": 5,
"retry-pause": 5,
"safe": false,
"syslog": false,
"threads": 20,

try this and you can experiment with "threads", can try to set it to 40, but i think you get performance loss.
also you can try HODL algorithm with hodlminer-avx2, but it's really heavy for CPU

## mzik91 | 2018-03-03T12:42:29+00:00
Thanks, i try your config, if i change only "threads" hs drops to 750 to 500..it's not stable, with default value it's stable to 750/770..I think we need to change cpu affinity or cpu priority, but i don't know how..

## g5-freemen | 2018-03-03T16:55:42+00:00
Cpu priority doesn't important I think 

## g5-freemen | 2018-03-03T17:02:01+00:00
And really read about HODL, nicehash server shows that it is most profitable cpu algorithm 

## mzik91 | 2018-03-03T18:42:30+00:00
I'm trying hodl optimized, uses only one processor, but uses the ht (20core + 20threads) 1700hs..any idea to make the second work?

## CthulhuVRN | 2018-03-05T06:03:59+00:00
@mzik91 try next:
A)
```
"cpu-affinity": "0xFFFFFF80010000000000"
"cpu-priority": 5
"threads": null
```
B)
```
"cpu-affinity": "0xFFFFF000010000000000"
"cpu-priority": 5
"threads": null
```

Variant A uses 50 threads (20 physical and 5 virtual per CPU), because your CPU has L3 50MB, so 25 threads per CPU can be used theoretically. But HT can slow down your total hash rate, then try Variant B (20 physical threads per CPU).

## rtau | 2018-03-05T07:26:39+00:00
In addition to that mentioned by grafptitsyn, you may try using the low power algorithm variant (-av 2), and use only 12 threads.

In low power variants, each thread will require double amount of cache, but will have a higher hash rate per thread.

## mzik91 | 2018-03-05T11:32:32+00:00
thanks for help me, I tried to change cpu affinity copying and pasting both code, I put null in threads. uses 25threads of a single CPU. hs remains the same as before (but when I launch xmr, is it normal that the "huge page" is unavailable?)

## CthulhuVRN | 2018-03-05T11:41:01+00:00
@mzik91 no, it's not normal if you enabled it.

## g5-freemen | 2018-03-05T11:44:16+00:00
Huge page requires reboot system to enable 

## mzik91 | 2018-03-05T12:58:14+00:00
I have enabled a huge page, now the HS is 950. but the operation of the processor is the same ... boh I have no other ideas ..


## CthulhuVRN | 2018-03-05T13:27:21+00:00
@mzik91 "the operation of the processor is the same" - what do you mean?

UPD: What OS do you use? Windows/Linux? There are different CPU affinity rules for different OS. I provided you the Linux kind.

## mzik91 | 2018-03-05T13:57:18+00:00
Windows 10 64bit...(sorry i''m italian) the processor work with 25threads

## CthulhuVRN | 2018-03-05T14:03:36+00:00
@mzik91 
1) "cpu-affinity": "0xAAAAAAAAAAAAA8000000"
2) In case of NUMA nodes check #86

## jamieturnough | 2018-08-01T09:08:43+00:00
Not sure if it will help, but I'm running dual Xeon 8176 ES chips (28core each, but ES chips reduced to 1800-2200mhz with turbo). 
Setting the threads to 28 gives me around 1140 h/s. but I run at 26 and 80% power so I can still use the machine, which reduces down to around 1040 each.

To get both CPU's running I have to run 2 instances of XMRIG, which brings my combined hashrate up to 2000-2200 h/s depending on other loading.

## xmrig | 2019-07-29T02:16:39+00:00
If this issue still actual, please check v2.99.2-beta release #1077.
Thank you.

# Action History
- Created by: mzik91 | 2018-03-02T11:51:17+00:00
- Closed at: 2019-08-02T12:39:39+00:00
