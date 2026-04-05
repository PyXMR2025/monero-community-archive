---
title: Mining cpu is going well.  Able to mine 4 cores w only 6MB cache.  Wondering
  if I squeeze something out of my GPU?
source_url: https://github.com/xmrig/xmrig/issues/2355
author: Entreprenerdz
assignees: []
labels: []
created_at: '2021-05-07T23:30:50+00:00'
updated_at: '2021-05-09T00:21:48+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Sorry as I'm certain this is probably more of a Reddit question but they seem to really not want me to log in there. (2FA fail, 'use google', ok, fail, grrr).... But I'm going to layout my path to here to hopefully help out a new miner with similar gear.

Been mining for 3 days... love xmrig... Here's my specs:

- Lenovo IdeaPad Y700 (2015)
- Product Number: 80RU00FSUS
- 32 Gb Ram
- intel i7-6700HQ (1 Socket, 4 Cores, 8 logical processors, 256KB L1, 1.0MB L2, 6.0MB L3 cache)
- nVidea 950M w 4GB Ram
- 240 M.2 SSD (OS, Monero blockchain)
- Samsung 850 Pro 512GB SSD (Secondary storage)
- Windows 10 Pro
- Hardware virtualization is turned off cuz I was running on 36-40 hours with no sleep and thought it would be a great idea to put a password on my BIOS.  Will need to tackle that after I get some accounting stuff taken care that only lives on this PC.

My first run at things, I think I just ran stock config.json created from wizard.  Results: 1085H/s

After more research, I was able to enable Large Pages by Run As Administrator.  Results: 1545H/s

3rd round, I find a Windows 10 tweak webpage and follow it as much as possible.  Set to best performace, disable non-MS services, O and O, etc... [Link here](https://www.reddit.com/r/MoneroMining/comments/f18825/windows_10_tuning_guide_for_randomx_mining/).  Reboot.  Results: 1565-1694H/s

This has been running with 3 threads up until now, but I see I have 8, with 3 pegged out at 100% and just felt like I should be able to get the 4/8 going.  (I understand the scratchpad size is 2048kb, but no idea how it works... so I tinker).  I had been playing with another PC and was able to tweak (easily) on command line with `-t 3` to `-t 4` but my rig runs via config.json so tinker and figure out I need to change `"rx": [0, 2, 4]` to `"rx": [0, 2, 4, 6]` and waddyaknow?  It works!  Not sure if this is a miracle, a fluke, or common, but 4/8 threads are 100%, other 4 are usings 11-12% cumulatively, Memory 10/32.  Results:  1780-1861 H/s

It may be working cuz I switched from 3-4 threads on the fly.  Here's a snapshot, which leads to my question(s):
![4 threads](https://user-images.githubusercontent.com/17835969/117515986-a412c180-af4c-11eb-91b7-1e8bc3f90396.png)

 My questions (in order of importance to me):
1.  How can I squeeze some effort outta my GPU?  I suspect I need to get CUDA working, have already updated my nVidea drivers, pretty sure I got a CUDA thrown in with it, just not sure if I need to run 2 xmrigs or config 1 properly.  I'm techy, but GPU stuff is outta my realm of comfort so don't be shy on the crayons when explaining please. :)
2. MSR - Is there something wrong with mine as openhardwaremonitor has nothing to do with mining.... BUT it does say 'register values for "intel" preset have been successfully' so I think I'm good here.
3. 4 threads - Not sure how but looking at the log it shows the switch and says `READY threads 4/4 (4) huge pages 100% 4/4 memory 8192 KB` which makes sense, but the previous line says `use profile rx (4 threads) scratchpad 2048 KB`.   Is that not supposed to be 2048KB for EACH thread so while the 8192KB adds up, I only have 6MB L3 cache.
4.  What's this all about?  I recall reading about locking this memory so it's always available, continuous, etc.  Is there anyway I could utilize my 32GB ram further by increasing this?  Also, looks like it's keeping 1/2 of it (1168/1168 +JIT) and I thought that only worked on Linux?  (Sorry if I missed something here, but I've been drinking from the Monero firehose for the past 48-72 hours and retention is slippery at best atm)
![2338](https://user-images.githubusercontent.com/17835969/117516919-62374a80-af4f-11eb-8c2c-353faf8781c9.png)
5.  Finally, I'm running a VPN (Mozilla), mainly to attempt to hide my mining from my ISP, and it's using a VPN in the same city as my pool's (supportxmr) server so I'm thinking it's not too bad.  I plan on switching pools to one that supports Tor (once I crack that nut and figure it out) and I hope that will give me a little more juice.  I'd get rid of the VPN now, but I don't want to see gains that will eventually be lost to Tor.  Thoughts?  Turf the VPN?  What's the possible outcomes should my ISP find out I'm mining?  I'm in Canada btw.

Low priority questions, verifications
1. OPENCL - disabled.  Can I do anything about it?  I'm guessing it's an AMD video thing so no.
2. Just wondering what the argon2 implementation AVX2 is all about cuz when I understand, I can tweak intelligently.
3.`1GB Pages unavailable`  - Linux thing... nothing can be done here.

Anyways, it's been running like this for about 5 hrs now, seems stable, fans are going pretty hard.  Gonna pop the case open and blast the dust out... betcha that gets me another 20H/s.
![hash2](https://user-images.githubusercontent.com/17835969/117517603-5e0c2c80-af51-11eb-9864-d6bcdb5f3b7c.png)

![cpu](https://user-images.githubusercontent.com/17835969/117517597-564c8800-af51-11eb-8f15-fc289b4bf667.png)
Thank you in advance for your time/effort.  I hope that this post aids a few newbies to the xmrig world and gets them going in short order.  Hit me up if you have any questions!

Now I'm gonna see if I can get 5 threads going... since apparently 6MB L3 cache isn't holding me back.

# Discussion History
## RS102839 | 2021-05-08T17:21:10+00:00
(5) Yes, always run a VPN

BTW:  I doubt if the ISP is concerned about this mining, but you don't need them to know.
TOR might reduce your throughput, but since you are mining at the rate of less than $2/week, why bother?

## Spudz76 | 2021-05-08T23:46:55+00:00
(1) Yes however it will work best on non-RandomX based coins and you will have another coin to exchange through some exchange (and maintain multiple types of wallets, if not relying on the exchange-wallet which may not be "your wallet" in a legal ownership sense)  RandomX is intentionally horrible on GPUs because it is intended to be CPU-only.  You can get around this limitation and hassle by using the MoneroOcean pool which pays XMR regardless what actual coins your equipment is mining (based on altcoin->XMR exchange values at the moment).  This requires a special fork of xmrig (at github/MoneroOcean) and xmrig-cuda also (it adds back CN-GPU which official fork removed a while back) with added features for sending all your hashrates for various algos to the pool so it can know what jobs to send.  And then yes you run two separate installs of xmrig, one for CPU-only and one for CUDA-only as they will be best at different "skills" - and running a single xmrig locks all backends to the same coin (almost never ideal, unless cn-heavy/xhv aka Haven is hot, but it is 4MB scratchpad so even worse vs your 6MB).

(2) Yes it's fine I run OHM also, and MSR stuff works fine via their WinRing0 driver despite the complaint.  You can set `verbose: 1,` in the config.json or use `--verbose` in commandline and it should say literally what it changed the MSRs from/to as additional confirmation.

(3) Yes you're overdriving cache size, it should not be faster, the reported hashrate might be inaccurate.  If anything you're killing some per-thread speed off the other three because the CPU has to "swap-out" cache loads to multitask four threads.  It might be doing that while waiting for slow system RAM which might be why it isn't getting "hurt" as much as it should (using wasted-anyway time).  Cache is always much faster than system RAM but RandomX needs to go read from the big dataset (2080MB) fairly often as well and then do some tight fast work using only the 2048KB cache.

(4) The amount of system RAM used will always be 2080+256MB per "node" so then if you had dual CPUs you would need 4160MB+256MB (the smaller shared bit is only needed once).  This is just how RandomX works.  There is no gain from forcibly using more memory.  However if you can overclock the memory or upgrade to the fastest your machine supports at least (if not already) which is all somewhat not possible on most laptops that would raise hashrate somewhat linearly.  Or if you have one stick but two slots usually having both slots filled allows double width bus which is faster (depends on motherboard design / chipset / CPU... whether this is a factor).  RandomX likes low latencies which is why buswidth or MHz both help out a lot.

(5) Lower RTT (the ms shown on accepted results) is always better, you want your findings to be sent to the pool ASAP in order to win any race conditions.  If another miner found a result at the exact same moment as you did, but your RTT sucks because it's bouncing around the Internet for no real reason, then the other guy wins.  Or, at the end of a round (when the "height" increments in the "new job" line) you might have a result that didn't make it due to a huge RTT.  Some pools pay "lates" some will reject them outright, most will split the winner with results that show up real close.  But your RTT looks good either way / Tor might really make it nasty though, and random.  Unsure why anyone would bother hiding anyway (unless in China, etc), use SSL pool connection and that mostly covers any concerns.  They can still know you're talking to "that pool" by IP but not anything being "said".  Most western democracies aren't going to block by IP like the Great Firewall of China.  If they do move to shut down mining they will follow the power usages so scan from the air with FLIR for hot-roofs just like with growing drugs.

## Spudz76 | 2021-05-08T23:58:58+00:00
Also most laptops have very barely good enough cooling, and the CPU and GPU both ride the same heatpipe apparatus, so mining both might/probably overheat it.  At least I had to quit heating up the GPU on mine (Lenovo W540) or it would directly shut off unexpectedly for thermal overload.  I've repasted a bunch of times the thermal pipes just can't do it.  Most aren't designed for full tilt on all the hot devices at the same time for 24/7 sort of duty cycle.  I do have an older Dell that does mine both okay but it just keeps going at 90C+ which isn't terrible but also not great.  It throttles back the CPU clock instead of shutting off, so the CPU hashrate dips out while it cools off a little.  The nVidia is older Fermi based Quadro and hits 87c which is also not good, but it is essentially a retired laptop and I won't cry if it fries itself.

## Spudz76 | 2021-05-09T00:09:06+00:00
Missed the sub-questions:

(1) OpenCL is for AMD, yes.  "would" work for nVidia also but CUDA is always faster.  If you compile yourself from source, and disable OpenCL then the message will go away completely.

(2) Argon2 is a crypto method that is used as a sub-part of other algorithms, when the coin uses it it will select the best ASM module/type for your CPU.  Newer 10000 series Intels have AVX512F which is faster but AVX is the best yours can do, it's not tweakable (other than forcing a different one, or disabling so it uses compiled C++ code rather than ASM module, both would lead to problems either slow, or "illegal instruction" because your CPU doesn't speak AVX512F).

(3) Yes 1GB Hugepages are only on Linux (and even then only on CPUs that support it).  Normal (2MB) hugepages are supported on Windows and since your allocations are all green 1168/1168 and etc, you've got that all good and the best Windows can be.

## Spudz76 | 2021-05-09T00:14:55+00:00
You can also compare with other reports of the same CPU, at the [xmrig benchmarks site](https://xmrig.com/benchmark?cpu=Intel%28R%29+Core%28TM%29+i7-6700HQ+CPU+%40+2.60GHz)

## Spudz76 | 2021-05-09T00:21:48+00:00
Also yes, the `-t 4` will never overdrive cache size in any case (it is a "hint" not a "command") which is why you had to manually add another core number to the array in the json file to obtain four threads.  And to get the autoconfiguration to reconfigure algos that were already put into the config.json you have to erase them from the config.json first (it does not even enter the autoconfig code if there is already a definition, thus doesn't even think about `-t` or other autoconf tweaks).  So really if you had a config.json with all the algos and used `-t 1` it would ignore you, because it doesn't need to do autoconf.

# Action History
- Created by: Entreprenerdz | 2021-05-07T23:30:50+00:00
