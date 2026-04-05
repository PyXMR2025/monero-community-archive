---
title: xmrig v2.16.0-beta
source_url: https://github.com/xmrig/xmrig/issues/1041
author: minerjed
assignees: []
labels: []
created_at: '2019-06-27T00:27:30+00:00'
updated_at: '2019-08-02T11:41:02+00:00'
type: issue
status: closed
closed_at: '2019-08-02T11:41:02+00:00'
---

# Original Description
Trying to build new version of xmrig on windows but can not find RANDOMX.  (Could NOT find RANDOMX (missing: RANDOMX_LIBRARY RANDOMX_INCLUDE_DIR)).  Were can I get this include directory? Thx...

# Discussion History
## xmrig | 2019-06-27T02:35:57+00:00
RandomX included to recent xmrig-deps (for msvc2017 and gcc) if it's not your case, you should build library by yourself: https://github.com/wownero/RandomWOW after successful build, specify path to include directory and library on cmake phase `cmake .. -DRANDOMX_INCLUDE_DIR=... -DRANDOMX_LIBRARY=...`

Another option if you don't need RandomWOW support is disable this algorithm `cmake .. -DWITH_RANDOMX=OFF`.
Thank you.

## minerjed | 2019-06-27T21:49:49+00:00
Thanks…

 

From: xmrig <notifications@github.com> 
Sent: Wednesday, June 26, 2019 10:36 PM
To: xmrig/xmrig <xmrig@noreply.github.com>
Cc: directdepot <directdepot@directdepot.net>; Author <author@noreply.github.com>
Subject: Re: [xmrig/xmrig] xmrig v2.16.0-beta (#1041)

 

RandomX included to recent xmrig-deps (for msvc2017 and gcc) if it's not your case, you should build library by yourself: https://github.com/wownero/RandomWOW after successful build, specify path to include directory and library on cmake phase cmake .. -DRANDOMX_INCLUDE_DIR=... -DRANDOMX_LIBRARY=...

Another option if you don't need RandomWOW support is disable this algorithm cmake .. -DWITH_RANDOMX=OFF.
Thank you.

—
You are receiving this because you authored the thread.
Reply to this email directly, view it on GitHub <https://github.com/xmrig/xmrig/issues/1041?email_source=notifications&email_token=AKD4O6HVGH2MVFAGSZSBVGDP4QRRVA5CNFSM4H3XBYF2YY3PNVWWK3TUL52HS4DFVREXG43VMVBW63LNMVXHJKTDN5WW2ZLOORPWSZGODYVPRII#issuecomment-506132641> , or mute the thread <https://github.com/notifications/unsubscribe-auth/AKD4O6EJUSZSJESCX5C36QLP4QRRVANCNFSM4H3XBYFQ> .  <https://github.com/notifications/beacon/AKD4O6AHZIK7B6WRO7M5PP3P4QRRVA5CNFSM4H3XBYF2YY3PNVWWK3TUL52HS4DFVREXG43VMVBW63LNMVXHJKTDN5WW2ZLOORPWSZGODYVPRII.gif> 



## Spudz76 | 2019-06-27T22:33:19+00:00
With msvc2017 x64 from xmrig-deps master:
```
c:\build\randomwow\src\randomx.cpp : fatal error C1083: Cannot open compiler generated file: 'x64\Release\randomx.asm': No such file or directory
```
But I have no `c:\build\` and there is no `randomx.asm`

## snipeTR | 2019-06-28T08:57:43+00:00
![image](https://user-images.githubusercontent.com/31975916/60330776-e146b980-999b-11e9-95ad-ce5340ce9886.png)
![image](https://user-images.githubusercontent.com/31975916/60330808-edcb1200-999b-11e9-8cf4-b3cedb47b1f3.png)


## nssy | 2019-06-28T09:01:51+00:00
Thanks for the response @xmrig
Have compiled on Linux and successfully started mining on wownero pool.
`git clone git@github.com:wownero/RandomWOW.git /tmp/RandomWOW`
`cd /tmp/RandomWOW && make`

Then on xmrig build folder
`cmake ..  -DRANDOMX_INCLUDE_DIR=/tmp/RandomWOW/src -DRANDOMX_LIBRARY=/tmp/RandomWOW/bin/librandomx.a`

## cryptonote-social | 2019-06-28T23:49:52+00:00
This version doesn't seem to tell if you are using hugepages?

`[2019-06-28 16:46:02.008] READY (CPU) threads 3(3) memory 3072 KB
`

## xmrig | 2019-06-29T05:35:43+00:00
@cryptonote-social Yep I removed huge pages information for RandomWOW algorithm, because it use own internal mechanism to allocate huge pages, it currently not integrated to miner source like other cryptonight algorithms.
Thank you.

## cryptonote-social | 2019-06-29T16:18:42+00:00
Thanks @xmrig  ... what's confusing though is it seems to work in the feature-randomx branch?

# Action History
- Created by: minerjed | 2019-06-27T00:27:30+00:00
- Closed at: 2019-08-02T11:41:02+00:00
