---
title: Rust CryptoNight
source_url: https://github.com/Cuprate/cuprate/issues/28
author: Boog900
assignees:
- dimalinux
labels:
- C-feature
- E-medium
- E-help-wanted
created_at: '2023-09-05T11:08:49+00:00'
updated_at: '2024-10-08T15:03:58+00:00'
type: issue
status: closed
closed_at: '2024-10-08T15:03:58+00:00'
---

# Original Description
Currently the `cryptonight` crate is the only crate in this repo that is not a Rust re-write and is instead bindings to the c impl, I would prefer to use a fully Rust impl.

# Discussion History
## vorot93 | 2023-09-05T15:11:42+00:00
I suggest skipping CryptoNight (e.g. using preverified lists of hashes) altogether as it's not used in Monero network today.

## Boog900 | 2023-09-05T15:48:12+00:00
We could do that but we would also have to account for every network as well as potential future ones (mainnet, testnet, stagenet) so I would rather have to use bindings than just skip it.

That is also the reason why I haven't prioritized a Rust impl (it's not used on current Monero).

## dan-da | 2023-09-05T17:08:20+00:00
I took a quick look at the cryptonight c source code in this repo.

It seems like porting all that directly from C to rust would be a significant amount of work.

otoh, there exist rust crates for several of the crypto primitives such as aes, blake, groestl, etc.  If we are able to use these, that would seem a faster path.  Is that what you have in mind?

anyway, I might be able to help out with this.



## dan-da | 2023-09-05T17:13:51+00:00
Another possibility might be to use [c2rust](https://c2rust.com/) to transpile the C code into unsafe rust, as a starting point.

## Boog900 | 2023-09-05T17:28:13+00:00
Yeah I should have been more clear, I was thinking of using those crates and not doing a total re-write.

Although interesting, IMO I don't think that c2rust transpiler will be very helpful. I think a clean start would be beter instead of a line-for-line re-write. 

I would very much appreciate you working on this if you are able to :) There are a few Rust CryptoNight impls but none of them that have much, if any, use and some even say there are known bugs but don't actually say what the bugs are, you may find them useful as example though.

Edit: and none of the Rust impls support all variants of CryptoNight that Monero uses 

## dan-da | 2023-09-07T18:31:05+00:00
Ok, I took a quick look and found these crates: cryptonight, cryptonight-rs, yellowsun, and cryptonight-hash.

Of these, my initial take is that [cryptonight-hash](https://github.com/bertptrs/cryptonight-hash) could provide the best starting point.  They offer a comparison with the other crates:

> There are already different crates that also implement this digest algorithm, but there are some differences. In decreasing order of downloads (as of 2019-10-25):
> 
> * cryptonight-rs simply wraps the function from the original Monero C code. It also claims to be unstable.
> * yellowsun implements the digest completely in Rust but does so in a way that requires using AES CPU extensions. If your platform doesn't have those, you can't use it.
> * cryptonight requires SSE (but not AES) extensions for the hash. It indirectly depends on some C-code to implement the secondary hashes.
>
> Aside from the differences above, this crate is the only one that can easily compute hashes incrementally and that can operate with the traits in the digest crate.

I like that cryptonight-hash is fully rust and offers fallback impl if SSE or AES not available.

@Boog900 I presume you've looked at cryptonight-hash.   Can you expand on what it is lacking or you don't like about it?    Presumably it does not support all variations, do you know which it is lacking, or that's an area for me to research?    ;-)

## Boog900 | 2023-09-07T19:27:55+00:00
Yeah a couple things I don't like about that crate: it hasn't been updated in a while, it has had very little (if any) usage and you can't actually use it as it depends on a yanked crate. 

Also it only implements one variant of CryptoNight, from standard 8, I think this is the initial Monero variant but am not 100% so it's missing v1,2 and R 



## dan-da | 2023-09-08T01:54:39+00:00
That is helpful, thx.

Ok, I took a look at cryptonight-hash code.   You are correct they only impl one version, called Cryptonight version 0 [here](https://github.com/bertptrs/cryptonight-hash/blob/5ee91ac2d2d216d17b4b741b86c810d99e453ee2/src/lib.rs#L49).

So it seems to me that the shortest path could be to fork cryptonight-hash, fix the slice-cast (yanked) dep then impl the missing variants using the C++ code as a guide.

Does that approach sound reasonable to you?






## Boog900 | 2023-09-08T13:25:20+00:00
If im honest I would rather a fresh start, that crate does a few things I don't like the look of, like using a lot of unsafe Rust. It may still be useful as an example though.

one of the comments even say:
`This is pretty much rustified C-code.`

Here is the link to the CryptoNight standard: https://web.archive.org/web/20190911221902/https://cryptonote.org/cns/cns008.txt 

Although starting from scratch will be more effort and I don't want to push a load of work on someone trying to help out I do feel in the long run starting from scratch will be better.

If you have Matrix it may be worth communicating on there: @Boog900:monero.social


## dan-da | 2023-09-08T17:28:44+00:00
Ok, that's fair.   Yeah I wasn't aware of all the unsafe until I started trying to get it to build last night.  Which I finally succeeded and it passes tests with aesni feature disabled, but segvs when enabled.  Unfortunately one of the 2 yanked crates is no longer even on github.  I don't plan to proceed any further with that.  Code that builds is [here](https://github.com/dan-da/cryptonight-hash).

Well I can probably take a crack at a from-scratch impl.  might get in over my head, we'll see.

don't have matrix.   will see about setting it up later.

## detherminal | 2024-04-05T23:55:52+00:00
For anybody looking this at the future time, [I have implemented](https://github.com/monumexyz/libmonero/blob/main/src/crypt/cryptonight/slow_hash.rs) the CryptoNight algorithm pure-Rust based on the [original whitepaper](https://web.archive.org/web/20190911221902/https://cryptonote.org/cns/cns008.txt). The problem is, Monero doesn't use the exact same algorithm as the original paper described. If you want to start working on this, checking the code might help you.

## Boog900 | 2024-04-06T17:41:14+00:00
@detherminal I am pretty sure this line is UB as you are casting a pointer from a potentially unaligned u8 array to a u64 which has a higher alignment requirement: https://github.com/monumexyz/libmonero/blob/main/src/crypt/cryptonight/slow_hash.rs#L116

## detherminal | 2024-04-06T17:56:04+00:00
Yeah, there may be problems because of the unsafe code but I don't want to work on it anymore 😄. With the test inputs of the whitepaper, we can be sure that it works successfull as it gives the same output as the whitepaper.

## Boog900 | 2024-04-06T18:59:30+00:00
> we can be sure that it works successfull as it gives the same output as the whitepaper

With UB successful runs are possible, but the behavior is not guaranteed, which means it could stop working arbitrarily. 

## dimalinux | 2024-09-05T05:02:00+00:00
Can this issue be assigned to me? I have a version that is fully working and didn't require the use of unsafe at all (except maybe in certain trusted libraries that it uses like RustCrypto).
https://github.com/dimalinux/cuprate/tree/dimalinux/cryptonote

I still have some documentation, cleanups and additional tests to add before creating the PR. I'll also remove the C code completely. Right now my branch has lots of changes to the C code to make porting and generating test cases over smaller subsets of the code easier. Just ignore those changes if you take a peek at the code before I create the PR.

@vorot93 What you wrote about the CryptoNote hash not being used anymore is mostly true, but not 100% true. If you have a password on a pre-Polyseed mnemonic phrase, version 0 of the hash is used as part of the algorithm to generate the private key.

# Action History
- Created by: Boog900 | 2023-09-05T11:08:49+00:00
- Closed at: 2024-10-08T15:03:58+00:00
