---
title: GLIBC error Linux Mint 20
source_url: https://github.com/xmrig/xmrig/issues/3483
author: kintaris3
assignees: []
labels: []
created_at: '2024-05-22T19:55:22+00:00'
updated_at: '2025-06-18T22:13:02+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:13:02+00:00'
---

# Original Description
Followed the steps off of the site exactly. Got ready to launch xmrig and got this error message.

./xmrig
./xmrig: /lib/x86_64-linux-gnu/libc.so.6: version `GLIBC_2.36' not found (required by ./xmrig)
./xmrig: /lib/x86_64-linux-gnu/libc.so.6: version `GLIBC_2.38' not found (required by ./xmrig)

I then too the steps to compile from source the proper GLIBC. I was successful and this was my result.

 ldd --version
ldd (GNU libc) 2.39.9000
Copyright (C) 2024 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
Written by Roland McGrath and Ulrich Drepper.

I go to run xmrig and had the same error as I did before. Am I doing something wrong? Is it because I am running Linux Mint and not Ubuntu? Is there anyway to install the two versions that is required for xmrig along side my current version? Or should I just build a static build? I apologize if I am asking obvious questions that many know the answer to. I am new to this whole process of mining crypto. 

I have xmrig-6.21.3
I selected the 24.04 Noble Numbat build.


# Discussion History
## SChernykh | 2024-05-22T19:58:57+00:00
> 24.04 Noble Numbat build.

This is probably not compatible with your distro. Try `xmrig-6.21.3-linux-static-x64.tar.gz`

## kintaris3 | 2024-05-22T20:03:29+00:00
> > 24.04 Noble Numbat build.
> 
> This is probably not compatible with your distro. Try `xmrig-6.21.3-linux-static-x64.tar.gz`

I gave it a try and it is running perfectly! Thank you!!! Problem solved!!!!!

## Spudz76 | 2024-05-30T13:50:11+00:00
Linux Mint 20 is based on Ubuntu Focal so you will have better luck choosing precompiled things for Focal (rather than Noble which is waaaaaaaaaay newer).  You may also bump up to Mint 21 which is based on Ubuntu Jammy and possibly have less trouble with not finding precompiles for (mostly deprecated) Focal.

It is also very weird your GLIBC is 2.39 and not tagged Ubuntu, on Mint20/Focal it should be `ldd (Ubuntu GLIBC 2.31-0ubuntu9.16) 2.31` while on Mint21/Jammy it would be `ldd (Ubuntu GLIBC 2.35-0ubuntu3.8) 2.35`

## kintaris3 | 2024-05-30T15:12:24+00:00
I downloaded and installed the GLIBC from the github. That could be why it doesn't say Ubuntu. I ended up using the static build and it worked great. Still running fine days later. On my next rig I set up with Linux Mint, I will try the build that best matches and see. I know Mint is based off the LTS builds of Ubuntu. 

# Action History
- Created by: kintaris3 | 2024-05-22T19:55:22+00:00
- Closed at: 2025-06-18T22:13:02+00:00
