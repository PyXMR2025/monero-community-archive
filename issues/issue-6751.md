---
title: 'Fresh monerod in macOS update silent fail: what''s mean "bus error" ?'
source_url: https://github.com/monero-project/monero/issues/6751
author: hrodrig
assignees: []
labels: []
created_at: '2020-08-07T15:59:24+00:00'
updated_at: '2022-02-19T04:21:18+00:00'
type: issue
status: closed
closed_at: '2022-02-19T04:21:18+00:00'
---

# Original Description
A fresh monero download, start a complete lmdb download, wait for 2 days and when near than 1 millon of rows left, all update attempt never finished..

I try by cli:

MacOS % ./monerod --data-dir /Volumes/Monero/Daemon --check-updates disabled --max-concurrency 2 --log-level ERROR
zsh: bus error  ./monerod --data-dir /Volumes/Monero/Daemon --check-updates disabled


# Discussion History
## selsta | 2020-08-07T16:30:03+00:00
What is /Volumes/Monero/Daemon ?

## fluffypony | 2020-08-07T17:33:29+00:00
@selsta /Volumes/ is where mount-points go, so /Volumes/Monero is either a mounted disk image, or a mounted physical partition, called Monero.

@hrodrig what version of macOS?

## selsta | 2020-08-07T17:34:22+00:00
@fluffypony I am aware of that, but I was curious if it is a network drive / HDD / SDD / ... :P

Network drives are known to have issues with syncing.

## fluffypony | 2020-08-07T17:40:04+00:00
lol sorry about that - I totally misread the nature of your question and answered it literally, my apologies:)

## selsta | 2020-08-07T17:40:56+00:00
Yea could have formulated my initial comment more clearly :D

## ndorf | 2020-08-07T20:16:38+00:00
1. Is /Volumes/Monero/Daemon full?

2. Is RAM and/or swap full?

## iDunk5400 | 2020-08-07T20:25:03+00:00
And is `/Volumes/Monero/Daemon` a FAT32 formatted volume, such as an USB thumb drive or external disk ?

## hrodrig | 2020-08-07T20:57:52+00:00
Hi, here my information....


1. df -h
Filesystem      Size   Used  Avail Capacity iused       ifree %iused  Mounted on
/dev/disk1s5   113Gi   10Gi   11Gi    48%  488210  1181043550    0%   /
devfs          195Ki  195Ki    0Bi   100%     675           0  100%   /dev
/dev/disk1s1   113Gi   85Gi   11Gi    89% 1750663  1179781097    0%   /System/Volumes/Data
/dev/disk1s4   113Gi  5.0Gi   11Gi    31%       5  1181531755    0%   /private/var/vm
map auto_home    0Bi    0Bi    0Bi   100%       0           0  100%   /System/Volumes/Data/home
/dev/disk3s1   1.8Ti  567Gi  1.3Ti    31% 4398877 19528698563    0%   /Volumes/MacData

2. Processes: 426 total, 4 running, 422 sleeping, 2447 threads
Load Avg: 6.12, 6.17, 5.98  CPU usage: 11.48% user, 7.65% sys, 80.86% idle  SharedLibs: 239M resident, 55M data, 15M linkedit.
MemRegions: 102187 total, 1939M resident, 72M private, 3166M shared. PhysMem: 9760M used (2266M wired), 2527M unused.
VM: 2537G vsize, 1991M framework vsize, 827637(0) swapins, 1370469(0) swapouts.
Networks: packets: 1233602/1266M in, 1139377/143M out. Disks: 1223938/26G read, 670677/14G written

3. macOS Catalina, iMac Retina 5K, 27-inch, Late 2015, procesador i5 de 3.3 GHz, 4 cores, 12 GB RAM 1600 DDR3

I deleted /Volumes/MacData/Monero/Daemon and do a new bootstrapping... I'm stil waiting... 

Thanks everybody for your time !!!


## ndorf | 2020-08-07T21:10:28+00:00
Are you running with `--data-dir /Volumes/Monero/Daemon`, or `--data-dir /Volumes/MacData/Monero/Daemon`?

Based on your `df` output, there's nothing mounted at the former, so it would go to your root filesystem, which only has 11GiB free.

## hrodrig | 2020-08-08T00:26:36+00:00
My boot sdd disk is small... for this reason I storge lmdb in second hdd disk...

(Y)

% mount
/dev/disk1s5 on / (apfs, local, read-only, journaled)
devfs on /dev (devfs, local, nobrowse)
/dev/disk1s1 on /System/Volumes/Data (apfs, local, journaled, nobrowse)
/dev/disk1s4 on /private/var/vm (apfs, local, journaled, nobrowse)
map auto_home on /System/Volumes/Data/home (autofs, automounted, nobrowse)
/dev/disk3s1 on /Volumes/MacData (apfs, local, journaled) 

## selsta | 2020-08-08T00:28:41+00:00
Did you plug out the HDD during sync?

# Action History
- Created by: hrodrig | 2020-08-07T15:59:24+00:00
- Closed at: 2022-02-19T04:21:18+00:00
