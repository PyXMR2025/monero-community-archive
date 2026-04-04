---
title: Integer overflow errors detected via Libfuzzer
source_url: https://github.com/monero-project/monero/issues/8121
author: swirsz
assignees: []
labels: []
created_at: '2021-12-23T05:17:28+00:00'
updated_at: '2022-02-18T22:53:15+00:00'
type: issue
status: closed
closed_at: '2022-02-18T22:53:15+00:00'
---

# Original Description
Numerous integer overflow errors detected via Libfuzzer & UndefinedBehaviorSanitizer.

./levin_fuzz_tests crash-c67

[crash-c67.txt](https://github.com/monero-project/monero/files/7766825/crash-c67.txt)

/src/monero/monero/external/easylogging++/easylogging++.cc:1594:58: runtime error: unsigned integer overflow: 18446744073709551615 + 1 cannot be represented in type 'unsigned long'
SUMMARY: UndefinedBehaviorSanitizer

/src/monero/monero/external/easylogging++/easylogging++.cc:1028:51: runtime error: unsigned integer overflow: 18446744073709551615 + 1 cannot be represented in type 'unsigned long'
SUMMARY: UndefinedBehaviorSanitizer 

/src/monero/boost_1_70_0/boost/uuid/uuid.hpp:184:73: runtime error: unsigned integer overflow: 17965778217539249913 + 4249519275351714093 cannot be represented in type 'unsigned long'
SUMMARY: UndefinedBehaviorSanitizer

/src/monero/boost_1_70_0/boost/unordered/detail/implementation.hpp:2626:22: runtime error: unsigned integer overflow: 4539525571228644494 + 17869460496119604336 cannot be represented in type 'unsigned long'
SUMMARY: UndefinedBehaviorSanitizer

/src/monero/boost_1_70_0/boost/unordered/detail/implementation.hpp:2626:36: runtime error: unsigned integer overflow: 3962241993638697214 + 18420413664540790272 cannot be represented in type 'unsigned long'
SUMMARY: UndefinedBehaviorSanitizer

/src/monero/boost_1_70_0/boost/unordered/detail/implementation.hpp:2628:22: runtime error: unsigned integer overflow: 3936129337794930765 + 15744517351179723060 cannot be represented in type 'unsigned long'
SUMMARY: UndefinedBehaviorSanitizer


# Discussion History
## moneromooo-monero | 2021-12-23T09:44:10+00:00
The first two seem OK to me. Unsigned overflow is well defined AFAIK, and while the code is a bit... clever... it seems OK: The first loop check will add 1 to ff...ff, going 0, so it starts looking at the start of the string. Now if size_t were to be signed, this'd break, but size_t is supposed to be unsigned (there's ssize_t for signed). Maybe I'm missing the point and the UB is not what I'm looking at ?

Probably still worth changing since I'm not sure npos is mandated to be ffff.ffff, which would break this code.

The rest should be reported to boost in case they're actual bugs.

## moneromooo-monero | 2021-12-23T09:48:41+00:00
Actually npos is mandated to be -1 (as unsigned), or so claims cppreference.com, which is usually good) so the code looks fine to me, so I'll need some hint to point out what is actually going on that's UB.
Thanks


## hyc | 2021-12-23T09:57:56+00:00
Yes, unsigned integer overflow is well defined. UBsan is wrong.

## selsta | 2022-02-18T22:53:15+00:00
Closing this as there isn't anything to do as far as I can see.

# Action History
- Created by: swirsz | 2021-12-23T05:17:28+00:00
- Closed at: 2022-02-18T22:53:15+00:00
