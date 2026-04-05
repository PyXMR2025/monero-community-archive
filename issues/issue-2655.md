---
title: Which code to change to make the xmrig.exe undetected from AV
source_url: https://github.com/xmrig/xmrig/issues/2655
author: Stockfishx64
assignees: []
labels: []
created_at: '2021-10-28T09:10:29+00:00'
updated_at: '2024-04-12T18:47:47+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Yeah, i know the background: Hackers put cryptominers on the computer of their victims, that's why AV's flag the miner-executables as malware (although it obviously isnt real malware).

I am pretty sure the detection is signature based. And since we have access to the source code, it should be possible to find a way around this, right? Does anyone has experience or assumptions which parts of the code one should modify to avoid a signature based detection of the xmrig.exe?

# Discussion History
## SChernykh | 2021-10-28T09:13:36+00:00
Open your antivirus settings and add xmrig folder to exceptions. Problem solved.

## Stockfishx64 | 2021-10-28T09:14:04+00:00
That's not what i asked for. 

## SChernykh | 2021-10-28T09:31:22+00:00
I'm pretty sure it only makes sense for
> Hackers put cryptominers on the computer of their victims

which is illegal. You won't get answers here. If you're a legit user, just add it to exceptions and be done with it.

## Spudz76 | 2021-10-28T09:38:02+00:00
Besides they detect the mining kernels so the only way to hide those fingerprints are to remove them, and then it's a pretty boring miner.  But it wouldn't set off the sensors.

## DeeDeeRanged | 2021-11-04T11:31:47+00:00
Plus antivirus programs don't just do signature based but also heuristic.

# Action History
- Created by: Stockfishx64 | 2021-10-28T09:10:29+00:00
