---
title: ubuntu-xmrig-2.6.0-beta2 hash rejects for sumo
source_url: https://github.com/xmrig/xmrig/issues/551
author: josef2600
assignees: []
labels:
- bug
- arm
created_at: '2018-04-13T21:04:43+00:00'
updated_at: '2018-09-22T05:14:46+00:00'
type: issue
status: closed
closed_at: '2018-09-22T05:14:34+00:00'
---

# Original Description
hi, thanks for your great app.
since fork changed, your app doesn't work for Ubuntu 16.x.x  on arm64. i have few boards (nice boards!) and they worked before but now non of your versions work on them. all new versions work great on win32, but not on Ubuntu. i have worked on them for 2 weeks now, and no luck. can you please check what is wrong with them ?
i get rejects with low difficulty.

if needed:
Sumowallet! is my wallet.

sudo ./xmrig -a cryptonight-heavy -o sumopool.de:2222 -u Sumowallet! -t 4 -p x
and
sudo ./xmrig -a cryptonight-heavy -o sumo.aleajecta.com:4444 -u Sumowallet! -t 4 -p x

the pools and runner works perfectly on win10.
best regards, Josef.

# Discussion History
## xmrig | 2018-04-16T01:02:15+00:00
Looks like something broken for ARMv8 builds, in some cases it produce invalid hashes. For the record you don't see messages like `thread 0 error: "hash self-test failed"` when miner starts? Also what boards is they support hardware AES?. I will start investigate this bug later.
Thank you.

## auto-joe | 2018-04-16T20:11:34+00:00
In response to "what boards is they support hardware AES?"

I tried xmrig 2.6.0-beta2 on a pi3b (armv8) running bamarni/pi64 this week. Even though it supposedly supports hardware AES, I got the "illegal instruction" error when attempting to use a --av value of 0, 1 or 2. 

FWIW, cryptonight-heavy has been working fine for me on armv7

## josef2600 | 2018-04-17T22:36:48+00:00
thanks man for your answer. sorry for the delay.
my boards are "PINE64+ OS is Xenial Mate 16.0.4 x64"
http://wiki.pine64.org/index.php/PINE_A64_Main_Page
with crypto they work great. even now. but after fork changed, no sumo and no xmr.
and it doesn't report any error. just reject hashes for low difficulty.
aes is enable-4 treat is enable- (number of cores don't matter)- huge page available and enabled-
everything is green except hashes !!!
as i have told, on win32 they work perfect. and i decided to work on my PC win10x64 too. but i have a bit of problem there too! i have a win10 LTSB for my work, and it doesn't start working. i don't know why ! 
i have lot of soft in it "compilers for micro and visual studio 2017 and ..." and it always is up to date. xmr-stack work on it. but for some reasons i like to work with your program. for start , i don't know why (!) it work faster on CPU! but moor than that, i like your programming better. theirs i kind of eachi ! i dont like that. 
-------------------
and i have sent you a mail too !

thanks for your work.
best regards, Josef.


## xmrig | 2018-04-19T06:13:28+00:00
XMR should work fine, just don't ever touch `variant` option or set it to `-1` or `1`.
About SUMO, I localized location of the bug, it weird bug not all hashes bad, it reason of self test was successfully passed. In somokoin code a found [very dirty hack](https://github.com/sumoprojects/sumokoin/blob/master/src/crypto/cn_slow_hash_soft.cpp#L511) but it hack no work on ARMv8. Still trying to find solution.
Thank you.

## xmrig | 2018-04-19T13:36:22+00:00
I decided to postpone the fixes for ARM, you are right not only cn-heavy can work incorrectly. Don't like to delay v2.6.0-beta3, will fix ARM later, this issue is still high priority.

## josef2600 | 2018-04-20T22:02:21+00:00
thank you. i never touch variant. i know that ! it is for CPU modules and model.
ill be waiting. and want to tell each arm board gets over 14 has/sec if difficulty is under 700. if it gets higher , hash rate is less. i know why! and the CPU atom z3735 gets a hash rate of 25 h/s if difficulty is under 1000. if CPU gets hot, hash rate gets very low because freq gets low.

best regards, Josef.


## vlad230 | 2018-05-21T08:13:28+00:00
Has this been fixed? I'm getting the same issues when mining OMBRE (cn-heavy coin). I've tried the latest 2.6.2 build with different variant configs (-1, 0, 1) but it's still rejecting my shares.

## xmrig | 2018-06-02T19:59:31+00:00
Fixed, but now sumopool.de NOT support cn-heavy.
@vlad230 Did you change algo option? variant option ignored for cn-heavy this algorithm has no variants.

## xmrig | 2018-09-22T05:14:34+00:00
Should be fixed in v2.6.3+.

# Action History
- Created by: josef2600 | 2018-04-13T21:04:43+00:00
- Closed at: 2018-09-22T05:14:34+00:00
