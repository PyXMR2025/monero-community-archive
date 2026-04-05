---
title: rx 1 Gb huge pages error
source_url: https://github.com/xmrig/xmrig/issues/1411
author: exty357
assignees: []
labels: []
created_at: '2019-12-13T08:37:13+00:00'
updated_at: '2021-06-05T18:43:28+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:10:07+00:00'
---

# Original Description
Hello!

[2019-12-13 11:31:17.395]  rx   msr kernel module is not available
[2019-12-13 11:31:17.395]  rx   init dataset algo rx/loki (20 threads) seed 57605565760671d4...
[2019-12-13 11:31:17.975]  **rx   failed to allocate RandomX dataset using 1GB pages**
[2019-12-13 11:31:18.023]  rx   allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (627 ms)
[2019-12-13 11:31:20.628]  rx   dataset ready (2605 ms)
[2019-12-13 11:31:20.628]  cpu  use profile  rx  (20 threads) scratchpad 2048 KB
[2019-12-13 11:31:21.011]  cpu  READY threads 20/20 (20) huge pages 100% 20/20 memory 40960 KB (384 ms)

i have 20 vCPU + 64 Gb RAM.

cat /etc/sysctl.conf | grep huge
vm.nr_hugepages =  4096

# Discussion History
## pawelantczak | 2019-12-13T09:01:14+00:00
You can remove entry from sysctl.conf, xmrig will do it for you (make sure running it with sudo).

## setuidroot | 2019-12-13T17:33:01+00:00
Typically 1GB hugepages must be enabled at boot with a (linux) kernel boot parameter.  I don't know if xmrig does this on its own (I don't see how it could unless you had already activated 1GB hugepages at boot with the kernel cmdline parameters.)  Unless xmrig adds the kernel boot parameters itself (I'm not sure because I've been using my own forked version that is behind on the latest commits.)  But even still you would have to reboot to have 1GB hugepages working because they're created at boot not runtime; they are allocated at runtime, but only if they've been configured to be 1GB in size at boot.

I see that xmrig (when run as root) will allocate its own hugepages (no need for "sysctl vm.nr_hugepages=1200") as xmrig grabs hugepages automatically.  The problem here is that hugepages are 2MB by default (on most systems.)  I'm specifically using Ubuntu/Debian for my examples here, but this should apply to other distros give or take a few commands and/or file paths.


To set 1GB hugepages as the default hugepage size you'll need to append some kernel boot parameters (I'll get to that later.)  First it's best to look at /etc/sysctl.conf and comment out any vm.nr_hugepages=x you might have added to it.  This is easily done with:

````
sudo nano /etc/sysctl.conf
````

Check sysctl.conf and make sure you didn't add anything hugepage related at the end of the file, if so it's best to comment it out (using # in front of the line.)  I don't know if this is necessary, but you're going to change the kernel's default hugepage size from 2MB to 1GB... so if you have vm.nr_hugepages=1200 set at boot, hopefully you have 1200+ GB of RAM (otherwise it'll swap to disk or probably error out.)  I don't know what it would do because I removed my hugepages entry from /etc/sysctl.conf beforehand.  You don't need hugepages set by sysctl.conf because xmrig (when run as root) will allocate it's own hugepages (so we need to set the system to 1GB hugepages so that xmrig can allocate them.)

**Run all my commands here as root**, start with this:
````
sudo su
````
Enter your sudo password and now you will be logged in as root for the shell session (Ubuntu is annoying with the non-root users and all the sudoing and password typing lol.)  But be careful what you type in when running as root if you're new to Linux.  Stick to copy/paste my commands here and you should be fine.

Note: I also set swappiness to 0 in sysctl.conf (you want to have enough RAM to do this and use 1GB hugepages; I'd say at least 8GB of RAM, multiply that by number of NUMA nodes or set **"numa": false** in config.json.)  Set swappiness to zero with the command below (this makes it so that Linux won't swap memory pages to disk unless absolutely necessary; it won't be necessary if you have enough RAM.)  If you don't have enough RAM, maybe set swappiness=1 so it'll swap to disk before crashing or killing programs.  The default swappiness is 60 (0-100 are valid) and this is too swappy for me lol.  I don't want it trying to swap my hugepages to disk (although those should be locked in memory anyways.)

````
sudo echo "vm.swappiness=0" >> /etc/sysctl.conf
````

Now on to 1GB hugepages:

First you'll want to check and make sure your system has 1GB hugepage capabilities... most newer (18.04+) Ubuntu versions do have this (I'm on kernel 5.0.0-37 currently.)  But check for hardware compatibility as well:

````
lscpu | grep -w "pse\|pdpe1gb"
````

The command above should print out cpu flags with "pse" and "pdpe1gb" highlighted in red.  If you don't see "pdpe1gb" printed out in red, then your hardware doesn't support 1GB hugepages; if you only see "pse" in red, then it only supports regular 2MB hugepages.

Not having **pdpe1gb** in cpu flags... it's like not having **aes**, it is a hardware limitation.  If you do see **pdpe1gb** and **pse** then continue on.  

Next we'll check to make sure 1GB hugepages are an option in sysfs... 

````
ls -Al /sys/devices/system/node/node*/hugepages/*1048*/
````

You should see these 3 files:

````
rw-r--r-- root root  nr_hugepages
r--r--r-- root root  free_hugepages
r--r--r-- root root  surplus_hugepages
````

nr_hugepages is r/w by root, this is the file that allocates 1GB hugepages.  These hugepages are **per NUMA node**... so if you have 2 NUMA nodes, you'll see two sets of these files (and so forth.)  I have 4 nodes, so I see 4 such sets of files... for me to control the number of 1GB hugepages per node, I would do something like this (example.)

For this example let's say we have 2 NUMA nodes and each node has enough RAM (3GB+ RAM) for 1GB hugepages per node.  Let's say we have xmrig's example system with 20c/40t, 2 NUMA nodes and plenty of RAM.

This system: https://raw.githubusercontent.com/xmrig/xmrig/master/doc/screenshot_v5_2_0.png

We will want to allocate (at least) 3 1GB hugepages per NUMA node... this is done like so:

For the first node:

````
sudo echo "3" >> /sys/devices/system/node/node0/hugepages/*1048*/nr_hugepages
```` 

For the second node:

````
sudo echo "3" >> /sys/devices/system/node/node1/hugepages/*1048*/nr_hugepages
```` 

If you have enough RAM you can allocate 3 1GB hugepages for each and every NUMA node like so:

````
sudo echo "3" >> /sys/devices/system/node/node*/hugepages/*1048*/nr_hugepages
```` 

Oh, but you cannot write to "nr_hugepages" (even though root can write to the file with permissions being rw-r--r--) this is because we must first activate 1GB hugepages at boot time with the kernel parameter.  But once we do that, this is how you would allocate the pages per node.  However, I think xmrig will allocate the 1GB hugepages automatically once we set them up to run at boot.


To setup 1GB hugepages, you must put them in /etc/default/grub so they'll append to the kernel command line (/proc/cmdline)

To do that, just add "hugepagesz=1GB default_hugepagesz=1GB hugepages=6" to GRUB_CMDLINE_LINUX

Open it with nano...

````
sudo nano /etc/default/grub
````

Then you'll see the grub options... go to (probably the last uncommented) line, it'll look like this:

````
GRUB_CMDLINE_LINUX=""
````

Make it look like this:

````
GRUB_CMDLINE_LINUX="hugepagesz=1GB default_hugepagesz=1GB hugepages=6"
````

Then save it (Ctrl+O in nano) and then:

````
sudo update-grub
````

Then when you reboot, you will have 1GB hugepages activated on the kernel cmdline (this is, to my knowledge, the **only** way to activate 1GB hugepages; at boot time I mean, it can't be done at runtime... or maybe it can but I'm not aware of such ability.)

Once you've added these kernel parameters and rebooted, then xmrig should automatically find and use 1GB hugepages.


================================


````
GRUB_CMDLINE_LINUX="hugepagesz=1GB default_hugepagesz=1GB hugepages=6"
````

^ the last line **hugepages=X** change that number to the number of 1GB hugepages you want configured.  Don't use more than you have RAM... "hugepages=6" means 6GB of RAM (6,144 MB) for hugepages.  Make sure you have enough RAM for that, otherwise change the number.  Xmrig needs a **minimum** of 3 1GB hugepages for this to even work.  You'll need at least 4GB of RAM on your system and even that would be a tight squeeze for a full Ubuntu desktop installation... so 5-6GB of RAM is a more realistic minimum amount for a single NUMA node CPU.

oh and yes, it's "hugepages**z**" with a "s" and a "z"  ... don't ask why lol


I'm making a shell script to enable this at boot... I'll probably make a PR with it if it'll help people.  I'm busy testing BIOS settings at the moment though.

## xmrig | 2019-12-13T18:10:45+00:00
@setuidroot Actually write to `/sys/devices/system/node/node0/hugepages/hugepages-1048576kB/nr_hugepages` and same for 2MB pages work fine without modifying boot kernel parameters, it may fail if system has not enough memory, reserve pages on boot is better, but unnecessary. At least on all tested systems it was work fine.

@exty357 you can't use 1GB pages in VM, theoretically it possible with special care, reserve 1GB pages on host and special VM configuration, but out of box it not possible.
Thank you. 

## exty357 | 2019-12-13T18:16:08+00:00
@xmrig what exactly do you mean by special configuration VM?
I have access to my ESXi and vCenter and I can apply the settings I want J


## xmrig | 2019-12-13T18:19:43+00:00
For example https://stackoverflow.com/questions/44379170/hugepagesize-is-not-increasing-to-1g-in-vm (but I did't check it by self).
Thank you.

## nabeards | 2019-12-17T02:53:40+00:00
I cannot get 1GB pages working, even after following @setuidroot's directions above and ensuring all of my config is correct. I am on CentOS 7 and Intel Xeon E5-2630s with 128 GB RAM.

Steps taken:
- Added these to my `GRUB_COMMAND_LINE`: `hugepagesz=1GB default_hugepagesz=1GB hugepages=6`
- Set `/sys/devices/system/node/node0/hugepages/hugepages-1048576kB/nr_hugepages` to `3`
- JSON config has:
```
    "randomx": {
        "init": -1,
        "mode": "auto",
        "1gb-pages": true,
        "wrmsr": true,
        "numa": true
    },
```
- Rebooted between all of these
- Also tried setting the command line switch directly, `--randomx-1gb-pages`

Edit to add:
`/proc/meminfo` reveals
```
HugePages_Total:       6
HugePages_Free:        0
HugePages_Rsvd:        0
HugePages_Surp:        0
Hugepagesize:    1048576 kB
```


## SChernykh | 2019-12-17T09:53:50+00:00
Remove this from GRUB: `default_hugepagesz=1GB`
You don't want to allocate 1GB huge page for every mining thread.

## nabeards | 2019-12-17T23:21:46+00:00
@SChernykh thanks for the suggestion, but no change.

## nabeards | 2019-12-27T22:13:17+00:00
Following up on this, I dug into the source code to try to find out more about how XMRig is checking for the availability of 1GB pages. What I found is that in my (latest) version of CentOS 7.7, including the header `<sys/mman.h>` and testing for `MAP_HUGE_SHIFT` (as the code in VirtualMemory_unix.cpp does [here](https://github.com/xmrig/xmrig/blob/06e105821aa97b5d425066b41ff57f34d160560b/src/crypto/common/VirtualMemory_unix.cpp#L43)) fails.

If I instead include `<asm/mman.h>`, `MAP_HUGE_SHIFT` is present now. Is there a way to use the `asm` header file to get the build process to see that I do, in fact, have 1GB pages available? Or perhaps a settings I can send to `make` to force it?

Here's my c test file:
```
#include <cstdlib>
#include <stdio.h>
/*#include <sys/mman.h>     /* prints 'no' */
#include <asm/mman.h>     /* prints 'yes' */

int main() {
#   ifdef MAP_HUGE_SHIFT
        printf("yes\n");
#   else
        printf("no\n");
#   endif
    return 0;
}
```

## nabeards | 2019-12-29T22:38:48+00:00
Please let me know if there's any other info I can provide to help troubleshoot!

## nabeards | 2020-01-12T16:52:49+00:00
Thought I'd try one more bump here to see if anyone has any suggestions. Thanks @xmrig @setuidroot !

## telans | 2020-08-18T08:58:27+00:00
> Thought I'd try one more bump here to see if anyone has any suggestions. Thanks @xmrig @setuidroot !

You might want to check if `CONFIG_TRANSPARENT_HUGEPAGE_ALWAYS` is set in your kernel config, it may help

`zcat /proc/config.gz | grep CONFIG_TRANSPARENT_HUGEPAGE`

## nabeards | 2020-08-18T17:44:22+00:00
Thanks @telans! On CentOS, the command is:
```
cat /boot/config-$(uname -r) | grep CONFIG_TRANSPARENT_HUGEPAGE
```
which returned
```
CONFIG_TRANSPARENT_HUGEPAGE=y
CONFIG_TRANSPARENT_HUGEPAGE_ALWAYS=y
# CONFIG_TRANSPARENT_HUGEPAGE_MADVISE is not set
```
so it looks like it is enabled.

## mckaygerhard | 2021-06-05T18:43:28+00:00
ok in alpien the grub parameters must be parsed and the kernel must have enables the settings, by example the virt kernel does not have it! i dont know why!

# Action History
- Created by: exty357 | 2019-12-13T08:37:13+00:00
- Closed at: 2021-04-12T15:10:07+00:00
