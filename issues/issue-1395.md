---
title: Segmentation error
source_url: https://github.com/xmrig/xmrig/issues/1395
author: sangraf
assignees: []
labels: []
created_at: '2019-12-08T11:26:26+00:00'
updated_at: '2021-04-12T15:10:35+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:10:35+00:00'
---

# Original Description
**Describe the bug**
Segmentation error

**To Reproduce**
sudo apt-get install git build-essential cmake libuv1-dev libssl-dev libhwloc-dev
git clone https://github.com/xmrig/xmrig.git
cd xmrig && mkdir build && cd build
cmake ..
make
./xmrig -a rx -o xmr-eu1.nanopool.org:14444 -u mywallet -p x -t 8 --donate-level 5

**Expected behavior**
start mining

**Required data**
 - [https://ibb.co/nm3VPvW](url)
 - OS: [Ubuntu 18.04]
 - Ryzen 1800X

**Additional context**
Segmentation error. How to fix?


# Discussion History
## SChernykh | 2019-12-08T20:06:02+00:00
Can you try to disable "Opcache" in BIOS? It fixes crashes on some 1st gen Ryzen systems.

## sangraf | 2019-12-09T02:44:53+00:00
> Can you try to disable "Opcache" in BIOS? It fixes crashes on some 1st gen Ryzen systems.

thanks, helped!

## 2010phenix | 2019-12-10T13:04:22+00:00
@xmrig, @SChernykh this is  not a AMD, even not know if need this one... if need make new issue..
find Intel even not start mining (think not detect L3 or even more not L3 ;))
Windows Server 2008 R2 (16 core)

 * ABOUT        XMRig/5.1.1 gcc/9.2.0
 * LIBS         libuv/1.31.0 hwloc/2.0.4
 * HUGE PAGES   unavailable
 * CPU          Intel(R) Core(TM)2 Duo CPU T7700 @ 2.40GHz (1) x64 -AES
                L2:64.0 MB L3:0.0 MB 16C/16T NUMA:1
 * MEMORY       5.1/8.0 GB (63%)

## setuidroot | 2019-12-11T14:24:29+00:00
> @xmrig, @SChernykh this is not a AMD, even not know if need this one... if need make new issue..
> find Intel even not start mining (think not detect L3 or even more not L3 ;))
> Windows Server 2008 R2 (16 core)
> 
>     * ABOUT        XMRig/5.1.1 gcc/9.2.0
> 
>     * LIBS         libuv/1.31.0 hwloc/2.0.4
> 
>     * HUGE PAGES   unavailable
> 
>     * CPU          Intel(R) Core(TM)2 Duo CPU T7700 @ 2.40GHz (1) x64 -AES
>       L2:64.0 MB L3:0.0 MB 16C/16T NUMA:1
> 
>     * MEMORY       5.1/8.0 GB (63%)

Intel Core 2 Duo T7700 with 16 cores (on 1 NUMA node) with 64MB L2 cache and no L3 cache?  I must have missed something lol.

The Intel T7700 has 2 cores and 4MB of L2 (without L3.)  I suppose a server with 8 of these T7700 CPUs could give you 16 cores and 32MB L2 without L3... but that would give you 8 NUMA nodes and a cool space heater.


I forked off xmrig's dev branch the other day and it's been running fine for me... difference is I compiled it with hwloc 1.11.9 (default from Ubuntu 18.04's APT package repository.) 


I think this issue along with the guy in #1403 are caused by the newer hwloc version(s.)  I'm not sure when this problem started as I've alway just used the default Ubuntu hwloc version... no actually, I built it with ~2.0.2 before and it worked fine but had no improvement so I never bothered updating it in my builds.  I manually configure my miners anyways.


@xmrig I suggest you try building 5.2.0 with an older (known working) hwloc version you used to build older xmrig versions that didn't have these issues.  It appears here that 2.0.4 is flawed from 2010phenix's post.

Maybe try hwloc ≤ 2.0.3?  I will start building with different hwloc versions and see if I can find which version starts these issues.  I'll report back any findings.


Or maybe I'm wrong... maybe it's just a problem with Windows (that shouldn't surprise anyone.)  But xmrig 5.2.0-dev code has been running well for me on Ubuntu 18.04 with package manager default hwloc 1.11.9 since around this time yesterday.

I suppose it could be the updated libuv version all the same... but (to my knowledge) libuv doesn't detect CPU caches.  I'm running xmrig 5.2.0-dev (with MO algo switch code) compiled with gcc/7.4.0 on Ubuntu 18.04 (5.0.0-37-generic kernel.)  I compiled it with default Ubuntu PM library versions: libuv/1.18.0 OpenSSL/1.1.1 hwloc/1.11.9.  This also works fine for me compiled with gcc-8, gcc-9 and clang-8/9/10; but I've found gcc-7.4.0 gives me the best hashrate, which is unexpected given performance improvements in gcc-9.  Probably my old Ubuntu distro.

Edit:

Another thought just came to me... @2010phenix try running your miner (the very same as above) with your config.json file set with "numa": false, (this is under RandomX part of config.)

````
"randomx": {
    "init": -1,
    "mode": "auto",
    "1gb-pages": false, //Not available in Windows, or xmrig less than 5.2.0
    "numa": false //Default is true, try setting to false
},
````

Maybe that numa=false won't make a difference on your system, but it does if you have multiple CPU sockets and I've been running mine with numa set to false because it tries to allocate 4 datasets (one for each of my NUMA nodes and one of my memory channels has failed so I had to disable the NUMA autoconfiguration and set it up manually for my particular system.)  My system is a dual socket AMD Opteron 6276 server FYI.

## 2010phenix | 2019-12-11T16:40:23+00:00
@setuidroot, coz not last... on issues time last - XMRig/5.1.1 gcc/9.2.0
and yes, other CPU work correct but this one not (and i think thay to cant correct detect threads)



## xmaci | 2019-12-15T18:28:46+00:00
> @setuidroot, coz not last... on issues time last - XMRig/5.1.1 gcc/9.2.0
> and yes, other CPU work correct but this one not (and i think thay to cant correct detect threads)

Me too has this error. I've 6 ryzens and 2 of them has this error. I tried everything, "1gb-pages": false, "opache" in the bios, new version xmrig. Can anybody give one more advice how to solve it?

# Action History
- Created by: sangraf | 2019-12-08T11:26:26+00:00
- Closed at: 2021-04-12T15:10:35+00:00
