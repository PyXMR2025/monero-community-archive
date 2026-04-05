---
title: KawPow algo low hashrate compared to other mining software..
source_url: https://github.com/xmrig/xmrig/issues/2879
author: mauricioscotton
assignees: []
labels: []
created_at: '2022-01-19T20:53:38+00:00'
updated_at: '2022-01-20T08:43:20+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**Describe the bug**
Hey there guys!
I'm not sure if this is the correct place to open this issue but I'l post here due to the activity of this project. (Please let me know if I should open it somewhere else.)

I have a few GPUS and amongst them there is one GTX 1060 OC PNY 6GB (No user OC), this GPU based on kryptex (https://www.kryptex.org/en/hardware/nvidia-gtx-1060-6gb) should be yelding about 11MH/s and weirdly it was only producing around 7.4x\~7.8x MH/s as seen on XMR-Workers (https://github.com/coolhaircut/xmr-workers - CUDA now supported):
![image](https://user-images.githubusercontent.com/34411735/150210086-3fbb5957-0231-429b-a217-9d5aa5005630.png)

So then I thought, hey... its a PNY... what are you expecting from it eh?!
Upon placing it in my test rig, I have used T-Rex and KawpowMiner to compare results and was when Ive noticed that the other miners have at least 2MH/s difference!
So, I ask myself... is it CUDA optimization or is it their mining algo implementation?!

I have also played with threads, blocks, bfactor and bsleep but I only managed to increase the rate to 8MH/s but that was it...

Results:
XMRig: 7.4\~7.8MH/s
T-Rex: 9.90\~9.99MH/s
KawpowMiner: 9.73\~9.86MH/s

I really wanted to continue using XMRig as Ive liked the way it works and even contributed to XMR-Workers with CUDA support (Too bad I havent got any ATI laying around..)

BR,
Mauricio Scotton

**To Reproduce**
Use XMRig on Kawpow, then use T-Rex(https://github.com/trexminer/T-Rex/releases) or Kawpowminer(https://github.com/RavenCommunity/kawpowminer) to compare results

**Expected behavior**
XMRig to have a hashrate similar to other mining software.

**Required data**
 - Miner log as text or screenshot
![image](https://user-images.githubusercontent.com/34411735/150210561-f4e0321b-b2fb-4fbe-83ad-dd5f3808c359.png)

 
 - Config file or command line (without wallets)
 Kawpow CFG untouched:
 `        "kawpow": [
            {
                "index": 0,
                "threads": 256,
                "blocks": 20480,
                "bfactor": 0,
                "bsleep": 0,
                "affinity": -1
            }
        ],
`

 - OS: [e.g. Windows]
 Tested on both: Ubuntu Server 18.04 (x64) and Ubuntu Desktop 18.04 (x64)

 - For GPU related issues: information about GPUs and driver version.
 

**Additional context**
![image](https://user-images.githubusercontent.com/34411735/150211221-f7339f6a-c454-48ec-a0e3-693b937fd897.png)


# Discussion History
## Spudz76 | 2022-01-19T23:37:29+00:00
I have a bunch of the same PNY triple fan 6GB OC cards, they are actually one of the best somehow.  Besides the fans die every year and a half or so.  But I have had zero full-deaths and they thermal throttle nicely and the VRM on board seems one of the better ones.  They keep on going with fan and paste maintenance now and then.  Also their BIOS has the same clocks in P0 and P2 so they work fine even with nvidia's stupid P2-lock.  Contrasting I had a bunch of single fan short format MSI's and they are almost all dead (no heatsinking or  spreaders on the memory chips so some of them developed heat cracks, others I think ate their similarly badly cooled VRMs...)  And those have pretty nasty slow timings in P2 so I have to run the in Windows where I can disable the P2-lock (so they run in P0).

And admittedly I haven't been using the xmrig kawpow because it tends to explode on init and I run algo-switching so it will kill and init xmrig somewhat often.   So I use T-Rex (or lolMiner for AMDs) because it inits every time correctly.  I never quite made it to noticing the speed was or wasn't close to the others since having it crash out on an algo-switch for hours before I notice loses a lot more than the minor devfee to the other closed-source miners does.  And xmrig never really achieved enough stable work history to gauge its average performance.

All the 1060s are running ethereum, except for one that is cross-mining to XMR payout on MoneroOcean runs c29v most of the time because apparently it's worth more than kawpow (even T-Rex) anyway.

I will take it down for a few minutes to benchmark various kawpow miners and see if I can duplicate your results.

An immediate difference could be `mtweak` but if you weren't using it on T-Rex then that's not why it's faster (it's not on by default).

## Spudz76 | 2022-01-19T23:41:58+00:00
Okay first result, T-Rex 0.24.7
```
 GPU #0: GTX 1060 6GB - 12.28 MH/s, [T:80C, P:140W, F:0%, E:88.3kH/W], 15/15 R:0%
```

I am faster because of clocking, this card is +140 core and +1533 mem over stock-OC.  And powerlimit is set to 140 which it's using all of (might go faster, but hotter, with more watts).

## Spudz76 | 2022-01-19T23:51:56+00:00
Scores identical to yours on stock clocking, and 0.24.8, since I figured testing with extra OC and mtweak 1 and a different version was not really science.

## Spudz76 | 2022-01-20T00:09:35+00:00
Same rate as yours for xmrig also, confirmation achieved.

Also of note, xmrig draws 125W (vs 140W) and seems to stay about 4C lower thermally so it is somehow doing less work where it could be doing more.

EDIT: ended up 2C lower after running longer, seems to have topped out now.  125-127W fairly constant

## mauricioscotton | 2022-01-20T08:43:20+00:00
**Spudz76**, Thank you very very much for time and benchmarking your GPUS so that we could verify!
I'll try and set my other GPUS to P0 as I believe im loosing some hashes on them as well...

____________________________
> Okay first result, T-Rex 0.24.7
> 
> ```
>  GPU #0: GTX 1060 6GB - 12.28 MH/s, [T:80C, P:140W, F:0%, E:88.3kH/W], 15/15 R:0%
> ```
> 
> I am faster because of clocking, this card is +140 core and +1533 mem over stock-OC. And powerlimit is set to 140 which it's using all of (might go faster, but hotter, with more watts).

Ive noticed that you have posted your OC settings (Cheers for that), I'll try and set them to see if I can reproduce your OC speeds as well on T-Rex and KawpowMiner...
On core you mean CoreClock right?! or you mean CoreVoltage? (I assume it is clock, because i still havent figured out how to force undervolt on ubuntu)

____________________________


> Scores identical to yours on stock clocking, and 0.24.8, since I figured testing with extra OC and mtweak 1 and a different version was not really science.

Re: mtweak, I have tested on T-Rex mate, but I have not set MemTweak to test.... would this bring an hashrate improvement?

____________________________

> Same rate as yours for xmrig also, confirmation achieved.
> 
> Also of note, xmrig draws 125W (vs 140W) and seems to stay about 4C lower thermally so it is somehow doing less work where it could be doing more.
> 
> EDIT: ended up 2C lower after running longer, seems to have topped out now. 125-127W fairly constant

So, definitely there was something shady on XMRig hashrates!
And yes! youre right, you can clearly see that the GPUS are undertaking work... 

____________________________

Another thing I've noticed is that it looks like the hashrate oscilates more compared to other miners... 
(From the red point on)
![image](https://user-images.githubusercontent.com/34411735/150302960-00b6a0ad-fdf1-4da8-8609-314056d8f54b.png)
(rig-01 is running xmrig, same version but on Ubuntu 18.04 Server)
![image](https://user-images.githubusercontent.com/34411735/150303251-54fa71be-4aa5-43e4-8319-0d2a275f5c05.png)


# Action History
- Created by: mauricioscotton | 2022-01-19T20:53:38+00:00
