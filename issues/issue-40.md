---
title: Build Targets
source_url: https://github.com/Cuprate/cuprate/issues/40
author: hinto-janai
assignees: []
labels:
- C-discussion
created_at: '2023-12-04T22:01:13+00:00'
updated_at: '2024-05-27T00:57:22+00:00'
type: issue
status: closed
closed_at: '2024-02-04T21:39:04+00:00'
---

# Original Description
## What
This is a request for comment on the build targets Cuprate should support.

The common 2 architectures:
- `x86_64`
- `ARM64`

and common 3 operating systems:
- Windows
- macOS
- Linux

would be a given, however supporting older/obscure combinations is the discussion point.

As an alternative to Monero and not the main implementation, only supporting common targets may be okay.

## Which
Relatively old/obscure architectures supported by Monero:
- `x86`
- `armv7`
- `armv6`
- Many cross-compile targets, e.g `x86_64-w64-mingw32`

Relatively old/obscure OS's supported by Monero:
- FreeBSD
- OpenBSD
- NetBSD
- Solaris

## Pros
- Build target parity with Monero
- Wider accessibility on different machines

## Cons
- Cost of maintenance and testing
- Code portability limitations

In terms of code portability:
- The dependency tree must also support targets we support
- 64-bit invariants cannot be assumed

For example:
```rust
u64 as usize; 
```
would be preferred to:
```rust
match usize::try_from(u64) {
    Ok(u) => u,
    Err(_) => /* handle the conversion error */
}
```
assuming only 64-bit targets will be supported, otherwise it might lead to disaster on 32-bit platforms.

Other types/code relying on pointer sizes would need to be accounted for, as well as OS specifics (e.g directory locations).

# Discussion History
## SyntheticBird45 | 2023-12-18T13:53:13+00:00
> - x86

32 bit `x86` is on the verge of extinction. 
Supporting it would be a lost of time. Even the cheapest and oldest VPS now use 64 bit. The latest versions of windows became impractical on 32 bit platform (lack of software support and max memory usage). We can only assume 32 bit platforms are used through Linux. But taking community trends into account, most people hosting a monero node or even monero wallet is most likely to have a 64 bit CPU.
The amount of effort needed to support `x86` and debug it is too much for a platform that will disappear in the next 5~10 years

> - armv7
> - armv6

As for ARM, The first raspberry pi used an ARMv7 32 bit cpu and later switch to a 64 bit for the second edition. It should be take as a reference for understanding the use of a node in an `embedded` environment. There are no more ARMv6 CPU out in the wild. Lot of cheap smartphones are stuck to ARMv7. I think supporting ARMv7 64bit should be the minimum.
Through the years we should see more and more CPU switch to ARMv9 or ARMv8.5-A. It support memory tagging, one of the most significant hardware mitigation to memory corruption/vulnerabilities. LLVM added support two years ago but there is still no official rustc support. I think it should be something to keep track on.

> - Many cross-compile targets, e.g `x86_64-w64-mingw32`

I already tried cross-compiling from Linux to Windows and the environment is quite tricky to setup. mingw should be easy, but most windows applications would prefer using MSVC runtime. This can be done by using tools like cargo-xwin and some crates to static link msvc.dll. I'm not against but it requires some work

> - *BSD

Lot of criticism has been made on OpenBSD security architecture and development practices. I'm not knowledgeable enough on BSD internals to say if BSD really respect its said goal. But a lot of monero folks out there really like BSD and have converted their servers onto it. I think OpenBSD is the only BSD distribution to put focus on.

> - Solaris

No one use Solaris. It's a dead OS. Last release was 3 months ago. At the time of writing there are only 4 people online on r/solaris. It still use GNOME 1. Also I bet no one will have the motivation to install Solaris and start debugging it + x86_64 Solaris is only [Tier 2 rustc suppot](https://doc.rust-lang.org/nightly/rustc/platform-support.html#tier-2-without-host-tools) and [isn't even mention the rust reference book](https://doc.rust-lang.org/reference/conditional-compilation.html#target_os)
I know my opinion on Solaris is harsh but I think it is realistic. 

Summary of my opinion:
- no 32 bit support
- minimum armv7
- look forward armv9/8.5-A
- cross-platform, msvc or mingw ?

## hinto-janai | 2023-12-23T16:51:32+00:00
For reference, Debian[^1] (and the kernel[^2] as a whole) is slowly but surely dropping support for 32-bit architectures.

It is also safe to say that 128-bit will not be a concern for many, many years[^3], so something like this should be safe:
```rust
usize as u64;
```

[^1]: https://lists.debian.org/debian-devel-announce/2023/12/msg00003.html
[^2]: https://lore.kernel.org/lkml/CAHk-=wjrpH1+6cQQjTO6p-96ndBMiOnNH098vhS2jLybxD+7gA@mail.gmail.com
[^3]: https://en.wikipedia.org/wiki/128-bit_computing

## SyntheticBird45 | 2024-02-03T15:00:48+00:00
I think we can make a decision on this topic pretty soon.
My actual opinion is:
- x86_64, armv7_64
- Linux, Windows, macOS and OpenBSD

Pending questions:
- Do we cross-compile ? (from linux to windows) using mingw or msvc ?
- Is FreeBSD worth it ?

## hinto-janai | 2024-02-04T14:07:09+00:00
Agree with only supporting 64-bit.

Windows builds (at least in CI, maybe release builds too) can just use the default `x86_64-pc-windows-msvc`. I don't think testing/documenting cross-compiling is worthwhile if it can be compiled natively. I think it's also safe to only support `ARM` for `macOS` and `Linux`. Windows on `ARM` exists but there's no users.

If we support BSDs, it'll increase testing time for a relatively small userbase, but it feels wrong not to support them. @Boog900 what do you think? 

## SyntheticBird45 | 2024-02-04T17:59:57+00:00
I guess we could provide for BSD later on ?

## Boog900 | 2024-02-04T21:04:27+00:00
I agree, I think we should look at supporting BSD later.

I think for now we shouldn't stress too much about supported builds and should just go with the "common" architectures/ OS.

We should probably look at adding windows and macOS back to CI.

## SyntheticBird45 | 2024-02-04T21:39:04+00:00
Alright let's close this issue for now.
First planned build targets are:
- (64bit only)
- Linux (x86_64, ARMv7)
- Windows (x86_64)
- MacOS (x86_64, ARMv7)

# Action History
- Created by: hinto-janai | 2023-12-04T22:01:13+00:00
- Closed at: 2024-02-04T21:39:04+00:00
