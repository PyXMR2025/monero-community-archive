---
title: Command line parameters not working
source_url: https://github.com/xmrig/xmrig/issues/715
author: UselessGuru
assignees: []
labels: []
created_at: '2018-07-08T23:47:34+00:00'
updated_at: '2018-07-17T21:51:38+00:00'
type: issue
status: closed
closed_at: '2018-07-17T21:51:19+00:00'
---

# Original Description
As it seems  XMRig/2.6.3 libuv/1.20.3 MSVC/2017 is completely ignoring the command lines parameters and always uses config.json:

```
xmrig.exe --api-port=3334 -a cryptonightV7 -o stratum+tcp://us-east.cryptonight-hub.miningpoolhub.com:20580 -u MyUser:Name -p x --keepalive --nicehash --donate-level 1
 * VERSIONS     XMRig/2.6.3 libuv/1.20.3 MSVC/2017
 * HUGE PAGES   available
 * CPU          Intel(R) Core(TM) i5-8600K CPU @ 3.60GHz (1) x64 AES-NI
 * CPU L2/L3    1.5 MB/9.0 MB
 * THREADS      5, cryptonight, av=0, donate=5%
 * POOL #1      proxy.fee.xmrig.com:9999 variant 1
 * COMMANDS     hashrate, pause, resume
[2018-07-09 01:46:02] READY (CPU) threads 5(5) huge pages 5/5 100% memory 10.0 MB
[2018-07-09 01:46:02] use pool proxy.fee.xmrig.com:9999 108.61.164.63
[2018-07-09 01:46:02] new job from proxy.fee.xmrig.com:9999 diff 20000 algo cn/1
```


# Discussion History
## Smeagol001 | 2018-07-09T01:13:22+00:00
have same problem aparantly even if i fall back to the 2.6.2 it does the same just ignoring everything i have configured in awesomeminer and is defaulting to proxy.fee.xmrig.com:9999

## UselessGuru | 2018-07-09T05:01:16+00:00
>  even if i fall back to the 2.6.2 

Yep, so do I

## xmrig | 2018-07-09T05:23:01+00:00
`cryptonightV7` is not valid algorithm name, so miner ignore all command line params and try failback to config.json in same directory with exe file, more details https://github.com/xmrig/xmrig-amd/issues/135#issuecomment-399905956

## Smeagol001 | 2018-07-09T06:14:10+00:00
for me its not working with "cryptonight" which is default value in awesomeminer and cant be changed from my side it seems

## xmrig | 2018-07-09T07:08:21+00:00
@Smeagol001 Is it possible somehow get full command line?
Thank you.

## Smeagol001 | 2018-07-09T15:07:55+00:00
What do you mean

xmrig <notifications@github.com> schrieb am Mo., 9. Juli 2018, 09:08:

> @Smeagol001 <https://github.com/Smeagol001> Is it possible somehow get
> full command line?
> Thank you.
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/715#issuecomment-403381056>, or mute
> the thread
> <https://github.com/notifications/unsubscribe-auth/ANMMzd7pqRLsNCYCU-DzC0ynOFtSvBmKks5uEwFtgaJpZM4VG7DA>
> .
>


## xmrig | 2018-07-10T17:01:27+00:00
@Smeagol001 I don't use awesome miner, so don't know how it works, if it use command line to run miner, that command line params can help to understand what exactly wrong.
Thank you.

## UselessGuru | 2018-07-17T21:51:18+00:00
> cryptonightV7 is not valid algorithm name

For me this is working well when I use the correct algos as listed here:
xmrig/xmrig-amd#135



# Action History
- Created by: UselessGuru | 2018-07-08T23:47:34+00:00
- Closed at: 2018-07-17T21:51:19+00:00
