---
title: Minimum Supported Rust Version
source_url: https://github.com/Cuprate/cuprate/issues/41
author: hinto-janai
assignees: []
labels:
- C-discussion
created_at: '2023-12-05T03:36:54+00:00'
updated_at: '2024-05-27T00:57:17+00:00'
type: issue
status: closed
closed_at: '2024-02-03T22:22:32+00:00'
---

# Original Description
## What
Once Cuprate stabilizes, we should set a Minimum Supported Rust Version (MSRV) and `#![deny]` code using future features.

An initial CI failure on a MSRV violation would start a discussion if that particular situation is worth upgrading for. 

The benefit would be that older toolchains would be able to compile Cuprate.

For context, the current Rust version on [Debian stable is `1.63.0`](https://packages.debian.org/bookworm/rust-all).

[`Rust 2024`](https://blog.rust-lang.org/inside-rust/2022/04/04/lang-roadmap-2024.html) which is soon approaching is bound to contain many changes, but that may be a topic for another time.

## Current
As of `2023-12-16` on commit 34dd105a0c585dc34ba0a1ace625663bde00a1dc the effective MSRV is `1.74.0` caused by [`monero-serai v0.1.4-alpha`](https://github.com/cuprate/serai.git?rev=4a5d860#4a5d8601).

This can be checked with [`cargo msrv`](https://github.com/foresterre/cargo-msrv). 

## Version Candidates
This list will be updated to contain versions that could be considered for usage as Cuprate's MSRV, ending at the current minimum effective MSRV.

Features of interest that could be used in Cuprate are also listed per version, bolded means very applicable in Cuprate's case.

Rust changes can be viewed in the [release changelogs](https://github.com/rust-lang/rust/releases) or on [`releases.rs`](https://releases.rs/docs/1.75.0).

#### [`1.76.0 (February 8, 2024)`](https://releases.rs/docs/1.76.0)
- Stabilize C string literals (`c"this_is_a_cstr"`)

#### [`1.75.0 (December 23, 2023)`](https://releases.rs/docs/1.75.0)
- **Stabilize `async fn` and return-position `impl Trait` in trait**
- Windows: Support sub-millisecond sleep
- Allow partially moved values in `match`

#### [`1.74.0 (November 16, 2023)`](https://releases.rs/docs/1.74.0)
- impl Step for IP addresses
- Stabilize the `Saturating` type

# Discussion History
## kayabaNerve | 2023-12-16T22:30:07+00:00
I'm unapologetic for using the latest Rust stable version due to its impact on supply chain security and code cleanliness.

There's effectively five practices used when deciding msrv.

1) Go as early as feasible. I recently made a PR to a project which supported the 2018 edition of Rust, which means they support compilers 4+ years old.
2) Specify a specific version and offer it as LTS. tokio picked, I believe, 1.43 and won't bump that until March of 2024.
3) Figure out what you naturally have as a msrv and try not to raise it.
4) `n - 2`, which I can't claim to understand. It requires build environments update in a timely manner, yet doesn't simply use the latest. I guess it gives a few months to update, instead of a few days?
5) Make no msrv guarantees and use whatever (such as latest).

I understand Cuprate will likely need to support old toolchain versions shipped with various distros, and accordingly will effectively end up under option 2. This is in conflict with Serai's policy, which is an issue so long as Cuprate relies on Serai. Cuprate can either use a modified set of Serai crates or see the below.

My proposal is to create `serai-polyfill`, a crate which can be used as `serai_polyfill:*`. From there, it defines a series of traits/functions offering std backends, yet *which can be patched to offer distinct backends*. In order to ensure Serai's supply chain is minimal, I do believe a complete patch is sane. The other option would be to use feature flags, so undesired crates are in the Cargo.lock yet not compiled, and then anyone needing polyfills can simply *include serai-polyfill as a dependency themselves, setting the needed feature(. Please note I am not proposing to have these features be propagated among Serai's libraries, and anyone wanting to enable polyfills would not do `monero-serai = { features = ["polyfill-1.43"] }` yet would add a new dependency of `serai-polyfill` and feature it. This would somewhat dirty our Cargo.lock and make Serai responsible for guaranteeing the integrity of the Polyfills, hence the preference for a solution based on patches.

This would make Serai responsible for all routing of modern APIs through the Polyfill library, which I believe we could create a reasonable CI for (we do define a patched polyfill, yet one which simply panics at runtime, and verify it compiles). The main issue with this is:
1) It'd require creating a second workspace to execute the tests.
2) It'd require we not use dependencies which have too high a msrv. Serai, as an entire project, relies on several libraries which follow `n-2`. I'm unsure how `monero-serai`'s dependencies stack up, and how feasible that promise is.

## SyntheticBird45 | 2023-12-18T14:05:27+00:00
> Make no msrv guarantees and use whatever (such as latest).

The effort needed at setting up and maintaining `serai-polyfill` is far greater than the difficulty of setting up the latest rust environment. you can download the latest compiler from debian-unstable repo or equivalent for other distributions. There is still the sh script from rust-lang.org that works well. Install and switching targets isn't hard at all.

It would be a shame to limit ourselves to old features and potentially slow down transition to a secure/patched version.

## kayabaNerve | 2023-12-18T14:46:59+00:00
While Serai has made the decision to track the latest, accepting what that entails, that doesn't change Cuprate shouldn't flippantly decide what would likely make it *ineligible* for packaging via the Debian repos.

If Cuprate is fine with not being packaged via official repos, then I'd say just use latest.

## silverpill | 2023-12-18T14:59:36+00:00
I think Debian stable is a good target with regards to MSRV. User experience is paramount and people should be able to use their default package manager wherever possible.

If the current MSRV is 1.74, the optimal strategy would be (3) with the goal of aligning with Debian stable over the next couple of years:

>Figure out what you naturally have as a msrv and try not to raise it.

@kayabaNerve Perhaps you could decouple monero-serai from the rest of the codebase, move it to a separate repo and use different policies there? As a potential user of this library, I would be in favor of a more conservative MSRV policy (in my own  projects I try to follow the Debian stable policy desribed above).

## kayabaNerve | 2023-12-18T15:44:52+00:00
There's an explicit and massive distinction between supporting the packaged Rust in order to support shipping packages of your Rust projects and supporting the packaged Rust in order to let it be used for development. I completely disagree Rust developers should use/have a right to use their default package manager to install Rust. The extremely dated compiler frequently present on Linux distros *isn't recommended for use by the Rust Team* and isn't even mentioned under other installation methods (https://forge.rust-lang.org/infra/other-installation-methods.html).

To enable using Debian's packaged rustc would require using a *2 year old clippy* with a fraction of the linting and tooling. For the CI to still use a modern clippy would require disabling a ton of lints or for developers to consistently have local failures which they need to debug over CI.

It'd also effectively make using rustfmt in CI impossible.

---

@silverpill I am not splitting up the monorepo. The monorepo ensures the integrity of the Serai project regardless of how components move. To split it up would increase the paperwork and cause asynchronicity where pushes made be made in one repo and require fixing for regressions. It'd also reduce the amount of tests run on monero-serai as monero-serai is decently tested by its use in the Serai CIs. That is not to say it doesn't have independent tests/is not decently tested on its own. It's to say a notable quantity of *additional* tests only exist via its pseudo-real-world usage in the Serai processor tests.

Without breaking the monorepo, we can still offer a msrv guarantee on monero-serai. That doesn't require breaking up the monorepo, yet may require making a second workspace in the monorepo (as I'm unsure our usage of the workspace Cargo.toml will work on older toolchains).

Please see https://github.com/Cuprate/cuprate/issues/41#issuecomment-1858944286.

Using recent Rust versions has caused cleaner implementations and a reduced tree for our project. To support an older msrv would increase our vulnerability to supply chain security problems. This is to say nothing about how we do have dependencies which have a msrv > 1.63 and would need to drop functionality/increase our dependency tree even more to get down there.

My option of creating a polyfill library offered an option where a minimal supply chain exists while also ensuring it could be used on archaic Rust versions. While yes, this library would need effort to be implemented/maintained, I'd need to put in most of the same effort to downgrade the project and maintain it in a pseudo-archaic state. If there's not interest in a polyfill library, which I'm not here to judge, the options for Cuprate become:

1) Don't bother supporting packaged rustc, which likely means it won't be included in official packaging repos (which may be acceptable)
2) Vendor their own monero-serai and still put in the effective effort for the polyfill library

## kayabaNerve | 2023-12-18T15:49:07+00:00
Bah. If we don't have a proper workspace Cargo.toml, we'd have to manually specify all the clippy lints we run. I *think* there's some cfg hacks for that we can remove the clean toml solution for, which I wouldn't prefer yet would accept if optimal, yet the other potential option would be to build a sh script just to run clippy, which would make developing from Windows less feasible...

This vein of items is why I don't care to bother with old versions and why I maintain my personal support offer limited to usage of polyfillable APIs.

## kayabaNerve | 2023-12-18T15:51:36+00:00
As one final comment, without further prompting, I'd suggest cuprate focus on security and pleasantry for now and accept inability to be officially packaged. Once cuprate is a working binary stable enough to be packaged, discussions to reduce the msrv can be had *with the full scope of damage it'd do clearly visible* (via the PR removing all the modern APIs in use and adding whatever crates as polyfills).

## SyntheticBird45 | 2023-12-18T16:07:15+00:00
> I'd suggest cuprate focus on security and pleasantry for now and accept inability to be officially packaged

Yes. To be honest, Cuprate's years away from being recognized useful enough by the different linux distribution. User Repositories (like AUR) will likely be the first to package us. But being integrated into Debian and Fedora official repos will require times and dedication.

## silverpill | 2023-12-18T17:53:37+00:00
>There's an explicit and massive distinction between supporting the packaged Rust in order to support shipping packages of your Rust projects and supporting the packaged Rust in order to let it be used for development.

@kayabaNerve I was referring to Cuprate users, who will run the software after compiling it from source. No need to make their life more difficult. I agree that using a version Rust that is 2 years old for development makes little sense (though the Rust Team is hardly an authority on this question, their approach to packaging is horrible).

>I am not splitting up the monorepo

OK


## kayabaNerve | 2023-12-18T22:13:05+00:00
Wouldn't users download a binary and not need to locally build it?

I do get builds from source exist/can be desirable, yet anyone putting in the effort can go through downloading a signed build of Rust.

## silverpill | 2023-12-19T22:33:55+00:00
Some people use binaries, some people build from source. The latter category may not be delighted when they are forced to use some shitty shell script instead of standard tools, that's all I'm trying to say.

## kayabaNerve | 2023-12-20T02:33:39+00:00
rustup, the standard way to download and install Rust, is hardly a "shitty shell script".

While I agree it as an additional requirement is unfortunate, I'd ask you direct your frustration towards Linux distros which ship 2 year old Rust versions.

## hinto-janai | 2023-12-28T20:49:00+00:00
Recently I've been thinking if Cuprate could go the other extreme - no MSRV, track latest stable Rust.

Considering Rust will probably continue to move fast for the next few years, we would be missing out on a lot if we stuck to an older toolchain. A newer toolchain would be nice to have (cargo features, lints, `std` APIs), but the primary motive here is actually continual/incremental upgrading.

Although Rust edition changes aren't as painful as C++, incremental upgrades would spread out the pain (I don't think anyone wants to review a 45,837 lines changed PR going from `Rust 2021 -> 202x`). This can be applied to other big dependencies as well, e.g `tokio`.

Obvious downside - people building Cuprate (and/or using it as a library) need the latest toolchain.

## SyntheticBird45 | 2024-02-03T15:04:49+00:00
I agree with @hinto-janai and @kayabaNerve. I support the tracking of the latest stable Rust.
If there are no more concerns I propose we accept this policy.

## silverpill | 2024-02-03T17:40:23+00:00
I think everyone here agrees that there's no reason to restrict yourselves to an older version of Rust at the current stage of development (although I don't quite understand the intention to use latest stable rather than the version you actually need).

The MSRV policy will become more important when people start using Cuprate in production. Then it might be reviewed.

## Boog900 | 2024-02-03T22:22:32+00:00
Yep, for now I agree with roughly tracking latest stable. We may need to revisit this in the future though.

# Action History
- Created by: hinto-janai | 2023-12-05T03:36:54+00:00
- Closed at: 2024-02-03T22:22:32+00:00
