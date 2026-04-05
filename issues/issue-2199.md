---
title: 'why donate level is 5% ?even though I modify the donate.h '
source_url: https://github.com/xmrig/xmrig/issues/2199
author: seisdr
assignees: []
labels:
- question
created_at: '2021-03-22T00:59:01+00:00'
updated_at: '2021-03-23T05:17:37+00:00'
type: issue
status: closed
closed_at: '2021-03-23T05:17:37+00:00'
---

# Original Description
I do like to donate but not with a old dumb laptop

# Discussion History
## seisdr | 2021-03-22T01:01:53+00:00
```
* ABOUT        XMRig/6.10.0 gcc/8.3.0
 * LIBS         libuv/1.41.0 OpenSSL/1.1.1j hwloc/2.4.1
 * ABOUT        XMRig/6.10.0 gcc/8.3.0
 * 1GB PAGES    disabled
 * CPU          Intel(R) Core(TM) i3-4030U CPU @ 1.90GHz (1) 64-bit AES
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          Intel(R) Core(TM) i3-4030U CPU @ 1.90GHz (1) 64-bit AES
                L2:0.5 MB L3:3.0 MB 2C/4T NUMA:1
                L2:0.5 MB L3:3.0 MB 2C/4T NUMA:1
 * MEMORY       2.8/3.8 GB (74%)
                Bottom-Slot 1(left): 4 GB DDR3 @ 1600 MHz HMT351S6EFR8A-PB
 * MOTHERBOARD  Hewlett-Packard - 227F
 * MOTHERBOARD  Hewlett-Packard - 227F
 * ASSEMBLY     auto:intel
 * DONATE       5%
 * POOL #1      gulf.moneroocean.stream:10128 algo auto
 * POOL #1      gulf.moneroocean.stream:10128 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
 * OPENCL       disabled
 * CUDA         disabled
``

## seisdr | 2021-03-22T01:03:36+00:00
also how can I do it like stop the mining waiting for the laptop to cool down then resume mining automatically

## Lonnegan | 2021-03-23T00:25:12+00:00
Default dev fee is 1% not 5%. But you are not really asking the developer how to disable the developer fee, are you? ROFL

You are mining to moneroocean. Is it possible, that you are not using the official xmrig version, but moreoocean's one?

## seisdr | 2021-03-23T00:28:51+00:00
no the official

## seisdr | 2021-03-23T01:00:08+00:00
![IMG_٢٠٢١٠٣٢٣_٠٣٥٨٤١](https://user-images.githubusercontent.com/45742462/112076852-1a14c200-8b73-11eb-8991-fd5d980e5884.png)
see

## xmrig | 2021-03-23T03:41:28+00:00
Don't forget to edit your `config.json` too.
Thank you.


# Action History
- Created by: seisdr | 2021-03-22T00:59:01+00:00
- Closed at: 2021-03-23T05:17:37+00:00
