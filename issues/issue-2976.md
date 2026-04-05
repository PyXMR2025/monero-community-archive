---
title: proxy question
source_url: https://github.com/xmrig/xmrig/issues/2976
author: Sakuya-CN
assignees: []
labels: []
created_at: '2022-03-17T02:59:25+00:00'
updated_at: '2026-02-20T08:14:50+00:00'
type: issue
status: open
closed_at: null
---

# Original Description

My local prohibition of mining, so I want to disguise network behavior when executing xmring.exe, I use my own VPN to make xmring.exe forward to the mining pool through the proxy, which will be much safer, but it seems to be unsuccessful, No matter how I set it up, xmring always connects directly to the mining pool IP, rather than connecting to the mining pool through a proxy. Forcing proxy forwarding, the connection will fail. What is going on? Task, why doesn't xmring work?

# Discussion History
## nahuhh | 2022-04-14T16:24:03+00:00
You can use tor

Download tor or tor browser and set the "socks" section of the pool config to 9050 or 9150 respectively 

## snipeTR | 2022-04-14T16:33:45+00:00
You can use multiple strategies. but TOR is not one of them. because it's too slow. You cannot forward the blocks you find to the pool in time.
First you need to set up VPN on your VPS. then you can connect to that ip over the encrypted channel. If you use port 80, no one will ever be able to tell what you are sending there and what you are not sending.

## nahuhh | 2022-04-14T16:43:01+00:00
> You can use multiple strategies. but TOR is not one of them. because it's too slow. You cannot forward the blocks you find to the pool in time.
>

When mining to an onion address I've had no issues with latency re finding shares.

Of course, not all pools have onion addresses, but I mine to my node over my hidden service. 


## cojocariucatalin | 2022-06-20T04:51:02+00:00
Hey, ive instal termux on my phone to try mining xmr but when i put github account and pase it say faill why? Can anyone to help ME? Im New in mining sow please help me
If im ouț of topic please tell me
Thank you! 

## SChernykh | 2022-06-20T05:34:46+00:00
> when i put github account and pase it say faill why?

How can anyone say why without seeing the exact error, also you don't need a github account for mining.

## Spudz76 | 2022-06-20T22:34:40+00:00
> > You can use multiple strategies. but TOR is not one of them. because it's too slow. You cannot forward the blocks you find to the pool in time.
> 
> When mining to an onion address I've had no issues with latency re finding shares.
> 
> Of course, not all pools have onion addresses, but I mine to my node over my hidden service.

Most (decent) pools also have plenty of grace period even 2000ms would be accepted.

## mymirai-nikki | 2026-02-20T08:14:50+00:00
is there a way to test or measure the latency before mining?

# Action History
- Created by: Sakuya-CN | 2022-03-17T02:59:25+00:00
