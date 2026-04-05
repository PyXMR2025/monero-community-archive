---
title: 'Loki Will be using RandomXL  a custom RandomX variant '
source_url: https://github.com/xmrig/xmrig/issues/1044
author: SomethingGettingWrong
assignees: []
labels: []
created_at: '2019-06-28T16:30:46+00:00'
updated_at: '2019-07-12T15:59:52+00:00'
type: issue
status: closed
closed_at: '2019-07-11T16:29:14+00:00'
---

# Original Description
 testnet pool here: https://dev.imaginary.stream and a fork of xmrig that supports it here: https://github.com/jagerman/xmrig/tree/beta

Will you add to yours so that its integrated when OPENCL an CUDA Versions will be finished?

# Discussion History
## trasherdk | 2019-06-29T00:37:52+00:00
See #1028 :^)

## jagerman | 2019-06-30T16:07:34+00:00
> See #1028 :^)

What does #1028 have to do with this?

## necro-nemesis | 2019-07-05T16:42:53+00:00
Looks like SChernykh is at work on OpenCL.

https://github.com/SChernykh/RandomX_OpenCL

## Spudz76 | 2019-07-06T18:38:20+00:00
RandomX already works on CPU and has for at least a week (if you compile from beta branch)
CUDA has both merged into dev branch a couple hours ago (again, compile)
OpenCL is apparently next but nothing to see yet.

All devices require 2080MB of VRAM to run RandomX - and that's before any work scratchpads - so 3GB or more VRAM is definitely a requirement.  Not sure about RandomXL but I think any RandomX-based-algo has the 2080MB requirement regardless of the scratchpad size or other tweaks.

So, if you expect to run RandomX on small VRAM cards (like CN) you will be quite literally unable.  This algo deprecates hardware almost as bad as dagger (at least the waste of VRAM doesn't grow with time?)

## SomethingGettingWrong | 2019-07-10T15:05:40+00:00
Random X according to the designer has made it easy to modify it in config.h. **So there should be an expectancy of many variations in the coming months**.  I was letting the developer know so that he can go ahead and add Random XL into his miner. The links i posted in the original post were from a an fork for Loki project by one of the core Loki devs.  

## jagerman | 2019-07-10T18:24:04+00:00
@SomethingGettingWrong - the `evo` branch now has generic RandomX support, including for RandomXL, that supports RandomX configuration at run-time rather than compile-time.  (The current `beta` branch, though, only supports a linking to a single randomx lib; the change in `evo` fixes the issue.)

## Spudz76 | 2019-07-12T15:58:05+00:00
Aha!  I had switched to evo recently and thus did not know dev or beta didn't have this too.

## Spudz76 | 2019-07-12T15:59:52+00:00
Also the designer of the algo *and* the one doing the code here, are the same person.  I'm pretty sure they know how to use their own libs. :)

# Action History
- Created by: SomethingGettingWrong | 2019-06-28T16:30:46+00:00
- Closed at: 2019-07-11T16:29:14+00:00
