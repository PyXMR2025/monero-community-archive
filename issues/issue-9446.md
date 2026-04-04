---
title: '[Proposal] General rule for minimum package versions and distribution support'
source_url: https://github.com/monero-project/monero/issues/9446
author: tobtoht
assignees: []
labels:
- important
- proposal
- discussion
- build system
created_at: '2024-08-20T14:15:45+00:00'
updated_at: '2026-04-02T19:18:31+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
It would be nice if we could reach consensus on a general rule for minimum package versions and distribution support. This comes up occasionally (e.g. #9443, #9171, #8922) and it always seems to spark a debate that goes nowhere.

I would like to propose that we guarantee support for distributions until EOL date + 1 year, to give users ample time to upgrade their machine.

Users on distributions that don't package the minimum version of a required library can still build Monero using `make depends`. 

#### Why?

- To give developers access to new library features when they believe this would benefit their code.
- To reduce maintenance burden associated with guaranteeing compatibility with a wide range of library versions / compilers / operating systems.
- To prevent us from having to argue about this every time a minimum version change is proposed.

#### Example

| OS           | EOL date    | Boost version | Supported   |
|--------------|-------------|---------------|-------------|
| Ubuntu 16.04 | 02 Apr 2021 | 1.58          | No          |
| Ubuntu 18.04 | 21 May 2023 | 1.65          | No  |
| Ubuntu 20.04 | 02 Apr 2025 | 1.71          | No         |
| Debian 9 (LTS) | 01 Jul 2022 | 1.62 | No |
| Debian 10 (LTS)    | 30 Jun 2024 | 1.67          | No          |
| Debian 11 (LTS)   | 31 Aug 2026 | 1.74          | Yes |

With the proposed rule, we would currently guarantee support for Boost 1.71 at minimum.

#### A more complete list

| Build tool   | Version |
|--------------|---------|
| binutils     | 2.35 |
| cmake        | 3.18 |
| curl         | 7.74.0 |
| cxx standard | c++17 |
| doxygen      | 1.9.1 |
| gcc          | 10.2.1 |
| graphviz     | 2.42.2 |
| make         | 4.3 |
| python       | 3.9 |
| **Library**  |          |
| boost        | 1.74 |
| hidapi       | 0.10.1 |
| libsodium    | 1.0.18 |
| libusb       | 1.0.23 |
| libzmq       | 4.3.2 |
| openssl      | 1.1.1w |
| protobuf     | 3.12.4 |
| readline     | 8.1 |
| unbound      | 1.13.1 |
| **Runtime**  |         |
| glibc        | 2.31 |

| Operating system | Version   | Until       |
|------------------|-----------|-------------|
| [macOS](https://endoflife.date/macos)            | 13        | 15 Sep 2026 |
| [Windows](https://endoflife.date/windows)          | 10 (22H2) | 14 Oct 2026 |
| [Android](https://endoflife.date/android)          | 13        | 02 Mar 2027 |
| [FreeBSD](https://endoflife.date/freebsd)          | 13        | 30 Apr 2027 |
| [Debian](https://endoflife.date/debian) | 11 | 31 Aug 2027 |
| [Ubuntu](https://endoflife.date/ubuntu)           | 22.04     | 01 Apr 2028 |


# Discussion History
## iamamyth | 2024-08-20T15:19:07+00:00
I support this rule; it's exactly what motivated my comment about upgrading to Boost 1.67 on https://github.com/monero-project/monero/pull/9443.

## 0xFFFC0000 | 2024-08-20T16:08:04+00:00
I support this proposal. I think we need a well defined / official approach like this. 

We can discuss more about the details and versions. But the proposal itself is very needed. 

## tobtoht | 2024-08-20T16:41:23+00:00
I don't think EOL + 1 year is aggressive. Users (and devs) shouldn't be running security sensitive software on distributions that no longer receive security updates. It doesn't make sense to waste development time or withhold features to encourage bad practices.

Official binaries would continue to work on 18.04 (because we statically link Boost). Development builds would continue to work on Ubuntu 18.04 using `depends`. I'm not aware of any sites that have statistics, and I'm not sure how accurate they would be.

Keep in mind that if the version bump goes into `master`, it will only start affecting release branch builds when we branch from master, which doesn't happen that often (typically only when we hardfork?).

## selsta | 2024-08-20T16:42:42+00:00
@tobtoht I deleted my comment because I misunderstood your proposal

## tobtoht | 2024-08-20T17:12:58+00:00
Ah, the page hadn't updated. Yes, to clarify: this isn't about dropping support for anything the minute we reach the EOL + 1 year mark. We would guarantee support for that long and update a minimum when there is a reason to.

For example:

- feature x isn't possible without a newer library version
- feature x is better implemented with a newer library version
- there is a security benefit to updating the minimum (if it affects release builds)
- the minimum version is causing breakage for another change
- there is ongoing maintenance work associated with keeping support for the minimum version
- updating the minimum version doesn't affect anyone (and there is some benefit to bumping)

## jeffro256 | 2025-11-22T15:36:39+00:00
I generally support this rule. I do have one question: as it currently stands, `make depends` will only get you so far on older systems when we update the minimum C++ language version, right? For example, if we updated to C++20 right now, Ubuntu 18.04 wouldn't be able to compile with `make depends` because its highest supported GCC version is 7.5 AFAIK. Is that correct?

## jeffro256 | 2025-11-22T15:38:45+00:00
I guess you could probably bootstrap the compiler on those systems, but that's probably not worth the effort / bloat. So then is it worthwhile to make a rule about supporting certain systems with the `make depends` route? Specifically, having a more conservative rule about language version bumps. 

## nahuhh | 2025-11-22T15:46:52+00:00
>Ubuntu 18.04 wouldn't be able to compile with `make depends

why not drop support for 18.04? Hasnt it been eol for a while

## jeffro256 | 2025-11-22T15:51:49+00:00
Well at the moment, we use Ubuntu 18.04 for gitian reproducible builds. Tbf, we could change that. 

## tobtoht | 2025-11-22T16:32:07+00:00
This issue concerns the `master` branch. For the `release` branch, minimum version bumps for build dependencies should be avoided when possible, and under no circumstances should we bump the cxx standard or runtime requirements of release binaries (such as the minimum glibc version). 

This way, downstream projects (e.g. GUI / Cake Wallet) aren't required to make changes to their build systems and users don't need to upgrade their system between minor releases. Minimum versions for the `release` branch are essentially "frozen" until we branch from `master`.

 >Well at the moment, we use Ubuntu 18.04 for gitian reproducible builds. Tbf, we could change that.

We wouldn't be able to bump the Ubuntu version in Gitian without affecting the minimum glibc requirement. E.g. if we bump it to Ubuntu 20.04, binaries wouldn't be able to run on Ubuntu 18.04.

The next time we branch from `master` releases will be built with [Guix](https://github.com/monero-project/monero/tree/master/contrib/guix#bootstrappable-monero-builds), using GCC 12 (or 14 #9969), C++17 (up from 14), and dynamically linked against [glibc 2.27](https://github.com/monero-project/monero/blob/bba6aa518ba4533859766672cf996f6427b8f1a4/contrib/guix/manifest.scm#L175) (so they run on Ubuntu 18.04). 

(In the future, I would like us to ship fully static binaries linking either glibc (#9207) or musl (#10208), so we don't need to worry about runtime requirements at all. These binaries will run on any Linux distribution.)

>why not drop support for 18.04? 

As it stands, we don't support 18.04. (See table in OP.)

# Action History
- Created by: tobtoht | 2024-08-20T14:15:45+00:00
