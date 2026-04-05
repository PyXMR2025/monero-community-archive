---
title: Inconsistant benchmark numbers (v2.4.0)
source_url: https://github.com/xmrig/xmrig/issues/207
author: pjdouillard
assignees: []
labels:
- bug
created_at: '2017-11-19T07:38:03+00:00'
updated_at: '2019-12-22T19:20:43+00:00'
type: issue
status: closed
closed_at: '2019-12-22T19:20:43+00:00'
---

# Original Description
Hello,

I am using an i7-8700k (not OC but core enhancement active, so that's all core at 4.7Ghz - system is watercooled, relidded with liquiq-metal, and it runs at 50C under full load (that's 30C vs the toothpaste Tim) and I am getting very inconsistant benchmark numbers with the algo.  

Under Win 10, with no activity else the benchmarking via Nicehash interface, I get speed ranging from 440 to as low as 192 - with no parametrisation whatsoever.   At some point, I thought the cpu was "broken" because next to it is another system with an old i7-980x (another 6-core with HT enabled) that performs flawlessly at 262.  Another system with 2 old Xeon X5690 performs both at 243.

Sometimes, when I do run the algo to mine, it gets only 3 threads, other times it get 6.  Sometime those 6 threads give 200 H/s, and some other time 360.

So I dig and found I could setup cpu affinity (which I did) but I can't get better than 363 with a mask of 0x0555 (0000 0101 0101 0101).

Is there something I am missing here, or this cpu is just too fast for proper benchmarking?

I am open to help test code for you against this cpu if you need, because this baby is a jewel of speed.

While typing this, I re-did another benchmark, now I got 475...

When I received my Ryzen back from AMD (RMA'd for the segfault-bug), I hope numbers will less fluctuate.

# Discussion History
## gryle | 2017-11-20T10:50:12+00:00
Hi

I have the same issue with a coffee lake i5 8600k.
Sometimes the hashrate is 140, sometimes 220 and other times 310H/s
I thaught there was some issue with my new system


## gennadicho | 2017-11-22T23:49:29+00:00
@gryle set up monitoring on your system, and look for another process who eating CPU. 

## gryle | 2017-11-23T16:54:10+00:00
The only way to solve it is restarting xmrig until it gets the good hashrate.
Using the RAMMap utility from sysinternals and it's various "Empty..." options between restarts helps also

## pjdouillard | 2017-11-23T17:57:19+00:00
On the 5 systems I am using the algo on, all with Win 10, only this one is doing this.  All other systems have their Win 10 installed since quite a while now vs the 8700k who is kind of fresh (3-4 weeks).  

The CPU of the other systems are 980X, 5690X (dual), 4790k and a Ryzen 7 1800X.  
None of those are behaving like that.  
Speed I have on the CPUs while running:
980X : 260 H/s
5690X (dual) : 265 H/s (on each cpu)
4790k: 325 H/s
1800X : 530 H/s

When the cpu gets bugged down on those machines, the H/s goes down, but as soon as the cpu freed itself, the H/s rises again to its usual speed.  

While continue to investigate and come back when I have something.

Edit: On the command line, when start xmrig.exe, and press 'h' to see its hashrate, I always get around 415-420 H/s.  I am using it through Nicehash, so maybe it's them who reports a lower speed so they are paying me less?
Edit2: On the 1800X, I get 600 H/s on the command line...

## gryle | 2017-11-24T00:26:05+00:00
This issue seems specific to the new intel coffee lake CPUs.
I don't have this issue on other systems, one with an i5 3570k and another with an i5 4690.

## pjdouillard | 2017-11-27T17:08:50+00:00
Can you - and others also - post your benchmark vs your cpu@xGhz please and how many threads you are running please?  I am testing each system individually from 1 to 12 threads and nothing their speeds and where it seems (sometimes - not always) where performance drops (or diminishing return) as you increase the number of threads.

Will post back with my outputs.

## tarvcode | 2017-12-01T14:54:13+00:00
Just wanted to post that I'm seeing this same issue on my 8700k.  Hash from 280 - 400, hash rate stays stable at whatever rate it picks and doesn't move unless I restart the miner.

I was previously running a Ryzen 1600X and never saw this issue, speed was always consistent.

I just swapped my motherboard and processor and didn't reinstall, so programs running in the background isn't the issue.  Same exact setup as previously running the old processor.

## pjdouillard | 2017-12-01T15:59:00+00:00
On my 1800X@4Ghz, although sometimes it starts low, it climbs its way back to around 630-650 H/s eventually (with large pages and 8 threads - affinity set or not).

On the old Intel Gulftown/Westmere cpu (980X and X5690 Xeon), output is always the same at around 260-265 H/s with large page and 6 threads.

On the 4790k, I see the same kind of behavior as on the 8700k : on a 'good' start, it get 340 H/s (with large pages) or it can stick to low output at 220ish and stay there forever.  If I manually ramp up its threads, it finally reaches its 320-360 H/s with LP active.


Best I can get on the 8700k@5Ghz + large pages is around 450 H/s on a 'good' start.

When I 'crank' up the threads manually, it reaches around it best speed of 450 H/s as we can see here:

1 thread:
[2017-12-01 10:30:02] speed 2.5s/60s/15m 90.2 n/a n/a H/s max: 90.3 H/s

2 threads:
[2017-12-01 10:31:55] speed 2.5s/60s/15m 171.5 n/a n/a H/s max: 172.7 H/s

3 threads:
[2017-12-01 10:33:04] speed 2.5s/60s/15m 267.0 n/a n/a H/s max: 266.9 H/s

4 threads:
[2017-12-01 10:34:20] speed 2.5s/60s/15m 351.2 n/a n/a H/s max: 351.0 H/s

5 threads:
[2017-12-01 10:34:55] speed 2.5s/60s/15m 414.6 n/a n/a H/s max: 413.9 H/s

6 threads:
[2017-12-01 10:37:32] speed 2.5s/60s/15m 456.7 455.3 n/a H/s max: 456.3 H/s

I haven't check the code, so I don't know if it is done or not in it, but maybe some benchmark phase should be made with only 1 thread to have a ballpark figure of what N thread (minus some % of efficiency) should be. 

For example, let us say that a 1 thread bench on the 8700k is 85 H/s.  Theoretically, 6 threads would yield around 510 H/s in a perfect world but that is not possible due to OS overhead and other processes taking cpu time it will necessarily be lower.

In my case, 450 H/s seems the maximum I could reach with 6 threads so that is a 75% efficiency rating.

So if a system system with allocated N threads to the algo is performing at less then 75%  (ex: 1 thread bench is 50 H/s and the algo is asked to run with 3 threads => 3 x 50 H/s = 150 H/s @ 75% = 112 H/s) then we should warn the user that either the system is being used too much by other processes and the number of threads should be reduced.

The other things that is running in the back of my head is that the L3 cache is not able to load the entirety of its job workload and thus that why we see threads outputting only half of what they normally should.  Then maybe a pre-load should be done to get the cache at speed and force it to actually 'cache' what needs to be loaded.  That way, there won't be any slowdown.  That's what I do went I ramp up on the number of threads as the cache is 'getting ready'.

Or, threads are not launched all at the same time like it seems to be the case.  Instead they are launched one at a time so that each threads can allocated the L3 cache properly and starts to work near (@75% efficiency) of the 1-thread bench mark.  That way, I am sure we would not see such discrepancies between run and we would get way better stable numbers and efficiency.  Right now, it is a bit of a lottery to see if the L3 cache will be load up properly on those cpu.

Any thoughts?

## HansHagberg | 2017-12-16T01:43:31+00:00
Same issues here on a fresh i5-8600K rig. Installed latest Win 10 just 2 hours ago and XMRig was the first thing I tried after installing all drivers and stuff. Not even a GPU yet in the system.

I got around 220 at first attempt. Enabled huge pages, rebooted and then it wont go past 132.
This is with 4 threads. This CPU has 9MB L3 cache so that should be optimal.
2 cores doing nothing so definitely no extra CPU load causing this.

I have another coffee machine (I3-8350K) running at same frequencies but 3 threads producing 240 H/s so I know the new machine does not perform properly.

The above is version 2.4.2
When disabling huge-pages from command line (--no-huge-pages), hash rates goes up to 220.
Performance with different thread count is as follows

Threads....Hash rate......Hash rate without huge-pages
1....................84...................74
2.................160.................136
3.................163.................200
4.................130.................222
5.................199.................199
6.................193.................183

Looks like something is going on with the L3 cache here?

I also did some more testing with 2.4.3
Same behaviour but hash rate is max 225 with 4 threads on this one.
For the record, all the above is mining XMR.

## pjdouillard | 2017-12-16T02:02:39+00:00
Lately, I have used a tool called Process Lasso to force everything to run on HT core #0 & #1 (i.e. Windows process and the GPU mining process & threads), and force 5 threads of xmrig to run on the 5 remaining cores.  I was able again to reach 400ish H/s this way 'forcefully'.

What I am starting to think is those 8700/8600 CPU from Intel are not behaving like the previous gen.  I will say that even after rebooting and letting Windows 10 'sink in' for a few min of idling, 60% of the time I can't reach the maximum 450 H/s with just xmrig running.  

On those occasion that I can't get a good hash rate, I ramp up the threads one by one.  One, two and three threads gives me the maximum number of H/s for their thread count, but as soon as I go pass 3 threads, the H/s goes down and is lower sometimes then 2 threads **on a 6-core cpu**.  I just can't explain what is going on.

There is really something weird with these chip.  The same thing happens with xmr-stak so I am discarding the problem coming from xmrig.

On the Ryzen side, on the 4GHz 1800X, xmrig alone reaches 660 H/s (or 600 H/s stock clock)
My old 4790k (stock clock) with xmrig alone reachs 350 H/s without any retries or ramp up.

Will be interesting to see what is causing this behavior.

## MaKla89 | 2018-02-23T17:29:09+00:00
Sorry for digging in this old thread, but is there any update on the matter? :/ 
I just got my 8600k yesterday (after I've been playing around with xmrig for quite a while) and my system behahves like this:

i5 8600k @ 4,7 GHz (OC'ed) / 1,28 VCore

10% of all XMRIG-starts: about 120 H/s
80% of all XMRIG-starts: about 230 H/s
10% of all XMRIG-starts: about 340 H/s (!!)

The "decision" about WHICH of these states is being picked seems to be done the very instant I start XMRIG and won't change within any given time (even over night). I'd be quite happy about 340 H/s (if minnig would have been my only goal I'd have gone for Ryzen, but I like the intel parts :D) , but this completely annoying inconsistency really blows :( 

## gryle | 2018-02-24T22:52:50+00:00
No update that I know of :(
I seem to have better luck in getting 300H/s by running xmrig on windows startup 

## xmrig | 2018-03-14T23:51:03+00:00
Definitely something wrong with 8*** CPUs.
Thank you.

## pjdouillard | 2018-03-15T00:35:40+00:00
I am really starting to believe the 8000 series didn't follow the same '6-core' design of previous gen (or any gen for the matter).  It migh be an 8-core with 2 disabled cores and the frequency upped for higher IPC but somehow, the available 12MB cache isn't always fully available which would explain those drops.

That would somewhat explain that with 4 threads you often get the best hashrate at any given time, but you have to stop restart continuously with 5,6-core to get the optimal 440+ish hashrate that occurs once every full moon.  It's just speculation I know, but any other Intel 6-core cpus don't behave like that: they are consistaly reaching their optimal hashrare, whenever you launch xmrig (same thing with Ryzen 8-core chip).

## MaKla89 | 2018-03-15T06:05:35+00:00
Hm, either I'm more lucky over the last days or something changed: 5 out of 5 times in a row I reached 310 H/s without having to restart the miner at all :D I only updated the NiceHash Legacy miner, but I guess that cannot really be the origin of this improvement..

## bmatthewshea | 2018-07-07T16:41:29+00:00
Read thru thread. Yep: My 8700k/Coffeelake gets 400H using 5/6 cores (via configured threads).
But, it gets 320-330H if using all 6 cores/same configs. So.. I'm missing about 80h when all cores selected?
Occasionally, it will run at about 400-420h (starting it on all 6 cores). But i haven't seen it do that in a awhile. Running on 5 cores for now.. (v2.6.3)

## tarvcode | 2018-07-08T23:04:09+00:00
For what it's worth.
I've been having decent success getting maximum hash rate by doing the following...

1) Start XMRIG and let it run for about a minute, then
2) Start another instance of XMRIG and let it run for a minute as well, then
3) Exit the first instance of XMRIG and wait 30 seconds, check hash rate of remaining instance.
4) If hash rate isn't where it should be (around 430h), go back to step 2.

Usually works in the first three tries.  Works best if the computer has just been restarted and you aren't trying to multi-task while doing this.

## bmatthewshea | 2018-08-24T02:15:05+00:00
Thanks for tip @tarvcode , but I had that work like that maybe twice - sat here like 20-30 mins trying a few times - sometimes "never" works. I think it's just a roll of dice to be honest.
Almost always starts at 330-335H for me - occasionally lower - but can usually get it to ~330 after a few restarts. 

![image 1](https://user-images.githubusercontent.com/984097/44561296-b2c3d680-a719-11e8-9e7a-11524115a41b.png)

Those -all- should all be in the upper 70s/80. (And they are when it starts correctly @~430H. But that is rare.) 
It may show them on different cores on restarts, but it's always 2 "normal", the rest lower unless it starts correctly.

On Windows task manager it shows same percent of CPU being used regardless of hash rate (can be 100, 260, 330, 430). Same 'cpu load'.

Another clue(?) is if you can start it at higher/normal 430+ rate (i.e. you got lucky) it tends to restart at same higher rate if you stop it. (Unless you've stopped mining for a long time - and do something else cpu intensive) Then you're back to  330h or lower when you start it again.

## tarvcode | 2018-08-24T17:32:09+00:00
@bmatthewshea a few differences on my config.  I limit to five threads (six makes no difference, or even makes it worse) and specify affinity to make sure it's spread out on all the cores and not a hyperthread core.

`--threads=5 --cpu-priority=0 --cpu-affinity=0xAAA --max-cpu-usage=50`

![image](https://user-images.githubusercontent.com/16649815/44598763-b1d28980-a799-11e8-8edf-a16be402e407.png)

![image](https://user-images.githubusercontent.com/16649815/44598834-fd853300-a799-11e8-8f8c-72925a4275af.png)

![image](https://user-images.githubusercontent.com/16649815/44598855-1392f380-a79a-11e8-81a2-2239de8f272f.png)

The rest of these tips, YMMV;

Luck will drop to get that 430h/s if I'm running other programs, Chrome especially.   Fresh reboot seems to work best, or close everything.

Waiting 30 seconds or so between launching and closing seems to work best.  IE: Launch first instance, wait 30, launch 2nd instance, wait 30, close 1st instance, wait 30.  If no go, launch 2nd instance again and wait 30.  3 or 4 tries should do her.

## bmatthewshea | 2018-08-25T15:47:16+00:00
Thanks @tarvcode - had some luck killing/closing processes. Messing with threads/affinity/etc shouldn't be needed. Either it starts right or it doesn't (on 6). Not playing cpu config "games" to pump +100 more hashes when it should work in first place on defaults. I've spent enough time on this. -> No offense meant. -> I do appreciate your help.
Anyway..

One culprit on mine I think was the "Windows Modules Installer" service running at a continuous 10% load I had not noticed previously. (-> No windows updates are available - it's up-to-date. Not sure why it does that. Typical MS Windows, though..)

Killed that service off and waited till system was in 'calm' state as much as possible.
and:
![image 3](https://user-images.githubusercontent.com/984097/44619903-b2c6f200-a851-11e8-8f5e-032959ea4b18.png)
(Seen it higher, but good enough.)
Killed that.
Ran chrome. Waited a minute.
Started miner. 330h.
Closed Chrome waited for 'calm' (~30-60 secs.)
Started a new miner window and got ~430 again.
Maybe isn't reproducible 100%, but I have a bit more confidence that may be the chips 'issue'.

At any rate, this CPU problem needs to be addresses in code. It's still very annoying.
Worse: if you automate things at all, you can never guarantee the miner will (re)start at max level.

No other CPU I have does this w/ xmrig/xmr-stak. Does anyone have an idea on what is going on with the 8700? Articles (Intel)? 'Weird' cache (L2/L3) problems as proposed/mentioned? I have googled and don't see much. Just more complaints & guessing.

Seems to me If we don't even know what the issue really is (literally all I have seen are guesses), there is no way it will ever be addressed it this code or others.. just my 1.5 cents.



## apl-git | 2018-10-03T23:28:04+00:00
Any updates on this bug? Any estimations when, in which version will it be fixed? The bug can be easily reproduced in version 2.6.4 on my i5-8600K, under Ubuntu 16.04 and 18.04. Hashrate can take any values between 120 H/s and 300 H/s, but most of the times it is around 200 H/s. Getting 200 H/s is relatively easy, but getting 300 H/s usually takes several hours of babysitting the program.

# Action History
- Created by: pjdouillard | 2017-11-19T07:38:03+00:00
- Closed at: 2019-12-22T19:20:43+00:00
