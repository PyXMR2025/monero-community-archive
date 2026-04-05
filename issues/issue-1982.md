---
title: cannot load MSR addresses
source_url: https://github.com/xmrig/xmrig/issues/1982
author: nolash
assignees: []
labels: []
created_at: '2020-12-16T08:03:26+00:00'
updated_at: '2021-04-12T14:28:32+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:28:32+00:00'
---

# Original Description
**Describe the bug**

Error during startup:

```
Dec 16 09:00:48 amoroso xmrig[64531]: [2020-12-16 09:00:48.326]  msr      cannot read MSR 0x000001a4
Dec 16 09:00:48 amoroso xmrig[64531]: [2020-12-16 09:00:48.326]  msr      cannot set MSR 0x000001a4 to 0x0000000f
Dec 16 09:00:48 amoroso xmrig[64531]: [2020-12-16 09:00:48.326]  msr      FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW
```

**To Reproduce**

Using (arch)linux 5.9.12 xmrig 6.6.2 xmrig-cuda 6.5.0 msr-tools 1.4


# Discussion History
## SChernykh | 2020-12-16T08:41:02+00:00
1) Run as root to enable MSR mod
2) MSR mod works only on a physical hardware, not in a VM

## nolash | 2020-12-16T13:47:39+00:00
Is there another way than running as root?

I tried giving the user running the xmrig access to `/dev/cpu/*/msr` with udev, but it didn't make a difference...

## SChernykh | 2020-12-16T13:59:51+00:00
You can run https://github.com/xmrig/xmrig/blob/master/scripts/randomx_boost.sh to apply MSR mod separately.

## nolash | 2020-12-16T14:44:44+00:00
Doesn't seem to quite hit the spot :/

```
[root@amoroso tmp]# rmmod msr
[root@amoroso tmp]# bash randomx_boost.sh 
Detected Intel
MSR register values for Intel applied
[root@amoroso tmp]# systemctl restart xmrmine
[root@amoroso tmp]# journalctl -fu xmrmine
-- Journal begins at Sat 2020-08-01 21:38:13 CEST. --
Dec 16 15:43:33 amoroso xmrig[1023]:  * CUDA GPU     #0 01:00.0 GeForce GTX 1080 Ti 1683/5505 MHz smx:28 arch:61 mem:11035/11178 MB
Dec 16 15:43:33 amoroso xmrig[1023]:  * CUDA GPU     #1 04:00.0 GeForce GTX 1060 6GB 1771/4004 MHz smx:10 arch:61 mem:6009/6078 MB
Dec 16 15:43:33 amoroso xmrig[1023]: [2020-12-16 15:43:33.417]  net      use pool de.minexmr.com:7777  94.130.164.163
Dec 16 15:43:33 amoroso xmrig[1023]: [2020-12-16 15:43:33.417]  net      new job from de.minexmr.com:7777 diff 175004 algo rx/0 height 2253502
Dec 16 15:43:33 amoroso xmrig[1023]: [2020-12-16 15:43:33.417]  cpu      use argon2 implementation SSSE3
Dec 16 15:43:33 amoroso xmrig[1023]: [2020-12-16 15:43:33.432]  msr      cannot read MSR 0x000001a4
Dec 16 15:43:33 amoroso xmrig[1023]: [2020-12-16 15:43:33.432]  msr      cannot set MSR 0x000001a4 to 0x0000000f
Dec 16 15:43:33 amoroso xmrig[1023]: [2020-12-16 15:43:33.432]  msr      FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW
Dec 16 15:43:33 amoroso xmrig[1023]: [2020-12-16 15:43:33.432]  randomx  init dataset algo rx/0 (2 threads) seed 59a8474950630ca0...
Dec 16 15:43:33 amoroso xmrig[1023]: [2020-12-16 15:43:33.433]  randomx  allocated 2336 MB (2080+256) huge pages 0% 0/1168 +JIT (1 ms)
```

## SChernykh | 2020-12-16T15:02:21+00:00
> MSR register values for Intel applied

It worked.

## nolash | 2020-12-16T16:43:10+00:00
yeah but then look below at the log for xmrig run after, still "cannot read MSR ..."

## SChernykh | 2020-12-16T16:45:42+00:00
Yes, because you don't run it as root. It can't read/write MSR and complains, but they were already changed by the script before it. Everything as expected.

Edit: I see you run everything as root. Then make sure it's not a VM because MSR mod works only on a physical hardware.

## Josef3110 | 2020-12-20T09:08:42+00:00
If you run Linux 5.9 or later then you have to add 

msr.allow_writes=on

to the kernel boot parameters. Otherwise even root cannot write into MSR.

## SChernykh | 2020-12-20T09:16:20+00:00
There's a workaround for Linux 5.9 in XMRig: https://github.com/xmrig/xmrig/pull/1912
It should work with 5.9

## nolash | 2020-12-21T15:29:19+00:00
@SChernykh thanks for the heads up. Apparently it's already enabled on my system; I can confirm that it works when running as root.

What I was trying before was with udevadm to change the permissions on the `dev/...` files that are setup by udev when installing the msr module. But it seems it was not sufficient. In general running things as root is something I prefer not to do. Is there a way of giving access more surgically here?

## sadnix | 2021-03-22T12:40:42+00:00
for running xmrig from user need set capability CAP_SYS_RAWIO to open the MSR device file:
https://stackoverflow.com/questions/18661976/reading-dev-cpu-msr-from-userspace-operation-not-permitted

so reproduce steps:
```
sudo setcap cap_sys_rawio=ep ./xmrig
sudo modprobe msr
sudo wrmsr -a 0x1a4 0xf  ## for intel
## and maybe needed
sudo chown user:root /dev/cpu/*/msr
```

verified on linux 4.17
for linux > 5.8 must add kernel boot parameter msr.allow_writes=on


# Action History
- Created by: nolash | 2020-12-16T08:03:26+00:00
- Closed at: 2021-04-12T14:28:32+00:00
