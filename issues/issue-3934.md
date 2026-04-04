---
title: Monero wallet shows active p2pool mining when no mining is taking place
source_url: https://github.com/monero-project/monero-gui/issues/3934
author: Poecilia
assignees: []
labels: []
created_at: '2022-05-29T11:06:05+00:00'
updated_at: '2025-12-10T05:18:51+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Setup:
-Ubuntu 22.04 on older PC (Core i7-4790K - 8 GB - 120 GB SSD - 4Ghz)
-Downloaded pruned version of node (30+GB)
-p2pool mini mining 6/8 threads around 1200 H/s

Problem:
-Monero GUI reports "Connected & Mining" with hashrates looking active (changing values once in a while) even when Ubuntu System Monitor shows no cpu activity is taking place for p2pool (usually shows 75% when mining).

Possible cause;
-either because Ubuntu display was set to turn off automatically, or because I'd set wallet to lock automatically. I have turned both off and now it doesn't seem to be happening anymore. 

In any case, the Wallet is reporting active mining that isn't taking place. This can be confusing for people new to Monero GUI and to mining.

# Discussion History
## selsta | 2022-05-29T21:42:28+00:00
Wallet lock should be unrelated here. It is visual only.

## Poecilia | 2022-05-30T05:02:14+00:00
Update: I can't figure out what the reason is actual p2pool mining stops on my PC. The issue remains the same, which is that Monero GUI reports 'Connected & Mining' and shows active H/s when no mining is taking place on the PC.

## gooseyman | 2022-05-31T16:44:02+00:00
I too am experiencing this issue with Pop OS 22.04 (ubuntu). I can see cpu usuage when solo mining. However, when p2pool mining, the wallet reads connected + mining but there is no CPU usage.  

## Poecilia | 2022-05-31T17:02:38+00:00
I discovered the problem why the mining wasn't happening: a faulty ethernet switch that was sometimes connecting, sometimes not connecting to the internet. The issue remains that Monero GUI reports inaccurately about the status of connectivity and mining.

## devhyper | 2022-06-01T07:28:47+00:00
I'll look into this.

## gooseyman | 2022-06-01T14:39:13+00:00
nethogs is showing the monerod process on my end has activity so I don't think I have the same issue regarding connectivity. 

## ghost | 2022-08-06T21:06:44+00:00
Can confirm. GUI showing "Connected + Mining" however 'status' command output shows "on mainnet, not mining." monerod shows minimal activity in task manager.

## selsta | 2022-08-07T12:37:32+00:00
@username-username-null p2pool mining works with p2pool, so entering "status" on monerod will say "not mining" even if p2pool is mining. That is expected.

## ghost | 2022-08-07T14:34:20+00:00
Ah, I understand, thank you. That just leaves the very low CPU usage. 

## selsta | 2022-08-07T18:27:11+00:00
@username-username-null Did you only check the CPU usage for monerod or your whole system?

## ghost | 2022-08-07T18:39:56+00:00
Both. Based on your reply above, I would guess monerod usage does not apply. For the whole system CPU usage appears unchanged whether P2Pool is on or off.

## tylerrihn | 2023-05-20T23:02:58+00:00
Just wanted to say this problem appears to be ongoing. My miner says I'm mining to the p2p pool however when I ask the daemon its status it says "not currently mining". I also haven't received any awards since this issue started, though cpu usage seems to imply mining.

## devhyper | 2023-05-21T05:08:43+00:00
> Just wanted to say this problem appears to be ongoing. My miner says I'm mining to the p2p pool however when I ask the daemon its status it says "not currently mining". I also haven't received any awards since this issue started, though cpu usage seems to imply mining.

Pretty sure the daemon only reports the status for the built in solo mining. If the CPU usage is high it is probably mining.

## tylerrihn | 2023-05-21T13:50:17+00:00
@devhyper Thanks sir, that seems to be my understanding now. The daemon isn't really 'running', but I am still mining the cpu usage is just going to the p2pool rather than my personal daemon. I think my hash rate is just very low so it takes me awhile to see rewards.

## ERoCx420 | 2024-04-18T00:21:52+00:00
Mine is now doing the same. Before I had an issue with amd adrenaline and ryzen master not showing cpu temp. So I went through a reinstall to fix them. Then after I got that working I opened up Monero gui and started to mine and now it doesn't show hashrste. It says connected and mining but there is no cpu usage. When I check status it says not mining. What should I do?

Windows 11 
5950x
7800xt
64 gig ram

## BO2148 | 2025-06-30T00:20:29+00:00
If I am the one who found the block share. The reward has been divided and announced on the wall. But I did not receive the reward to the wallet. Why? Can anyone tell me? Thanks.

![Image](https://github.com/user-attachments/assets/cf3d459c-cf87-46f7-bcc2-49a93381bf32)


## Spoolingturbo6 | 2025-12-10T05:18:51+00:00
Log always shows " not mining " when getting status. Monero GUI MacOS, Windows, Linux .. 
I've tried following setup guides and videos , not sure if this is mining or not . When "mining solo" I see lots of CPU activity . 

When "mining P2Pool" there is little activity, and Advanced/Manage miner/ Status always shows "StartingP2Pool"
>>print_net_status shows network activity.

I get more CPU activity moving a window around 3 displays -VS- Monerod 
Monerod shows 0.02-0.8 % CPU usage . I gave it 8 of 24 cores because on solo that was about all the heat BTU I could dissipate .

<img width="907" height="1417" alt="Image" src="https://github.com/user-attachments/assets/13429cd9-30fd-4a50-848f-8516b2c44438" />

<img width="1041" height="1459" alt="Image" src="https://github.com/user-attachments/assets/3308eac0-62f4-481b-8c44-eaa5aceead44" />

<img width="1041" height="1459" alt="Image" src="https://github.com/user-attachments/assets/e7792b70-5f8d-4ccd-b072-bce5299cda62" />


# Action History
- Created by: Poecilia | 2022-05-29T11:06:05+00:00
