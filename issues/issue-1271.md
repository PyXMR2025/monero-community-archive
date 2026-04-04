---
title: Don't use Insecure Userland PRNG for random_scalar()
source_url: https://github.com/monero-project/monero/issues/1271
author: paragonie-scott
assignees: []
labels:
- enhancement
- important
created_at: '2016-10-29T01:30:02+00:00'
updated_at: '2023-04-28T14:08:11+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
### Problem

Instead of just directly using the Cryptographically Secure Pseudo-Random Number Generator provided by the operating system, a hash-based userland PRNG is being used instead.
### Offending Code
- https://github.com/monero-project/monero/blob/master/src/crypto/crypto.cpp#L83-L89
- https://github.com/monero-project/monero/blob/18e406a0e6c520d3772461bf271fe96247912986/src/crypto/random.c#L116-L142
### Consequences

Using a _userland_ PRNG instead of the kernel's CSPRNG is an antipattern (even if it's seeded by the OS). It doesn't create defense-in-depth against an insecure kernel CSPRNG.
- The security of your entire system depends on `/dev/urandom` being secure.
- A userland PRNG just creates additional points of failure.
- The Debian weak key bug affected a userspace PRNG, not the kernel's.
### Solution

See [How to Generate Secure Random Numbers in Various Programming Languages](https://paragonie.com/blog/2016/05/how-generate-secure-random-numbers-in-various-programming-languages).

This is certainly a security issue, but not one that I have an exploit for on-hand.


# Discussion History
## moneromooo-monero | 2016-10-29T10:23:31+00:00
I think that PRNG is the construct described by the authors of Keccak in "Sponge-based pseudo-random number generators", though I'm not 100% sure about it. Changing this to always ask /dev/urandom or getrandom is possible, but I'm a bit worried about what happens if the kernel runs out of entropy. Hopefully it can't get worse than using our own, but some of the code uses a lot of random numbers (eg, output selection rounds). I wonder if we could switch to kernel for key and related randomness, and keep on using the Keccak construct for the rest. Or would that be no problem ?

man 2 getrandom mentions such a case, though how much is too much isn't mentioned, and probably depends on how fast the kernel's entropy pool can replenish on that particular machine.


## fluffypony | 2016-10-29T10:34:09+00:00
Thanks for opening this issue, @paragonie-scott :)

@moneromooo-monero urandom (and the Windows `CryptGenRandom`) are non-blocking, so it's not possible to run out of entropy per se. /dev/random can "run out" of entropy, but since urandom is seeded from that (typically using a stream cipher) there's an unlimited amount of randomness that can be derived once /dev/random has enough entropy.

There are only three instances where /dev/random will lack entropy:
1. A newly installed system's very first boot
2. A VM cloned from an image, on its very first boot
3. A live CD/USB boot, assuming it's a fresh boot without persistence

These are alleviated within a couple of minutes at most, and I don't suspect we'll have too many people that will need to create a transaction that quickly in instances 1 and 2. Instance 3 is a possible scenario where it could occur, but seeing as how they'd still have to load things up and get ready to generate a transaction this also shouldn't be a concern.

For all other environments, the state of /dev/random (and the Windows equivalent) is saved to disk and loaded on reboot, so good PRNG entropy is available immediately.

If we're deeply concerned about the risks at first boot we can check system uptime and have a warning prompt on tx creation for the first, say, 5 minutes.


## moneromooo-monero | 2016-10-29T10:44:06+00:00
OK, that sounds fair enough. And looking at the libsodium source linked from the page above, it seems like a good idea to switch.


## anonimal | 2016-10-29T10:45:45+00:00
Well... kovri uses cryptopp. Shall we kill two birds with one stone (poor birdy)?


## moneromooo-monero | 2016-10-29T10:55:13+00:00
Do you have a link to its PRNG code ?


## fluffypony | 2016-10-29T10:55:34+00:00
@anonimal we use libsodium for crypto_ops_builder already, so either or?


## fluffypony | 2016-10-29T10:59:21+00:00
Also I have it on good authority that TweetNaCl is working towards formal verification of all of its functions, in which case it would be the preferable library for offloading crypto_ops_builder and some others, which would make cryptocpp a logical choice.


## anonimal | 2016-10-29T12:36:10+00:00
@moneromooo-monero at the [lowest level](https://www.cryptopp.com/docs/ref/osrng_8cpp_source.html)? [AutoSeededRandomPool](https://www.cryptopp.com/docs/ref/class_auto_seeded_random_pool.html) may be of more interest?


## paragonie-scott | 2016-10-29T21:52:30+00:00
You might want libsodium instead of TweetNaCl, for a lot of reasons beyond RNGs.
- TweetNaCl was an academic exercise based on NaCl, to compose an entire crypto library in the space of 100 tweets.
- Libsodium is focused on being a production-usable extension of what NaCl started. Some of its more useful features include:
  - `crypto_pwhash*`
  - `crypto_box_seal*`
  - `crypto_aead_chacha20poly1305_ietf*`
  - `sodium_memzero`
  - `sodium_bin2hex` and `sodium_hex2bin` (cache-timing-safe encoding)

TweetNaCl is good. Libsodium is good. Libsodium offers more. Both are intensely studied.


## fluffypony | 2016-10-30T09:42:36+00:00
@paragonie-scott excellent points! In my discussions with djb at Ei/PSI a couple of months ago he indicated a preference for TweetNaCl for projects where correctness and safety are most important, which is an influencer. Nonetheless, this will definitely require further evaluation:) Thank you for your assistance!

![scott-arciszewski](https://cloud.githubusercontent.com/assets/1944293/19835640/d77a7256-9e95-11e6-8674-6e27e93bd9ae.png)


## paragonie-scott | 2016-10-30T09:48:49+00:00
Sure thing. :)

Just want to add one more note: All CryptoNote-based currencies have likely inherited the exact same problem, since it originates upstream, and I've been led to believe that fixing it there won't lead to a trickle-down effect for everyone else.

Therefore, if any of the [other currencies on this list](https://en.wikipedia.org/wiki/CryptoNote#Current_CryptoNote_currencies) are still active, it may be a good idea to point them here too.


## paragonie-scott | 2016-10-30T10:03:05+00:00
I've pointed the projects that seem somewhat active towards here, after verifying that the same problem exists in their codebase. It's likely that I overlooked at least one.


## vtnerd | 2016-12-15T04:06:12+00:00
There was a discussion recently on Metzdowd about linux RNG. Kernel 3.17 added a new system call, `getrandom`, which by default only blocks if the kernel RNG has not been properly seeded.

## anonimal | 2017-01-24T16:59:12+00:00
https://github.com/monero-project/meta/issues/38 is a reminder that we *could* use OpenSSL's API. Furthermore, Tor is very active with their OpenSSL RNG implementation; I remember this changelog from their semi-recent 2.8.6 release:

```
  o Minor features (security, RNG):
    - Adjust Tor's use of OpenSSL's RNG APIs so that they absolutely,
      positively are not allowed to fail. Previously we depended on
      internal details of OpenSSL's behavior. Closes ticket 17686.
    - Never use the system entropy output directly for anything besides
      seeding the PRNG. When we want to generate important keys, instead
      of using system entropy directly, we now hash it with the PRNG
      stream. This may help resist certain attacks based on broken OS
      entropy implementations. Closes part of ticket 17694.
    - Use modern system calls (like getentropy() or getrandom()) to
      generate strong entropy on platforms that have them. Closes
      ticket 13696.
```

Reviewing their implementation and/or simply patching monero's is something to consider instead of waiting for a new library refactor (since we already have OpenSSL available). I'm not endorsing either-or, just dropping a message 😄 

## ghost | 2017-11-01T13:20:56+00:00
@moneromooo-monero Is this still a live issue with all the recent OpenSSL pulls and discussion re: CSPRNGs?

## paragonie-scott | 2017-11-01T14:07:08+00:00
I would ask Rich Salz (not tagging him directly in case he doesn't have the time/emotional bandwidth to read this thread right now) of the OpenSSL team for details, but https://github.com/openssl/openssl/issues/898

## iamsmooth | 2017-11-01T22:35:56+00:00
Tor's approach quoted by @anonimal above (not relying exclusively on one source) is similar to what the Bitcoin RNG module does, which we are exploring in #2731 

## dEBRUYNE-1 | 2018-01-08T12:43:47+00:00
+enhancement

## dEBRUYNE-1 | 2018-01-08T12:47:43+00:00
+important

## LouisLibre | 2023-04-25T23:07:40+00:00
I just did a review of the Bitcoin approach to this and they seem to harvest entropy from multiple sources of randomness as to not trust a single source ( In contrast to Monero approach of just trusting /dev/urandom ).

- [**GetOSRand**](https://github.com/bitcoin/bitcoin/blob/2cc43de69bdb995ac7faff4ed67caf773026ab29/src/random.cpp#L275) ( harvest entropy from /dev/urandom )
- [**GetRdRand**](https://github.com/bitcoin/bitcoin/blob/2cc43de69bdb995ac7faff4ed67caf773026ab29/src/random.cpp#L110) ( harvest from the hardware device if available / RDRAND asm instruction  )
- [**RandAddDynamicEnv**](https://github.com/bitcoin/bitcoin/blob/2cc43de69bdb995ac7faff4ed67caf773026ab29/src/randomenv.cpp#L226) ( computer env stuff like /proc/*, vmstat, meminfo, processes, disk stats, etc)
- [**RandAddStaticEnv**](https://github.com/bitcoin/bitcoin/blob/2cc43de69bdb995ac7faff4ed67caf773026ab29/src/randomenv.cpp#L307) (compile-time static properties)
- [**RandAddEvent**](https://github.com/bitcoin/bitcoin/blob/2cc43de69bdb995ac7faff4ed67caf773026ab29/src/random.cpp#L582) ( harvest entropy from [network events](https://github.com/bitcoin/bitcoin/blob/2cc43de69bdb995ac7faff4ed67caf773026ab29/src/net.cpp#L799) )
- [**SeedTimestamp**](https://github.com/bitcoin/bitcoin/blob/2cc43de69bdb995ac7faff4ed67caf773026ab29/src/random.cpp#L452) ( harvest from [hardware](https://github.com/bitcoin/bitcoin/blob/2cc43de69bdb995ac7faff4ed67caf773026ab29/src/random.cpp#L51) time stamp or fallback to os )

They combine all this sources of randomness on [seed initialization](https://github.com/bitcoin/bitcoin/blob/2cc43de69bdb995ac7faff4ed67caf773026ab29/src/random.cpp#L524) and also update it periodically.

# Action History
- Created by: paragonie-scott | 2016-10-29T01:30:02+00:00
