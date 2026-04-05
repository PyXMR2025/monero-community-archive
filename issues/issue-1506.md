---
title: RandomX issue on AMD Bulldozer based systems
source_url: https://github.com/xmrig/xmrig/issues/1506
author: Lonnegan
assignees: []
labels:
- stability
created_at: '2020-01-20T07:03:17+00:00'
updated_at: '2020-08-31T05:48:09+00:00'
type: issue
status: closed
closed_at: '2020-08-31T05:48:09+00:00'
---

# Original Description
Hi,

since Monero has switched to RandomX, my AMD Bulldozer based systems don't run smooth anymore. They work with xmrig for hours or days, but sometimes they stop to hash. The program continues to run, but the hashrate drops to 0. Same for RandomXL. I've attached a screenshot from Hashvault, where you can see the problem.
![xmrig_bulldozer](https://user-images.githubusercontent.com/60088495/72705222-35450580-3b5b-11ea-94a7-1337e342267d.png)


# Discussion History
## Lonnegan | 2020-01-21T22:31:15+00:00
A complete logfile if it helps.
[debugxmrig.txt](https://github.com/xmrig/xmrig/files/4094094/debugxmrig.txt)


## Lonnegan | 2020-01-23T20:11:50+00:00
I think I have an idea. I've always used xmrig with priority 0 or 1. Since I've reverted to default (priority null) for testing on the Bully the problem has not occured anymore?! :o

## cryptonius | 2020-02-11T02:27:28+00:00
Same here with Ryzen 3600.

## Lonnegan | 2020-02-11T07:02:24+00:00
Yes, it's the same with Pinnacle Ridge, it's not a Bulldozer issue anymore. With the new Ryzen 5 1600 "Pinnacle Ridge" (which is a throttled 2600) as well as with Ryzen 7 2700 when priority is set to 0. Both running with Windows 10 v1903 or v1909. Interestingly it's not the case with a Ryzen 9 3900X running on Windows Server 2019 v1809. Perhaps it's related to the new scheduler with "Topology Awareness" introduced with v1903?
https://bit.ly/2HbQlCv

It's just unknowable that sometime they run for days without this behaviour.

## Lonnegan | 2020-02-13T07:37:16+00:00
I've tested again. On both Bulldozer and Zen based CPUs the issue does not occure if you leave priority at null. That's not ideal for systems which are not dedicated exclusively for mining.

With Ryzen, tested on Matisse, Pinnacle Ridge and Summit Ridge, it seems to help when you use power plan High performance or Ryzen High performance instead of Balanced or Ryzen balanced. I have to do further testings, because the problems on Zen based systems come and go; sometimes the systems work without this issue for days, sometimes I struggle with it days long.

On Bulldozer (more precisely: Piledriver/Vishera) the power plan doesn't matter. Here the only way to fix it is to leave priority at null and it's reproducible within minutes.

All systems common is Windows 10 x64.

## cryptonius | 2020-02-13T17:23:33+00:00
My system lags a lot without priority set, this needs to be fixed.

## SChernykh | 2020-02-13T22:44:32+00:00
The problem is that I _never_ had this issue on any of my machines (and I have 3 different ones for testing). I even tried running with priority=0 in config for days. @Lonnegan @cryptonius can you try to clean up any Windows bloat from the machines where it happens: https://www.reddit.com/r/MoneroMining/comments/f18825/windows_10_tuning_guide_for_randomx_mining/ ? So we can be sure it's not some background process taking away CPU time from xmrig.

## cryptonius | 2020-02-13T22:46:01+00:00
Even if I set priority via Task Manager, I get the same bug (double digit H/s) sooner or later.

## Lonnegan | 2020-02-14T07:42:30+00:00
@SChernykh one of the recommendations in the RandomX guide is to set power plan to High performance. As I said, this solved the problem on Zen based systems.

On the Bulldozer/Piledriver system it didn't. But there's no other task or process, that eats away the CPU time. You can see in the advanced mode of the taskmgr, that xmrig is still running on the allocated cores, on the FX-8300 on cores 0,2,4,6, but I've also tested 1,3,5,7 without difference. xmrig puts load on the cores – and just xmrig, nothing else – but the hashrate then is 0 respectively "n/a". Some minutes later the hashrate suddenly comes back to normal for a while just to repeat again and again as you can see in the screenshot in the first post.

On Zen based systems it's not so reproducible when power plan is set to balanced. There sometimes it works for a whole day and then xmrig hashes 0 H/s ("n/a") for hours while still loading the allocated cores.

There are no fancy tools on that systems, no "security" suites, nothing strange, almost Windows 10 out-of-the box plus AMD chipset drivers, Ethernet drivers and GPU drivers. That's it.

As crypotonius said leaving priority at null is not ideal for systems that are used for other purposes than mining, as well, 'cause they are laggy and slow in their response compared to mining priority 0.

So how can I help you to investigate that problem?

@cryptonius: do you have that problem on your Ryzen 5 3600 even if you set power plan to "Ryzen high performance"?

## cryptonius | 2020-02-14T10:47:08+00:00
I don't want to change my power plan (1usmus Ryzen Universal).

As I said, this is an all-around PC and of course I want responsiveness and low idle power when I'm not mining.

## cryptonius | 2020-02-19T10:44:55+00:00
@Lonnegan I switched to "Ryzen high performance" power plan and I still get the same issue (double digit hashrates).

While that happens, the Task Manager still reports 99-100% CPU usage, which means I'm wasting power for basically nothing. Also, the app sometimes randomly closes.

It's very inconsistent. You can mine for 2 days straight with zero issues and then poof, everything goes haywire!

## cryptonius | 2020-02-27T10:52:52+00:00
@SChernykh No response? With High Performance power plan it takes longer to happen (3-4 straight days of mining). With Balanced power plan it happens sooner.

What gives?

## Lonnegan | 2020-03-02T22:27:18+00:00
@cryptonius I've done a few further tests with my different systems. I gave up Bulldozer, it does what it wants, but perhaps I can figure out why some of my Ryzen systems work fine with priority 0 and others don't. cryptonius, can you (for testing) please go to control panel, system, and set the performance optimization for background services, not for applications, please? Then reboot and test with xmrig for a few days.

## Lonnegan | 2020-03-02T23:34:18+00:00
@cryptonius 
please forget my last posting

@SChernykh 
while I posted the last text I had an idea!

- Win7/Server2011 with priority 0 = never had problems
- Win8.1/Server2012R2 with priority 0 = never had problems
- Win10/Server2019v1809 with priority 0 = never had problems

The only problems I have, I had with systems higher than v1809; so v1903/v1909. As I mentioned earlier they got a new scheduler:
https://bit.ly/2HbQlCv

That's why I suggested to try background priority in the control panel settings, but as I realised quickly by myself, that was not the solution.

Instead I went back to my critical Bulldozer system with Win10 v1903. This system went to n/a hashrate after a few minutes when priority was set to 0. Now, with my new idea it works with normal hashrate despite of priority 0. What I'd changed? I disabled the new parameter "yield" to "false". Since this change the hashrate even of the critical Bulldozer system is normal even with priority 0. Before this system dropped to zero after a few minutes, as showed in the first post.

I cannot promise, that "yield": false will work on every affected systems, but at least on my affect Bulldozer system, which I already gave up it worked! :) In my opinion, the parameter yield is not compatible with the Win10 scheduler newer than 1809. Obviously it gives away compute power in certain situations and never claims it back?!


## cryptonius | 2020-03-06T02:26:18+00:00
@Lonnegan Will that work with Ryzen balanced power plan?

## Lonnegan | 2020-03-06T06:43:54+00:00
@cryptonius 
I've tested for several days now. The parameter yield solved the urging problem with Bulldozer and priority 0, which occured after minutes, but it hasn't for Ryzen as soon as v1903 or higher is used. I don't have a problem with Ryzen and v1809, it works for weeks with priority 0, but with v1903/v1909, the problem occures after hours or not later than days. I had to set priority to "null" on these systems otherwise it occures with balanced (sooner) and high power plan (later)

## cryptonius | 2020-03-06T11:35:06+00:00
@Lonnegan 

Yeap, I switched yield to false and it happens within minutes!

@SChernykh 

Can you do more testing with the new Windows 10 scheduler (v1903/1909) and priority 0 on Zen CPUs?

## Lonnegan | 2020-03-06T11:38:48+00:00
I'll try an other miner now on these systems for testing to see if it is a miner problem or a Windows problem. But of course I don't know how much code the other programmers have "stolen" from xmrig since it is open source and therefor have the same issues since they use xmrig's code base.

## Lonnegan | 2020-03-10T06:44:53+00:00
Ok, after 4 days of working without problems it's the same with SRBMiner-Multi-0-3-8. Trying XMR-stak now for cross-check.

![SRBMiner-Multi-0-3-8_problem](https://user-images.githubusercontent.com/60088495/76286826-5399c880-62a3-11ea-86ad-5c20348c205e.png)




## SChernykh | 2020-03-10T06:49:00+00:00
> I had to set priority to "null" on these systems otherwise it occures with balanced (sooner) and high power plan (later)

Do I get it right than it doesn't happen with higher priority (not 0)? SRBMiner doesn't use low priority.

## Lonnegan | 2020-03-10T06:54:31+00:00
It again only happens when priority is set to idle; xmrig priority = 0, with SRBMiner-Multi the parameter is cpu_priority = 1.
And again only the system with Windows 10 v1909 is affected. The other Ryzen 7 systems with Windows 10 v1809 have ran for weeks now smoothly with idle priority. But sooner or later I'll have to update them, as well, when MS quits the support for older win10 builds

> [2020-03-10 00:53:50] CPU :    5957.78 H/s
[2020-03-10 00:53:50] Total:    5957.78 H/s
[2020-03-10 00:53:59] New job received [s/1KsLt3OZeVlZZYWqtFIPbDG6Nv], block height 2050963
[2020-03-10 00:54:06] CPU result 0x58265d74 accepted [31ms]
[2020-03-10 00:54:21] CPU result 0x7874175d accepted [26ms]
[2020-03-10 00:54:27] New job received [zuktSLuKjppviYCcWRBbQdRYeE5i], block height 2050964
[2020-03-10 00:54:30] New job received [9um8thPnuDV947Srfsy/34KDXDQY], block height 2050965
[2020-03-10 00:54:35] New job received [0zNgjwjFjekpjPMsGZ0QDDCGWWno], block height 2050966
[2020-03-10 00:54:36] TLS socket closed while receiving data
[2020-03-10 00:54:36] Reconnecting to pool.supportxmr.com:9000 in 30 seconds
[2020-03-10 00:55:06] SSL/TLS fingerprint: SHA256:f4welul2aj2ndBy66S+LRtM4YkNf5sV6OLWkzsDsbhA=
[2020-03-10 00:55:06] Connected to pool.supportxmr.com:9000
[2020-03-10 00:55:06] Difficulty changed to 100001.00000000
[2020-03-10 00:55:06] New job received [cEmla4xjpxJoi3NWiB/b4KiKTpj8], block height 2050966
[2020-03-10 00:56:46] Difficulty changed to 50000.00000000
[2020-03-10 00:56:46] New job received [PwFgysKFsmIeq7U83HRS8gbzpVdF], block height 2050966
[2020-03-10 00:56:50] CPU :    4407.41 H/s
[2020-03-10 00:56:50] Total:    4407.41 H/s
**_[2020-03-10 00:57:54] New job received [LNocBapEUeNICqYtrWGH3eC+UeSU], block height 2050967
[2020-03-10 00:59:50] CPU :    93.72 H/s
[2020-03-10 00:59:50] Total:    93.72 H/s
[2020-03-10 01:02:50] CPU :    94.17 H/s
[2020-03-10 01:02:50] Total:    94.17 H/s
[2020-03-10 01:05:39] Not authenticated to the pool, switching to next pool
[2020-03-10 01:05:39] User initiated pool switch to pool.supportxmr.com:9000 [0]
[2020-03-10 01:05:39] Just a moment...
[2020-03-10 01:05:39] SSL/TLS fingerprint: SHA256:BkF/5C9qfvBkiUmmcJ5FOPfX2KVidlpARLgPIEsk13A=
[2020-03-10 01:05:39] Connected to pool.supportxmr.com:9000
[2020-03-10 01:05:39] Difficulty changed to 100001.00000000
[2020-03-10 01:05:39] New job received [4D+NFj6ioSofd7DZ8wCmLqKCxxOc], block height 2050970
[2020-03-10 01:05:50] CPU :    94.62 H/s
[2020-03-10 01:05:50] Total:    94.62 H/s
[2020-03-10 01:07:19] New job received [e4f3Zdp3M27OwdUXjN+rn5FW88uB], block height 2050971
[2020-03-10 01:07:21] Difficulty changed to 50000.00000000
[2020-03-10 01:07:21] New job received [QTwfewK+7mK02LSpYixyVJQYBYNE], block height 2050971
[2020-03-10 01:08:50] CPU :    93.22 H/s
[2020-03-10 01:08:50] Total:    93.22 H/s
[2020-03-10 01:09:35] CPU result 0x0a6274d1 accepted [40ms]
[2020-03-10 01:09:54] New job received [TZcKAbuye59+IA5WwddkI8qIr1T9], block height 2050972
[2020-03-10 01:10:14] New job received [8UuRpCaTwVPIWomsFXBWwHJ93DMV], block height 2050973
[2020-03-10 01:10:21] New job received [2iZyDJ3UGOxkgW0qgs4T8p9lw4ci], block height 2050973
[2020-03-10 01:11:21] New job received [y0FhnOa1aQWyXZShrOTgRLTyAuY0], block height 2050973
[2020-03-10 01:11:34] CPU result 0xae175d74 accepted [39ms]
[2020-03-10 01:11:50] CPU :    94.40 H/s
[2020-03-10 01:11:50] Total:    94.40 H/s
[2020-03-10 01:12:17] New job received [xhs5vBQH3bzoNBj6MZfO2da1PqN/], block height 2050974
[2020-03-10 01:12:21] New job received [ALxdEELXEAzLt7Mm0Wg2eIR/VOlR], block height 2050974
[2020-03-10 01:13:17] CPU result 0x36d34517 accepted [39ms]
[2020-03-10 01:13:21] New job received [g84QmgUaXiqsrKWpkowU5oYa4ykk], block height 2050974
[2020-03-10 01:13:35] New job received [hsPPuJgiZxRGEwITx4imFNGLbIxR], block height 2050975
[2020-03-10 01:14:21] New job received [qwQNRatDBT5OR7kMloKgzL8RtAvE], block height 2050975
[2020-03-10 01:14:50] CPU :    94.71 H/s
[2020-03-10 01:14:50] Total:    94.71 H/s
[2020-03-10 01:15:21] New job received [2+6ab3Uv0frzAyqltuc5DZWTrXLR], block height 2050975
[2020-03-10 01:16:21] New job received [mLvTlCuDRkUyKZmZej/46XynVkp+], block height 2050975
[2020-03-10 01:17:21] New job received [/W/mVKTe64gwUjniV3s9HkpU63v3], block height 2050975
[2020-03-10 01:17:44] New job received [ki25YG0eMbZZOKbSogTYIL7D0oHN], block height 2050976
[2020-03-10 01:17:50] CPU :    94.78 H/s
[2020-03-10 01:17:50] Total:    94.78 H/s
[2020-03-10 01:18:10] New job received [L27gScVMObDBqpamnKan2Xhvarkw], block height 2050977
[2020-03-10 01:18:21] New job received [Vy+T2yySsxNb/O5iEtM2XMgwwqyb], block height 2050977
[2020-03-10 01:19:21] New job received [oDJEpDTe4cLE9G+LB716Nx9JFW5g], block height 2050977
[2020-03-10 01:20:21] New job received [TpncMpuoCVpOYBiul5Pq/zpkf7oF], block height 2050977
[2020-03-10 01:20:25] New job received [z3ZRQ0hYlah6Auw0tiaWd0hqrUCr], block height 2050978
[2020-03-10 01:20:50] CPU :    88.55 H/s
[2020-03-10 01:20:50] Total:    88.55 H/s
[2020-03-10 01:23:51] CPU :    106.85 H/s
[2020-03-10 01:23:51] Total:    106.85 H/s
[2020-03-10 01:26:51] CPU :    94.61 H/s
[2020-03-10 01:26:51] Total:    94.61 H/s
[2020-03-10 01:29:51] CPU :    94.40 H/s
[2020-03-10 01:29:51] Total:    94.40 H/s
[2020-03-10 01:32:51] CPU :    93.48 H/s
[2020-03-10 01:32:51] Total:    93.48 H/s
[2020-03-10 01:34:13] Not authenticated to the pool, switching to next pool
[2020-03-10 01:34:13] User initiated pool switch to pool.supportxmr.com:9000 [0]
[2020-03-10 01:34:13] Just a moment...
[2020-03-10 01:34:13] SSL/TLS fingerprint: SHA256:1tOfm3Nc7H5bskUHX8dyclY1RPI9tzQxchLoQPQVcYI=
[2020-03-10 01:34:13] Connected to pool.supportxmr.com:9000
[2020-03-10 01:34:13] Difficulty changed to 100001.00000000
[2020-03-10 01:34:13] New job received [26mvwSa84tKhU2po1fhQQVBP1fSv], block height 2050985
[2020-03-10 01:34:21] Difficulty changed to 157897.00000000
[2020-03-10 01:34:21] New job received [Qn4CD9l5d5Xg0KzqW0BkgmUYhEG+], block height 2050985
[2020-03-10 01:35:21] Difficulty changed to 105263.00000000
[2020-03-10 01:35:21] New job received [pJLPzgMfVFj8wuO1FopfEYPKeLT1], block height 2050985
[2020-03-10 01:35:38] New job received [gZYRKcv6GPHGPxZWTSuyKsyZvS2w], block height 2050986
[2020-03-10 01:35:51] CPU :    93.41 H/s
[2020-03-10 01:35:51] Total:    93.41 H/s
[2020-03-10 01:36:21] Difficulty changed to 70175.00000000
[2020-03-10 01:36:21] New job received [wCeeJgLwx58wFzTUvKIMBvzuewgP], block height 2050986
[2020-03-10 01:37:21] Difficulty changed to 50000.00000000
[2020-03-10 01:37:21] New job received [rk26iv21ZxcouQpfmWmKo8DcGq8x], block height 2050986
[2020-03-10 01:37:29] New job received [6tZJ9hro/ol+TFY2J48JP+YrUh7C], block height 2050987
[2020-03-10 01:38:51] CPU :    93.57 H/s
[2020-03-10 01:38:51] Total:    93.57 H/s
[2020-03-10 01:39:33] New job received [rMdgjXmdA/65wTqQFEAqhVWJI2GD], block height 2050988
[2020-03-10 01:39:34] CPU result 0xf5a28b2e accepted [39ms]
[2020-03-10 01:40:21] New job received [mKONs4b+w5xjMU2ncy8EWU//3FVt], block height 2050988
[2020-03-10 01:41:21] New job received [UkLBjmvPcbJ4FAAbe/taT3tYMWLP], block height 2050988
[2020-03-10 01:41:51] CPU :    92.50 H/s
[2020-03-10 01:41:51] Total:    92.50 H/s
[2020-03-10 01:42:21] New job received [bd8fhLx4yH4LN29oPJpPvaavbFVq], block height 2050988
[2020-03-10 01:43:21] New job received [r+avPW0tah7BeQeyueG+WPxvArcH], block height 2050988
[2020-03-10 01:44:21] New job received [+IUBMwxqm/khM4LG8XBL5kOJrbgK], block height 2050988
[2020-03-10 01:44:51] CPU :    95.38 H/s
[2020-03-10 01:44:51] Total:    95.38 H/s
[2020-03-10 01:45:21] New job received [lIDt+pt37Y7LWwDxW4N/I1PAKhrj], block height 2050988
[2020-03-10 01:46:21] New job received [bOzmgNPG9pBm8eu7kCXDJwt9RQln], block height 2050988
[2020-03-10 01:46:33] New job received [MFYCasIXSVFCtTIzKPDF+q2+2Tqo], block height 2050989
[2020-03-10 01:47:21] New job received [WzJMN4tT8MmQgJEJn6zFwa/B5qec], block height 2050989
[2020-03-10 01:47:51] CPU :    93.10 H/s
[2020-03-10 01:47:51] Total:    93.10 H/s
[2020-03-10 01:50:52] CPU :    94.65 H/s
[2020-03-10 01:50:52] Total:    94.65 H/s
[2020-03-10 01:53:52] CPU :    94.07 H/s
[2020-03-10 01:53:52] Total:    94.07 H/s_**
[2020-03-10 01:53:59] Not authenticated to the pool, switching to next pool
[2020-03-10 01:53:59] User initiated pool switch to pool.supportxmr.com:9000 [0]
[2020-03-10 01:53:59] Just a moment...
[2020-03-10 01:54:00] SSL/TLS fingerprint: SHA256:1tOfm3Nc7H5bskUHX8dyclY1RPI9tzQxchLoQPQVcYI=
[2020-03-10 01:54:00] Connected to pool.supportxmr.com:9000
[2020-03-10 01:54:00] Difficulty changed to 100001.00000000
[2020-03-10 01:54:00] New job received [T35mLU9JnXMG56KQz4Si3MflTHJf], block height 2050991
[2020-03-10 01:54:10] New job received [Z5U7akredF0Tzhvfk8+E4LEs/Wuc], block height 2050992
[2020-03-10 01:54:23] CPU result 0x9f8fd145 accepted [42ms]
[2020-03-10 01:54:41] CPU result 0x9f124617 accepted [42ms]
[2020-03-10 01:54:42] New job received [5mib4eMlr1OQN4IJtqcepNaLFrMM], block height 2050993
[2020-03-10 01:54:44] CPU result 0xfe32bae8 accepted [56ms]
[2020-03-10 01:54:45] CPU result 0xb54b175d accepted [43ms]
[2020-03-10 01:55:02] CPU result 0xb962bae8 accepted [60ms]
[2020-03-10 01:55:19] New job received [8eiSxsnl7k/oH8cOe86RsedcNvIl], block height 2050994
[2020-03-10 01:55:19] CPU result 0x0334a38b accepted [66ms]
[2020-03-10 01:55:22] Difficulty changed to 219511.00000000
[2020-03-10 01:55:22] New job received [T1WrwjnPXDwA6HphnU4UgeXUYjHs], block height 2050994
[2020-03-10 01:55:34] CPU result 0x06190000 accepted [39ms]
[2020-03-10 01:56:22] Difficulty changed to 173135.00000000
[2020-03-10 01:56:22] New job received [iC7Xu4YaTRba+d4Hf5EKLf/GZ/76], block height 2050994
[2020-03-10 01:56:52] CPU :    6340.95 H/s
[2020-03-10 01:56:52] Total:    6340.95 H/s
[2020-03-10 01:57:20] CPU result 0xd0262fba accepted [61ms]

> 

## Lonnegan | 2020-03-10T07:47:33+00:00
Ok, fortunately I didn't have to wait for long. Same issue with xmr-stak-rx when priority is set to idle. With xmr-stak-rx I had to do this in the taskmgr since that miner has no parameter for cpu priority. 

So three very different miner software has the same issue mining RandomX(L) as soon as priority is set to idle and Windows 10 version is v1903 or higher. So I don't think anymore it's a miner bug, it seems to be a Windows scheduler bug.

Is there a possibility in xmrig not to bind threads to certain cores, but say --threads 11 for example and let the Windows scheduler decide which cores  to take; as it was in earlier versions of xmrig? Just to do a cross-test if it has something to do with cpu binding.

@moderator: can you split this thread? The original issue (and the thread title) was an issue on a Bulldozer system. That I was able to fix setting the parameter yield to false, als described here:
https://github.com/xmrig/xmrig/issues/1506#issuecomment-593678237

The issue we are talking about with Ryzen I think should have a separate thread. :)

## SChernykh | 2020-03-10T07:50:51+00:00
> Is there a possibility in xmrig not to bind threads to certain cores

Use -1 instead of core number in config.json: `"rx/0":[-1,-1,...,-1]`

## Lonnegan | 2020-03-10T07:53:57+00:00
Ok thx, I'll try...

## cryptonius | 2020-03-10T12:55:44+00:00
Unfortunately I don't think Microsoft will bother with this, since they consider (via Windows Defender) every miner a "malware" app.

It's miner developers that will need to find a solution for this issue, whatever that may be...

## Lonnegan | 2020-03-10T14:51:54+00:00
@cryptonius 
it's way too early of course, but xmrig has been running for 6 hours now with priority 0 without an issue on a Ryzen system with v1909. Can you test it on your system, please, running xmrig without cpu binding?

Edited: running for 24 hours now, still no problem despite priority 0 and v1909...

## SChernykh | 2020-03-11T12:46:31+00:00
@Lonnegan so your conclusion? It's a combination of v1909, priority 0 and threads pinned to cores?

## Lonnegan | 2020-03-11T13:13:34+00:00
> @Lonnegan so your conclusion? It's a combination of v1909, priority 0 and threads pinned to cores?

@SChernykh 
At the moment, it looks that way, yes. The Ryzen 7 3700X has been running for 36 hrs now without an issue. But as I said, it's not reproducible immediately. Sometimes it took days to occur. I'll try a Ryzen 5 1600 (12 nm/Pinnacle Ridge) this night for futher testing.

It might be affected by the special topology of Ryzen "Summit Ridge", "Pinnacle Ridge" and "Matisse" CPUs, which are not monolitic  multi-core CPUs, but consist of two CCX. I have a Ryzen 3 2200G APU, too, which consists of only one CCX and I've never had this problems despite of Win10 v1903/1909 and priority 0. I don't have Intel CPU for mining, so I can't do further cross-tests.

So perhaps we should add the summand "Ryzen CPU" to your formula:

Win10 v1903/v1909 with topology aware scheduler + priority 0 + threads pinned to cores + Ryzen CPU with >1 CCX = issue 





## cryptonius | 2020-03-11T13:15:05+00:00
Can I switch to Ryzen balanced plan without CPU binding and still have proper hashrates?

## Lonnegan | 2020-03-11T13:20:59+00:00
> Can I switch to Ryzen balanced plan without CPU binding and still have proper hashrates?

With the Ryzen 7 3700X and 11 threads running I had 6350 H/s with cpu binding and have 6450 H/s now without cpu binding. So it's even higher! The new scheduler itself obviously tries to hold the threads on the best cores. Look, this is without cpu binding!

![xmrig_binding-1](https://user-images.githubusercontent.com/60088495/76421086-6c89a300-63a3-11ea-8609-b658711e79a7.png)

I haven't tried this with balanced power plan, yet. Atm I'm using Ryzen high power plan.


## cryptonius | 2020-03-11T13:28:13+00:00
I guess it's OK to use 12 threads with my Ryzen 3600, right?

## Lonnegan | 2020-03-11T13:33:21+00:00
> I guess it's OK to use 12 threads with my Ryzen 3600, right?

From the point of scratchpad size you can use 12 threads on your Ryzen 5 3600, so you are using all logical cores. personally I prefer to not use all logical cores of a CPU for mining on systems I use for daily work, because the responsiveness is much better if you only start 11 or 10 threads on your logical 12 core system. You have to try out the best compromise between responsiveness and hash rate for yourself, the loss of hash rate is not linear, because with less threads the cache hit rate is higher and the turbo can boost higher, which compensates the fewer threads partly.

## cryptonius | 2020-03-11T13:38:15+00:00
> > I guess it's OK to use 12 threads with my Ryzen 3600, right?
> 
> From the point of scratchpad size you can use 12 threads on your Ryzen 5 3600, so you are using all logical cores. personally I prefer to not use all logical cores of a CPU for mining on systems I use for daily work, because the responsiveness is much better if you only start 11 or 10 threads on your logical 12 core system. You have to try out the best compromise between responsiveness and hash rate for yourself

To me it seems quite responsive with priority 0, I can even play video games while mining. As long as the double-digit hashrate doesn't happen, that's all that matters to me.

Thanks, I'll try the suggestion and I will report back after a few days. :)

## cryptonius | 2020-03-11T14:04:48+00:00
The hashrate seems lower in my case, I used to get around 7480 H/s and now it's down to 7200 H/s with CPU binding ("rx": [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]).

## cryptonius | 2020-03-14T04:08:47+00:00
Just got the low hashrate bug again. :\

## cryptonius | 2020-03-14T09:57:06+00:00
Even if I restart the app, it does it again after a few minutes (shorter period, WTF).  Even a reboot doesn't help this time around.

Since I was mining for 3+ days straight with no issues, I suggest you guys test it for 3-4 days straight minimum. 1-2 days ain't gonna cut it.

## Lonnegan | 2020-03-14T10:09:09+00:00
Changed a 3700X "Matisse" and a 1600 "Pinnacle Ridge" to -1 (no cpu binding). No issues so far anymore despite priority 0 and v1909.

## Spudz76 | 2020-03-23T08:16:21+00:00
[zen changes in Win10v1903](https://borncity.com/win/2019/06/30/windows-10-v1903-optimization-for-zen-based-amd-cpus/)
This seems to explain what they changed and it seems like it wants to keep CCX blocks from being used until the first one is "full".  So then I suppose setting them hard to a "core" would also try to place them on other CCX when the first one is not filled, which makes the new cpuscheduler angry.

Also a side effect of Zen not really having actual "cores" but just virtual ones mapped into CCX spaces.  Maybe affinity will never work correctly.  But hey, the changes made Rocket League like 15% faster so there's that.

## cryptonius | 2020-04-04T12:12:48+00:00
The binding solution doesn't work. What else should I do?

## Lonnegan | 2020-04-04T14:51:34+00:00
Intentionally using an older Windows 10 version like 1809 is not an option for you?

## cryptonius | 2020-04-04T14:54:16+00:00
@Lonnegan I'm afraid not. Windows 10 only gets 18 months of support and you need the latest version for certain apps and features.

Is there no hope of making a workaround for the latest scheduler? This will affect more and more people as time passes by.

## Lonnegan | 2020-04-04T15:02:11+00:00
You can try to play around with Process Lasso:
https://bitsum.com/changes/processlasso/

Or last option: install VirtualBox, install Ubuntu Server LTS as a guest and try to run xmrig in a virtualized Linux guest. Perhaps it helps...

## cryptonius | 2020-04-04T15:05:42+00:00
Virtualization means I'll get lower hashrates and besides, I would still need to have the VM at low priority (as I said, web browsing feels like using a Pentium MMX PC from the 90s).

I'll wait for an official fix (been waiting for 2+ months now TBH) or maybe switch to another miner.

## Lonnegan | 2020-04-04T15:08:22+00:00
An other miner won't help. Have tried two already. It's the same. As I've written already a few posts earlier, I don't think anymore it is a miner bug but a Windows bug.

## cryptonius | 2020-04-04T15:10:12+00:00
Then I'm wondering if mining apps could implement a workaround, because I don't think MS will bother to do anything. No other app seems to have performance issues with the new scheduler.

## Lonnegan | 2020-04-04T15:13:21+00:00
TBH there are very little apps that run for days and weeks in a row at full load. Perhaps other apps would be affected as well if they would.

Your last short-term option: try process lasso.

In a few week Windows 10 version 2004 will be released. You can try if there are some changes in the behavior of the scheduler.

## cryptonius | 2020-04-04T15:15:31+00:00
2004 probably won't change anything, since this issue persists since 1903.

What does process lasso do exactly? Does it just change the priority?

## Lonnegan | 2020-04-04T15:19:45+00:00
1909 was just an update to 1903, was installed without the usual upgrade installation. 2004 instead will be installed as an upgrade again not just as an update. So there's a chances that there will be much more changes than between 1903 and 1909.

Process Lasso does much more than just change the priority. Pls read here what it does:
https://bitsum.com/

## xmrig | 2020-08-31T05:48:09+00:00
https://xmrig.com/docs/miner/randomx-stability-troubleshooting-guide

# Action History
- Created by: Lonnegan | 2020-01-20T07:03:17+00:00
- Closed at: 2020-08-31T05:48:09+00:00
