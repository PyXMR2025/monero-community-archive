---
title: Huge pages supported, but "0%" being used
source_url: https://github.com/xmrig/xmrig/issues/3160
author: comminutus
assignees: []
labels: []
created_at: '2022-11-14T16:15:07+00:00'
updated_at: '2023-09-20T14:38:06+00:00'
type: issue
status: closed
closed_at: '2022-11-15T19:11:39+00:00'
---

# Original Description
**Describe the bug**
I've enabled huge pages but when xmrig starts it says that huge pages are supported but it appears that none of them are being used.  It says "0% 0/1168 +JIT" 

**To Reproduce**
1. Enabled huge pages by executing `sudo sysctl -w vm.nr_hugepages=1280`
2. Start xmrig with sudo: `sudo ./xmrig`

**Expected behavior**
On other machines that I have the same version of xmrig running (and same OS), it says "100%" of the huge pages are being used.

**Required data**
 - Miner log as text or screenshot
 ```
 * ABOUT        XMRig/6.18.1 gcc/9.3.0
 * LIBS         libuv/1.44.1 OpenSSL/1.1.1o hwloc/2.7.1
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          Intel(R) Core(TM) i5-8500B CPU @ 3.00GHz (1) 64-bit AES
                L2:1.5 MB L3:9.0 MB 6C/6T NUMA:1
 * MEMORY       4.3/7.6 GB (56%)
                DIMM_A0: 4 GB DDR4 @ 2667 MHz [REDACTED]
                DIMM_B0: 4 GB DDR4 @ 2667 MHz [REDACTED]
 * MOTHERBOARD  [REDACTED]
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      [REDACTED] algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
[2022-11-14 11:03:12.427]  net      use pool [REDACTED]  [REDACTED]
[2022-11-14 11:03:12.427]  net      new job from [REDACTED] diff 4002K algo rx/0 height 2755682 (12 tx)
[2022-11-14 11:03:12.427]  cpu      use argon2 implementation AVX2
[2022-11-14 11:03:12.428]  msr      register values for "intel" preset have been set successfully (0 ms)
[2022-11-14 11:03:12.428]  randomx  init dataset algo rx/0 (6 threads) seed [REDACTED]...
[2022-11-14 11:03:12.429]  randomx  allocated 2336 MB (2080+256) huge pages 0% 0/1168 +JIT (2 ms)
```
 - Config file or command line (without wallets)
    `sudo ./xmrig -o [REDACTED]`

 - OS: Ubuntu 22.04


# Discussion History
## Spudz76 | 2022-11-14T21:02:15+00:00
Most likely disabled in `config.json`, look for the `cpu` section inside which there is `huge-pages` setting, which I'd bet is `false` (must be `true`)

Command line options do not override an existing `config.json` in most cases.

## SChernykh | 2022-11-14T21:05:07+00:00
`sudo sysctl -w vm.nr_hugepages=1280` doesn't guarantee that the system will actually allocate these pages. `MEMORY       4.3/7.6 GB (56%)` suggests that it failed (a lot of memory was already used when you tried it). Try to do it right after reboot, or better allocate hugepages in grub.

## Spudz76 | 2022-11-14T21:10:15+00:00
Also, check `cat /sys/kernel/mm/hugepages/hugepages-2048kB/nr_hugepages` to verify they were all actually reserved (the sysctl or any other method simply requests they be allocated if possible, and if `1280` weren't available it will just try to get as many as it can up to that amount).  Running the command multiple times can increase the reservations if a few more were available each time.  Using kernel args to force allocation before userspace boots and dirties all the pages always works (assuming you have enough memory in the first place, which you appear to have).

[beaten by minutes but hey I already had it mostly typed out]

## Spudz76 | 2022-11-14T21:29:26+00:00
Also 8GB works great if you're running console only, but once X has to run it pukes all over memory and you'd probably need 16GB to still have unmolested pages somewhere.  Do you really need a GUI?

If anything puts 4KB (one regular page) of allocation into any of the aligned 2MB zones, it can't use that zone anymore.  Thus it's real easy for no 2MB regions aligned to 2MB intervals to be clean once more than about half of memory is camped upon by something else.  And kernels/glibc intentionally randomize where in memory it places stuff so it's less predictable (because ability to predict where something will allocate is part of most hacks, especially buffer overflows).  Once memory is swiss-cheesed you can't get full slabs anymore.

If you do have to run a GUI then probably kernel args are the only way (put up the fences before releasing the livestock). Add `hugepages=2048` to your grub kernel cmdline string, `update-grub`, `reboot`, check that sys file to verify it happened.



## comminutus | 2022-11-15T19:11:39+00:00
Setting `hugepages-2048` as a kernel parameter worked beautifully.  Thanks @Spudz76 and @SChernykh !

# Action History
- Created by: comminutus | 2022-11-14T16:15:07+00:00
- Closed at: 2022-11-15T19:11:39+00:00
