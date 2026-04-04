---
title: Corrupted binaries built from Ubuntu 22.04
source_url: https://github.com/monero-project/monero/issues/9371
author: woodser
assignees:
- '0xFFFC0000'
labels:
- bug
- arm
- critical
- important
created_at: '2024-06-19T18:40:36+00:00'
updated_at: '2024-08-11T01:31:17+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Building the Monero binaries on Ubuntu 22.04 completes successfully but produces corrupted binaries, wherein at least the wallet files are incompatible and also multisig wallets are broken.

For example, by building on Ubuntu 22.04 ARM64 with the command `make depends target=aarch64-linux-gnu`, the build completes successfully, but multisig wallets will fail to import multisig info from the corrupted peer, with the error `Multisig info is for a different account`.

This led to an issue in which users were unable to recover their funds except by restoring from seed with good binaries.

The instructions indicate that only Ubuntu 18.04 and 20.04 are tested. To avoid loss of funds, I think the build should produce an error or at least a warning when building from Ubuntu >20.04, until later versions are officially tested.

# Discussion History
## hyc | 2024-06-20T17:29:25+00:00
I think it's sufficient to say that only 18.04 and 20.04 are supported. 22.04 is definitely broken; that was what prompted me to write the dockrun script since I could no longer get workable builds on my native 22.04 dev environment.

## selsta | 2024-06-20T19:00:16+00:00
@hyc it seems to be a more general issue, not necessarily gitian / depends related. Some changes between the compiler in ARM64 Ubuntu 20.04 and 22.04 causes serialization incompatabilies if I understand it right.

## 0xFFFC0000 | 2024-08-08T12:21:01+00:00
> Building the Monero binaries on Ubuntu 22.04 completes successfully but produces corrupted binaries, wherein at least the wallet files are incompatible and also multisig wallets are broken.
> 
> For example, by building on Ubuntu 22.04 ARM64 with the command `make depends target=aarch64-linux-gnu`, the build completes successfully, but multisig wallets will fail to import multisig info from the corrupted peer, with the error `Multisig info is for a different account`.
> 
> This led to an issue in which users were unable to recover their funds except by restoring from seed with good binaries.
> 
> The instructions indicate that only Ubuntu 18.04 and 20.04 are tested. To avoid loss of funds, I think the build should produce an error or at least a warning when building from Ubuntu >20.04, until later versions are officially tested.

I am looking into this and trying to reproduce it. In the mean time, any specific tests that I can run to reproduce the error? or the executable fails to run at all? 

## woodser | 2024-08-08T12:24:08+00:00
You should be able to save a wallet file from one binary and open in the other binary to observe an error and confirm they're not compatible.

## 0xFFFC0000 | 2024-08-08T12:25:09+00:00
> You should be able to save a wallet file from one binary and open in the other binary to observe an error and confirm they're not compatible.

Thanks. I will try it in my VM.

## 0xFFFC0000 | 2024-08-08T15:47:20+00:00
Ran the tests on ubuntu 22.04 x86, and no issues were detected. Trying arm64.

## 0xFFFC0000 | 2024-08-08T15:53:38+00:00
Thanks to @woodser running the tests under ARM64 we know these tests fail: 

```
The following tests FAILED:
	  6 - unit_tests (Subprocess aborted)
	 11 - hash-slow (Failed)
	 12 - hash-slow-1 (Failed)
	 13 - hash-slow-2 (Failed)
	 14 - hash-slow-4 (Failed)
```	 

## hyc | 2024-08-08T15:57:33+00:00
Just to be clear - you create a wallet using a binary built on Ubuntu 18.04, and try to open it using a wallet binary built on Ubuntu 22.04, correct? (And vice versa.)

## hyc | 2024-08-08T15:59:56+00:00
> @hyc it seems to be a more general issue, not necessarily gitian / depends related. Some changes between the compiler in ARM64 Ubuntu 20.04 and 22.04 causes serialization incompatabilies if I understand it right.

My point is that the only way to get a usable binary is to use Ubuntu 18 or 20, so I wrote dockrun to make it easy to have it built in the correct Ubuntu environment. It's not a problem with gitian or depends, it's merely that they're a known working system and Ubuntu 22 is known not to work.

## 0xFFFC0000 | 2024-08-08T16:02:43+00:00
> > @hyc it seems to be a more general issue, not necessarily gitian / depends related. Some changes between the compiler in ARM64 Ubuntu 20.04 and 22.04 causes serialization incompatabilies if I understand it right.
> 
> My point is that the only way to get a usable binary is to use Ubuntu 18 or 20, so I wrote dockrun to make it easy to have it built in the correct Ubuntu environment. It's not a problem with gitian or depends, it's merely that they're a known working system and Ubuntu 22 is known not to work.

@hyc Are you sure? because I tried with ubuntu 22.04 (x86_64) and was able to build `master` and pass the tests. Do you remember what was the exact error you saw? Maybe there are two different issues with ubuntu 22.04 here (one in arm64 and one in x86_64).

## hyc | 2024-08-08T16:24:31+00:00
Passing the tests is irrelevant since they don't test by writing a wallet file from one binary and reading it from a differently built binary.


## 0xFFFC0000 | 2024-08-09T02:56:16+00:00
After a private discussion with @hyc and @woodser ( and help from @nahuhh ), I am able to reproduce this issue. 

Cross-compiled binaries built from ubuntu 20.04 and ubuntu 22.04 are acting differently.

The `monero-wallet-cli` built in ubuntu 22.04 cannot open the wallet file created with `monero-wallet-cli` built in ubuntu 20.04.


Only aarch64 and x86 tested. The x86 wallets work without issue. 

## 0xFFFC0000 | 2024-08-09T17:33:37+00:00
Here is the latest information about the bug:

```
(a) the bug only happens on the armv8 platform. 
(b) bug only happens when (cross) building on newer platforms like Debian 11 or Ubuntu 22.04. 
(c) bug only occurs with the default release build. If I build with `-O0 -g3` we don't hit the bug. Which makes the debugging extremely hard. Since with default build `-Ofast`, the debugger does not have any info on most of the functions and no easy way of tracing the runtime.
```

If anybody has any suggestions, I appreciate it.

## 0xFFFC0000 | 2024-08-10T19:49:05+00:00
( Thanks to @tobtoht for finding the actual function bug happens ) 

If you add `__attribute__((optimize("O0"))` to the `cn_slow_hash` function at `src/crypto/slow-hash.c`, the bug does not happen. 

## 0xFFFC0000 | 2024-08-10T21:16:31+00:00
Here is a list of updates that we know about this bug. 

Only happens with `-O1 -fipa-ra -frerun-cse-after-loop` and will not happen with `-O1`. 

I generated both `tree-dump` and `rtl-dump` of the GCC for this compilation unit. `tree-dump` is the same, which is why the bug only happens in ARM 64. So the bug in GCC (mis-compilation) has to happen in the backend and instruction selection/backend side. 

I have gcc's `dump` and `rtl` log files here. In case anyone wants to look at it. I am talking to GCC devs to see what we can do about this.





## nahuhh | 2024-08-11T01:31:16+00:00
This is fixed in gcc 12.2+ (perhaps earlier - untested) 
debian 12 and ubuntu 24.04 ship >=12.2

# Action History
- Created by: woodser | 2024-06-19T18:40:36+00:00
