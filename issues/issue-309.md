---
title: 'Working Linux Portable binary! '
source_url: https://github.com/xmrig/xmrig/issues/309
author: davidtavarez
assignees: []
labels:
- META
- review later
created_at: '2018-01-01T18:28:34+00:00'
updated_at: '2019-08-02T13:15:06+00:00'
type: issue
status: closed
closed_at: '2019-08-02T13:15:06+00:00'
---

# Original Description
Hi! I just create a linux portable binary using Open Build Service to generate AppImages. You can download it here: [https://download.opensuse.org/repositories/home:/davidtavarez:/branches:/OBS:/AppImage:/Templates/AppImage/](https://download.opensuse.org/repositories/home:/davidtavarez:/branches:/OBS:/AppImage:/Templates/AppImage/) download the file `xmrig-latest-x86_64.AppImage`.

This is how you can run it.

![xmrigrunning](https://user-images.githubusercontent.com/337107/34470052-f398506e-eeff-11e7-9e5a-d710810d72a5.png)

You can see the commits https://github.com/davidtavarez/xmrig/commits/master (I guess I did wrong committing on master). Should I open a Pull Request?

# Discussion History
## davidtavarez | 2018-01-03T03:14:40+00:00
I will place the apps here https://github.com/davidtavarez/portable-monero-miners

## adem4ik | 2018-01-03T05:43:18+00:00
btw it seems like "HUGE PAGES" is disabled on your Linux, you can enable it as described in xmr-stack-cpu config.txt (https://github.com/fireice-uk/xmr-stak-cpu/blob/master/config.txt):
`On Linux you will need to configure large page support "sudo sysctl -w vm.nr_hugepages=128" and increase your ulimit -l. To do do this you need to add following lines to /etc/security/limits.conf - "* soft memlock 262144"  and "* hard memlock 262144". You can also do it Windows-style and simply run-as-root, but this is NOT recommended for security reasons.`

## kronoscrasher | 2018-01-03T10:22:41+00:00
It's not portable, it still needs GLIBC...

## davidtavarez | 2018-01-03T12:53:21+00:00
@kronoscrasher yep, that's true... it's not recommended to static linking of glibc but I will try to make some test, stay tuned!

## probonopd | 2018-01-06T14:11:01+00:00
> It's not portable, it still needs GLIBC...

Most AppImages assume certain basic libraries (such as glibc) to be present on each target system. As long as the AppImage was compiled on a system no newer than all target systems, this should not be an issue though.

## sthitajena | 2018-02-03T07:56:47+00:00
@knorhaan Dude, i don't know how but working fine. Thanks a ton, i was searching like anything for this. Can you publish source code or binary ? 

## z3dm4n | 2018-02-12T10:50:27+00:00
@knorhaan Could you please provide your build instructions i.e. cmake command line?

## z3dm4n | 2018-02-12T11:22:11+00:00
You can also turn libmicrohttpd off by running cmake with `-DWITH_HTTPD=OFF`.

## xxoxx | 2018-02-27T09:01:31+00:00
@knorhaan  Your file include this
us-backup.supportxmr.com
444bLxV4jojdhJMJHNadHjVsn5pM5EWo499zLZ2tUqcoExFBmDRBmQHTDKdtb82uw

## xxoxx | 2018-02-28T03:38:39+00:00
@knorhaan Thanks.

## AkKrock | 2018-03-16T05:33:24+00:00
Hi, thanks for work.
Great job btw. If you improve  more, it will be age-changing (like mobile mining).

I suggest to make following additions:
- allow HugePages like previously mentioned.
- Add some controls addition to resume, pause and hashrate, like: results, cpu details etc.
- It'd be great to have control on CPU threads but i think it will be asking too much from a mobile miner.

Best luck!

## sergzhukov | 2018-04-16T10:37:43+00:00
Hei, is there anybody going to place new monero7 algo miner binary here? :)
Having trouble with compiling  xmr-stak and other new miners on CentOS7 with cmake, is there a binary for some monero7 cpu miner?

## brandsalazar | 2018-05-30T01:53:37+00:00
@sergzhukov I've made a standalone binary for the new algo, you can get it at https://github.com/brandsalazar/xmrig 
It is made with the compile instructions from https://github.com/xmrig/xmrig/issues/238


## danielhuang | 2018-11-20T02:37:24+00:00
@davidtavarez There are many reports of Minergate being a scam. I would encourage you to switch to a more reputable pool.

Source: https://www.reddit.com/r/Monero/wiki/avoid

## hashyg0d | 2019-06-16T01:35:38+00:00
Can this run on Big Endian arch?

# Action History
- Created by: davidtavarez | 2018-01-01T18:28:34+00:00
- Closed at: 2019-08-02T13:15:06+00:00
