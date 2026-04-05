---
title: amd hashrate n/a
source_url: https://github.com/xmrig/xmrig/issues/3148
author: pmrk74
assignees: []
labels: []
created_at: '2022-10-29T07:35:16+00:00'
updated_at: '2025-06-18T22:51:46+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:51:46+00:00'
---

# Original Description
I want to mine Monero currency through this program, but the problem is that the program shows the hash rate n/a, it also shows this error:
opencl disabled (failed to start thread)

how i can fix this?

my system;
windows 11
amd 580 8gb

# Discussion History
## SChernykh | 2022-10-29T07:46:25+00:00
First of all, you have to mine with CPU, not GPU. GPUs are very slow on RandomX. Second, you need to show the screenshot of XMRig window when it starts and shows this error, or I can't tell you what exactly went wrong.

## pmrk74 | 2022-10-29T08:56:35+00:00
https://s6.uupload.ir/files/untitled-ss_9a1o.png 

## Lonnegan | 2022-10-29T15:24:02+00:00
Why do you say "amd hashrate n/a"?! You have an Intel CPU!

## SChernykh | 2022-10-29T15:27:34+00:00
If you really want to mine on your AMD GPU, try Windows 10 and probably older AMD drivers. But hashrate will be very low, it's better to mine Monero on CPU only and use GPUs for something else.

## pmrk74 | 2022-10-31T07:46:16+00:00
yes i have intel cpu but i want to do this with gpu because cpu power is low for this task

## SChernykh | 2022-10-31T07:59:10+00:00
Radeon RX 580 will give you only 470 h/s even if you manage to make it work.

## pmrk74 | 2022-10-31T13:32:13+00:00
So, how to solve the hashrate n/a problem?

## SChernykh | 2022-10-31T13:41:54+00:00
- Mine on CPU
- Windows 10 and older driver to mine on GPU

## Spudz76 | 2022-10-31T15:27:46+00:00
Guess at which drivers aren't buggy:
* “good” AMD drivers for Windows: from 18.12.1.1 to 19.7.5 (inclusive), and from 19.12.2 to 20.11.1 (inclusive)

# Action History
- Created by: pmrk74 | 2022-10-29T07:35:16+00:00
- Closed at: 2025-06-18T22:51:46+00:00
