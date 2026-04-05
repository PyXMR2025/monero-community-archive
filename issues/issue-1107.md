---
title: Argon2id support for trtl
source_url: https://github.com/xmrig/xmrig/issues/1107
author: ibrahimk157
assignees:
- xmrig
labels:
- enhancement
- algo
created_at: '2019-08-08T08:37:19+00:00'
updated_at: '2019-08-31T03:05:40+00:00'
type: issue
status: closed
closed_at: '2019-08-31T03:05:40+00:00'
---

# Original Description
Hello,

I’m not sure if someone has already opened up an issue about this (I don’t see myself trying to look for such a post). 

Is argon2id support being worked on? I want the official xmrig to support it, I don’t want to use any forks.

Thanks

# Discussion History
## bobbieltd | 2019-08-08T11:49:02+00:00
+1 For both Argon2id Turtlecoin Chukwa and Chukwa variant WRKZ (Chukwa lite, currently ~ 2Mh/s nethash)

## xmrig | 2019-08-08T18:44:53+00:00
I'm not sure, new algorithm is not cryptonight variant and not RandomX variant.
Thank you.

## brandonlehmann | 2019-08-12T13:22:37+00:00
Here's where we've added support, although I'm sure there is a better way, in the TurtleCoin fork of xmrig: https://github.com/turtlecoin/trtlrig/commit/76ae2e503dfc7596519ed7528d11576d5494d435

## xmrig | 2019-08-12T15:17:03+00:00
Any test pool available for it? with testnet wallet address (if required).
Thank you.

## ibrahimk157 | 2019-08-12T18:44:03+00:00
brandonlehmann I’m trying to avoid using a fork for several reasons:
1) More likely to be abandoned compared to using the real deal
2) Might have reduced performance 
3) Might be less secure 

## ibrahimk157 | 2019-08-12T18:46:00+00:00
xmrig i heard they’ve got a argon2id test in the dev branch of the turtlecoin repo. (To see how your setup might perform with the new algo). Maybe try seeing what pool they’re using there?

## fadatsai | 2019-08-13T10:49:30+00:00
testnet
publicnode.ydns.eu:3420
 wallet address
TRTLuyJXVc9Ma7ffSaYQAGbkwf2LY2g8gHr2RdYDYiqyFrUtACmATLJGrs1pgd6mudft6uUMwdm2zWMo74P9bWKh6zjKFufhvGE


## xmrig | 2019-08-13T18:02:51+00:00
@fadatsai `[publicnode.ydns.eu:3420] error: "invalid address used for login", code: -1`.

## xmrig | 2019-08-14T18:09:17+00:00
Scheduled for v3.1 (next minor release), algorithm name will be `argon2/chukwa`, I still have bad feelings about it, many coins want own miners and Turtlecoin is not exception, but I got a lot of requests for support it, so lets add second non-cryptonight algorithms family.

## ibrahimk157 | 2019-08-14T18:43:50+00:00
Thank you so much! I wanted this badly and you added support for it at an extremely fast rate! I really cannot thank you enough ❤️

## bobbieltd | 2019-08-14T21:07:26+00:00
Cool 👍👍👍. Thanks. xmrig number one !

## L1LjSHX | 2019-08-17T10:55:25+00:00
Thanks :3

## xmrig | 2019-08-17T13:19:43+00:00
Argon2 ready in dev branches for CPU miner and proxy, I will make release in 1 or 2 days.

### Notes
* Algorithm names: `argon2/chukwa` and `argon2/wrkz`.
* Config file is compatible with v3.0, miner will add new CPU profile with name `argon2`.
* Auto-configuration usually will use all available threads, because of small memory requirements of selected algorithm params.
* Algorithm switch on fork will work only if pool support algorithm negotiation, so if you not use https://turtle.hashvault.pro/en/ please contact to your pool support.

## bobbieltd | 2019-08-17T15:51:16+00:00
Ohhhhhh yeahhhhhh ! Thanks xmrig 👍👍👍

## xmrig | 2019-08-18T20:30:00+00:00
https://github.com/xmrig/xmrig/releases/tag/v3.1.0
https://github.com/xmrig/xmrig-proxy/releases/tag/v3.1.0

## ibrahimk157 | 2019-08-19T12:08:37+00:00
YESSSSS!!!!! THANK YOU SOOOO MUCH!!!!

# Action History
- Created by: ibrahimk157 | 2019-08-08T08:37:19+00:00
- Closed at: 2019-08-31T03:05:40+00:00
