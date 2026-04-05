---
title: '"msr kernel module is not available"'
source_url: https://github.com/xmrig/xmrig/issues/2165
author: appletechgeek
assignees: []
labels: []
created_at: '2021-03-08T14:42:13+00:00'
updated_at: '2021-04-12T14:00:33+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:00:33+00:00'
---

# Original Description
hello good day.

for some reason even when running xmrig in sudo. i stil get the msr fnot working error.

![photo5922416544774731559](https://user-images.githubusercontent.com/24513137/110336123-d83d3500-8024-11eb-9bbd-f6976449c246.jpg)


# Discussion History
## SChernykh | 2021-03-08T22:53:26+00:00
You're running it inside a VM. MSR mod doesn't work there because there is no access to a physical CPU.

## jabronimus | 2021-03-09T21:23:37+00:00
> You're running it inside a VM. MSR mod doesn't work there because there is no access to a physical CPU.

This is incorrect. I am getting the same issue, and I am 100% not running it on a virtual machine - I am running it on a physical machine with Ubuntu 18.0. I did not have this issue in previous versions of xmrig.  This only started with this most recent version.

Things I have tried, based on all the internet searches I've done and people having this problem in the past, include:

1. Running the program with sudo
2. Running the program as root
3. Installing msr-tools
4. Applying "randomx_boost.sh"
5. Rebooting and trying all of the above again

What I'm noticing is that only *some* of the algorithms have this MSR mod issue, while some don't.

For example, my benchmark for algorithm panthera has a hashrate of 406.3 H/s.

My benchmark for algo cn-heavy/xhv has a hashrate of 24.8 H/s, and shows "cannot read MSR 0x000001a4 / FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW" during benchmarking.

My benchmark for algo  rx/0 also shows the "cannot read MSR ... " error as above, but the hashrate is higher at 141.9 H/s.

I also notice that at the top of the output when I run xmrig, I get this line: "hwloc auto configuration for algorithm "cn-heavy/0" failed."  I'm assuming this is related.

<img width="912" alt="1" src="https://user-images.githubusercontent.com/27851570/110539862-c2e30c00-80f3-11eb-8598-48c505aa75c9.png">

<img width="916" alt="2" src="https://user-images.githubusercontent.com/27851570/110539874-c70f2980-80f3-11eb-9409-e1321542761b.png">

<img width="923" alt="3" src="https://user-images.githubusercontent.com/27851570/110539879-cb3b4700-80f3-11eb-9d23-302959e41871.png">

For now, I plan on deactivating the cn-heavy algorithm and possibly the rx/0 algorithm in the config file so xmrig doesn't try to use them.


## SChernykh | 2021-03-09T21:27:06+00:00
@jabronimus We're not responsible for possible bugs in MoneroOcean's version. If you have issues with stock XMRig, create a new issue.

## jabronimus | 2021-03-09T21:32:50+00:00
> @jabronimus We're not responsible for possible bugs in MoneroOcean's version. If you have issues with stock XMRig, create a new issue.

That's fair - I could try building the official version and see if I get the same bug.  Let me try it and see what happens!

## jabronimus | 2021-03-09T22:18:12+00:00
> @jabronimus We're not responsible for possible bugs in MoneroOcean's version. If you have issues with stock XMRig, create a new issue.

@SChernykh  Ok. I tried building the official version of xmrig - *not* the MoneroOcean version - using *both* the "Basic" build instructions and the "Advanced" build instructions. (I even took out the MoneroOcean pools that I was using, just because.)

Am getting the same error in terms of "cannot read MSR 0x000001a4 / FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW".

I'm happy to make this as a new issue if you'd like.  (This is my first post on github, so I'm not sure what the proper protocol is.)

Here you go - as I said, happy to make this a new issue.

Basic build:

![Basic](https://user-images.githubusercontent.com/27851570/110545526-3d635a00-80fb-11eb-8877-bd05609661be.png)

Advanced build:

![Advanced](https://user-images.githubusercontent.com/27851570/110545636-64ba2700-80fb-11eb-874b-521f77d4eb63.png)


## SChernykh | 2021-03-09T22:23:56+00:00
Can you try older versions and find the first one where MSR doesn't work? You can just download compiled binaries for a quick test.

## jabronimus | 2021-03-09T22:24:54+00:00
> Can you try older versions and find the first one where MSR doesn't work? You can just download compiled binaries for a quick test.

@SChernykh - Yes! Would be happy to. Let's see what happens.

## Spudz76 | 2021-03-11T16:30:59+00:00
@jabronimus:
Panthera msr-apply is broken and I can't find the bug yet, it doesn't trigger the msr-apply step even though it's in the right family, which should be plenty to trigger it.

Other than that RandomX family and CN-Heavy are the only ones that get help from cache lookahead msr and thus are the only ones it attempts to apply (as you noticed).  Normal for no attempt at msr write on all other algos.

Also those hashrates all look pretty good anyway.  The "LOW HASHRATE" warning is not exactly telling the truth, come CPUs don't have a gain with prefetches turned off, some especially Atom or Celeron don't even have the cache option MSR (but xmrig will still try it).

[Pentium N3710](https://ark.intel.com/content/www/us/en/ark/products/91830/intel-pentium-processor-n3710-2m-cache-up-to-2-56-ghz.html) wow 6W TDP is amazing.  You're a bit short on cache size.  Very likely has no cache-control MSRs.

----

@appletechgeek (OP) Could try blocking all kvm modules to avoid putting host cpu into VM mode.  Have seen a few cases where having some virtualization server or client installed will flip the main cpu to VM mode for no real reason.

## jabronimus | 2021-03-11T18:56:05+00:00
> @jabronimus:
> Panthera msr-apply is broken and I can't find the bug yet, it doesn't trigger the msr-apply step even though it's in the right family, which should be plenty to trigger it.
> 
> Other than that RandomX family and CN-Heavy are the only ones that get help from cache lookahead msr and thus are the only ones it attempts to apply (as you noticed). Normal for no attempt at msr write on all other algos.
> 
> Also those hashrates all look pretty good anyway. The "LOW HASHRATE" warning is not exactly telling the truth, come CPUs don't have a gain with prefetches turned off, some especially Atom or Celeron don't even have the cache option MSR (but xmrig will still try it).
> 
> [Pentium N3710](https://ark.intel.com/content/www/us/en/ark/products/91830/intel-pentium-processor-n3710-2m-cache-up-to-2-56-ghz.html) wow 6W TDP is amazing. You're a bit short on cache size. Very likely has no cache-control MSRs.
> 
> @appletechgeek (OP) Could try blocking all kvm modules to avoid putting host cpu into VM mode. Have seen a few cases where having some virtualization server or client installed will flip the main cpu to VM mode for no real reason.

@SChernykh - Sorry for the late reply.  The very day we talked previously, I started downloading each prior version of XMRig that had a bionic release, all the way back to 6.3.3.  Weirdly, I couldn't find a release that *didn't* have the error we mentioned before.  I didn't go back to 6.3.2 or further because there were only Xenial releases for those versions.  So, I figured maybe the issue was with my hardware (or something else in my Ubuntu 18.04 setup) as opposed to the base xmrig software.

@Spudz76 Thank you for your reply.  It's interesting that Pantera is the one with the bug, and that's why it doesn't show the msr error that we were mentioning previously!

Just as an aside - when I try to run the "./randomx_boost" script, I get the following output:

<img width="508" alt="Randomx_boost" src="https://user-images.githubusercontent.com/27851570/110839043-26df0f00-8271-11eb-8fc9-ef786ee8ab1a.png">

I don't really know what it means on my machine that " CPU 0 cannot set MSR 0x000001a4 to 0x000000000000000f", and I do already have msr-tools installed as you can see .... not really sure what the issue is but thought perhaps it had something to do with my hardware or Ubuntu setup (though, there's nothing super fancy or modified about my setup).


## SChernykh | 2021-03-11T19:00:36+00:00
It might be Secure Boot option in BIOS that disables access to MSR, check your BIOS settings.

## jabronimus | 2021-03-11T19:37:35+00:00
> It might be Secure Boot option in BIOS that disables access to MSR, check your BIOS settings.

@SChernykh - checked using mokutil, secureboot disabled:

<img width="537" alt="secure-boot check" src="https://user-images.githubusercontent.com/27851570/110844322-4842f980-8277-11eb-9c47-7cf8aedb4583.png">


# Action History
- Created by: appletechgeek | 2021-03-08T14:42:13+00:00
- Closed at: 2021-04-12T14:00:33+00:00
