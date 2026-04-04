---
title: Provide macOS Universal Binary (M1) release
source_url: https://github.com/monero-project/monero-gui/issues/3495
author: t-anon
assignees: []
labels: []
created_at: '2021-05-22T00:46:47+00:00'
updated_at: '2023-04-16T04:58:48+00:00'
type: issue
status: closed
closed_at: '2023-04-16T04:58:47+00:00'
---

# Original Description
monero-wallet-gui uses a lot of energy running on ARM M1 Macs due to translation. We should provide a universal binary.

# Discussion History
## counterbeing | 2021-11-07T15:50:17+00:00
I actually can't even seem to get `monerod` running. It just unexpectedly quits immediately. 😢 

## selsta | 2021-11-07T17:17:04+00:00
As a first step the next release will make it easy to compile monero and monero-gui on Apple Silicon, currently some manual changes are required.

## BigslimVdub | 2022-03-12T04:22:44+00:00
@selsta 
Is this the only change needed (as of today master) to build on M1:
https://github.com/monero-project/monero-gui/pull/3804

Just git pull master then make -j4 ?

## selsta | 2022-03-12T04:24:05+00:00
master should build fine on M1.

Just clone and then `make`.

## artisr | 2022-05-05T12:58:04+00:00
master builds, however when trying to mine with P2Pool it gives an error "Error starting mining" "Couldn't start mining"
Solo option works.

## selsta | 2022-05-05T13:02:30+00:00
First step towards M1 binaries: https://github.com/monero-project/monero/pull/8312

## selsta | 2022-05-05T13:02:48+00:00
@artisr what hardware are you using?

## artisr | 2022-05-05T13:14:34+00:00
I managed to get it working, I compiled https://github.com/SChernykh/p2pool and replaced p2pool binary in monero-wallet-gui/Contents/MacOS

If I'm guessing right, the app downloads the binary and we need to update it to download the correct one?

I'm using 16" M1 pro

## selsta | 2022-05-05T13:16:06+00:00
Correct, p2pool doesn't offer M1 binaries yet.

## Janaka-Steph | 2022-08-20T23:50:31+00:00
Can I ask an ETA for this?

## selsta | 2022-08-20T23:55:30+00:00
Qt only added official M1 support in 5.15.9: https://www.qt.io/blog/commercial-lts-qt-5.15.9-released

This version won't be available open source until April 2023. It might be possible to get it working with previous versions but I didn't spend much time on it yet.


## Janaka-Steph | 2022-08-20T23:58:47+00:00
> Qt only added official M1 support in 5.15.9: https://www.qt.io/blog/commercial-lts-qt-5.15.9-released
> 
> This version won't be available open source until April 2023. It might be possible to get it working with previous versions but I didn't spend much time on it yet.

Oh okay. Thank you for the quick reply

## Ishaanahuja7 | 2023-04-08T10:00:50+00:00
Qt 5.15.9 Community Version Officially Released [here](https://download.qt.io/official_releases/qt/5.15/5.15.9/single)

## selsta | 2023-04-10T14:52:24+00:00
Qt doesn't provide precompiled libraries for Qt 5.15.3 or later, which means I have to compile it myself. I've been doing some tests but I wasn't successful yet.

## selsta | 2023-04-15T15:52:38+00:00
I made some progress here, I got the packaged GUI running natively with the following 2 issues:

- ~~Starting local node fails~~ found a workaround
- ~~Some icons don't display correctly~~ solved

## selsta | 2023-04-16T04:58:47+00:00
Next release will have native macOS ARM binaries.

# Action History
- Created by: t-anon | 2021-05-22T00:46:47+00:00
- Closed at: 2023-04-16T04:58:47+00:00
