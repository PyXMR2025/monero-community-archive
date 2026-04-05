---
title: Bus error doing anything on armv7
source_url: https://github.com/xmrig/xmrig/issues/2895
author: benthetechguy
assignees: []
labels:
- bug
- arm
created_at: '2022-01-25T05:31:59+00:00'
updated_at: '2022-06-27T19:14:07+00:00'
type: issue
status: closed
closed_at: '2022-06-27T19:14:06+00:00'
---

# Original Description
**Describe the bug**
When attempting to mine on armv7l devices, there is a bus error shortly after initialization and the program quits.
I have tested this on a Raspberry Pi 2, Android 10 device with Termux, and multiple VMs, using multiple distros.

**To Reproduce**
1. Compile xmrig on an armv7l device
2. Attempt to mine (I've used `--bench` and `--stress` in my testing)
3. See bus error and program quitting

**Expected behavior**
The program should mine like it does on any other architecture.

**Required data**
After the line `use profile  rx  (2 threads) scratchpad 2048 KB`, The message `Bus error` appears and the program exits.
The following shows up in dmesg right before the bus error:
```
[ 1639.859563] Alignment trap: not handling instruction f9430a2f at [<005fa0a2>]
[ 1639.860023] Alignment trap: not handling instruction f9430a2f at [<005fa0a2>]
[ 1639.860321] 8<--- cut here ---
[ 1639.860338] Unhandled fault: alignment exception (0xa21) at 0xb5000618
[ 1639.860375] pgd = 248d079d
[ 1639.860547] [b5000618] *pgd=45a37003, *pmd=13f815003
[ 1639.861673] 8<--- cut here ---
[ 1639.861892] Unhandled fault: alignment exception (0xa21) at 0xb5100618
[ 1639.862646] pgd = 248d079d
[ 1639.862712] [b5100618] *pgd=45a37003, *pmd=13f815003
```

**Additional context**
This problem was previously broght up in https://github.com/xmrig/xmrig/issues/2876#issuecomment-1016931810, but the issue was closed early and a request for it to be reopened was unanswered after a few days, so I have opened this new issue.

# Discussion History
## Spudz76 | 2022-01-25T10:06:57+00:00
Yes sorry I have not had a chance to fire up a test VM yet and investigate this, and I guess nobody else has either.  Should have a chance soon.

## SChernykh | 2022-01-25T10:45:34+00:00
I'm looking into it. Something somewhere makes unaligned memory access which is not allowed in armv7l. That said, RandomX requires 2 GB memory to run at full speed and your RPi probably doesn't have that. Also, there's no JIT compiler for 32 bit so it will be very slow, less than 1 h/s.

## SChernykh | 2022-01-25T11:20:34+00:00
It seems to be working for me:
![Untitled](https://user-images.githubusercontent.com/15806605/150967731-3b68a584-47c0-4880-8d5c-85d3a8cc8461.png)


## benthetechguy | 2022-01-25T18:40:44+00:00
This was 6.16.2 that I was compiling, maybe something changed between now
and then? If so, we'll need to figure out what that change was so I can
apply a patch for my Debian package.
I'll compile master on my armv7l devices instead of 6.16.2 and see if that
works.


## Spudz76 | 2022-01-25T20:04:23+00:00
There is a 6.16.3 release tag now so you could just bump your sourcefiles rather than patch on top of 6.16.2?

## benthetechguy | 2022-01-25T21:06:38+00:00
Cool, there was a new release after I originally made the issue. I've updated my package to it.
However, this new release doesn't solve the problem. I've compiled 6.16.3 and master, and they both still give me the bus error on a VM and Raspberry Pi.
@SChernykh, which version of Raspberry Pi is it and what distro are you running? 3 and up are aarch64 CPUs, and Raspbian's version of armhf has some tweaks that makes it a bit different than other distros. I'm using a Raspberry Pi 2 and Debian sid, though I have also tried Arch Linux ARM and Ubuntu.

## Spudz76 | 2022-01-25T21:17:09+00:00
If you are not using `--randomx-mode=light` then it is probably being killed for not enough free memory for the 2080MB dataset.

## benthetechguy | 2022-01-25T21:23:28+00:00
This would make sense on the Raspberry Pi, but my VM has 4 GBs of memory allocated.

## SChernykh | 2022-01-25T21:26:17+00:00
@benthetechguy this was a qemu virtual machine https://github.com/paulden/raspbian-on-qemu-armv7
Maybe the emulation doesn't emulate everything and it doesn't crash there.

## benthetechguy | 2022-01-25T21:31:50+00:00
My VM is also QEMU, but instead of emulating a Raspberry Pi, I used machine type `virt` which is just a generic armv7l CPU.

## benthetechguy | 2022-01-25T22:07:40+00:00
I have received an email from the Debian side of things:
> FWIW you can use UBSan to track down these unaligned accesses even on a platform that allows unaligned access. E.g. on an x86-64 machine:
> ```
> $ cat main.c
> int main(void) {
>   int x[2] = {0};
>   int *y = (int*)((char*)x + 1);
>   return *y;
> }
> $ gcc -std=c99 -fsanitize=undefined main.c
> $ ./a.out
> main.c:4:10: runtime error: load of misaligned address 0x7ff7bb54d591 for type 'int', which requires 4 byte alignment
> 0x7ff7bb54d591: note: pointer points here
>  00 00 00  00 00 00 00 00 00 00 00  2b 00 6f 49 b0 51 99 f7  b0 d6 54 bb f7 7f 00 00  fe 04 58 0d 01
>                ^
> SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior main.c:4:10 in
> ```
> This only works if the compiled code for armhf and x86-64 are sufficiently similar, but HTH.

I don't know enough about how this stuff works to take advantage of that information, but it may be able to help someone else here.

## SChernykh | 2022-01-25T22:50:20+00:00
Yes, `-fsanitize=alignment` shows a lot of misaligned accesses in various places in code. I'll see if they're easy to fix.

## SChernykh | 2022-01-26T16:21:02+00:00
https://github.com/xmrig/xmrig/pull/2904 might help with bus error.

## benthetechguy | 2022-01-27T00:28:45+00:00
Unfortunately, still happening. Is anyone else able to reproduce this, or am I just crazy? I've used multiple distros, two VMs, and real hardware.

## Botspot | 2022-03-13T21:35:23+00:00
> Unfortunately, still happening. Is anyone else able to reproduce this, or am I just crazy? I've used multiple distros, two VMs, and real hardware.

I can reproduce it, and I'm using a Pi4 on Raspberry Pi OS 32-bit. Any suggestions are welcome, as I'm trying to add Xmrig to the [Pi-Apps](https://github.com/Botspot/pi-apps) store.

## Botspot | 2022-03-14T01:44:37+00:00
After a lot of diagnosis, I found that out of all supported xmrig algorithms, ONLY ghostrider worked.
ALL other algorithms failed to run with Bus error. So, for the time being, I'm using the ghostrider algorithm.

## benthetechguy | 2022-03-14T02:08:42+00:00
Interesting… now we just need to figure out what's different about ghostrider.


## Botspot | 2022-03-14T02:24:43+00:00
> Interesting… now we just need to figure out what's different about ghostrider.

Most of the other algorithms seem to be using RandomX. Right before the Bus error, xmrig says "`failed to allocate RandomX dataset, switching to slow mode`".
For all of these RandomX algorithms, they use a lot of RAM on my Pi and I am limited to using two cores due to cache constraints.
With ghostrider however, xmrig barely consumed any RAM at all and I was able to run it on all 4 cores to double the hashing speed.

TL;DR It appears that all algorithms that fail with Bus error, also have RandomX in common. Is ghostrider really the only one that doesn't use RandomX?

## benthetechguy | 2022-03-14T02:36:24+00:00
Seems like it's probably unaligned memory access somewhere in the randomx code.
We attempted to get rid of those in #2904, but it's possible we didn't catch all of them.


## Botspot | 2022-03-14T02:43:06+00:00
> Seems like it's probably unaligned memory access somewhere in the randomx code. We attempted to get rid of those in #2904, but it's possible we didn't catch all of them.

Is there anything I can do to help? Alternatively, are you aware of a "known good" version of xmrig that I can use in the meantime?

## Botspot | 2022-03-17T23:59:55+00:00
Any ideas, @xmrig?

## Botspot | 2022-03-21T14:10:00+00:00
When can this be worked on, @SChernykh @xmrig?

## PaxJaromeMalues | 2022-03-21T22:37:34+00:00
 Was able to reproduce this back in Feb.
 Haven't found any solution sofar.

## Botspot | 2022-03-23T16:30:48+00:00
@SChernykh, could you take a look at this?

## Botspot | 2022-04-07T22:36:26+00:00
This is ridiculous. I've pinged several people and nobody has regarded this issue in the slightest.

I'd be happy to donate some XMR to whomever fixes this bug, but right now I can't even *make* any XMR because the miner is completely broken. I have access to a lot of armhf devices, and until this is fixed they are just sitting around useless.

I thought the Monero community was better than this. Pinging everyone one last time...
@xmrig @SChernykh @Spudz76

## SChernykh | 2022-04-08T05:22:19+00:00
You do realize that even if they work, they can mine 1 cent a year, right? I've fixed all bus errors I could find in qemu, but spending more time on this and/or buying armv7 device is just not worth it. Use armv8 64-bit devices, they're fully supported.

## Botspot | 2022-04-08T13:50:49+00:00
> You do realize that even if they work, they can mine 1 cent a year, right?

Actually, it's closer to 100 cents per year per device. And I have access to potentially hundreds of devices.

> I've fixed all bus errors I could find in qemu, but spending more time on this and/or buying armv7 device is just not worth it.

That's understandable. I'd be happy to give you remote access to my device. I've done this a few times with other developers, and it has worked well.

> Use armv8 64-bit devices, they're fully supported.

While doing that would be optimal, many of these devices must be running an armhf OS for other reasons. The processor itself is armv8, so workarounds are possible, but they involve chroots and kernel changes which consume an unreasonable amount of storage space in addition to unwanted side-effects.

@SChernykh, would you accept a PayPal donation to expedite this issue?
For setting up the remote desktop connection, is it best to email you at `sergey.v.chernykh@gmail.com`?

## Botspot | 2022-04-20T20:25:59+00:00
@SChernykh @xmrig

These devices can mine over 100 cents per year per device. And I have access to potentially hundreds of devices.

> I've fixed all bus errors I could find in qemu, but spending more time on this and/or buying armv7 device is just not worth it.

That's understandable. I'd be happy to give you remote access to my Pi. I've done this a few times with other developers, and it has worked well.

> Use armv8 64-bit devices, they're fully supported.

While doing that would be optimal, **many of these devices must be running an armhf OS** for other reasons. The processor itself is armv8, so workarounds are possible, but they involve chroots and kernel changes which consume an unreasonable amount of storage space in addition to unwanted side-effects.

Would you accept a PayPal donation to expedite this issue? (I would donate XMR, but I don't have any due to this issue)

## Milo123459 | 2022-05-12T23:20:47+00:00
Any updates on this? My raspberry pi keeps exiting with "Bus error" :(

## SChernykh | 2022-05-20T16:45:47+00:00
I've reproduced this bus error on a Raspberry Pi 3b+ running the latest 32-bit Raspberry Pi OS. So chances are high I'll fix it this weekend.

## Milo123459 | 2022-05-20T17:02:28+00:00
Fwiw, upgrading to a 64 bit os fixed it. A fix for 32 bit os' is going to be super cool.

## benthetechguy | 2022-05-20T18:29:05+00:00
This issue is specifically for armv7; you can't always "upgrade to a 64 bit OS." The fact that the majority of Raspberry Pi users are on a 32 bit OS baffles me because all Raspberry Pis except the 1, 2, and 0 are 64 bit. Thank you @SChernykh for making some good progress on the issue!

## Crilum | 2022-05-20T19:06:47+00:00
>The fact that the majority of Raspberry Pi users are on a 32 bit OS baffles me because all Raspberry Pis except the 1, 2, and 0 are 64 bit.

The 64-bit version of Raspberry Pi OS feels much slower to me, and it has bugs (freezes often for a few seconds, below the menubar sort of flashes, etc).. I suppose other 64-bit OS's might not have these problems, but I haven't really tried them.

## SChernykh | 2022-05-20T19:18:07+00:00
You can try https://github.com/xmrig/xmrig/pull/3054 - tested on `rx/0`, `astrobwt/v2` and `ghostrider` algorithms. `astrobwt/v2` makes the most sense to mine on 32-bit devices - 1970 h/s on Raspberry Pi 3b+

## Milo123459 | 2022-05-20T19:21:22+00:00
> > The fact that the majority of Raspberry Pi users are on a 32 bit OS baffles me because all Raspberry Pis except the 1, 2, and 0 are 64 bit.
> 
> The 64-bit version of Raspberry Pi OS feels much slower to me, and it has bugs (freezes often for a few seconds, below the menubar sort of flashes, etc).. I suppose other 64-bit OS's might not have these problems, but I haven't really tried them.

I've been using it for about a week now and it works amazingly. Perhaps try updating?

## GYKgamer | 2022-05-20T19:23:37+00:00
> > > The fact that the majority of Raspberry Pi users are on a 32 bit OS baffles me because all Raspberry Pis except the 1, 2, and 0 are 64 bit.
> > 
> > 
> > The 64-bit version of Raspberry Pi OS feels much slower to me, and it has bugs (freezes often for a few seconds, below the menubar sort of flashes, etc).. I suppose other 64-bit OS's might not have these problems, but I haven't really tried them.
> 
> I've been using it for about a week now and it works amazingly. Perhaps try updating?

I agree with you, @Crilum seems to be a problem on your end, also I will also try and help contribute with the problem.

## Crilum | 2022-05-20T19:24:51+00:00
> > > The fact that the majority of Raspberry Pi users are on a 32 bit OS baffles me because all Raspberry Pis except the 1, 2, and 0 are 64 bit.
> > 
> > 
> > The 64-bit version of Raspberry Pi OS feels much slower to me, and it has bugs (freezes often for a few seconds, below the menubar sort of flashes, etc).. I suppose other 64-bit OS's might not have these problems, but I haven't really tried them.
> 
> I've been using it for about a week now and it works amazingly. Perhaps try updating?

I just flashed it this week..

## benthetechguy | 2022-05-20T19:25:46+00:00
> > The fact that the majority of Raspberry Pi users are on a 32 bit OS baffles me because all Raspberry Pis except the 1, 2, and 0 are 64 bit.

> The 64-bit version of Raspberry Pi OS feels much slower to me, and it has bugs (freezes often for a few seconds, below the menubar sort of flashes, etc).. I suppose other 64-bit OS's might not have these problems, but I haven't really tried them.

The 64 bit version of Raspberry Pi OS is fresh out of beta and people still seem to have a lot of issues with it. My recommendation is to just not use Raspberry Pi OS at all. It's not better than other distros (actually being worse in many ways). The only reason it even exists is because the raspberry pi couldn't boot mainline Linux until 2018. If you use a proper aarch64 distro like Debian, Arch Linux ARM, or Fedora, you will have a much better experience.

## Crilum | 2022-05-20T19:25:50+00:00
If you get an error while building about missing hwloc stuff: 
```
sudo apt install hwloc libhwloc-dev
```

## Crilum | 2022-05-20T21:16:47+00:00
I don't know if this is a problem, but XMRig `failed to allocate RandomX dataset`:
```
 * ABOUT        XMRig/6.17.1-dev gcc/10.2.1
 * LIBS         libuv/1.40.0 OpenSSL/1.1.1n hwloc/2.4.1
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          ARM Cortex-A72 (1) 32-bit -AES
                L2:0.0 MB L3:0.0 MB 4C/4T NUMA:1
 * MEMORY       3.2/3.7 GB (86%)
 * DONATE       5%
 * POOL #1      gulf.moneroocean.stream:10032 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2022-05-20 15:12:13.517]  net      use pool gulf.moneroocean.stream:10032  54.188.223.206
[2022-05-20 15:12:13.517]  net      new job from gulf.moneroocean.stream:10032 diff 32000 algo rx/0 height 2627836 (14 tx)
[2022-05-20 15:12:13.517]  cpu      use argon2 implementation default
[2022-05-20 15:12:14.722]  randomx  init dataset algo rx/0 (4 threads) seed 6ac097ea635e9d1d...
[2022-05-20 15:12:14.723]  randomx  failed to allocate RandomX dataset, switching to slow mode (0 ms)
[2022-05-20 15:12:19.368]  randomx  dataset ready (4645 ms)
[2022-05-20 15:12:19.368]  cpu      use profile  rx  (4 threads) scratchpad 2048 KB
[2022-05-20 15:12:19.381]  cpu      READY threads 4/4 (4) huge pages 0% 0/4 memory 8192 KB (12 ms)
[2022-05-20 15:12:43.597]  net      new job from gulf.moneroocean.stream:10032 diff 32000 algo rx/0 height 2627837 (9 tx)
[2022-05-20 15:13:19.441]  miner    speed 10s/60s/15m 0.42 n/a n/a H/s max 0.84 H/s
[2022-05-20 15:14:01.912]  net      new job from gulf.moneroocean.stream:10032 diff 32000 algo rx/0 height 2627838 (17 tx)
[2022-05-20 15:14:19.521]  miner    speed 10s/60s/15m 0.84 0.64 n/a H/s max 0.84 H/s
```
What pools support `astrobwt`?

## Botspot | 2022-05-20T21:22:12+00:00
> I don't know if this is a problem, but XMRig `failed to allocate RandomX dataset`:

That's normal. The RPi3 doesn't have the necessary 2.2GB of ram necessary for the fast mode.
However, [installing ZRAM](https://forums.raspberrypi.com/viewtopic.php?t=327238) increases total RAM to 4GB, so it would be amazing if xmrig took that into consideration. 

## Botspot | 2022-05-20T21:24:27+00:00
> What pools support `astrobwt`?

MoneroOcean

## Crilum | 2022-05-20T21:35:24+00:00
> > I don't know if this is a problem, but XMRig `failed to allocate RandomX dataset`:
> 
> That's normal. The RPi3 doesn't have the necessary 2.2GB of ram necessary for the fast mode. However, [installing ZRAM](https://forums.raspberrypi.com/viewtopic.php?t=327238) increases total RAM to 4GB, so it would be amazing if xmrig took that into consideration.

I'm using a Pi 4 with 4G ram, plus the More RAM app.. But most of my memory is being used right now, so I guess I should test with more free RAM.

## Spudz76 | 2022-05-21T01:36:12+00:00
> > What pools support `astrobwt`
>
> MoneroOcean

Nope.  They haven't fixed it since the DERO-HE fork.  They did support the original `astrobwt` but not `astrobwt/v2` (yet? been months).

## benthetechguy | 2022-05-21T02:55:59+00:00
@SChernykh, thank you for the fix; it worked for me and seems to have worked for everyone else so far as well. All that for two lines of code.

## Crilum | 2022-05-21T03:01:23+00:00
Yeah, it works for me!

## SChernykh | 2022-05-21T08:01:44+00:00
> @SChernykh, thank you for the fix; it worked for me and seems to have worked for everyone else so far as well. All that for two lines of code.

Most of the other unaligned memory accesses were fixed before. These two lines are just what didn't show up in the emulator.

> What pools support astrobwt?

You have to run your own Dero node and connect to it like this:
```
./xmrig -o daemon+wss://YOUR_NODE_IP:10100 --daemon -u YOUR_DERO_WALLET_ADDRESS -a astrobwt/v2
```

## Spudz76 | 2022-05-21T13:45:18+00:00
And I'd bet the whole stupid `daemon+wss:` protocol is why it's not integrated with MoneroOcean yet.  They could have just stayed with normal daemon connections (or at least supported them in addition to dumb-new-method).

## Crilum | 2022-05-21T15:36:11+00:00
Is there a time frame the next release?

## Botspot | 2022-05-21T19:11:14+00:00
I've requested for MoneroOcean/xmrig to update their repo as well.

## Spudz76 | 2022-05-21T22:46:14+00:00
> I've requested for MoneroOcean/xmrig to update their repo as well.

Apparent policy is to rebase whenever a new `xmrig/master` is released.  They won't roll a special release just for ARM32 people, wait for the next master and then it'll happen.  A master was just rolled but the only changes were docs (probably should have included this patch).

## benthetechguy | 2022-06-27T19:14:06+00:00
This issue is fixed in the latest release, closing.

# Action History
- Created by: benthetechguy | 2022-01-25T05:31:59+00:00
- Closed at: 2022-06-27T19:14:06+00:00
