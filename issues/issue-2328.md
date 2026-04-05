---
title: Can two XMRIGs be run on a M1 Apple at the same time?
source_url: https://github.com/xmrig/xmrig/issues/2328
author: esaruoho
assignees: []
labels: []
created_at: '2021-04-29T15:11:22+00:00'
updated_at: '2021-04-30T19:09:26+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hi, I'm trying to mine some XHV and some Monero, but is it possible for me to run two instances of XMRig at the same time so that one is mining Monero and the other XHV?

If so, should I have two copies of xmrig in separate folders and start them, or..?

I was briefly fiddling around with the idea of running 4hours of one config and then 4hours of another config, but now not sure if that's so feasible. Or can there be a timer set for xmrig where it will only run for a set period of time and then exit cleanly?

# Discussion History
## RS102839 | 2021-04-30T16:10:57+00:00
Current payback on mining Monero on M1 seems so low to be hardly worthwhile even if you did that full time and were hitting 2349 H/s, which appears to be the best you can expect with the current release of XMRIG.

Trying:
- Separate sub-folders with their own config.json, though you don't need two copies of XMRIG
- Limit two threads in the config.json for Haven and 4 for the other.

I did successfully run two xmrig instances, one running Haven, and also I tried Haven by itself (on M1) but was only getting around 220 H/s because that coin is using CN/Heavy.  Which makes it a lot less worthwhile than it appears.
Note: CN/Heavy uses 4 GB per thread

@esaruoho : suggest you close this issue as your question is answered.

## Spudz76 | 2021-04-30T19:09:26+00:00
It's essentially like driving your car two directions at once, unless you run XHV on a GPU and something else on the CPU.

You could use MoneroOcean to autoswitch based on profit (they pay XMR equivalent value for any algo mined) - switching based blindly on clock (not profitability) or running two miners on the cpu at the same time is only shooting yourself in the foot.

# Action History
- Created by: esaruoho | 2021-04-29T15:11:22+00:00
