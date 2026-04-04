---
title: ARM hash rate greatly reduced following latest pulls
source_url: https://github.com/monero-project/monero/issues/1069
author: ghost
assignees: []
labels: []
created_at: '2016-09-11T17:58:52+00:00'
updated_at: '2016-09-17T21:18:17+00:00'
type: issue
status: closed
closed_at: '2016-09-17T21:18:17+00:00'
---

# Original Description
Aloha!

Prior to the latest set of pulls, my little ARMv8 box was managing 8H/sec (dizzying, I know). However, now it can only do 2H/s.

@radfish Maybe something related to #1049?


# Discussion History
## iamsmooth | 2016-09-11T22:19:13+00:00
Is yours running in 64 bit? It is possible that the arm asm mul code (reenabled by #1049) is worse than what the compiler generates on 64 bit. If so the asm code should only be enabled on 32-bit arm, not all arm.


## ghost | 2016-09-11T23:29:51+00:00
Iiiinteresting - I am running on 64 bit...


## radfish | 2016-09-15T07:54:37+00:00
@NanoAkron.. could you please run an experiment for comaprison by invoking cmake with `-DNO_OPTIMIZED_MULTIPLY_ON_ARM=ON` and holding all else constant?


## ghost | 2016-09-15T14:54:23+00:00
Hi @radfish, so I did `cmake -DNO_OPTIMIZED_MULTIPLY_ON_ARM=ON` followed by `make` but the binary it produced crashed. Was this the right way to do what you were asking, or should I have done `make release`?


## radfish | 2016-09-16T02:09:42+00:00
Yes, just to make sure (assuming your slow-hash-rate build was from `make release`):

```
cd monero
mkdir build-no-asmmul && cd build-noasmmul
cmake -DNO_OPTIMIZED_MULTIPLY_ON_ARM=ON ..
make
./bin/monerod
```

Without the optimized asm code, the build should be the same as before #1049. If you successfully built and ran before #1049, then this crash you are getting now is probably unrelated. In any case, might be worth running with gdb to get a stack trace, to document this crash.


## ghost | 2016-09-16T12:23:08+00:00
Just an interim report - have pulled in #1077 which has doubled the hash rate from 2 to 4H/s...but this is still less than half the hash rate I was getting before #1049 :(

Will test properly later tonight.


## ghost | 2016-09-16T13:51:49+00:00
Have just tried with `cmake -DNO_OPTIMIZED_MULTIPLY_ON_ARM=ON ..` but sadly no change - hash rate still 4H/s

I wonder whether we need to change the compile flags in CMakeLists.txt now that @hyc has added the custom AES code. Will investigate later.


## hyc | 2016-09-16T16:06:54+00:00
Before my patch in master, ARMv8 was using the generic C code. After #1077 , ARMv8 uses the ARM-specific code. Also, the NO_OPTIMIZED_MULTIPLY_ON_ARM flag only affects ARMv7/ARMv6.


## ghost | 2016-09-16T18:32:46+00:00
:(


## hyc | 2016-09-16T19:17:40+00:00
eh? With #1077 The ARMv8 code always uses fast multiply.


## ghost | 2016-09-16T22:02:23+00:00
The sad face was because it makes my loss of hash power even more confusing.

Going to try to roll back to about #1041 and then just pull in #1077 to test it out


## ghost | 2016-09-17T14:02:13+00:00
Increasing the thread count does push the mining rate up above where it was before. I may have done something silly here, but I'm going to try adjusting gcc -mtune because I was running a fully customised version before.


## ghost | 2016-09-17T21:18:15+00:00
I'm going to close this. My has rate is now at 14/sec with the new ASM code and compiling with +crypto, was at 11-12 without +crypto. Have submitted #1088.


# Action History
- Created by: ghost | 2016-09-11T17:58:52+00:00
- Closed at: 2016-09-17T21:18:17+00:00
