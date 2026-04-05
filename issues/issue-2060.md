---
title: Apple M1 not running to full potential
source_url: https://github.com/xmrig/xmrig/issues/2060
author: coleburg
assignees: []
labels: []
created_at: '2021-01-24T15:38:56+00:00'
updated_at: '2026-03-19T06:11:38+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:21:49+00:00'
---

# Original Description
I have tried changing the flags in the config to make sure all cores are being used and also set the % of CPU all the way up 
ie
"max-cpu-usage": 100,
 "threads": 8
but the hash rate never changes and the Mac mini doesnt seem to even get warm, as though its not running 100% on all cores.

[2021-01-24 15:35:28.190]  miner    speed 10s/60s/15m 2261.7 2281.5 n/a H/s max 2350.5 H/s

Looks like im going to be mining about 3p a day haha

Is this normal?  should it be hashing higher and the box at least getting warm to show its doing something at least?

Thanks for any help.

# Discussion History
## xmrig | 2021-01-24T16:04:07+00:00
#1991 hashrate is about to right and it uses all cores out of box, global options `"max-cpu-usage"` and `"threads"` no longer exists, all CPU related options now inside `"cpu"` object.
Thank you.


## coleburg | 2021-01-24T16:57:37+00:00
oh ok, thank you for your response.  Doent look like im getting rich anytime soon.

:-)

## SChernykh | 2021-01-24T20:00:05+00:00
@coleburg It does 2350 h/s using less than 20 watts of power which is very energy efficient, better than Ryzen CPUs. No surprise it's not getting warm.

## Spudz76 | 2021-01-24T21:21:11+00:00
You're getting a lot more rich than an Intel where it burns 45+ watts for the same.  Almost twice as rich?

## AndyRPH | 2021-01-26T00:11:40+00:00
> #1991 hashrate is about to right and it uses all cores out of box, global options `"max-cpu-usage"` and `"threads"` no longer exists, all CPU related options now inside `"cpu"` object.
> 
> Thank you.
> 
> 

Is the code referenced in https://github.com/tevador/RandomX/pull/197#issuecomment-735451026  something already implemented in Xmrig's implementation of randomX or a potential pathway to squeezing more performance from the M1 systems?

## xmrig | 2021-01-26T07:45:58+00:00
@AndyRPH It is already implemented, but it is not faster, actually I didn't notice any performance difference, maybe some future macOS updates will implement promised speedup. Anyway macOS is the main bottleneck of the M1 processor.
Thank you.

## AndyRPH | 2021-01-29T02:45:05+00:00
Are you implying that booting Linux instead would make xmrig much faster?  I've been meaning to toy with that option since the corellium folks released details on getting Ubuntu running on an M1 Mac. 

> @AndyRPH It is already implemented, but it is not faster, actually I didn't notice any performance difference, maybe some future macOS updates will implement promised speedup. Anyway macOS is the main bottleneck of the M1 processor.
> 
> Thank you.



## xmrig | 2021-01-30T15:21:38+00:00
I was wrong about macOS, Linux is not faster https://xmrig.com/benchmark/6L2aUa.
Thank you.

## AndyRPH | 2021-01-30T16:12:36+00:00
Thanks for checking! Hopefully that may change as better Linux support developers for the M1 based hardware. 

## xmrig | 2021-01-30T22:39:23+00:00
https://xmrig.com/benchmark/47Dr5v better result, but still slower than macOS. This result was achieved with 32 MB huge pages (benchmark page shows wrong count of pages). Support for custom and not widely supported huge page sizes will be added to the next version on Linux.
Thank you.

## rovo79 | 2021-02-02T12:24:46+00:00
Is there a way to enable Huge Pages or Super Pages on an M1 setup?

## xmrig | 2021-02-02T22:42:33+00:00
@rovo79 If you are talking about macOS it is not supported by OS.

If Linux:
1. Use the latest dev branch or v6.8.1+ when it is released.
2. Reserve huge pages `sudo sysctl -w vm.nr_hugepages=82` usually the miner can reserve huge pages automatically if run it with sudo, but not this time, since sysfs interface for huge pages is not supported.
3. Enable 32 MB huge pages in config `"huge-pages": 32768,` in `"cpu"` object or command line `--hugepage-size 32768`


## rovo79 | 2021-02-03T03:36:03+00:00
Thank you @xmrig . Yes, referring to MacOS. I was thinking Super Pages was a Mac thing, but I misunderstood. 

Does XMrig harness the M1 beyond the 8 cores of the CPU? 

Besides the 8-core CPU, there's also an 8-core GPU, and a 16-core Neural Engine. 

Maybe those are already factored in, just curious. 


## xmrig | 2021-02-03T09:35:51+00:00
@rovo79 Only CPU cores used, use GPU for RandomX generally a bad idea and all cores share the same memory.

## rovo79 | 2021-02-03T11:54:42+00:00
@xmrig thanks for the insight. I appreciate it. 


## rovo79 | 2021-03-03T16:38:35+00:00
@xmrig Does this mean mining with XMRig is very Memory dependent, so whichever Algo is currently running will most likely run best when utilizing the max amount of available Memory? 

I'm thinking running two instances of XMRig, one Algo for CPU, and one Algo for GPU.

Interesting piece I read,
>there’s no need to carve out portions of memory for each part of the SoC and then shuttle data between the two spaces for different parts of the processor. Instead, the GPU, CPU, and other parts of the processor can access the same data at the same memory address.

src: https://www.howtogeek.com/701804/how-unified-memory-speeds-up-apples-m1-arm-macs/

## rovo79 | 2021-03-04T13:35:33+00:00
Does this mean the Apple M1 is currently only running in Light mode?

> RandomX can operate in two main modes with different memory requirements:

>Fast mode - requires 2080 MiB of shared memory.
>Light mode - requires only 256 MiB of shared memory, but runs significantly slower

## rovo79 | 2021-03-04T14:13:53+00:00
This is well beyond me, but I think there is support for Huge Pages in the form of Superpages in Mac OS. 

This example shows how it can be utilized:
https://opensource.apple.com/source/xnu/xnu-2050.7.9/tools/tests/superpages/testsp.c

By making use of:
`mach_vm_address_t`
`mach_vm_size_t`

More about those VM types here:
https://developer.apple.com/documentation/kernel/mach/mach_vm

@AndyRPH

## rovo79 | 2021-04-12T15:12:58+00:00
@xmrig 
I guess Closing the issue is the response?

## xmrig | 2021-04-12T15:15:48+00:00
Superpages supported on Intel macOS and M1 running in full memory mode.
Thank you.

## AndyRPH | 2021-04-12T16:12:59+00:00
Ah, I didn't see that in the release notes,  as earlier here on 2/2 you said that it wasn't supposed by MacOS on the M1s https://github.com/xmrig/xmrig/issues/2060#issuecomment-772063329

So it's enabled standardly in newer versions of XMRig for M1 macs?

## xmrig | 2021-04-12T16:22:17+00:00
> Intel macOS

It's still not supported on M1 on OS level, nothing can do on the miner side. Full/light mode not related to Huge/Super pages.


## UnixCro | 2022-02-21T05:05:25+00:00
<img width="1193" alt="Bildschirmfoto 2022-02-21 um 06 01 44" src="https://user-images.githubusercontent.com/70098046/154892617-5f0d9c18-594b-449e-badd-ec74a1486ffd.png">

Huge Pages have always given me 50-100% better performance. Any way to activate this no matter how?

Edit:

LOL

```
sudo sysctl -w vm.nr_hugepages=82
sysctl: unknown oid 'vm.nr_hugepages'
```

No JIT, No MSR, No Huge Pages. The M1 would have so much potential :(

## Spudz76 | 2022-02-21T05:30:57+00:00
M1 has no small pages (4KB)... only 16KB pages which it uses always.

I [have a patchset I was working on](https://github.com/Spudz76/xmrig/tree/dev-m1-superpages) that makes it more obvious what's happening.

## UnixCro | 2022-02-21T05:41:12+00:00
Does it bring more hashrates? If so, what should I type in the terminal to get your script to run?

## Spudz76 | 2022-02-21T06:24:15+00:00
No, it just says more clearly that it is using 16KB "not so super" pages.

git clone it and build it

## UnixCro | 2022-02-21T18:14:51+00:00
Then I don't need it. Thanks. I already know from you that the Apple M1 uses 16kb pages.

One request to @xmrig. They said it's due to the operating system layer that huge pages can't be used. But if it's the software. Then you can change these parts via root so that you can get it to work.

Or what about that slow JIT compiler you mentioned. And why can't you use a faster one? https://developer.apple.com/documentation/apple-silicon/porting-just-in-time-compilers-to-apple-silicon

Just like with MSR. There are definitely ways to disable hardware prefetchers without at least activating cache QoS.

I think you have the knowledge for this & I would appreciate if you make the Apple M1 more customizable as I am very sure there is still room for improvement. And I'm not one to turn off the donation level, I support you and your team.

## Spudz76 | 2022-02-22T03:01:15+00:00
Half assed attempts at unlocking the extended permissions are in that patch branch.  I am nowhere near an Apple developer but apparently you have to make a "plist" file and then sign the application with the permissions and junk, but I have no idea how to do that.  I found a few items for unlocking SecureJIT at least, maybe.

2MB superpages do allegedly exist in the chip, but are only available to the kernel.  Userspace can't use them no matter who they are, root or otherwise, not yet any plist item to unlock it.

Linux is available for M1 and probably will support all page sizes before MacOS does, lol.

## UnixCro | 2022-02-22T05:41:44+00:00
Wait you got Secure JIT working? Then it would have to increase the hash rate, right?

Most likely I'll reboot my M1 to Linux when I'm not using it to get more hashes. But it's only an emergency solution.

## Spudz76 | 2022-02-22T13:10:44+00:00
No not at all, but I was beginning to follow breadcrumbs about how to sign the permission into an app to unlock cool stuff, non of which worked or made any sense yet (other than I made a rough-guess plist file).

If Apple decides to allow superpages outside of the kernel space it will likely be a signed permission item.

## UnixCro | 2022-02-23T12:25:28+00:00
Stupid question, but would it be possible if xmrig from the M1 uses the neural engine?

## SChernykh | 2022-02-23T12:30:03+00:00
Neural engine is an ASIC for machine learning/AI. So the answer is no unless someone create a mining algorithm for it.

## UnixCro | 2022-03-17T15:07:26+00:00
This is not an error or anything like that. But a recommendation to anyone with the Apple silicon processors over XMRig mint.

Dear Apple Silicion users, I strongly recommend that you check whether "Low Power Mode" is activated or deactivated in the system settings.

```
Activated: approx. 1528 H/s 8.5 watts CPU 45 degrees 0 rpm fan
Deactivated: approx. 2330 H/s 18 watts CPU 92 degrees 3000 rpm fan
```

It's not worth mining with the power saving mode turned off at all. You damage your hardware and draw more power than you get hashes.

I think it's because Apple is reducing the voltage on the cores.
<img width="875" alt="Bildschirmfoto 2022-03-17 um 15 56 29" src="https://user-images.githubusercontent.com/70098046/158832258-100e39eb-e64b-40be-bf8a-dbc71bb00581.png">


Turn it on


## henrikhelmers | 2022-04-12T08:14:19+00:00
> Dear Apple Silicion users, I strongly recommend that you check whether "Low Power Mode" is activated or deactivated in the system settings. [...] It's not worth mining with the power saving mode turned off at all. You damage your hardware and draw more power than you get hashes.

Apple M1 chips are built with performance (Firestorm) and efficiency (Icestorm) cores. Various configurations exist, the "regular" M1, as well as the Ultra, contains 4 Icestorm cores, the others 2.

You can't damage the cores by utilizing them. You could probably run them at 100% 24/7 for years without issue. At worst they will throttle and carry on. I don't understand the numbers though, any fan should be able to dissipate 18W.

If you're not satisfied with the possibilities in the config file, I can recommend an app called "App Tamer", which allows you to force background processes onto efficiency cores. It also allows you to throttle them. I use it to extend battery life, but it would likely work with xmrig as well, without having to force power-saving mode for the rest of the system.

## UnixCro | 2022-04-17T08:33:33+00:00
>You can't damage the cores by utilizing them. You could probably run them at 100% 24/7 for years without issue. At worst they will throttle and carry on. I don't understand the numbers though, any fan should be able to dissipate 18W.

They can damage any processor once it has too much heat. In physics, one calculates 1.16194 Celcius per watt + ambient temperature. Even if 18 watts result in approx. 21 degrees without ambient temperature according to the calculation. Don't forget that due to the design of a notebook, all components are very close together, so inherently there is poor cooling performance.

As soon as a processor also heats up, the temperature of the environment increases, which in turn, according to the formula, increases the processor temperature, which in turn allows the environment to continue to rise and so on.

And if you've had any experience with Macs yourself, then you know that Apple runs the fans very late and never delivers full cooling performance, since Apple believes it's better to slow down the processor than annoy the user.

<br>

>At worst they will throttle and carry on.

No processor can downclock itself so far that there is a significant temperature difference.


Take a look at the MacBook Air. Apple doesn't install any fans there at all. Apple doesn't even think that some people are mining with it, so they don't implement that either.

Think before you write anything...

<br>

>If you're not satisfied with the possibilities in the config file, I can recommend an app called "App Tamer", which allows you to force background processes onto efficiency cores. It also allows you to throttle them. I use it to extend battery life, but it would likely work with xmrig as well, without having to force power-saving mode for the rest of the system.

`--cpu-max-threads-hint=N maximum CPU threads count (in percentage) hint for autoconfig`

<br>

@xmrig If I were you I would reopen the problem again as we have not come to a solution...

## henrikhelmers | 2022-04-17T09:59:19+00:00
> Take a look at the MacBook Air. Apple doesn't install any fans there at all. Apple doesn't even think that some people are mining with it, so they don't implement that either.

I have been using MacBook Airs for computationally intensive tasks, previously an Intel 11" i7 and now the M1. Even without a fan, the M1 runs noticeably cooler. Then again the fan in the 11" sounded more like an angry wasp than a proper cooling system 😄. 

> No processor can downclock itself so far that there is a significant temperature difference.

One way to deal with this could be to move workloads from Firestorm to Icestorm cores, which use [10% of the energy](https://eclecticlight.co/2021/09/01/m1-icestorm-cores-can-still-perform-very-well/). This is why I suggested AppTamer above. I am no expert in xmrig (so apologies if I'm holding it wrong), but was unable to move it to the Icestorm cores with the config. Xmrig would use the same cores with both

>         "rx": [
>             [0, 0],
>             [1, 1],
>             [2, 2],
>             [3, 3]
>         ],

and

>         "rx": [
>             [0, 4],
>             [1, 5],
>             [2, 6],
>             [3, 7]
>         ],



## UnixCro | 2026-03-18T14:13:27+00:00
Why doesn't xmrig offer the option to mine only E-cores?

## xmrig | 2026-03-19T06:11:38+00:00
It might sound unbelievable, but macOS (as an operating system) doesn't support setting thread affinity. Nothing really useful can be done on an application level.

Thank you.

# Action History
- Created by: coleburg | 2021-01-24T15:38:56+00:00
- Closed at: 2021-04-12T14:21:49+00:00
