---
title: How can I make my xmrig config as fast as possible?
source_url: https://github.com/xmrig/xmrig/issues/3616
author: MrHyplex9511
assignees: []
labels: []
created_at: '2025-01-11T04:37:38+00:00'
updated_at: '2026-02-22T06:35:20+00:00'
type: issue
status: closed
closed_at: '2025-01-14T17:03:12+00:00'
---

# Original Description
Recently I have been interested in mining **MONERO** and I am loving it. But i think that my laptop isn't running on its true potential.
What can I do to improve my hash rate?

![image](https://github.com/user-attachments/assets/95522e9b-48f9-4b47-b3e8-1aa9cb6869c3)
![image](https://github.com/user-attachments/assets/269ddfca-b28e-4ea8-8469-480809145403)
 

# Discussion History
## geekwilliams | 2025-01-11T04:57:00+00:00
That's actually not bad for an i3

- Are you using Monero ocean's fork of xmrig? If so you may want to post this over on their repo instead

## MrHyplex9511 | 2025-01-11T05:02:46+00:00
> That's actually not bad for an i3
> 
> * Are you using Monero ocean's fork of xmrig? If so you may want to post this over on their repo instead

Idk. but i downloaded this repo and inserted the monero ocean pool link

## MrHyplex9511 | 2025-01-11T05:12:48+00:00
HOW CAN I MAXIMIZE MY THING. I NEED POWER

## geekwilliams | 2025-01-11T06:22:16+00:00
First step would be to enable MSR mods.  You can try to run xmrig as admin first and see if that works.

## SChernykh | 2025-01-11T09:28:58+00:00
You need to run 2 threads, not 3. The best results here: https://xmrig.com/benchmark?cpu=Intel%28R%29+Core%28TM%29+i3-1005G1+CPU+%40+1.20GHz are all with 2 threads running. And you need to enable MSR mod - run XMRig as admin, disable all hardware virtualization settings in BIOS.

## MrHyplex9511 | 2025-01-12T12:33:40+00:00
I ran it with admin but it wont work but MSR wont work
![image](https://github.com/user-attachments/assets/559a2986-f2a0-44da-87ea-124294ed816f)


## SChernykh | 2025-01-12T16:02:56+00:00
MSR doesn't work because XMRig runs in a VM on your PC.

> disable all hardware virtualization settings in BIOS


## MrHyplex9511 | 2025-01-12T16:34:30+00:00
> MSR doesn't work because XMRig runs in a VM on your PC.
> 
> > disable all hardware virtualization settings in BIOS

how to fix that. i dont even have any vm softwares

## SChernykh | 2025-01-12T17:33:37+00:00
>  i dont even have any vm softwares

You do, it's called Windows. Try to disable any core isolation and memory integrity settings in Windows. If it doesn't help, you will have to disable virtualization options in BIOS.

## MrHyplex9511 | 2025-01-12T17:45:42+00:00
I disabled it in the BIOS and i got +100 H/s THX.
But is there anything that i can do to make it MORE FASTER?

## MrHyplex9511 | 2025-01-12T17:49:11+00:00
Explain to me, how does this small little program makes money by generating numbers?

## SChernykh | 2025-01-12T18:50:57+00:00
> I disabled it in the BIOS and i got +100 H/s THX. But is there anything that i can do to make it MORE FASTER?

What is your hashrate now? You can compare with numbers in https://xmrig.com/benchmark?cpu=Intel%28R%29+Core%28TM%29+i3-1005G1+CPU+%40+1.20GHz

## MrHyplex9511 | 2025-01-13T01:34:03+00:00
> > I disabled it in the BIOS and i got +100 H/s THX. But is there anything that i can do to make it MORE FASTER?
> 
> What is your hashrate now? You can compare with numbers in https://xmrig.com/benchmark?cpu=Intel%28R%29+Core%28TM%29+i3-1005G1+CPU+%40+1.20GHz

It was around 750 before now its 900/ 950

## MrHyplex9511 | 2025-01-13T01:35:08+00:00
im around the fourth place

## VK-VZ | 2025-01-13T21:51:14+00:00
Thanks 

## a11yot | 2026-02-22T06:32:23+00:00
World record with my 12650H
https://xmrig.com/benchmark/wntEJ

[2026-02-22 07:21:06.802]  miner    speed 10s/60s/15m 6567.6 6577.7 n/a H/s **max 6811.5 H/s**
[2026-02-22 07:21:06.802]  bench    93.55% 935454/1000000 (141.179s)
[2026-02-22 07:21:16.766]  bench    benchmark finished in 151.142 seconds (6616.3 h/s) hash sum = 6A6968F08944BD43
[2026-02-22 07:21:16.899]  cpu      stopped (1 ms)
[2026-02-22 07:21:16.994]  bench    benchmark submitted https://xmrig.com/benchmark/wntEJ
[2026-02-22 07:21:16.994]  bench    press Ctrl+C to exit

# Action History
- Created by: MrHyplex9511 | 2025-01-11T04:37:38+00:00
- Closed at: 2025-01-14T17:03:12+00:00
