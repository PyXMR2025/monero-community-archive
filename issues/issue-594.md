---
title: v2.6.0-beta3 100H/s less than 2.5.3 release
source_url: https://github.com/xmrig/xmrig/issues/594
author: jcastro
assignees: []
labels:
- bug
created_at: '2018-04-30T13:25:57+00:00'
updated_at: '2019-08-02T13:58:55+00:00'
type: issue
status: closed
closed_at: '2019-08-02T13:58:55+00:00'
---

# Original Description
Hey guys,

So I just found out that v2.6.0-beta3 gives me 100H/s less than 2.5.3 release

This is the output for 2.5.3 release
` * VERSIONS:     XMRig/2.5.3 libuv/1.19.2 gcc/5.4.0
 * HUGE PAGES:   available, disabled
 * CPU:          Genuine Intel(R) CPU 0000 @ 2.00GHz (1) x64 AES-NI
 * CPU L2/L3:    5.0 MB/50.0 MB
 * THREADS:      25, cryptonight, av=1, donate=1%
 * POOL #1:      pool.supportxmr.com:7777
 * COMMANDS:     hashrate, pause, resume
[2018-04-30 15:24:10] use pool pool.supportxmr.com:7777 149.202.83.171
[2018-04-30 15:24:10] new job from pool.supportxmr.com:7777 diff 25000
[2018-04-30 15:24:17] new job from pool.supportxmr.com:7777 diff 40541
[2018-04-30 15:24:19] speed 2.5s/60s/15m 764.4 n/a n/a H/s max: 762.9 H/s`

This is the one from the beta3

` * VERSIONS:     XMRig/2.6.0-beta3 libuv/1.19.2 gcc/5.4.0
 * CPU:          Genuine Intel(R) CPU 0000 @ 2.00GHz (1) x64 AES-NI
 * CPU L2/L3:    5.0 MB/50.0 MB
 * THREADS:      25, cryptonight, av=1, donate=1%
 * POOL #1:      pool.supportxmr.com:7777
 * COMMANDS:     hashrate, pause, resume
[2018-04-30 15:22:27] READY (CPU) threads 25(25) huge pages 0/25 0% memory 50.0 MB
[2018-04-30 15:22:27] use pool pool.supportxmr.com:7777 37.59.52.83
[2018-04-30 15:22:27] new job from pool.supportxmr.com:7777 diff 25000
[2018-04-30 15:22:32] accepted (1/0) diff 25000 (66 ms)
[2018-04-30 15:22:44] new job from pool.supportxmr.com:7777 diff 44100
[2018-04-30 15:23:04] speed 2.5s/60s/15m 626.6 n/a n/a H/s max: 635.7 H/s`

# Discussion History
## 2010phenix | 2018-04-30T23:20:42+00:00
use more long time frame for test speed

## JuanMao1997 | 2018-05-01T07:01:50+00:00
Hash rate will be stable after 3~24 hours. BTW, did u mine xmo? I found xmo speed was slower than xmr.

## jcastro | 2018-05-01T08:18:15+00:00
I’m mining XMR

yeah I mined for several hours, it’s just I wanted to copy the output for the report

Thanks guys!

Sent from my iPhone

> On 1 May 2018, at 01:20, 2010phenix <notifications@github.com> wrote:
> 
> use more long time frame for test speed
> 
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub, or mute the thread.
> 


## proton171717 | 2018-05-02T08:07:04+00:00
HugePages disabled!?
Do you try with to enable?
I tried 2.6.0 beta1 - it was the same like 2.5.3

my cpus are 4 x E7-4830 
ubuntu OS

## jcastro | 2018-05-02T09:42:03+00:00
@proton171717 I don't explicitly have it disabled on the command line and I'm running it as root so I'm not sure why they're not enabled... but looking at the readme there's no way to force it other than executing it as root which I'm already doing

## proton171717 | 2018-05-02T12:52:35+00:00
@jcastro which is your OS - root means linux - ubuntu/deb ??
at ubuntu/deb youhave to add line in file.

## jcastro | 2018-05-02T12:54:05+00:00
It’s unRaid, which uses as a base Slackware

> On 2 May 2018, at 14:52, proton171717 <notifications@github.com> wrote:
> 
> @jcastro <https://github.com/jcastro> which is your OS - root means linux - ubuntu/deb ??
> at ubuntu/deb youhave to add line in file.
> 
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub <https://github.com/xmrig/xmrig/issues/594#issuecomment-385967108>, or mute the thread <https://github.com/notifications/unsubscribe-auth/AALmVPFRytnve073TIFo7AJzK35mnJd2ks5tuawhgaJpZM4TslFr>.
> 



## proton171717 | 2018-05-02T13:54:33+00:00
with 2.5.3/2 I have better hashrate with gcc7 and weaker with gcc 5  (compiled both)
I downloaded 2.6 without compile + gcc7 = it was the same like upper info 
But in your case the difference is much !!
I use ubuntu server 16.04

## xmrig | 2019-08-02T13:58:55+00:00
Merge with #808 

# Action History
- Created by: jcastro | 2018-04-30T13:25:57+00:00
- Closed at: 2019-08-02T13:58:55+00:00
