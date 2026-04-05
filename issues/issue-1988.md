---
title: MSR errors on Clear Linux
source_url: https://github.com/xmrig/xmrig/issues/1988
author: agentpatience
assignees: []
labels:
- question
created_at: '2020-12-20T02:42:15+00:00'
updated_at: '2021-04-12T14:27:58+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:27:58+00:00'
---

# Original Description
Hi, 

I am getting MSR Allocation errors on Intel Clear Linux
![3AB07997-7B5F-4302-898D-EEF1C74B2315](https://user-images.githubusercontent.com/36264810/102703897-0049a300-4243-11eb-9197-ba5f33abd285.jpeg)


# Discussion History
## xmrig | 2020-12-21T09:52:39+00:00
This warning should be already fixed #1912 I suspect you load the `msr` module before the miner starts without `allow_writes=on` parameter. Anyway it's just a warning not error.
Thank you.


## agentpatience | 2020-12-21T16:33:38+00:00
Hi XMRIG,

I understand the MSR errors are just warning now but are you saying to pass --allow-writes=on in xmrig command line?

Also, Clear Linux is having trouble allocating 1GB huge pages, as seen in the photo "failed to allocate randomx dataset using 1GB pages." 

How can I fix this?


## bp3tk0v | 2020-12-21T17:32:43+00:00
> Anyway it's just a warning not error.

For now.

I'd strongly suggest you guys stop poking at the MSRs directly from userspace but use a proper file in sysfs. Would you be willing to test a patch if we expose the hw prefetcher controls somewhere in /sys/devices/system/cpu/cpuN/... and you convert your tool to write to that file instead of using the wrmsr tool?

Thx.


## xmrig | 2020-12-22T09:15:18+00:00
@bp3tk0v Which file exactly? and please note there is no single value for prefetcher controls even for same vendor CPUs https://xmrig.com/docs/miner/randomx-optimization-guide/msr `advanced format` to use masks read/write access is required.
Thank you.


## bp3tk0v | 2020-12-22T11:59:06+00:00
> @bp3tk0v Which file exactly? and please note there is no single value for prefetcher controls even for same vendor CPUs https://xmrig.com/docs/miner/randomx-optimization-guide/msr `advanced format` to use masks read/write access is required.

Well, that is the good thing about putting it in the kernel - one is free to design the abstraction as optimally as possible. Also, from reading that page a bit, you won't need to fiddle with secure boot either, once you have a sysfs interface.
And you can hide all that complexity and vendor-specific bit settings in the kernel too.

So, for example, if you only want to disable prefetchers, I think it could be something as simple as

echo "disable" > /sys/devices/system/cpu/config/prefetchers

or so. This way you can disable the prefetchers globally. The exact name and place will be the result of the usual LKML bikeshedding. :-)

The control can be also finer-grained - per CPU, disable single prefetchers only, etc, etc. It all is dictated by the requirements people would have.

So once you know what your requirements are - i.e., how you want to disable the prefethers from your tool - just send a note to x86-at-kernel.org (replace "-at-" with @) where we can continue designing it and test patches.

Thx.

## SChernykh | 2020-12-22T12:48:03+00:00
@bp3tk0v It would be nice if you figured it out and XMRig would happily use it, but the problem is that MSR registers that control this are not documented at all. Current patch is the result of many trials and errors and is essentially a black box. I have only a vague idea what each of the 4 registers controls and what some bits in them do. They control more than just prefetchers. You can't expose `/sys/devices/system/cpu/config/prefetchers` without getting some heavy NDA'd documents from AMD first.

## bp3tk0v | 2020-12-22T13:21:51+00:00
@SChernykh that all depends on the use case, of course. I saw yesterday while browsing through those issue pages here that Intel have actually documented the prefetchers:

https://software.intel.com/content/www/us/en/develop/articles/disclosure-of-hw-prefetcher-control-on-some-intel-processors.html

the gist being that for some workloads disabling the prefetchers might make sense. So I don't see why AMD won't follow there **if** it makes sense to do so. Like they've done in the past for other things.

What people should **not** do is poke at random MSRs. This is always a bad idea and we're tainting the kernel if userspace has done so so that people looking at bug reports can know that the CPU configuration has been changed in an unexpected way.

Now, do you have a writeup somewhere and perhaps even performance data to show that disabling the prefetchers for your workload makes sense?

Hard proof data always helps when talking to hw people. :) 

Thx.

## SChernykh | 2020-12-22T13:56:16+00:00
> So I don't see why AMD won't follow there if it makes sense to do so. Like they've done in the past for other things.

They only share it with motherboard manufacturers. It's not a public information. Why? Ask them.

> Now, do you have a writeup somewhere and perhaps even performance data to show that disabling the prefetchers for your workload makes sense?

Silly question. No, we're tinkering with MSRs just for fun, you know. All necessary links were already quoted here.

## xmrig | 2020-12-22T14:28:58+00:00
* Disabling raw access to MSR registers will make impossible research or fine tuning, you really suggest to use Windows for it in future?
* Users do not update the kernel every time, so for example some LTS users will wait for changes in prefetchers for years until the next release.
* Even for Intel where is only one MSR register it is not possible to implement a simple `disabled` value, because it is much more complicated than a single value.

@bp3tk0v I understand your position and motivation and will be happy to consensus, but right now it looks like disallowing knives, because people can do weird things with knives, not possible to provide a safe interface for every possible case.

## bp3tk0v | 2020-12-22T15:04:16+00:00
> They only share it with motherboard manufacturers. It's not a public information. Why? Ask them.

There are multiple reasons why. And sometimes, if it makes sense, they - and by they I mean **all** vendors - document stuff publicly.

> Silly question. No, we're tinkering with MSRs just for fun, you know. All necessary links were already quoted here.

I was being serious but your call. If you wanna solve this properly, get back to me with performance proof that shows that disabling the hw prefetchers shows a difference which is not in the noise.

## bp3tk0v | 2020-12-22T15:12:22+00:00
>     * Disabling raw access to MSR registers will make impossible research or fine tuning, you really suggest to use Windows for it in future?

I cannot talk about the future. Right now MSR writes are not disabled - there's an innocent warning that gets issued into dmesg and the kernel gets tainted. What that means is that bug reports about such kernels might not be taken seriously. Just like bug reports when using proprietary software. IOW, users are on their own.

>     * Users do not update the kernel every time, so for example some LTS users will wait for changes in prefetchers for years until the next release.

LTS kernels get stable backports. If desired, that functionality can be backported there pretty easily.

>     * Even for Intel where is only one MSR register it is not possible to implement a simple `disabled` value, because it is much more complicated than a single value.

It all depends on how/what you want to achieve. And it doesn't matter how many MSRs there are - you can write them all in one go.
 
> @bp3tk0v I understand your position and motivation and will be happy to consensus, but right now it looks like disallowing knives, because people can do weird things with knives, not possible to provide a safe interface for every possible case.

No, we're not doing that. We're asking people to help us define a proper interface and move their tools to using it instead of poking at random MSRs. And I've converted our in-tree tools already so it is very easily doable actually.

I hope that makes sense.

Thx.


## xmrig | 2020-12-22T15:20:28+00:00
> I was being serious but your call. If you wanna solve this properly, get back to me with performance proof that shows that disabling the hw prefetchers shows a difference which is not in the noise.

I already linked above to the page https://xmrig.com/docs/miner/randomx-optimization-guide/msr it contains all information, what registers changed with values and it also contains links to early reddit discussions. You can also measure performance differences by yourself.

## SChernykh | 2020-12-22T15:20:33+00:00
> get back to me with performance proof that shows that disabling the hw prefetchers shows a difference which is not in the noise.

I think you are not being serious. It's been a common knowledge for over a year that turning off prefetchers (using MSR mod) increases hashrate significantly. As I said, links are in this topic, take your time and follow to the reddit discussions from https://xmrig.com/docs/miner/randomx-optimization-guide/msr

What we need is the access to all MSR registers listed in https://github.com/xmrig/xmrig/blob/dev/scripts/randomx_boost.sh , all bits in them. If it doesn't work in some future Linux release, we'll find a workaround anyway.

## bp3tk0v | 2020-12-22T15:30:05+00:00
> You can also measure performance differences by yourself.

What would be a typical workload to run?

## Spudz76 | 2020-12-22T16:03:43+00:00
Guessing wildly here but, probably to benchmark things you'd run one of the provided benchmark scripts, with and then without the MSR "random writes" to very specific places with very specific values.

Then copy the working proven "random writes" into your kernel support for when someone writes "disable" to whatever sysfs location.  I don't see how this makes the writes any less "random".

And then maintain knowledge of which CPUs like which MSRs so that an Atom without them doesn't complain, AMD MSRs are purely guesses, etc.  Good luck.

## SChernykh | 2020-12-22T16:09:41+00:00
> > You can also measure performance differences by yourself.
> 
> What would be a typical workload to run?

`./xmrig --bench=1M` without sudo and not under root so it can't apply MSRs. Then the same with sudo or under root. And you need to enable huge pages first to exclude that factor (preallocate 1280 huge pages).

# Action History
- Created by: agentpatience | 2020-12-20T02:42:15+00:00
- Closed at: 2021-04-12T14:27:58+00:00
