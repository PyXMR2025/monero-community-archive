---
title: 'Question: RandomX on DDR3 with speed 1600 vs 1866'
source_url: https://github.com/xmrig/xmrig/issues/1369
author: minzak
assignees: []
labels: []
created_at: '2019-12-02T19:35:46+00:00'
updated_at: '2021-04-12T15:12:37+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:12:37+00:00'
---

# Original Description
Any one have DDR3 both speed 1600 and 1866?
To check hashrate?

I have DDR3 with 1600 speed:
```
 * CPU          Intel(R) Xeon(R) CPU E5-2660 0 @ 2.20GHz (2) x64 AES
                L2:4.0 MB L3:40.0 MB 16C/32T NUMA:2
 * MEMORY       7.6/251.8 GB (3%)
...
 speed 10s/60s/15m 5663.1 5677.9 n/a H/s max 5682.0 H/s
```

How much Hashes will be with DDR3 1866 ?
Thanks.

# Discussion History
## pawelantczak | 2019-12-02T20:56:52+00:00
Hi.
Your CPU doesn't support 1866.

## minzak | 2019-12-03T13:24:30+00:00
E5 v1 - yes maximum 1600 for my current workstation https://www8.hp.com/h20195/v2/getpdf.aspx/c04111526.pdf
But E5 v2 some CPUs - can use at maximum:
Intel XeonE5-2609 v2 processor 1333
Intel XeonE5-2630 v2 processor 1600
Intel XeonE5-2650 v2 processor 1866

But how much will be different on 1333/1600/1866 ?

## Ca2F | 2019-12-03T14:06:22+00:00
I have a single socket 2680 v1 server with 1600Mhz dual channel i get 279 H/s with one thread.
On my Dual socket 2680 v2 server with 1866Mhz quad channel i get 550 H/s with one thread. 
So there is a decent difference, i am running right now 8 threads on each 2680 v2 right now in vm's on ESXI and the total hashrate is  7400 H/s.

## x151973 | 2019-12-04T07:21:26+00:00
> 
> 
> I have a single socket 2680 v1 server with 1600Mhz dual channel i get 279 H/s with one thread.
> On my Dual socket 2680 v2 server with 1866Mhz quad channel i get 550 H/s with one thread.
> So there is a decent difference, i am running right now 8 threads on each 2680 v2 right now in vm's on ESXI and the total hashrate is 7400 H/s.

Quick question, for dual socket system the term dual or quad channel mean each socket or both? in another word, assume one socket have only one slot each channel,  in your current successful quad channel implementation , how many physical mems you inserted into mobo?4 or 8?

## Ca2F | 2019-12-04T08:05:57+00:00
Quad channel is the memory configuration, dual socket refers to that i have two cpu's on that motherboard.  
https://en.wikipedia.org/wiki/Multi-channel_memory_architecture

Quad channel in my case is per cpu on the dual socket board with 4 sticks of 8gb for each cpu. 
In heavy memory applications like this one with a dual socket setup, you should try and limit the cross utilization between the sockets, since the QPI link between the cpu's are bandwidth limited. I noticed that when running one vm with 30 threads spread over both cpu's performed worse then 8 threads on one single cpu. 

# Action History
- Created by: minzak | 2019-12-02T19:35:46+00:00
- Closed at: 2021-04-12T15:12:37+00:00
