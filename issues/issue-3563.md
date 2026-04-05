---
title: 'Create a Android binary only build '
source_url: https://github.com/xmrig/xmrig/issues/3563
author: shenlo666
assignees: []
labels: []
created_at: '2024-10-15T08:04:35+00:00'
updated_at: '2024-10-30T14:54:39+00:00'
type: issue
status: closed
closed_at: '2024-10-30T14:54:39+00:00'
---

# Original Description
Hi, is it possible to build xmrig only for android devices?
I mean, a binary which is not possible to run in Linux OS.
If i build the xmrig binary in Termux, you can launch this on Unix (with some tricks).
So is there a workaround?
Thanks a lot, my best!

# Discussion History
## ahorek | 2024-10-15T17:08:45+00:00
> is it possible to build xmrig only for android devices?

yes, Termux works (as far as I know)

> If i build the xmrig binary in Termux, you can launch this on Unix (with some tricks).

no, Android binaries aren't fully compatible with Linux, but you can use UserLAnd on Android


## shenlo666 | 2024-10-16T21:14:28+00:00
Thanks @ahorek, yes xmrig works great on Termux, but my question was about "only for android"!
As far as i know, UserLand is for run Linux app on Android, sorry this is not what i want, i want to build Android Only binaries, so i cant run on Linux OS.
So if you said that they aren't fully compatible that's fine i hope.

Another point, somebody knows howto embed (store in binaries) xmrig arguments/command line options like pool, port,...?
So the user dont have to pass the option in the command line.
Thank you. 

## ahorek | 2024-10-17T09:54:42+00:00
> So if you said that they aren't fully compatible that's fine i hope.

I'm wondering what your goal is, but yes, binaries built for Android won't work on UserLAnd / Linux or Windows :)

> somebody knows howto embed (store in binaries) xmrig arguments/command line options like pool, port,...?

why do you need it in the binary? isn't a JSON config enough?
https://github.com/xmrig/xmrig?tab=readme-ov-file#usage

## shenlo666 | 2024-10-17T17:25:22+00:00
> I'm wondering what your goal is, but yes, binaries built for Android won't work on UserLAnd / Linux or Windows :)

Nothing special, i test pool mining on android devices and want to restrict linux os...

> why do you need it in the binary? isn't a JSON config enough?

I want a no config binary with hard code option implemted in the code, like the dev fee for example.
No config.json, i want to run the binary with less options in command line.
Thanks for your ideas @ahorek 



# Action History
- Created by: shenlo666 | 2024-10-15T08:04:35+00:00
- Closed at: 2024-10-30T14:54:39+00:00
