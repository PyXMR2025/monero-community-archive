---
title: New daemon slows down Ubuntu 16.04 to a halt
source_url: https://github.com/monero-project/monero/issues/2455
author: reppolice
assignees: []
labels: []
created_at: '2017-09-16T22:05:21+00:00'
updated_at: '2018-03-20T14:39:56+00:00'
type: issue
status: closed
closed_at: '2017-10-02T19:30:23+00:00'
---

# Original Description
I have tried the new daemon on both a 2011 Macbook, as wells as a Quad Core laptop with Ubuntu and 32GB RAM, and while the Mac managed a complete sync in about a day without too much strain, my Ubuntu can hardly do anything while the daemon is syncing, even though "top" never shows more than 45% of CPU. It looks like the process might still complete in a day, but quite a mystery! Putting the disk under too much strain perhaps? Something more evil?

# Discussion History
## moneromooo-monero | 2017-09-16T22:57:35+00:00
Do these have spinning HDDs or SSDs ?

## reppolice | 2017-09-17T00:47:37+00:00
HDD on the fast computer, a slow SSD on the Mac, it is impossible to justify a "hanging" computer for 24 hours just to sync the 2GB or whatever the size of Monero's blockchain

## celavek | 2017-09-17T21:31:21+00:00
I have witnessed something similar, although my system does not go to a total halt but it gets really slow. I'm on Debian 9 and I'm using netdata to collect information about my system and the disk backlog(an indication of the duration of pending disk operations) is very high and often goes to critical levels during the whole sync operation with cpu iowait also through the roof.

## hyc | 2017-09-17T21:46:43+00:00
Have you actually compared sync performance using v0.10.3.1 on the same machine?

For the record, I've noticed freezes on my linode running v0.11 too, that never occurred before running v0.10. During those times, top shows monerod eating a lot of CPU. If you can build from source, try compiling master plus #2446 and see how that behaves. It has definitely reduced the impact on my systems.

## reppolice | 2017-09-18T14:43:16+00:00
Well, it is certainly the worst performance I've seen in a daemon, speaking from weak human fallible memory :) It has to be said the blockchain has grown to 28GB while I was not watching. The whole thing feels very suboptimal, "obviously" it is ignoring my available RAM, would it be too much to ask for more RAM caching?

## hyc | 2017-09-18T14:51:03+00:00
Unfortunately, we tried that in earlier releases. Too many Windows users got corrupted blockchains from system crashing during a sync. So now we flush data to disk more frequently by default, to avoid that. You can always start monerod with an explicit --db-sync-mode setting if your system doesn't have such reliability issues.

Note that you will generally need to tweak settings in /proc/sys/vm (like writeback, expire, etc) to actually get full utilization of available RAM, and filesystems like ext3/ext4 will still flush on their own schedule, regardless of system-wide settings.

## reppolice | 2017-09-18T15:16:23+00:00
Thanks for the info, @hyc. Though I can't believe that Windows is that unreliable, we are talking about caching up to 50MB here, isn't it the more ecological approach to pass a parameter through the  Windows GUI rather that defaulting to uncached on all systems? I mean, it is maxxing out our HDDs!

## hyc | 2017-09-18T15:24:30+00:00
If you pay close attention with a system monitoring tool you'll see that far more than 50MB is already being cached by default. And again - if you know your system is reliable, you can change the settings yourself. But yes, experience over the past year has shown us that using unsafe defaults results in broken files, and the majority of users are (1) using windows and (2) using default settings.

## moneromooo-monero | 2017-09-22T09:48:04+00:00
hyc's threading code got merged, can you report whether it feels better now ?

## ghost | 2017-09-27T21:29:09+00:00
@reppolice 

## moneromooo-monero | 2017-10-02T19:27:53+00:00
No reply, and believed fixed. Reopen if it's still as bad. It is subjective, but don't reopen just becaus it'd be nice if even faster. As long as it doesn't wedge the machine too much, it should be fine.

+resolved

## Bomper | 2018-03-06T00:09:17+00:00
I don't think this is fixed. I've just download the latest GUI (monero-gui-linux-x64-v0.11.1.0.tar.bz2) and the daemon that ships with it, and on Ubuntu 16.04, CPU usage goes through the roof: towards the end of syncing the blockchain, switching tasks takes seconds, the mouse cursor skips when moving etc. This makes the wallet unusable and I can't wait for the blockchain to sync, see my transaction, transfer the XMR elsewhere, uninstall, and recover the [gobs of disk space that the wallet uses](https://github.com/monero-project/monero-gui/issues/1164).

![image](https://user-images.githubusercontent.com/34669048/37006816-1266ca14-208f-11e8-8efc-248d7624863b.png)


## lh1008 | 2018-03-20T14:39:55+00:00
My pc freezes as well when GUI is running and synchronizing. I don't know how to slow the synchronization. I have been using the monerod manually but I can't do anything else while is running in the cpu(laptop) the same as @Bomper. :) Hope this gets fixed. Are there are any instructions on how to slow down the blockchain sync? Thank you for your support.. 

# Action History
- Created by: reppolice | 2017-09-16T22:05:21+00:00
- Closed at: 2017-10-02T19:30:23+00:00
