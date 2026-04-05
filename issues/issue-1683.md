---
title: How to mine using 10, or 11 cores for stability?
source_url: https://github.com/xmrig/xmrig/issues/1683
author: juanjolozadap
assignees: []
labels: []
created_at: '2020-05-20T18:58:57+00:00'
updated_at: '2021-04-12T14:56:43+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:56:43+00:00'
---

# Original Description
Hi, I'm trying to mine in the best setting possible. I also have two (2) GPUs hooked to this motherboard which mine ETH, but no matter what I try, when I try to get the CPU to mine, after some time the whole system crashes.

Individually, the CPU can mine just fine, so do the cards, but it is when I configure it all to mine at the same time when things go south.

I am just looking for basic hints what's causing the problems and how better to configure. I'm using NiceHash which has "Extra Launch Parameters" which I prefer to use over touching .json file, so I can rapidly switch from configuration to another, since this is also a gaming computer.

Any kind of help will be appreciated. The PSU is 1000W and it doesn't seem to be an issue. It seems like a stability issue, but the problem arises when I try to mine with CPU+2.GPUs

Any help setting CPU Affinity, or Priority, or working Thread count, or a mixture of all, will be awesome. This seems rather uphill, and I consider myself savvy enough.

Thanks in advance

# Discussion History
## Masterbob79 | 2020-05-21T22:25:52+00:00
Try setting up Hiveos. You can boot it from a flash drive. It's a pain to set up, but then you dont have to deal with windows. I got my cpu mining xmr, and 2 gpus mining etc.

## Kudabelangfx | 2020-05-25T19:42:05+00:00
nicehash miner isnt here.. 
my rig mining eth and cpu xmrig same time without crash on windows. 

## divinity76 | 2020-06-15T23:19:08+00:00
instead of mining on the cpus, see if the same stability issue happens if you just torture the cpus, compile this little C program:
```
int main(){for(;;);}
```
and run as many instances of that program as you have real (non-hyperthreaded) cores, does the same happen when you just torture your cores?

## Spudz76 | 2020-07-09T03:10:54+00:00
Lots of "1000W" psu are really 750-850w if you're running them hard 24/7.  The "1000W" is peak.  Most reputable brands stopped doing that and list the 100% duty cycle watts where they won't overheat and get noisy.  Some cheaper knockoffs are "1000W" but have less ripple filtering or it gets noisy toward redline which will bitflip stuff and cause random untraceable crashes without tripping over-wattage protect and shutting off.

Add fans to make sure the internal case temp isn't going crazy, especially around the mobo vregs.  If the psu is sucking already hot air through itself it might as well be the same as a dead psu fan (it's moving air but the air is unhelpful).  Check for hotspots, laser thermo gun, I'd bet your psu is hotter than spec after being redlined + heat load from the gpus.  It should run a little longer with just one GPU mining and the other one idle if heat soak is the problem.

Also what CPUs and GPUs and how close are you to 1000w if you sum their max watts eaten?  Don't forget 12w for magnetic disk, or 5w for ssd, and watts for the fans, and everything - those can nickel and dime you up another 120w without being obvious.

## divinity76 | 2020-07-09T09:15:00+00:00
@Spudz76 i've been running a Corsair AX1600i for ~1600-1700W non-stop for weeks at a time (powering RX580 GPUs) without issues, it's rated as a 1600W PSU and has no problem delivering 1600-1700W 24/7 (also tested how far it could go, got unstable around 1800W, but it could deliver 1800W for short periods)

# Action History
- Created by: juanjolozadap | 2020-05-20T18:58:57+00:00
- Closed at: 2021-04-12T14:56:43+00:00
