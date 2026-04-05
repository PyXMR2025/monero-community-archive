---
title: Mining using GPU on Mac Pro
source_url: https://github.com/xmrig/xmrig/issues/2451
author: val3riefr
assignees: []
labels: []
created_at: '2021-06-20T18:01:45+00:00'
updated_at: '2021-06-21T10:02:57+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hi, i've been mining using xmrig but it's using CPU
I can't find a tutorial or set up as to how use the GPU instead
is it possible? I have a Mac Pro / 16 core / AMD Radeon Pro Vega II Duo 32 Go / 96 go RAM
I would be faster using GPU instead of CPU ..
Help would be much appreciated! 
Thanks

# Discussion History
## Lonnegan | 2021-06-20T18:39:28+00:00
Depends on what you are planning to mine. RandomX (Monero) is a CPU only algo, GPUs perform terribly bad in RandomX. Mine ETH or Ergo with your Radeon and stay at CPU only with Monero.

## val3riefr | 2021-06-20T19:36:53+00:00
Really? it's not possible to take advantage of the graphic card? AMD Radeon Pro Vega II Duo 32 Go is quite powerfull i think,  and i thought i could get better use of it compare of CPU...
I was starting to mine for ADA. Honestly i don't really know all the mining app or platform...
I would just like to benefit from the power of my graphic card, and computer. GPU is supposed to be faster than CPU

## Spudz76 | 2021-06-21T03:24:10+00:00
With some algorithms, sure.  CryptoNight still works pretty good on everything but Monero forked away from that quite a while ago the moment there were decent non-CPU devices chewing the old algos and a few ASICs possibly on the horizon.

RandomX which has variants that several coins are based on is intentionally CPU-only and was designed to be terrible for GPUs (so that CPUs never become useless as with algorithms such as ethash GPUs work better, or sha256 where ASICs could be developed, which made CPUs completely left in the dust).

You can bypass this limitation by using an autexchange pool, where you can run various other CryptoNight or Ethash into the pool and it pays out XMR.  Many complain that this isn't supportive of Monero The Blockchain but it does put exchange transactions for it to process (without which all the decentralization and "support" in the world doesn't matter).  Also makes a lot of one-way buys which makes XMR look more desirable in the market (probably boosts value).  So it does help but in a less direct way, and the bonus is you can get a ton of XMR for it.  MoneroOcean.stream is where I run everything (none of my CPUs are that good at RandomX either since essentially it's pointless without Ryzen/ThreadRipper/EPYC processors and all my stuff is older, and I have a pile of otherwise useless GPUs).  It also switches algorithms to whatever is of highest value currently as the prices on exchange to XMR change constantly which is a nice autopilot feature for max profit (and tuned to your hardware capabilities/talents).

Also most of the workable Apple OpenCL support is not generally known as stable or working, other than through compiling your own from [my fork branch dev-fixAppleOpenCL](https://github.com/Spudz76/xmrig/tree/dev-fixAppleOpenCL) otherwise it sees "AMD" and thinks it has all the extensions (which Apple OpenCL doesn't offer) and then it fails to compile the kernels at runtime.

## val3riefr | 2021-06-21T10:02:57+00:00
Thanks for your reply, though it's a bit complicated for me to understand everything...
i just started yesterday via unmineable.com to mine ADA using xmrig after watching a youtube tutorial. it works but doesn't pay off much....that's why i'm looking for a better solution, using Mac which I know is less comon for mining..
Is AMD Radeon Pro Vega II Duo 32 Go a good graphic card? would it allow me to mine well with it?
If anyone can direct me to a tutorial for GPU MAC mining or a link to an app or something that'd be great. I'm not very familiar with all the terms you mentioned..

# Action History
- Created by: val3riefr | 2021-06-20T18:01:45+00:00
