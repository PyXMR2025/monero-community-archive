---
title: Boost portable binary serializer not working for Linux
source_url: https://github.com/monero-project/monero/issues/1511
author: kenshi84
assignees: []
labels: []
created_at: '2016-12-28T08:16:34+00:00'
updated_at: '2017-03-07T02:35:49+00:00'
type: issue
status: closed
closed_at: '2017-03-07T02:35:49+00:00'
---

# Original Description
When I was trying to use @moneroexamples's tx pusher, I realized that Boost's experimental portable binary serializer introduced in PR #1462 does not provide portability for Linux, see [Issue #19](https://github.com/moneroexamples/onion-monero-blockchain-explorer/issues/19). On the other hand, I confirmed that Cereal's portable binary serializer demonstrated in PR #1435 (which was not taken) provides binary portability for Windows, Mac and Linux as far as I tested.

Cereal is specialized in serialization with reasonably active developments and [testing](https://github.com/USCiLab/cereal/tree/master/unittests), while Boost's serialization is just one part of a big library and the unofficial portable serialization code is [quite old](http://www.boost.org/doc/libs/1_62_0/libs/serialization/example/portable_binary_iarchive.hpp) without decent testing. These points seem to justify the replacement of boost serializer with cereal. What do you think?


# Discussion History
## kenshi84 | 2016-12-29T11:03:48+00:00
I did some further experiments using my Mac (10.11.6) running Windows (10, 64bit) and Linux (Ubuntu 16.04.1 amd64) on a VM, and confirmed that the binary portability breaks only when letting Linux read any files created by Mac or Windows; i.e., Mac and Windows can read any files created in any platforms including Linux. So the problem seems to lie in the loading part.

I tried to find what's wrong with Boost's code while consulting with Cereal's code as a reference, but the task seemed a bit overwhelming to me:/

In any case, since the ability to save wallets in a portable and reliable manner seems quite crucial (i.e., in the worst case users may lose all the detailed information about their past transactions), I guess we should do some extensive testing before adopting changes.

## ghost | 2016-12-29T13:38:59+00:00
Have you considered submitting this to the boost team to see what they say?

## moneromooo-monero | 2016-12-29T17:13:57+00:00
Hmm. That sucks. It means we broke compatibility to release GUI binaries with broken formats :/

Make a test case for each type, starting with simple things (int, uint32_t, uint64_t), then going into strings, vectors, etc. Till you find one that breaks. Then we can look at that one.


## vtnerd | 2016-12-30T07:47:50+00:00
I think finding the issue in boost code would be preferable. Otherwise, code not understood by the team is being merged into the project.

I did see some undefined behavior in the code that I wanted to fix in the previous PR, but I didn't expect issues unless the value exceeded `numeric_limit<intmax_t>::max()` and the platform was _not_ 2's complement (rare). Are any floating point values serialized?

Also, AFAIK, only specific sized types (`std::uint32_t`, etc.) can be used with the Cereal portable binary format. Cereal never writes the length of integers, as boost does, which is critical because if `unsigned` is used internally then `sizeof(unsigned)` can vary across platforms. Although, this is also rare unless running on some embedded device. I recall seeing platform dependent types in several places, but perhaps they were avoided in these code paths ... ?

## moneromooo-monero | 2016-12-30T10:16:10+00:00
AFAIK, no floating point are being serialized. There might be some size_t.

## kenshi84 | 2016-12-30T10:21:55+00:00
@NanoAkron 
No, I wanted to make sure if it's really a bug before submitting a bug report. And looks like it's not the case.

@moneromooo-monero @vtnerd 
Thanks a lot for your advice! Embarrassingly enough, I realized that the error was not due to a bug, but rather it's an [intended behavior](http://www.boost.org/doc/libs/1_62_0/libs/serialization/doc/exceptions.html#unsupported_version); the Boost archives throw `unsupported_format` exception when trying to read a serialized file whose recorded archive version is newer than that of the current build. Please see PR #1515.


## vtnerd | 2016-12-30T17:42:34+00:00
I would have to look again, but I think the entire serialization format is controlled by the code within our codebase. If true, the serialization and check of the version can be replaced with something of our choosing. I _think_ it would then be possible for us to read/write across various boost versions since boost is just providing some of the boilerplate. A test containing the binary output could then be written - it could verify on that platform and boost version that its writing exactly as expected.

## kenshi84 | 2016-12-31T04:51:03+00:00
Should I close this ticket, or leave it?

## moneromooo-monero | 2016-12-31T10:28:03+00:00
I suggest making a number of tests first, saving a complex wallet cache on various archs/OSes and loadin git back on another.

## kenshi84 | 2017-01-01T03:51:37+00:00
@moneromooo-monero Should new tests be added to tests/unit_tests/serialization.cpp? And should example wallet files be added to tests/data?

## moneromooo-monero | 2017-01-01T12:54:03+00:00
Known good data which must be read properly seem like a good test indeed.
Writing and comparing seems more fraught, as there might be minute differences (ie, timestamps), but might also be worth doing.

## xmrdog | 2017-01-01T14:40:25+00:00
I had this problem too. Transferred unsigned transaction file from macOS (Sierra 10.12.2) to Linux (Ubuntu 16.04 LTS). Was not readable on the Linux machine.

## moneroexamples | 2017-01-01T21:50:46+00:00
@xmrdog 
>Transferred unsigned transaction

Writing and reading of unsigned and signed txs, seems to be fixed by those to PR:

- https://github.com/monero-project/monero/pull/1515
- https://github.com/monero-project/monero/pull/1507

If you want to can try applying these two patches to your monero on your os and linux, and test again. 


## kenshi84 | 2017-03-07T02:35:49+00:00
Forgot to close:)

# Action History
- Created by: kenshi84 | 2016-12-28T08:16:34+00:00
- Closed at: 2017-03-07T02:35:49+00:00
