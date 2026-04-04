---
title: Restoring multisig wallet fails
source_url: https://github.com/monero-project/monero/issues/8537
author: tmoravec
assignees: []
labels:
- important
created_at: '2022-08-25T16:12:21+00:00'
updated_at: '2022-09-15T05:34:33+00:00'
type: issue
status: closed
closed_at: '2022-09-15T05:34:33+00:00'
---

# Original Description
Steps to reproduce:

1. Generate 2/3 multisig wallet (the M and N are presumably irrelevant).
2. In the CLI wallet, run `seed` or `encrypted_seed` with no passphrase. Save the seed.
3. Run the CLI wallet with `--restore-multisig-wallet`.
4. Enter the seed from step 2.
5. Observe an error: `Error: failed to generate new wallet: invalid multisig seed`

If we use `encrypted_seed` with some passphrase, the CLI wallet segfaults on step 5 instead of showing an error.

Happens with both v0.17.3.2 and v0.18.1.0.

# Discussion History
## tmoravec | 2022-08-25T19:31:00+00:00
Here's the specific failure: 

    ERROR   wallet.wallet2  src/wallet/wallet2.cpp:4749     !(rct::rct2sk(skey) == spend_secret_key). THROW EXCEPTION: error::invalid_multisig_seed

## arnuschky | 2022-08-29T15:30:34+00:00
I can confirm this. Also tested with 0.18.1.0, same result for all 3 participants (threshold 2).
Can also replicate the segfault on passphrase entry.

## binaryFate | 2022-08-29T16:43:23+00:00
Marking as important. If confirmed, this can lead to loss of fund.

## tmoravec | 2022-08-29T17:58:27+00:00
It works with v0.17.2.0. So the process in the description is correct and this is indeed a regression.

## arnuschky | 2022-08-30T21:45:29+00:00
@UkoeHB any idea where this might come from?

## UkoeHB | 2022-08-30T22:19:39+00:00
I don't know, I don't recall any of the multisig PRs touching wallet restores.

## tmoravec | 2022-08-31T06:26:53+00:00
@UkoeHB It's been broken since `v0.17.3.X`. It's probably not related to all the recent multisig work.

## UkoeHB | 2022-08-31T14:10:03+00:00
@tmoravec could you guys try a git bisect to isolate the culprit commit?

## tmoravec | 2022-08-31T19:06:02+00:00
@UkoeHB I'm trying the bisect.

In the process I've noticed that there are TWO problems:

* Wallets created with *v0.17.2.0* can be restored up until (including) v0.17.3.2.
* Wallets created with *v0.17.3.2* cannot be restored with the same version or newer.

Looks like there's something fishy with generating the seed as well, and this issue was introduced somewhere in v0.17.3 line. Restoring older seeds was broken in v0.18.0.0.

I'm focusing on the first problem - restoring a seed generated with *v0.17.2.0* now.

## tmoravec | 2022-08-31T19:21:25+00:00
@UkoeHB Bisecting is not quite straightforward because of the dependencies. Would you advise how to proceed, please?

```
monero $ make -j4 debug
mkdir -p build/"Linux/_no_branch,_bisect_started_on_b6a029f22_"/debug
cd build/"Linux/_no_branch,_bisect_started_on_b6a029f22_"/debug && cmake -D CMAKE_BUILD_TYPE=Debug ../../../..
CMake Deprecation Warning at CMakeLists.txt:46 (cmake_minimum_required):
  Compatibility with CMake < 2.8.12 will be removed from a future version of
  CMake.

  Update the VERSION argument <min> value or use a ...<max> suffix to tell
  CMake that the project does not need compatibility with older versions.


-- CMake version 3.22.1
-- Found usable ccache: /usr/bin/ccache
-- Building without build tag
-- Checking submodules
CMake Error at CMakeLists.txt:203 (message):
  Submodule 'external/miniupnp' is not up-to-date.  Please update all
  submodules with

  git submodule update --init --force

  or run cmake with -DMANUAL_SUBMODULES=1

Call Stack (most recent call first):
  CMakeLists.txt:208 (check_submodule)


-- Configuring incomplete, errors occurred!
See also "/home/tadeas/monero/build/Linux/_no_branch,_bisect_started_on_b6a029f22_/debug/CMakeFiles/CMakeOutput.log".
make: *** [Makefile:55: cmake-debug] Error 1
monero $   git submodule update --init --force
fatal: remote error: upload-pack: not our ref 4c700e09526a7d546394e85628c57e9490feefa0
fatal: Fetched in submodule path 'external/miniupnp', but it did not contain 4c700e09526a7d546394e85628c57e9490feefa0. Direct fetching of that commit failed.
fatal:
```

## j-berman | 2022-09-01T02:27:53+00:00
The culprit commit is b0f97dd75e6321b5615c21a7aa651c387de81b43

The `invalid multisig seed` error is from this line: https://github.com/monero-project/monero/blob/5256fdd7a155f7543bd710e991d5dd407981b35a/src/wallet/wallet2.cpp#L4753

## UkoeHB | 2022-09-01T04:05:18+00:00
@tmoravec I always run these commands when switching to a branch with a different set of submodules (or in the case of git bisect an older commit):

```
git submodule sync
git submodule update --init --recursive
git submodule update --init --force
```

@j-berman what test case fails on [this commit](https://github.com/monero-project/monero/commit/b0f97dd75e6321b5615c21a7aa651c387de81b43) but succeeds on the previous commit? Is it: A) `make`, B) create multisig wallet seed, C) try to restore the multisig wallet seed?

Can you test: A) v0.17.2.0 create multisig wallet seed, B) git bisect on restoring seed?

## UkoeHB | 2022-09-01T04:13:59+00:00
Ok I remember what changed: multisig accounts no longer store a sum of multisig keyshares in the `spend_secret_key` slot. Instead it is the 'base multisig privkey', which is the private key used to sign key exchange messages post-update (and for the first step of key exchange both pre and post update). This explains why new multisig wallets are throwing an error (can be fixed by just deleting lines 4750-4754; there is no verification step like this for post-update spend secret keys).

It doesn't explain why old wallets are erroring.

## j-berman | 2022-09-01T08:39:52+00:00
Restoring a v0.17.2.0 seed via v0.18.1.0 fails with [`"failed to generate new mutlisig wallet"`](https://github.com/monero-project/monero/blob/5256fdd7a155f7543bd710e991d5dd407981b35a/src/simplewallet/simplewallet.cpp#L5097-L5101) because `m_multisig_rounds_passed` is 0 here:

https://github.com/monero-project/monero/blob/5256fdd7a155f7543bd710e991d5dd407981b35a/src/wallet/wallet2.cpp#L5214-L5215

It seems when restoring a multisig seed, the seed should already be assumed finalized (because [it was finalized when exported](https://github.com/monero-project/monero/blob/5256fdd7a155f7543bd710e991d5dd407981b35a/src/wallet/wallet2.cpp#L1407-L1416)), so perhaps we can just set `m_multisig_rounds_passed` to the required amount when restoring, or not do that check in that case?

____

On this:

> This explains why new multisig wallets are throwing an error (can be fixed by just deleting lines 4750-4754; there is no verification step like this for post-update spend secret keys).

This makes sense. After deleting those lines, I'm now running into the above `"failed to generate new mutlisig wallet"` error.

Also given that explanation, seems worth highlighting that [generating from multisig keys](https://github.com/monero-project/monero/blob/5256fdd7a155f7543bd710e991d5dd407981b35a/src/simplewallet/simplewallet.cpp#L4489-L4492) looks like it could use some testing.

___ 

I could repro the segfault when trying to restore an encrypted seed using v0.17.2.0 -> v0.17.2.0, so it seems that's a bug that's been there a while. Haven't checked earlier versions.

## UkoeHB | 2022-09-01T18:02:37+00:00
@j-berman ok, after [this line](https://github.com/monero-project/monero/blob/5256fdd7a155f7543bd710e991d5dd407981b35a/src/wallet/wallet2.cpp#L4764) you can add:

```
m_multisig_rounds_passed = multisig::multisig_kex_rounds_required(m_multisig_signers.size(), m_multisig_threshold) + 1;
```

If restoring from 'multisig keys', presumably the wallet is fully set-up, so it's fine to set the rounds passed here. Also, I would replace that line with a new function `multisig::multisig_setup_rounds_required(num signers, threshold)` and sub that in wherever we are doing `multisig_kex_rounds_required() + 1`.

[These lines](https://github.com/monero-project/monero/blob/5256fdd7a155f7543bd710e991d5dd407981b35a/src/simplewallet/simplewallet.cpp#L4489-L4492) you linked seem to be for merging multisig wallets into a normal wallet, which should work.

# Action History
- Created by: tmoravec | 2022-08-25T16:12:21+00:00
- Closed at: 2022-09-15T05:34:33+00:00
