---
title: '[Discussion] Blockers towards including Rust into monero codebase'
source_url: https://github.com/monero-project/monero/issues/9297
author: SyntheticBird45
assignees: []
labels:
- discussion
created_at: '2024-04-20T21:17:42+00:00'
updated_at: '2025-09-30T20:38:32+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
# Why ?

@kayabanerve proposal to implement the FCMPs over a Rust library, restarted the discussion of Rust being introduced into monero core. This discussion isn't about whether Rust should be integrated into monero but what are the blockers of doing so, if the team is willing to do so. 

# Blockers
Monero core introducing Rust into the codebase means introducing the necessary build tools. Interoperability between C++/Rust isn't necessarily an issue, as libraries exist for that purpose, and/or public functions can be defined by `extern "C" fn`, making it use the C API.

## Targets

What haven't been discussed yet, are the build targets. Monero Core offers official releases/reproducible builds for: Windows (x86(_64)) MacOS (x86, ARM), Linux (x86(_64), ARMv7, ARMv8, RISC-V), Android (ARMv7, ARMv8), FreeBSD (x86_64)
And provide documentation for building on:
OpenBSD, NetBSD, Solaris

The rust compiler offers different *Tier*s of guarantees depending of which platform we wish to build for. 

`Tier 1` means it is officially supported, guaranteed to work.
**Monerod targets falling into Tier 1**:
- `i686-unknown-linux-gnu` | *x86* 32-bit Linux (kernel 3.2+, glibc 2.17+)
- `x86_64-unknown-linux-gnu` | *x86* 64-bit Linux (kernel 3.2+, glibc 2.17+)
- `aarch64-unknown-linux-gnu` | ARM*v8-A* 64-bit Linux (kernel 4.1, glibc 2.17+)
- `i686-pc-windows-gnu` | *x86* 32-bit MinGW (Windows 7+)
- `x86_64-pc-windows-gnu` | *x86* 64-bit MinGW (Windows 7+)
- `x86_64-apple-darwin` | x86 64-bit macOS (10.12+, Sierra+)

`Tier 2` means it is officially supported, but only guaranteed to build. The Rust teams make no assumptions that the changes are scrutinized and some tests are not used. Bugs are possible and reports are welcome.
**Monerod targets falling into Tier 2**:
- `armv7-unknown-linux-gnueabihf` | ARMv7-A (32 bit) hardfloat (kernel 3.2, glibc 2.17)
- `riscv64gc-unknown-linux-gnu` | RISC-V Linux (64 bit) (kernel 4.20, glibc 2.29)
- `x86_64-unknown-freebsd` | *x86* 64-bit FreeBSD
- `armv7-linux-androideabi` | ARMv7-A (32 bit) Android
- `aarch64-linux-android` | ARMv8-A (64 bit) Android

`Tier 3` means the Rust codebase should work on these targets but the Rust project does not build or test them. There are no guarantees.
**Monerod targets falling into Tier 3**:
- `aarch64-unknown-openbsd` | ARMv8-A (64 bit) OpenBSD
- `x86_64-unknown-openbsd` | *x86* (64 bit) OpenBSD
- `aarch64-unknown-netbsd` | ARMv8-A (64 bit) NetBSD
- `x86_64-unknown-netbsd` | *x86* (64 bit) NetBSD
- `x86_64-pc-solaris` | *x86* (64 bit) Solaris

# Discussion History
## detherminal | 2024-04-20T21:50:12+00:00
~~I support adding Rust codebase to the project in general. Rust blocks memory-leaks, has built-in package manager and many features. It is also being used by many professional and world-wide apps, including Linux. It would be easier for other developers to develop, compile and run.~~
> Removed due to issue rename

Targeting part of the Rust codebase should be similar to the current one, where we officially build and publish the binaries and document the rest. That means the Tier 1 and Tier 2 is supported and Tier 3 is only left with documentation just like as it is now.

I also think we should start supporting aarch64 on darwin (macOS) as Apple is moving to the ARM (aarch64/arm64) architecture.

## SyntheticBird45 | 2024-04-20T22:22:08+00:00
> I support adding Rust codebase to the project in general. Rust blocks memory-leaks, has built-in package manager and many features. It is also being used by many professional and world-wide apps, including Linux.

I think Rust isn't near being discriminated or belittled. There are no doubts that it is a great language if not the greatest to become language. But there are valid critics against adding Rust into the monerod codebase. Ones being: build targets, binary size, interoperability, exploit mitigations support accross FFI, etc...

This is something that will require a non-trivial amount of tinkering accross the repository.

> Rust blocks memory-leaks

TBC, monerod compile with almost all exploit mitigation flags enabled + Memory leaks aren't considered an unsafe behavior by Rust.

## kayabaNerve | 2024-04-20T22:27:57+00:00
This issue needs to be properly scoped. The title makes this an issue about FCMPs over RingCT which this definitively should not be the issue for.

Is this:

1) Blockers towards introducing Rust.

Unopinionated on the topic, not sidetracked by if/why. Solely covering why it may not be possible in the first place.

2) Introducing Rust.

A place for people to discuss if/why, blockers being reasons for why not.

---

I'd personally prefer the former as it eliminates wide classes of arguments from this issue specifically and leaves them for a later date, when we have reasons for why (as we don't currently have any yet other than the vague concept of FCMPs which is not ready for merge and has no active CCS, unless one argues for Rust in general).

dethereminal's comment argued for Rust in general yet does so by advertising an anti-feature. Now I feel obligated to point out why Rust is 'actually bad' for having a package manager, per the opinions of Monero, when that's completely irrelevant here.

And then literally as I typed this, @SyntheticBird45 contributed more of a shill comment for Rust than I think I've ever written (despite being the Rust evangelist in my friend group). I don't want to spend the time rebuking it, so I'll instead repeat we should have a complete moratorium on all discussions about Rust and solely discuss the blockers to it *if it were to happen*.

---

Monero offers downloads for:

[Windows, 64-bit](https://downloads.getmonero.org/cli/monero-win-x64-v0.18.3.3.zip)
[Windows, 32-bit](https://downloads.getmonero.org/cli/monero-win-x86-v0.18.3.3.zip)
[macOS, Intel](https://downloads.getmonero.org/cli/monero-mac-x64-v0.18.3.3.tar.bz2)
[macOS, ARM](https://downloads.getmonero.org/cli/monero-mac-armv8-v0.18.3.3.tar.bz2)
[Linux, 64-bit](https://downloads.getmonero.org/cli/monero-linux-x64-v0.18.3.3.tar.bz2)
[Linux, 32-bit](https://downloads.getmonero.org/cli/monero-linux-x86-v0.18.3.3.tar.bz2)
[Linux, armv7](https://downloads.getmonero.org/cli/monero-linux-armv7-v0.18.3.3.tar.bz2)
[Linux, armv8](https://downloads.getmonero.org/cli/monero-linux-armv8-v0.18.3.3.tar.bz2)
[Linux, riscv64](https://downloads.getmonero.org/cli/monero-linux-riscv64-v0.18.3.3.tar.bz2)
[Android, armv7](https://downloads.getmonero.org/cli/monero-android-armv7-v0.18.3.3.tar.bz2)
[Android, armv8](https://downloads.getmonero.org/cli/monero-android-armv8-v0.18.3.3.tar.bz2)
[FreeBSD, 64-bit](https://downloads.getmonero.org/cli/monero-freebsd-x64-v0.18.3.3.tar.bz2)

per the latest release. I'd accordingly argue that's Monero's own tier one/two and ignore documentation-only targets (which are equivalent to Rust's tier three, and seem to completely overlap?).

## kayabaNerve | 2024-04-20T22:51:48+00:00
Tier 2:
- ARM macOS
- ARMv7 Linux
- RISC-V 64-bit Linux
- ARMv7, ARMv8 Android
- x86-64 FreeBSD

The rest of the platforms we build binaries for are tier 1, with the caveat that the tier-one Windows support by Rust is for Windows 10+. Since Windows 8.1 is over a year past EOL, I don't blame them for this decision. That... may work on older Windows version, just in an un-officially-supported fashion? Or may require shipping a distinct Windows 7 build from their tier-three Windows 7 target (or using an old Rust compiler which still had older Windows supported as tier one/two).

---

For the tier-two targets discussed, I'm not concerned. ARM macOS is widely used by the Rust community to the point I'm surprised it hasn't had the necessary steps to become tier-one (maybe due to commentary on acquiring/provisioning the hardware for it?). Given the large community using it without noise about issues, I'd legitimately assume it to be void of increased-frequency platform-specific bugs. Given people also use Rust for Android development, I'd have similar thoughts there.

That isn't to endorse every tier-two target as perfect. It's to say, yes, they're not tier-three and I largely assume them to work *especially* when we use the most popular ones. Current proposed usecases also use a minimal subset of platform-specific code (not hooking the OS, nor writing SIMD code, so current poposals may use just a couple lines for system RNG and so on) so I wouldn't expect impact there. I'd expect most impact to actually come from LLVM. Since we use LLVM on FreeBSD, it appears Monero has adopted LLVM use into its tier-one (at least for certain targets). Accordingly, I'm not concerned there either.

## ghost | 2024-06-17T22:44:48+00:00
Could the introduction of Rust in the monero project be done in phases? Similarly to the Linux kernel that is slowly introducing rust instead of swapping the whole project at once. This would be much easier to implement I assume.

## vtnerd | 2024-06-17T23:23:57+00:00
> Could the introduction of Rust in the monero project be done in phases? Similarly to the Linux kernel that is slowly introducing rust instead of swapping the whole project at once. This would be much easier to implement I assume.

I thought the initial suggestion was to use Rust just for crypto elements with FCMP, and not necessarily re-writing the whole thing in Rust (there is already a project doing that).

## SyntheticBird45 | 2024-06-17T23:40:56+00:00
> I thought the initial suggestion was to use Rust just for crypto elements with FCMP, and not necessarily re-writing the whole thing in Rust (there is already a project doing that).

Yes. your initial thought is right and this is actually still the case

## hhartzer | 2025-09-30T19:03:24+00:00
I am not sure if this is the appropriate forum to do so, but I would like to voice a couple of my concerns about incorporating Rust into Monero.

Rust buildtimes are incredibly long and require lots of memory. Many packages are no longer available on x86-32 architectures (Linux + BSDs) because rust tends to require more than 4GB of memory to build. This limits compiling Monero to larger/faster hardware than it does now.

Rust also changes at a fast pace. I frequently see where a package will require a new rust version not yet ported. Or two Rust packages not compatible with eachother. This is also a headache for trying to compile anything with Rust.

I understand that there are many benefits to Rust, but it's certainly not without drawbacks. I wonder if there is an alternative that would offer some of the benefits of Rust, but without making compilation such a headache.

## kayabaNerve | 2025-09-30T20:38:32+00:00
We only require a comparatively old version of Rust, 1.69, so the only concern would be the resource consumption. I don't believe that's sufficient in general and it's far too late now.

# Action History
- Created by: SyntheticBird45 | 2024-04-20T21:17:42+00:00
