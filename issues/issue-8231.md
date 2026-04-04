---
title: Can I contribute in rust?
source_url: https://github.com/monero-project/monero/issues/8231
author: daniel-brenot
assignees: []
labels: []
created_at: '2022-03-31T06:45:36+00:00'
updated_at: '2022-10-15T14:29:48+00:00'
type: issue
status: closed
closed_at: '2022-04-06T02:35:55+00:00'
---

# Original Description
I'm insterested in contributing to this project, and i'm looking at how to slowly convert a c++ project over to rust. It would have the following benefits:

 - Increased readability
 - Wider Portability
 - Potentially Increased performance(Sometimes the language can be faster, sometimes it's just because the rewrite uses more efficient methods)
 - Memory safety guaruntee
 - Easier to develop for
 
An estimated majority of CVEs are measured to be due to memory issues such as buffer overflow attacks. Rust doesn't have this issue when using safe code.

Additionally, tools such as clippy can be used to enforce prefered code conventions to the project, so code can be rejected automatically until it passes linting.

I'm looking at how to do this by replacing one piece at a time, and i'd love to hear if there would be any interest in this. There would also be less setup required to compile this since rust uses a package manager, so you would just need to run the build command after installing cargo and the packages would just download(sometimes you still have to install the library, but not always).


# Discussion History
## poiuty | 2022-03-31T10:36:44+00:00
https://github.com/monero-rs

## daniel-brenot | 2022-03-31T15:41:59+00:00
> https://github.com/monero-rs

That project is not official and only intends to support a subset of monero functionality. I'm talking about contributing to this official project and slowly porting over old functionality to rust while developing new features in it. It's an approach the linux kernel is taking and Linus Torvalds supports the direction because it generally has been improving code quality and readability.

## hyc | 2022-03-31T15:47:18+00:00
Big question to me is how complete is the toolchain support? We crosscompile for all targets - Linux, Android, Mac, Windows, FreeBSD, x86, x86_64, armv7, armv8 - from Linux. If any of those are missing in rust compiler support, then I'd say no.

## SamsungGalaxyPlayer | 2022-03-31T15:48:30+00:00
The best way to get started for now is by contributing to the unofficial monero-rs repo as @poiuty stated. There are no significant plans to establish an official Rust repo. They will certainly welcome the help in fleshing out the functionality and improving the code.

While unofficial, it doesn't mean that it's unimportant. There are other unofficial Monero projects, like monero-java, monero-python, and monero-javascript with various feature sets.

## hyc | 2022-03-31T15:50:18+00:00
There's also a practical matter of needing a population of competent rust programmers to review contributions. At this moment that would mean an entirely new population compared to the current contributors. Which in my mind means you're actually building a new project, one that should be separate from this one.

## daniel-brenot | 2022-03-31T16:15:48+00:00
> Big question to me is how complete is the toolchain support? We crosscompile for all targets - Linux, Android, Mac, Windows, FreeBSD, x86, x86_64, armv7, armv8 - from Linux. If any of those are missing in rust compiler support, then I'd say no.

The compiler seems to support all of those targets to the best of my knowledge. It is used in the linux kernel, so I can't imagine there are any huge issues with portability.



## daniel-brenot | 2022-03-31T16:21:57+00:00
> There's also a practical matter of needing a population of competent rust programmers to review contributions. At this moment that would mean an entirely new population compared to the current contributors. Which in my mind means you're actually building a new project, one that should be separate from this one.

That's a fair point, although an unfortunate one. I would like to attempt to recreate some of monero in rust, but overall i'm worried about investing time into this project if ultimately it would get rejected even if it is mature because someone has a strange hangup about rust.

So long as the contention with the idea is just that currently there isn't much of a comunity interest, I think I can understand that. What i'm interested to know is if the willingness to accept rust would be higher if there was a stable implementation that existed in rust that showed promise. Would the lack of knowledge in the language prevent current developers from working on this or would they be willing to learn the language if it showed promise?

On an additional note, i'm sure there would be much more contribution by the community if this was written in rust. The rust community has been growing and I can imagine they would be happy to contribute to a project like this.

## hyc | 2022-03-31T16:30:30+00:00
>The compiler seems to support all of those targets to the best of my knowledge. It is used in the linux kernel, so I can't imagine there are any huge issues with portability.

It's not about portability. It's not a question of whether rust supports those platforms at all. It's a question of whether rust supports them when crosscompiling from a Linux host. Cross-build environments tend to be a pain to set up, even if the native support exists.


## hyc | 2022-03-31T16:33:23+00:00
> Would the lack of knowledge in the language prevent current developers from working on this or would they be willing to learn the language if it showed promise?

I personally wouldn't trust my life savings (or my life, for that matter) to a project written by newly trained rust programmers.

> On an additional note, i'm sure there would be much more contribution by the community if this was written in rust. The rust community has been growing and I can imagine they would be happy to contribute to a project like this.

Sounds like all the better for them to work on monero-rs then. If they're as eager to contribute as you believe, then that project should grow rapidly.

## daniel-brenot | 2022-03-31T16:37:53+00:00
> 

That's a fair point I guess. I'll look at contributing to the monero-rs project for the moment, but if it comes to the point in the future where the project is mostly/completely interoperable with this project, then would there be a possibility of that implementation becoming the defacto standard?

## Gingeropolous | 2022-03-31T17:34:39+00:00
> then would there be a possibility of that implementation becoming the defacto standard?

who knows? I think it would really depend on where contributors are contributing. Monero is, first and foremost, a protocol. Second to that, its an open source project. Or maybe its the other way around. But nowhere does it say "monero shall be in c++ forever", nor is that a sentiment that wafts around the various places of development, as far as I can tell. 

Some projects parade the fact that they have multiple implementations of the protocol. Though some say this introduces the possibility for consensus breakage here and there. 

sort of a built it and they will come thing perhaps.

but what do I know. im just a dude. 

## iamamyth | 2022-03-31T21:03:19+00:00
I think your best bet would be creating a wallet library in rust, with an exported C interface, to replace the existing "wallet2" c++ code. The wallet interface has a lot of consumers, so it's arguably an area with the biggest potential impact. Furthermore, there has been talk of imposing certain consensus rules regarding decoy selection, so an additional, actually used wallet implementation will help force some sanity onto that process.

The trouble with trying to replace the entire daemon rests here:
> Some projects parade the fact that they have multiple implementations of the protocol. Though some say this introduces the possibility for consensus breakage here and there.

I doubt most could have even dreamed on c++'s many "features" in the area of "accidental breakage". You'd be in a very tough spot trying to make a functional daemon which interoperates on the network because it's fairly likely that, in the process of attempting such an undertaking, you find behaviors in the existing daemon which seem curious or even wrong or "unspecified", but, as there's no protocol specification, your only option is to just wholesale copy the current behavior, as best as you can (of course, you can engage in a lengthy conversation to determine what should really happen in these cases and appropriately update the c++ code, as needed, but inevitably you're stuck emulating the c++ behavior, or you risk partitioning yourself from the network).

## selsta | 2022-04-06T02:35:55+00:00
Closing this here, as this was mostly answered. `monero-rs` is the best place to contribute currently, unless someone wants to start their own rust project.

## tasty-water | 2022-10-15T14:29:47+00:00
> Big question to me is how complete is the toolchain support? We crosscompile for all targets - Linux, Android, Mac, Windows, FreeBSD, x86, x86_64, armv7, armv8 - from Linux. If any of those are missing in rust compiler support, then I'd say no.

Just a quick note, here's a list of all the officially supported platforms
https://doc.rust-lang.org/nightly/rustc/platform-support.html

# Action History
- Created by: daniel-brenot | 2022-03-31T06:45:36+00:00
- Closed at: 2022-04-06T02:35:55+00:00
