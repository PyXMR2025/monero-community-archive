---
title: static build in alpine linux x86
source_url: https://github.com/xmrig/xmrig/issues/1695
author: h4cnull
assignees: []
labels: []
created_at: '2020-05-28T00:25:58+00:00'
updated_at: '2020-08-28T16:23:11+00:00'
type: issue
status: closed
closed_at: '2020-08-28T16:23:11+00:00'
---

# Original Description
i build a static xmrig, no error, in alpine linux x86 VMworkStation15. when run , get a unkonwn error.


 * ABOUT        XMRig/5.11.2 gcc/9.2.0
 * LIBS         libuv/1.38.0 OpenSSL/1.1.1g hwloc/2.2.0
 * HUGE PAGES   disabled
 * 1GB PAGES    disabled
 * CPU          Intel(R) Core(TM) i5-7300HQ CPU @ 2.50GHz (1) -x64 AES
                L2:0.5 MB L3:6.0 MB 2C/2T NUMA:1
 * MEMORY       0.1/1.9 GB (4%)
 * DONATE       1%
 * POOL #1      mine.c3pool.com:13333 algo auto
 * COMMANDS     hashrate, pause, resume
 * OPENCL       disabled
 * CUDA         disabled
[2020-05-28 08:21:29.010]  net  use pool mine.c3pool.com:13333  35.163.175.186
[2020-05-28 08:21:29.010]  net  new job from mine.c3pool.com:13333 diff 25000 algo rx/0 height 2107859
[2020-05-28 08:21:29.010]  cpu  use argon2 implementation default
[2020-05-28 08:21:29.010]  rx   init dataset algo rx/0 (2 threads) seed 680de3c231ba6bb3...
[2020-05-28 08:21:29.010]  rx   not enough memory for RandomX dataset
[2020-05-28 08:21:29.021]  rx   failed to allocate RandomX dataset, switching to slow mode (11 ms)
[2020-05-28 08:21:30.551]  rx   dataset ready (1530 ms)
[2020-05-28 08:21:30.551]  cpu  use profile  rx  (2 threads) scratchpad 2048 KB
Segmentation fault

# Discussion History
## downystreet | 2020-06-01T12:40:05+00:00
This could be some kind of kernel conflict or also a conflict between the VM and the hardware. If it's switching to slow mode that probably means the program is not getting full access to the hardware. I've run xmrig on some very old machines that hash at around 0.5h/s and it switches to slow mode automatically because the CPU doesn't have the goods to run algorithms normally. As far as the segmentation fault, I have run xmrig on some older computers using older Linux operating systems and experienced segmentation fault. I'm not a developer of this software I'm just telling you what I've seen from my experience. Alpine linux is probably not ideal for running xmrig because it doesn't get tested as much if at all and some versions of alpine linux have a hardened kernel which I assume would also cause conflicts. Also it might depend on what version your kernel is. Your hardware looks fine and is newer than mine. If you want to try a different OS I can suggest several that I know work such as Fedora, Debian, Ubuntu, Linux Mint and CentOS.

# Action History
- Created by: h4cnull | 2020-05-28T00:25:58+00:00
- Closed at: 2020-08-28T16:23:11+00:00
