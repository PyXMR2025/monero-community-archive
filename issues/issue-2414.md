---
title: 'About ./xmrig: 2: Syntax error: "(" unexpected'
source_url: https://github.com/xmrig/xmrig/issues/2414
author: sabaren2010
assignees: []
labels: []
created_at: '2021-05-29T07:20:40+00:00'
updated_at: '2021-05-31T17:05:23+00:00'
type: issue
status: closed
closed_at: '2021-05-31T17:05:23+00:00'
---

# Original Description
Hi , 

1. Modify the Coin/Address in sonfig.Jason
2. $ "sudo ./xmrig"
3. Error show:   ./xmrig: 2: Syntax error: "(" unexpected

PC:   Raspberrypi 4B/8GB 
OS:   Ubuntu x 64
Version:   xmrig-6.12.1

Please help me to double check the issue , how should i do now ?
Thanks a lot !



# Discussion History
## sabaren2010 | 2021-05-31T05:31:42+00:00
Ok, i got it.  
So xmrig didn't support 32bit, correct ?
Thanks a lot !

## Spudz76 | 2021-05-31T07:02:20+00:00
aarch64 works fine.  And ARMv7 is the only 32-bit platform that still sort of works (but RPi3 or higher are aarch64 for sure)

You must have full 64-bit OS and compilers (some RPi / Raspbian are stupid hybrid 64-bit kernel with all-32-bit userspace)

The syntax error is probably from bad format in config.json

Perhaps use a graphical JSON-editor if you don't understand where you've made an error with by-hand editing.

## sabaren2010 | 2021-05-31T12:24:42+00:00
Hi Spudz76,

Thanks for reply !

I have to try , do nothing in config.json after  do the procedure as below
1. download file xmrig-6.12.1-focal-x64.tar.gz
2. $ tar xvzf xmrig-6.12.1-focal-x64.tar.gz
2. nothing for config.json
3. $ sudo ./xmrig

Still show the same error as I shown before.
Error show: ./xmrig: 2: Syntax error: "(" unexpected


## SChernykh | 2021-05-31T13:21:30+00:00
> download file xmrig-6.12.1-focal-x64.tar.gz

This is for AMD/Intel CPUs. You have to compile it yourself for Raspberry Pi, there's no precompiled binary for it. See https://xmrig.com/docs/miner/build/ubuntu

## sabaren2010 | 2021-05-31T17:05:17+00:00
Hi SChernykh,

I success to run xmrig now after follow your suggestion , thanks for your fully help.

# Action History
- Created by: sabaren2010 | 2021-05-29T07:20:40+00:00
- Closed at: 2021-05-31T17:05:23+00:00
