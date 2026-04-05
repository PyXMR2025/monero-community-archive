---
title: 'xmrig selection of NUMA node RX database memory allocation '
source_url: https://github.com/xmrig/xmrig/issues/1669
author: setuidroot
assignees: []
labels: []
created_at: '2020-05-05T08:54:02+00:00'
updated_at: '2021-04-12T14:57:48+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:57:48+00:00'
---

# Original Description
Hey, I have a question relating to NUMA memory allocation with xmrig.  First up, my hardware:


HP Proliant DL385 G7 Rackserver


Dual socket AMD Opteron 6276 CPUs


^ So I have two CPUs, each with 16 cores split evenly across two chip dies = two NUMA nodes per CPU.


Each server has 2 CPUs for a total of 4 NUMA nodes.  So in a way it's like I have 4 CPUs, but 2 CPUs are packaged together into one CPU chip.  The Ryzen and Threadripper CPUs are the same way, with the Threadripper having 2 Ryzens "glued" together onto one CPU chip... only mine are much older and they lose me money mining 😅.


Anyways, each server has two CPU sockets (with 2 NUMA nodes per socket) and each NUMA node has two memory channels... thus each CPU is quad channel.  With some of my dual socket servers I have (the performance optimal minimum requirement) of 8 RAM sticks.  Those 8 RAM sticks are required to keep all of the memory channels available for xmrig's mining threads to allocate a 2MB hugepage for each mining thread.  If I take any RAM sticks out, then I'd leave one (or more) of the 8 memory channels unpopulated and that results in ~50% loss of hashrate for the mining threads running on whichever of the 4 NUMA nodes that just lost one of its memory channels.


So all of my servers have 8 sticks of RAM... I don't have enough RAM to add any more and I don't want to spend money on DDR3 😎.


Some of my servers have 8 2GB sticks and the rest have 8 1GB sticks.  Well, the servers with 8 1GB sticks don't have enough RAM to run with 1GB hugepages (which is preferred over 2MB pages with *numa: true* because having only one dataset using 1GB pages gets better hashrate than having 4 datasets using 2MB pages.)  The CPU's TLB size is only 1536 4K pages... so even at 2MB pagesize, that is still more pages than the TLB is designed to handle.


Unfortunately my servers with 8 1GB RAM sticks won't run xmrig with 1GB hugepages; even with default_hugepagesz=1G and hugepages=3 (or 4) set on the kernel cmdline (/etc/default/grub) the server will only create a maximum of 2 1GB hugepages.  Which seems like some BS to me... 8GB RAM ≈ 7.7 GiB (7,884 MiB) and 2GB hugepages (2048 MiB) = 7,884 MiB (total RAM) - 2048 MiB (2 GB pages) = 5,836 MiB RAM remaining.  IMHO that's plenty of RAM left to make another 1 or 2 GB hugepages 🤔.  I think maybe I can get that working with a custom Linux Kernel compilation... I just haven't had the time (or the HDD space 😟) to really get around to doing that as of yet.  I'm running a stock installation of Lubuntu Eoan 19.10... or at least it started out as stock 😏.  I've since disabled a lot of bloat (including the desktop environment: sddm.)


Anyways I'll get down to my question:


Is it possible to run xmrig with a setting telling it how many NUMA nodes to use (say, 2 out of 4 NUMA nodes) and to tell it where (which NUMA nodes) to create the RandomX dataset on?  Specifically to me it would be important to be able to define **which** NUMA nodes xmrig uses 🤔.


The reason I ask is because I found out I can get the best hashrate on my 8GB RAM servers (that cannot run with 1GB hugepages or with numa: true) by using a little trick.  The trick is best done after a reboot (clean RAM and I boot only to terminal, no DE.)  I start xmrig with my config file set with numa: true ... xmrig creates 3 2080MB datasets, but it always fails (0% hugepages) on one of the four NUMA nodes after it makes three datasets, then it is killed off by OOM Killer.  Right after this I run the same xmrig binary (with the same config.json, only with numa: false set) and it starts up and runs with just the one dataset (2,336 MB total.)  But I **always** get a higher hashrate by starting xmrig in this manner.  <s>I don't understand why because when I look in /sys/devices/system/node/node*/hugepages/nr_hugepages I can see all 4 NUMA nodes and the exact number of allocated 2MB hugepages; looking at free_hugepages and subtracting the value of nr_hugepages tells me how many hugepages xmrig is actually using: it always only uses 1,168 2MB hugepages, which tells me that my trick of starting xmrig with *numa: true* to make it allocate more than one dataset before I run it with *numa: false* should **not** make any performance difference... but it does 🤔.</s>


============
**TL;DR** This part is newer:

Okay, I wrote most of this awhile back and I have new information since then.  I understand why my "trick" of running xmrig with numa: true and letting OOM killer kill it helps the hashrate.  It is because when I run xmrig normally (no "trick"); xmrig allocates the RX dataset to the inside two NUMA nodes (node 1 and 2) while using a few 2MB hugepages on the outside 2 NUMA nodes (node 0 and 3) for mining threads.


When I run xmrig with the "trick" method, then xmrig allocates the hugepages in an opposite manner: it uses the outside 2 NUMA nodes (node 0 and 3) for the RX dataset, while using the inside 2 NUMA nodes (node 1 and 2) for a few 2MB pages for mining threads.  Xmrig gets better hashrate when it uses the outside 2 NUMA nodes for the dataset.


But wait... there's more!


Using a series of commands (of which I don't really remember) combined with starting/stopping xmrig in various ways... I managed to get even better hashrate!  I've actually had this better hashrate in the past, but I didn't know why or how to obtain it until now.  It's getting a better hashrate now that xmrig has allocated most of the RandomX dataset to the outside 2 NUMA nodes (node 0 and 3) but it has now also allocated part of the dataset to NUMA node 1 (an inside node!)


Pictures are worth a thousand words... I made a simple bash script that prints out a nice table showing you where (which NUMA nodes) xmrig is using.  This table is most pretty if you set hugepages to zero (sysctl vm.nr_hugepages=0) after xmrig is up and running.  This way the system removed unused hugepages and you get to see exactly what and where xmrig has allocated its hugepages.


This picture probably explain best what I'm trying to explain:

![xmrig-NUMA-node-allocation](https://user-images.githubusercontent.com/32213080/81048895-c75ee880-8e82-11ea-915c-104916a06c4c.jpg)

The above picture I used this simple shell script (https://github.com/setuidroot/check-hugepages) to show xmrig's 2MB hugepage allocation per NUMA node.  In this picture NUMA is set to false (so only on RX dataset is made.)  Unfortunately I didn't get a picture of the bad hashrate I get without the "trick" method... but it's the exact opposite of the one labeled "Good Hashrate" (the RX dataset is allocated to the inside NUMA nodes 1 and 2.)

I would like to be able to set xmrig to run with 2 NUMA nodes (out of 4 available) so xmrig will maximize the usage of the available RAM.  I would also like to be able to tell xmrig which NUMA node(s) to use for allocating the RX datasets.  If I could control where it allocates the RX dataset, I could improve the hashrate even more.


I bet the best hashrate would be achieved with 2 RX datasets (the first allocated between NUMA nodes 0 and 1; the second allocated between NUMA nodes 2 and 3.)  This would keep the NUMA nodes local to their respective CPUs and maximize hashrate given less than optimal amount of RAM.


It would also help with 1GB hugepages (where you have enough system RAM) because you could control where to setup the 1GB hugepages... setting 2 1GB hugepage RX datasets (local to their respective CPU) just like I mentioned above would increase hashrate where I have 16GB of RAM (which is enough to make 10 1GB hugepages; but I cannot set NUMA: true because I'd need 3 GB hugepages per NUMA node and node 0 only has 1 GB hugepage.)


Basically... it would be cool to add a feature to xmrig so instead of setting NUMA: true or false; you could set it to a number (like 2) and it would make 2 RX datasets.  Controlling where (which NUMA node) xmrig makes these datasets would further increase its hashrate on multi-socket/NUMA systems.

# Discussion History
# Action History
- Created by: setuidroot | 2020-05-05T08:54:02+00:00
- Closed at: 2021-04-12T14:57:48+00:00
