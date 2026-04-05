---
title: Android (ARM) Support
source_url: https://github.com/xmrig/xmrig/issues/669
author: iranagame
assignees: []
labels:
- arm
created_at: '2018-05-30T23:05:36+00:00'
updated_at: '2019-08-02T13:14:15+00:00'
type: issue
status: closed
closed_at: '2019-08-02T13:14:15+00:00'
---

# Original Description
Any news for android (arm) support? It's shame that MinerGate providing complete android support but XMRIG with 1M users not!

# Discussion History
## L1LjSHX | 2018-05-31T15:44:00+00:00
u can try build with termux.

## iranagame | 2018-05-31T20:26:30+00:00
@qusstem There is a problem on ARMv7 via termux AFAIK, if termux get working then, we can also compile it with NDK for sure.
@xmrig Any ideas!?

## L1LjSHX | 2018-05-31T20:36:03+00:00
now i'm build in termux xmrig and it work

## iranagame | 2018-05-31T20:49:59+00:00
@qusstem May I know your xmrig version and your device spec?

## L1LjSHX | 2018-06-02T12:38:59+00:00
htc m8 arm7l 

## iranagame | 2018-06-04T12:49:43+00:00
I'm fully port it into an Android App (will add the source & repo once it completed) through NDK, works great on arm64-v8 but on arm7 got bus error!
Trying to fix that... 

## mssc89 | 2018-08-11T19:06:25+00:00
Another solution is to install app "Linux deploy" from play store, create XUbuntu ARM64 container, connect thru ssh/vnc, and simply build xmrig from git. Works like a charm, achieving around 60-70h/s on all 8 cores of my galaxy s8.

# Action History
- Created by: iranagame | 2018-05-30T23:05:36+00:00
- Closed at: 2019-08-02T13:14:15+00:00
