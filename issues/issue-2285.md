---
title: Considered as potentially-unwanted application/software (PUAS)
source_url: https://github.com/xmrig/xmrig/issues/2285
author: ethindp
assignees: []
labels:
- av
created_at: '2021-04-19T07:16:21+00:00'
updated_at: '2022-04-03T14:50:24+00:00'
type: issue
status: closed
closed_at: '2022-04-03T14:50:24+00:00'
---

# Original Description
I just tried using this today and malwarebytes immediately flagged/erased the executable. It considers it RiskWare.BitCoinMiner. I've read positive reviews but I feel that asking the developers directly about the security of the application and whether its malicious or not was also a good idea. I'd look through the code for myself but I don't have enough knowledge to audit this with the proper degree of certainty. So, is there a reason for this, and is it safe to mark as an exclusion? (According to research I've read there have been cases of xmrig being used in malware payloads, which may be the reason for it being flagged.)

# Discussion History
## Lonnegan | 2021-04-19T09:31:41+00:00
Malwarebytes has detected xmrig as a coin miner? Well, xmrig IS a coin miner?! 

## ethindp | 2021-04-19T19:44:30+00:00
That has to be the most unhelpful response ever.

## SChernykh | 2021-04-19T19:49:16+00:00
If you downloaded from https://github.com/xmrig/xmrig/releases and SHA256 sums match/PGP signature checks out then it's not malicious. Antiviruses always flag all miners.

## ethindp | 2021-04-19T20:05:03+00:00
I did. Had to allow it through. From my research it seems like people make modifications to XMRig in malicious code so you'd think the AV software would only flag those particular forks but maybe they can't tell so they just flag all the miners instead?

## SChernykh | 2021-04-19T20:07:47+00:00
AV flag all versions of xmrig, even the ones you compile yourself. This is just how it is.

## Lonnegan | 2021-04-19T21:36:20+00:00
The reason why miners got flagged is, that some bad boys used the hardware of innocent people for mining. For those people a coin miner is an unwanted application but since the AV cannot distinguish whether you installed the miner intentionally or whether it was pushed to you without your knowledge, most AV programs mark a miner as a "potentially unwanted application". When it detects a coin miner, it's ok. It IS a coin miner! It becomes dangerous if anything else is discovered.

# Action History
- Created by: ethindp | 2021-04-19T07:16:21+00:00
- Closed at: 2022-04-03T14:50:24+00:00
