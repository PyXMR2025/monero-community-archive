---
title: Bus error
source_url: https://github.com/xmrig/xmrig/issues/2926
author: kurciqs
assignees: []
labels:
- bug
- arm
created_at: '2022-02-07T18:40:55+00:00'
updated_at: '2022-06-27T19:48:41+00:00'
type: issue
status: closed
closed_at: '2022-06-27T19:48:41+00:00'
---

# Original Description
Although I've looked at many reports of this error, the most common answer was that XRandom needed at least 2.1GB of memory.
Well, I checked, my device has got that. So what's the problem?

This is what I get:

pi@raspberrypi:~/Documents/bots/xmrig/build $ sudo ./xmrig -o gulf.moneroocean.stream:10128 -u MY_ADDRESS -p MY_NAME
 * ABOUT        XMRig/6.16.4 gcc/10.2.1
 * LIBS         libuv/1.40.0 OpenSSL/1.1.1k hwloc/2.4.1
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          ARM Cortex-A72 (1) 32-bit -AES
                L2:0.0 MB L3:0.0 MB 4C/4T NUMA:1
 * MEMORY       2.1/3.7 GB (56%)
 * DONATE       1%
 * POOL #1      gulf.moneroocean.stream:10128 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2022-02-07 19:35:47.716]  net      use pool gulf.moneroocean.stream:10128  199.247.0.216
[2022-02-07 19:35:47.716]  net      new job from gulf.moneroocean.stream:10128 diff 128001 algo rx/0 height 2554447 (6 tx)
[2022-02-07 19:35:47.716]  cpu      use argon2 implementation default
[2022-02-07 19:35:48.919]  randomx  init dataset algo rx/0 (4 threads) seed 0478070098bd2c7f...
[2022-02-07 19:35:48.920]  randomx  failed to allocate RandomX dataset, switching to slow mode (1 ms)
[2022-02-07 19:35:52.786]  randomx  dataset ready (3866 ms)
[2022-02-07 19:35:52.786]  cpu      use profile  rx  (4 threads) scratchpad 2048 KB
Bus error
pi@raspberrypi:~/Documents/bots/xmrig/build $ 


Thanks.

# Discussion History
## Spudz76 | 2022-02-07T20:23:33+00:00
Maybe the zero cache.

Your allocation of 2080+256MB still fails, need even more free memory (OS probably not going to let you allocate every byte of free memory).  So it dropped back to slow mode.

But really in slow mode you're just going to get 1H/s (yes, one hash) even if it worked.  If it ever works without some cache.

## kurciqs | 2022-02-07T20:32:24+00:00
So what do you recommend doing?
Or should I just somehow make more memory available?

## whitlocj1 | 2022-02-19T20:55:58+00:00
Ok, after encountering the bus error and reading through the issues, I finally got ARM 7 32 bit working.  The bus error is due to a buffer being misaligned in memory and ARM cpus are sensitive to this.  I have only verified the fix for the astrobwt algo since I'm only mining dero, but I think as long as the device has enough memory, RandomX could also be fixed with the 'light' memory option.  Also, I'm running xmrig on low end Android phones through Termux/Userland so YMMV with other hardware.  Below is the complete set of steps I follow to get xmrig built and successfully mining dero (astrobwt) on 32 bit ARM 7 phones (note I'm starting with v6.16.4 source).

1.  `sudo apt-get install git build-essential cmake libuv1-dev libssl-dev libhwloc-dev`
2. `git clone https://github.com/xmrig/xmrig.git`
3. change this line in xmrig/cmake/flags.cmake from:
   ` set(CMAKE_CXX_STANDARD 11)`
    to:
    `set(CMAKE_CXX_STANDARD 17)`

    Also add `-fsanitize=alignment` to the end of CMAKE_C_FLAGS and CMAKE_CXX_FLAGS lines.  Note this flag is not strictly neccessary, but if you are building for a different algo, it will point out where the misaligned memory is at runtime
4.  Change to the xmrig/build directory and generate the make files (note these are the options I use for DERO mining):
`cmake -DARM_TARGET=7 -DWITH_HWLOC=OFF -DWITH_CN_PICO=OFF -DWITH_RANDOMX=OFF -DWITH_ARGON2=OFF -DWITH_KAWPOW=OFF -DWITH_OPENCL=OFF -DWITH_CUDA=OFF -DWITH_BENCHMARK=OFF -DWITH_SSE4_1=OFF -DWITH_CN_LITE=OFF -DWITH_CN_HEAVY=OFF -DWITH_CN_FEMTO=OFF ..`
5.  Edit the file xmrig/src/crypto/astrobwt/AstroBWT.cpp and right after:
  `#ifdef XMRIG_ARM`
`extern "C" {`
`#include "salsa20_ref/ecrypt-sync.h"`
`}`

add:

`uint64_t load64_le(uint8_t const* V)`
`{`
  `  uint64_t Ret;`
  `  memcpy(&Ret, V, sizeof(uint64_t));`
  `  return Ret;`
`}`

6.  For every occurrence of the call to  bswap_64, replace :

`*reinterpret_cast<const uint64_t*>`
with a call to the new function:
` load64_le()`

An example replacement would be:

`const uint64_t k = bswap_64(*reinterpret_cast<const uint64_t*>(v + (i - X)));`

to:

`const uint64_t k = bswap_64(load64_le(v + (i - X)));`

There will be 5 or 6 replacement needed in the whole file

7.  Switch back into the build directory and make as usual and this should produce a 32 bit ARM 7 version of xmrig with memory aligned correctly







## kurciqs | 2022-02-19T22:19:22+00:00
oh wow, this actually worked! thanks a lot! what a legend...
I think in the example you gave with
```An example replacement would be:

const uint64_t k = bswap_64(reinterpret_cast<const uint64_t>(v + (i - X)));

to:

const uint64_t k = bswap_64(load64_le(v + (i - X)));
```
you forgot a pointer at reinterpret_cast<const uint64_t>
just saying because I left the pointer there and I had to recompile


## whitlocj1 | 2022-02-19T22:47:54+00:00
> oh wow, this actually worked! thanks a lot! what a legend... I think in the example you gave with
> 
> ```
> 
> const uint64_t k = bswap_64(reinterpret_cast<const uint64_t>(v + (i - X)));
> 
> to:
> 
> const uint64_t k = bswap_64(load64_le(v + (i - X)));
> ```
> 
> you forgot a pointer at reinterpret_cast just saying because I left the pointer there and I had to recompile

Ah, yes you are right - copy/paste error on my part - I corrected the original post.  Thanks for pointing it out!

## benthetechguy | 2022-05-21T02:08:15+00:00
Should be fixed by #3054, discussed in the original version of this issue #2895.

## benthetechguy | 2022-06-27T19:19:52+00:00
Fixed in latest release. Can @xmrig @SChernykh please close this?

# Action History
- Created by: kurciqs | 2022-02-07T18:40:55+00:00
- Closed at: 2022-06-27T19:48:41+00:00
