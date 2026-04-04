---
title: ' monerod is crashing  when solo mining'
source_url: https://github.com/monero-project/monero/issues/6704
author: maogo
assignees: []
labels: []
created_at: '2020-07-12T15:40:38+00:00'
updated_at: '2020-07-20T05:19:36+00:00'
type: issue
status: closed
closed_at: '2020-07-20T05:19:36+00:00'
---

# Original Description
2020-07-12 15:33:34.053	11120	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO


# Discussion History
## moneromooo-monero | 2020-07-12T15:46:39+00:00
Do you have a stack trace for the crash ?

## maogo | 2020-07-12T17:23:07+00:00
and sometimes got this:
![6UXM7_0N2)~S6D@V$6QZDVW](https://user-images.githubusercontent.com/20197997/87252614-0cb51d00-c4a7-11ea-9f31-1eb8bbdff5fc.png)


## trasherdk | 2020-07-12T18:08:40+00:00
Looks like a pruned blockchain. Mine does the same, but everything seems to work.
```
2020-07-12 18:06:42.096        E   failed to find tx meta
2020-07-12 18:06:42.096        E   failed to find tx meta
2020-07-12 18:06:42.096        E   failed to find tx meta
2020-07-12 18:06:42.096        E   failed to find tx meta
2020-07-12 18:06:42.096        E   failed to find tx meta
2020-07-12 18:06:42.096        E   failed to find tx meta
2020-07-12 18:06:42.096        E   failed to find tx meta
status 
Height: 621501/621501 (100.0%) on stagenet, not mining, net hash 1.27 kH/s, v12, 3(out)+4(in) connections, uptime 6d 12h 24m 57s
```

## moneromooo-monero | 2020-07-12T18:15:51+00:00
You can ignore the meta message, it's harmless.

## maogo | 2020-07-13T03:57:32+00:00
> Do you have a stack trace for the crash ?

I can't debug , is there any other way?

## maogo | 2020-07-13T04:15:08+00:00
> Looks like a pruned blockchain.  

 local blockchain DB is full

## moneromooo-monero | 2020-07-13T13:38:09+00:00
What platforn is it running on ?

## maogo | 2020-07-13T14:26:07+00:00
> What platforn is it running on ?

Windows 10 professional  64 bit , version number 2004.   v0.15 work well .

## moneromooo-monero | 2020-07-13T16:50:52+00:00
Is it a Ryzen CPU ?

## maogo | 2020-07-13T19:50:16+00:00
Yes , Ryzen 1800X

## moneromooo-monero | 2020-07-13T23:09:06+00:00
Some Ryzen CPUs are known to be buggy in a way that makes them crash on randomx. IIRC there may be a workaround to do with disabling something to do with micro-op caching. I'll ask around.

## SChernykh | 2020-07-14T05:23:50+00:00
> Some Ryzen CPUs are known to be buggy in a way that makes them crash on randomx. IIRC there may be a workaround to do with disabling something to do with micro-op caching. I'll ask around.

Disabling opcache in BIOS helps. Or running without JIT.

## maogo | 2020-07-14T06:03:22+00:00
I  have  disabled opcache  control in BIOS  but look the same.

## SChernykh | 2020-07-14T06:07:24+00:00
The opcache fix is only for when it crashes during mining.

## maogo | 2020-07-14T06:24:56+00:00
Within seconds the monerod will crash when start mining

## SChernykh | 2020-07-14T06:30:52+00:00
Disabling opcache should've helped. You can try solo mining with XMRig, it supports mining directly to monerod and it has a fix for this crash.

## SomethingGettingWrong | 2020-07-14T06:32:40+00:00
> > Some Ryzen CPUs are known to be buggy in a way that makes them crash on randomx. IIRC there may be a workaround to do with disabling something to do with micro-op caching. I'll ask around.
> 
> Disabling opcache in BIOS helps. Or running without JIT.

Ryzen Cpu's are like the "ONLY" profitable Cpu's for the most part. if you disable micro-op caching the proccesor will be bad at everything else  and only good FOR mining. which means if you want to only dedicate a percentage of your cores to solo your pc will be much slower. thats a shame.  why is it only some ryzen cpu's? 
Which one should i avoid if i wnat to mine monero solo?


## SChernykh | 2020-07-14T06:49:36+00:00
>  why is it only some ryzen cpu's?

There's a hardware bug in some early 1st-gen Ryzen CPUs, but not all of them. XMRig has a workaround for it and can mine even with enabled opcache.

## moneromooo-monero | 2020-07-14T11:40:05+00:00
Would you mind adding the workaround to monerod ? It'd be a shame if someone people can't solo mine and are forced to use pools in order to mine :)

## SChernykh | 2020-07-14T12:20:56+00:00
@moneromooo-monero It's quite invasive workaround and it messes with low-level exception handling. It made sense in a specialized miner software for performance reasons, but I think it's not worth adding it to monerod for just a small fraction of 1st-gen Ryzens. Besides, that crash was always fixed by disabling opcache, so I'm not sure if it's the same crash here.

# Action History
- Created by: maogo | 2020-07-12T15:40:38+00:00
- Closed at: 2020-07-20T05:19:36+00:00
