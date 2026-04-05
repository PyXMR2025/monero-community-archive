---
title: What value should vm.nr_hugepages be set?
source_url: https://github.com/xmrig/xmrig/issues/2589
author: jpmolinamatute
assignees: []
labels: []
created_at: '2021-09-18T16:09:23+00:00'
updated_at: '2021-09-20T19:53:33+00:00'
type: issue
status: closed
closed_at: '2021-09-20T19:53:33+00:00'
---

# Original Description
**Describe the bug**
I'm looking at this [file](https://github.com/xmrig/xmrig/blob/6d66051d920be59be9547ea8ddbc88634a62b137/scripts/enable_1gb_pages.sh#L5) and in there, `nproc` will produce a number of CPUs. However, the [link](https://xmrig.com/docs/miner/hugepages#onegb-huge-pages) from the same file says we need to set it to a constant of 1280. This makes me to believe there is a discrepancy between the documentation and the script. If I'm correct, what should be the right value? and if I'm wrong why is this different?


# Discussion History
## SChernykh | 2021-09-18T16:15:35+00:00
1280 is for a setup without 1 GB pages. With 1 GB pages enabled you only need 1 huge page per thread (`nproc` in total) and 3x1 GB pages per NUMA node.

## jpmolinamatute | 2021-09-18T16:27:46+00:00
@SChernykh Thanks for answering my question! I understand now! :-)

## Spudz76 | 2021-09-18T16:44:15+00:00
Also various algorithms use various amounts of pages and only RandomX uses 1GB pages so if you are algo-switching then you need both 3x1GB pages and a whole bunch of 2MB ones.

I run the miner so it autoconfigures all algos, and shows what number of pages it tries to allocate and then set it to that number.  Note there are several allocation phases so add up all the allocations for the total number.  Sometimes there are a few more used but not shown so if it still doesn't fully allocate add however many were missing to the `nr_hugepages` amount.

You could also set it to 3000 or something crazy then run the miner with the max usage algo (astrobwt needs 10 per thread).  While the miner is running go to another shell and check `grep . /sys/devices/system/node/node*/hugepages/hugepages-*/*` which will show how many pages are actually in use (`nr_hugepages - free_hugepages`), then set the `nr_hugepages` to whatever that is.

Also note hugepages must be contiguous and aligned to an even pagesize boundary so 1GB hugepages usually need to be set with kernel options so that nothing pukes 5 bytes into all the regions during boot before they can be reserved by startup scripts (systemd tends to hit them a little late).  2MB are easier to find but if you have low total memory it may still not be able to get them all.  You can continually keep setting the `nr_hugepages` and each time it might find a few more.  I generally reserve both types from kernel args instead of bothering with setting it in userspace.  Such as: `hugepagesz=1GB hugepages=3 hugepagesz=2MB hugepages=84`

Note your CPU must support flag `pdpe1gb` or its memory controller doesn't do 1GB pages at all (in any OS).  `lscpu | grep pdpe1gb`  but also if it doesn't have the feature the `hugepages-1048576kB` sysfs directory won't exist so you'd see that it's unsupported in the check-grep from above because it uses globbing to pick up anything in there at all.  It will also show if you have more than one NUMA node, in which case each node needs its own 3GB dataset.

## jpmolinamatute | 2021-09-18T17:54:42+00:00
@Spudz76 this is so interesting!!! :-) as far as I know my motherboard / CPU supports NUMA nodes but they are not configured (at least I didn't) is there any real advantage on configuring one or more NUMA nodes??? (this machine will be used only for mining)

## Spudz76 | 2021-09-19T13:08:02+00:00
NUMA Nodes occur when needed by default, you don't configure them.  xmrig would say more than `NUMA:1` in the startup messages just below the CPU identification line:
```
 * CPU          Intel(R) Core(TM) i7-4700MQ CPU @ 2.40GHz (1) 64-bit AES
                L2:1.0 MB L3:6.0 MB 4C/8T NUMA:1
```
versus
```
 * CPU          Intel(R) Xeon(R) CPU X5660 @ 2.80GHz (2) 64-bit AES
                L2:3.0 MB L3:24.0 MB 12C/24T NUMA:2
```
Some AMD Threadrippers have multiple nodes in one physical CPU, but for the most part it only happens when you have a multiple physical CPU server motherboard.

NUMA Nodes just make sure each CPU (or, memory controller inside the CPU) all allocate from memory that is directly connected to that memory controller (so it doesn't have to go "far" to access it).  On these sort of boards certain DIMM slots are for certain CPU sockets and you must fill them up correctly (so each node gets 1/Nodes of the total RAM amount, and has locally wired RAM at all).

## jpmolinamatute | 2021-09-20T19:53:33+00:00
@Spudz76 thanks again for your explanation and for taking the time to reply to my message :-) very helpful

# Action History
- Created by: jpmolinamatute | 2021-09-18T16:09:23+00:00
- Closed at: 2021-09-20T19:53:33+00:00
