---
title: BUS_ADRALN on arm32
source_url: https://github.com/monero-project/monero/issues/3872
author: m2049r
assignees: []
labels: []
created_at: '2018-05-28T08:26:16+00:00'
updated_at: '2018-11-05T17:24:45+00:00'
type: issue
status: closed
closed_at: '2018-11-05T17:24:45+00:00'
---

# Original Description
On (some?) ```arm32``` Android devices https://github.com/monero-project/monero/blob/a2cef8cba44eb0badf330dc057856a24c2a39739/src/crypto/slow-hash.c#L90 throws a ```signal 7 (SIGBUS), code 1 (BUS_ADRALN)``` because https://github.com/monero-project/monero/blob/a2cef8cba44eb0badf330dc057856a24c2a39739/src/crypto/slow-hash.c#L74 is not aligned. Changing the ```NONCE_POINTER``` offset to 32 "works".
I understand that 35 is crucial to the CN variant, but letting code die doesn't seem to be right.

# Discussion History
## moneromooo-monero | 2018-05-28T10:09:36+00:00
There is a VARIANT1_PORTABLE_INIT macro which uses memcpy instead. You need to tweak the ifdefs so that it gets used for your particular target here (or, probably, for it to use the right cn_slow_hash version in that file).

## baryluk | 2018-06-12T20:27:53+00:00
Using an union with a second member being a struct with attribute((__packed__)) should help gcc and clang to generate memcpy for these loads. You can add an assert that the field offset is indeed 35. It should have no effect on x86. (to be verified)


## m2049r | 2018-06-15T15:09:10+00:00
@baryluk could you paste code to that effect? i would be happy to test & PR it.

## moneromooo-monero | 2018-11-04T22:58:54+00:00
Did you try to use the portable version on 32 bit arm then ?

## m2049r | 2018-11-05T17:24:45+00:00
no - mostly because i did not understand what it is i should try & did not find the time to find out. but... this error has not occurred in the past 60 days AFAICT. so closing.

if you could give me a further pointer i can investigate it.

# Action History
- Created by: m2049r | 2018-05-28T08:26:16+00:00
- Closed at: 2018-11-05T17:24:45+00:00
