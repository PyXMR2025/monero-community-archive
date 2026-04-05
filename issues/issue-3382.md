---
title: Inconsistent Hashrate on Zen3 EPYC
source_url: https://github.com/xmrig/xmrig/issues/3382
author: Chadwicksracing
assignees: []
labels: []
created_at: '2023-12-15T02:45:47+00:00'
updated_at: '2025-06-18T22:29:28+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:29:28+00:00'
---

# Original Description
**Describe the bug**
Inconsistent Hashrate on Zen3 EPYC 7773X.  

![image](https://github.com/xmrig/xmrig/assets/42011043/c816d6d8-e2aa-450c-a2bb-d6c6819b848a)

Pull 2

![image](https://github.com/xmrig/xmrig/assets/42011043/0dadbe77-bcad-4ebf-9cf7-3d28e0d560b4)

Pull 3

![image](https://github.com/xmrig/xmrig/assets/42011043/44be1af6-bfd1-4ac4-85f2-30d10fc55af1)

Pull 4

![image](https://github.com/xmrig/xmrig/assets/42011043/70814757-b45d-4e58-86bd-2720c3ddf84f)


**To Reproduce**
Run Benchmark over and over again.  

**Expected behavior**
I would expect to see similar hashrate has the 7742 or 7B12 (ZEN 2, 7 nm)

similar to this bench: https://xmrig.com/benchmark/36Smmu

I have 16 sticks of 8gb dual rank ram.  

**Required data**
 - Miner log as text or screenshot
 
 - Config file or command line: 
 @echo off
cd /d "%~dp0"
xmrig.exe --bench=1M --verbose
pause
 - OS: Windows 10 22H2 


**Additional context**
Add any other context about the problem here.


# Discussion History
## SChernykh | 2023-12-15T21:28:29+00:00
Does each of CPUs have 8 sticks of RAM? I see on the screenshot that one of the sticks is different from the others, maybe this is the reason.

It can also be because each of CPUs has 768 MB cache (3x more than needed), and some parts of cache are slower than others. Then it's just random where the allocated memory will be cached.

Can you run `xmrig --export-topology` and attach the resulting XML file here?

## Chadwicksracing | 2023-12-16T00:32:33+00:00
The different ram stick was due to a dead stick in my lot.

I can try to get same ram part #. But the specs are the same.

The 3d cache is supposed to be faster, from my understanding.

I will get the topology in a few.

On Fri, Dec 15, 2023, 4:28 PM SChernykh ***@***.***> wrote:

> Does each of CPUs have 8 sticks of RAM? I see on the screenshot that one
> of the sticks is different from the others, maybe this is the reason.
>
> It can also because each of CPUs has 768 MB cache (3x more than needed),
> and some parts of cache are slower than others. Then it's just random where
> the allocated memory will be cached.
>
> Can you run xmrig --export-topology and attach the resulting XML file
> here?
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/3382#issuecomment-1858510966>, or
> unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AKAQTI4CX5TVB2G3RJY5LCDYJS6IRAVCNFSM6AAAAABAVZNPTCVHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMYTQNJYGUYTAOJWGY>
> .
> You are receiving this because you authored the thread.Message ID:
> ***@***.***>
>


## SlavisaBakic | 2023-12-17T00:23:09+00:00
> The different ram stick was due to a dead stick in my lot. I can try to get same ram part #. But the specs are the same. The 3d cache is supposed to be faster, from my understanding. I will get the topology in a few.

Epycs and Ryzens have already enough L3 cache (2MiB per thread) and RandomX don't benefit from additional L3 (3D) cache.



## Chadwicksracing | 2023-12-18T05:24:03+00:00
> Does each of CPUs have 8 sticks of RAM? I see on the screenshot that one of the sticks is different from the others, maybe this is the reason.
> 
> It can also be because each of CPUs has 768 MB cache (3x more than needed), and some parts of cache are slower than others. Then it's just random where the allocated memory will be cached.
> 
> Can you run `xmrig --export-topology` and attach the resulting XML file here?

Had to change to txt file, but here it is:

[topology.txt](https://github.com/xmrig/xmrig/files/13699703/topology.txt)


# Action History
- Created by: Chadwicksracing | 2023-12-15T02:45:47+00:00
- Closed at: 2025-06-18T22:29:28+00:00
