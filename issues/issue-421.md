---
title: Question on Hash Rate @ Intel(R) Xeon(R) CPU E5-2660 v2
source_url: https://github.com/xmrig/xmrig/issues/421
author: kimats
assignees: []
labels:
- NUMA
created_at: '2018-03-01T13:30:10+00:00'
updated_at: '2019-08-02T12:54:36+00:00'
type: issue
status: closed
closed_at: '2019-08-02T12:54:28+00:00'
---

# Original Description
Hello,

Please have  a look if the hash rate is right or not...I think it is lower?

 * VERSIONS:     XMRig/2.4.5 libuv/1.8.0 gcc/5.4.0
 * HUGE PAGES:   available, enabled
 * CPU:          Intel(R) Xeon(R) CPU E5-2660 v2 @ 2.20GHz (1) x64 AES-NI
 * CPU L2/L3:    1.2 MB/25.0 MB
 * THREADS:      12, cryptonight, av=1, donate=1%
 * POOL #1:      pool.supportxmr.com:7777
 * COMMANDS:     hashrate, pause, resume

[2018-03-01 21:26:04] use pool pool.supportxmr.com:7777 103.253.40.188
[2018-03-01 21:26:04] new job from pool.supportxmr.com:7777 diff 25000
[2018-03-01 21:27:07] speed 2.5s/60s/15m 513.6 513.5 n/a H/s max: 513.6 H/s
[2018-03-01 21:27:45] new job from pool.supportxmr.com:7777 diff 11538
[2018-03-01 21:28:05] accepted (1/0) diff 11538 (312 ms)
[2018-03-01 21:28:07] speed 2.5s/60s/15m 513.7 513.4 n/a H/s max: 514.3 H/s
[2018-03-01 21:28:12] accepted (2/0) diff 11538 (313 ms)
[2018-03-01 21:28:44] new job from pool.supportxmr.com:7777 diff 5000

config file is:
  "algo": "cryptonight",
    "background": false,
    "colors": true,
    "retries": 5,
    "retry-pause": 5,
    "donate-level": 1,
    "syslog": false,
    "log-file": null,
    "print-time": 60,
    "av": 0,
    "safe": false,
    "max-cpu-usage": 95,
    "cpu-priority": 4,
    "threads": null,


# Discussion History
## sfeldmanjr | 2018-03-01T22:29:58+00:00
I'm running 2x E5-2660 and you are pulling better numbers with just 1 CPU plus a lower cpu-priority. Odd.

 * VERSIONS:     XMRig/2.4.5 libuv/1.8.0 gcc/7.1.0
 * HUGE PAGES:   available, enabled
 * CPU:          Intel(R) Xeon(R) CPU E5-2660 0 @ 2.20GHz (2) x64 AES-NI
 * CPU L2/L3:    8.0 MB/40.0 MB**
 * THREADS:      20, cryptonight, av=1, donate=5%
 * POOL #1:      ca.minexmr.com:3333
 * COMMANDS:     hashrate, pause, resume
**[2018-03-01 22:23:49] speed 2.5s/60s/15m 400.7 388.2 n/a H/s max: 400.7 H/s
[2018-03-01 22:24:22] speed 2.5s/60s/15m 400.3 397.9 n/a H/s max: 401.2 H/s
[2018-03-01 22:26:22] speed 2.5s/60s/15m 400.3 400.7 n/a H/s max: 401.4 H/s**

"algo": "cryptonight",
"av": 0,
"background": false,
"colors": true,
"cpu-affinity": null,
"cpu-priority": 5,
"donate-level": 5,
"log-file": null,
"max-cpu-usage": 95, 
"print-time": 60,
"retries": 5,
"retry-pause": 5,
"safe": false,
"syslog": false,
"threads": null,

## DrStein99 | 2018-03-01T23:53:57+00:00
I get about 475 h/s on (1) E5-2650 V1, 20mb cache @ 10 threads.  Fine-tune cpu affinities, and you can get the most out of hash-rate.  The auto-config (for me) only goes so far.

## kimats | 2018-03-02T00:16:18+00:00
@sfeldmanjr 
I feel happy now..(just a joke), which OS do you run? I use Ubuntu 16.04 Server...

@DrStein99 
Hero, I try to figure out CPU affinities, after reading wiki and issues opened... I see most of them are connected to NUMA.... 
And I am totally lost at CPU affinities,,,Could you please help me on this settings?

## sfeldmanjr | 2018-03-02T18:52:03+00:00
@kimats 
Debian 9 at the moment.

## g5-freemen | 2018-03-03T12:15:58+00:00
**kimats**
I'm not sure, but Intel site shows that E5-2660 v2 have 10 cores (20 threads) so why u using 12 threads? As i know Xmrig shows best performance if core number = xmrig threads number. Maybe i'm wrong, try to experiment with it.

**sfeldmanjr**
the same thing, Intel site shows E5-2660 = 8 cores, maybe try 8 xmrig threads ?

for me with Core i7-8700K (6 cores) @4.4Ghz xmrig (with 6 threads) shows now 360-438 H/s


## g5-freemen | 2018-03-03T12:19:33+00:00
Looks like XMRig have problems with auto config or xmrig set number of threads depending on CPU L2/L3 cache ?

## 2010phenix | 2018-03-03T13:17:35+00:00
@g5-freemen number of threads depending on CPU L3 cache
and about NUMA look on github.. already done by 2 person.. 2 version of this part

## kimats | 2018-03-03T13:36:36+00:00
@g5-freemen 
Hello man,
it is do related to L3 cache... the support team said, 4M=1thread..

## kimats | 2018-03-03T13:38:50+00:00
@2010phenix 
man, as a normal user,,,quite difficult to  look at github to figure out ... I just use the tutorial to build the application...what problem the NUMA solve? what shall i do？

## minzak | 2018-03-21T15:54:33+00:00
@DrStein99 Cool HashRate! What yours config?
How to configure 2xE5-2660v1 ?
Thanks.

## DrStein99 | 2018-03-29T16:58:06+00:00
Here are the relavant config settings I used for (2) E5- 2670 v1

`
	"cpu-affinity"	: "0xB9F8C75B",
	"cpu-priority"	: 4,
	"max-cpu-usage"	: 85,
	"safe"			: false,
`

## minzak | 2018-03-29T18:44:57+00:00
Thanks, i test with this cpu-affinity, but 701H - it is max.
In default variants with null - 715H - is max.

I think it is maximum, because i not see more Hashrate.

## xmrig | 2019-08-02T12:54:28+00:00
#1077 

# Action History
- Created by: kimats | 2018-03-01T13:30:10+00:00
- Closed at: 2019-08-02T12:54:28+00:00
