---
title: Dual EPYC 7452 (64 Cores total) But only doing 10-20 kh/s
source_url: https://github.com/xmrig/xmrig/issues/2384
author: Mighty33
assignees: []
labels: []
created_at: '2021-05-16T13:40:01+00:00'
updated_at: '2021-05-19T00:01:19+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hello,

I am running 2x EPYC 7452 (64 Cores total) But only doing 10-20 kh/s  (I tough would be around the benchmark 50 kh/s)
I used the wizard for the setup... Is there something wrong with my setup or does this need additional settings?  

I am desperate for help...  Can anyone point me to the right direction to maximize the hash rates? 

# Discussion History
## SChernykh | 2021-05-16T14:12:46+00:00
Take a screenshot of xmrig output when it starts and post it here.

## Mighty33 | 2021-05-16T14:24:42+00:00
Attached. 
![ScrSht1](https://user-images.githubusercontent.com/35414147/118400738-e913b380-b630-11eb-998b-081128d2d95b.PNG)


## Mighty33 | 2021-05-16T14:26:36+00:00
I can see it go up to 30 but never reaches 50 or anywhere close to it. 

Thank you so much for taking a look.... 

## SChernykh | 2021-05-16T14:31:37+00:00
EPYC has 8-channel memory. If you want to reach max hashrate, you need to install 8 memory sticks per CPU. Maybe 4 sticks per CPU will be enough. Check your motherboard manual to see which memory slots to fill in.

## Mighty33 | 2021-05-16T15:02:06+00:00
ahhh ok I will try!! Thank you so much. Will advise once I install. 

## Mighty33 | 2021-05-16T15:33:52+00:00

Hash rates did improve once I added 2 more additional memory sticks.  Thank you!

## Spudz76 | 2021-05-17T20:24:56+00:00
Also it supports up to 3200MHz and you have 2667MHz which hurts hashrate nearly as much as not having 8-channel enabled.

You can click down into the benchmark results and see the Memory header (on most) and it says how many sticks and what MHz they were running.

## Mighty33 | 2021-05-18T02:39:28+00:00
Thank you... Will try to boost up to 3200MHz. 
And try to get 8 channels of Memory added. 

## Spudz76 | 2021-05-19T00:01:19+00:00
Of course since you need so many sticks, 4GB minimal size ones make more sense.  Still 32GB and way more than needed, unless there was some other usage needing the 64GB total.

# Action History
- Created by: Mighty33 | 2021-05-16T13:40:01+00:00
