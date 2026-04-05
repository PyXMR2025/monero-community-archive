---
title: 'how to disable stdout in background=true mode? '
source_url: https://github.com/xmrig/xmrig/issues/1141
author: qutimqqcom
assignees: []
labels:
- bug
created_at: '2019-08-27T09:33:19+00:00'
updated_at: '2019-08-31T02:01:48+00:00'
type: issue
status: closed
closed_at: '2019-08-31T02:01:48+00:00'
---

# Original Description
previos version work silent

# Discussion History
## xmrig | 2019-08-27T21:22:56+00:00
I can't reproduce the issue, please provide more details.
Thank you.

## qutimqqcom | 2019-08-28T09:38:49+00:00
setup daemon mode using "background": true,
process fall to background 
but  logs appear  in console 

 * ABOUT        XMRig/3.1.0 gcc/7.4.1
 * LIBS         libuv/1.30.1 hwloc/1.11.8rc2-git
 * CPU          Intel(R) Core(TM) i7-4790 CPU @ 3.60GHz (1) x64 AES
                L2:1.0 MB L3:8.0 MB 4C/8T NUMA:1
 * DONATE       5%
 * ASSEMBLY     auto:intel
 * POOL #1      111.22.22.1:10016 algo auto
 * COMMANDS     hashrate, pause, resume

[2019-08-28 12:31:21.667] use pool 111.22.22.1:10016  111.22.22.1
[2019-08-28 12:31:21.667] new job from 111.22.22.1:10016 diff 500 algo cn/r height 1910587
[2019-08-28 12:31:21.667]  cpu  use profile  cn/r  (2 threads) scratchpad 2048 KB
[2019-08-28 12:31:22.166]  cpu  READY threads 2(2) huge pages 2/2 100% memory 4096 KB (499 ms)
[2019-08-28 12:31:33.896] accepted (2/0) diff 500 (196 ms)
[2019-08-28 12:31:33.961] accepted (3/0) diff 500 (94 ms)

## xmrig | 2019-08-30T06:59:56+00:00
I can't reproduce the issue, for me option `background` works fine, please provide all details, what OS do you use, how exactly option set: config, command line or mixed, etc.
Thank you.

## xmrig | 2019-08-30T07:16:51+00:00
Okay, fine I got this issue, this happen if no other logs options specified, `log-file` or `syslog`.

## xmrig | 2019-08-30T07:47:03+00:00
Fixed in dev branch.

## qutimqqcom | 2019-08-30T18:44:38+00:00
> Fixed in dev branch.

Can users take the dev version for the build?

## xmrig | 2019-08-30T22:33:39+00:00
https://buildbot.xmrig.com/#/ every commit in master, dev, evo and beta branches has binary builds also I will make v3.1.1 release soon.

## xmrig | 2019-08-31T02:01:48+00:00
https://github.com/xmrig/xmrig/releases/tag/v3.1.1

# Action History
- Created by: qutimqqcom | 2019-08-27T09:33:19+00:00
- Closed at: 2019-08-31T02:01:48+00:00
