---
title: Xmrig termux crash
source_url: https://github.com/xmrig/xmrig/issues/2226
author: arunAK47AK
assignees: []
labels: []
created_at: '2021-04-01T17:43:25+00:00'
updated_at: '2023-03-27T15:57:12+00:00'
type: issue
status: closed
closed_at: '2021-04-12T13:38:43+00:00'
---

# Original Description

My cpu cortex a-53 all settings fine , start mining termux closed


# Discussion History
## Spudz76 | 2021-04-01T19:28:28+00:00
`gcc -v` should say target aarch64, if not then you have 32-bit compiler which doesn't work.

Many OS have 64-bit kernel but 32-bit compiler included.  Both must be 64-bit (aarch64).

## arunAK47AK | 2021-04-01T19:33:59+00:00
Give any ideas for mining with Android mobile

## Spudz76 | 2021-04-01T20:42:33+00:00
Use cross-compile toolchain from Android SDK (matching your device Android revision) to build executable on normal Intel/AMD computer targeted for aarch64

Copy executable with ADB, or use Android SDK to build APK file, crossload.

## snipeTR | 2021-04-08T21:18:07+00:00
It is an extremely difficult affair to work on every android phone. and if you don't have tens of thousands of phones, you won't get any significant value.

## arunAK47AK | 2021-04-09T06:27:29+00:00
Ohh yes 🙂 in xmrfast pool shows my phone  has power 40 to 50  h/s 🙄🤔 few years take minimum withdraw 

## Spudz76 | 2021-04-10T01:38:01+00:00
It might be good enough at other algos, CN-Lite or something.

## afl45 | 2023-03-27T15:57:12+00:00
hi, i join this chat because i want learn xmrig on my honor 10 lite phone android, i know don't get a reward for a very long time but it's just for educational purposes. i lunch ./xmrig on termux but after 30 seconds, termux crash. can i have help on my problem ? i can't understand the bug report related to this incident.
[dumpstate_log.txt](https://github.com/xmrig/xmrig/files/11080644/dumpstate_log.txt)


# Action History
- Created by: arunAK47AK | 2021-04-01T17:43:25+00:00
- Closed at: 2021-04-12T13:38:43+00:00
